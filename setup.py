from setuptools import find_packages, setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="nb2py",
    version="0.0.1",
    description="Converts .ipynb files to .py files.",
    package_dir={"": "nb2py"},
    packages=find_packages(where="nb2py"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/subhranil2605/nb2py",
    author="Subhranil Sarkar",
    author_email="subhranil2605@gmail.com",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent"
    ],
    extras_require={
        "dev": ["pytest>=7.0", "twine>=4.0.2"],
    },
    python_requires=">=3.10"
)
