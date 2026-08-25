from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="print-toolkit",
    version="1.1.1",
    author="Hexofu",
    author_email="sashanaumov0101@gmail.com",
    description="Additional useful output features - multi‑colored text (RGB) and animated loading",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["print_toolkit"],
    python_requires=">=3.6",
)