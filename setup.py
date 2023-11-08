from pathlib import Path

from ensure import ensure_annotations
from setuptools import find_namespace_packages, setup

style_packages = ["black==22.10.0", "isort==5.10.1", "pylint==2.15.10"]
test_packages = ["pytest>=7.2.0", "pytest-cov==4.0.0"]

ROOT_DIR = Path(__file__).absolute().parent

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()


@ensure_annotations
def list_reqs(*, filename: str = "requirements.txt") -> list[str]:
    """This loads the required packages as a list."""
    with open(ROOT_DIR / filename, encoding="utf-8") as f:
        return f.read().splitlines()


setup(
    name="info-extraction",
    version="0.1.0",
    description="NLP project to identify and categorize named entities in an input text.",
    author="Chinedu Ezeofor",
    author_email="neidue@email.com",
    packages=find_namespace_packages(),
    url="https://github.com/chineidu/nyc-taxi-price-prediction",
    install_requires=list_reqs(),
    python_requires=">=3.9",
    extras_require={
        "dev": style_packages + test_packages,
        "test": test_packages,
    },
    include_package_data=True,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
)
