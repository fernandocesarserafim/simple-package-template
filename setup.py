from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="meu_pacote",
    version="0.0.1",
    author="fernando",
    author_email="ferdesigner@hotmail.com",
    description="meu pacote",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fernandocesarserafim/simple-package-template/",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)
