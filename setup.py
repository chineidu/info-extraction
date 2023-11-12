from pathlib import Path

from setuptools import find_namespace_packages, setup

# ============ Update this! ============
VERSION: str = "0.2.3"
URL: str = "https://github.com/chineidu/info-extraction"
PYTHON_REQUIRES: str = ">=3.9"
SHORT_DESCRIPTION: str = "NLP project to identify and categorize named entities in an input text."
STYLE_PACKAGES: list[str] = ["black==22.10.0", "isort==5.10.1", "pylint==2.15.10"]
TEST_PACKAGES: list[str] = ["pytest>=7.2.0", "pytest-cov==4.0.0"]

ROOT_DIR = Path(__file__).absolute().parent


with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()


def list_reqs(*, filename: str = "requirements.txt") -> list[str]:
    """This loads the required packages as a list."""
    with open(ROOT_DIR / filename, encoding="utf-8") as f:
        return f.read().splitlines()


setup(
    name="fast_token_classifier",
    version=VERSION,
    description=SHORT_DESCRIPTION,
    author="Chinedu Ezeofor",
    author_email="neidue@email.com",
    packages=find_namespace_packages(),
    url=URL,
    install_requires=list_reqs(),
    python_requires=PYTHON_REQUIRES,
    extras_require={
        "dev": STYLE_PACKAGES + TEST_PACKAGES,
        "test": TEST_PACKAGES,
    },
    include_package_data=True,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
)
