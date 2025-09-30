import setuptools

__version__ = "0.1.0"
REPO_NAME = "text-summarization"
AUTHOR_USER_NAME = "m3nnoun"

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    description="A text summarization package",
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    packages=setuptools.find_packages(),
    python_requires=">=3.12",
)