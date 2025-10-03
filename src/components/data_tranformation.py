import os
from src.entity import DataTransformationConfig
from src.logging import logger
from transformers import AutoTokenizer
from datasets import load_from_disk

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_name)

    ## validate all files are present, and add the value to the status file

    def convert_examples_to_features(self, examples):
        input_encodings = self.tokenizer(
            examples['dialogue'], max_length=512, padding='max_length', truncation=True
        )

        with self.tokenizer.as_target_tokenizer():
            target_encodings = self.tokenizer(
                examples['summary'], max_length=128, padding='max_length', truncation=True
            )
        return {
            'input_ids': input_encodings['input_ids'],
            'attention_mask': input_encodings['attention_mask'],
            'labels': target_encodings['input_ids'],
        }
    
    def convert(self):
        dataset_samsum =load_from_disk(self.config.data_path)
        logger.info(f"Dataset loaded from {self.config.data_path}")
        tokenized_datasets = dataset_samsum.map(self.convert_examples_to_features, batched=True)
        tokenized_datasets.save_to_disk(self.config.root_dir)
        logger.info(f"Tokenized dataset saved to {self.config.root_dir}")