import os
import sys
import logging

logging_str="[%(asctime)s - %(levelname)s - %(module)s - %(message)s]"

log_dir="logs"

log_file_path=os.path.join(log_dir,"logs.log")

os.makedirs(log_dir,exist_ok=True)


logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format=logging_str,
)

logger=logging.getLogger()
