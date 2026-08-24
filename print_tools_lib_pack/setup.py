from setuptools import setup, find_packages

with open("../README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="print-tools",
    version="1.0.0",
    author="Hexofu",
    author_email="your.email@example.com",
    description="Additional useful output features - multi‑colored text (RGB) and animated loading",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    python_requires=">=3.6",
)