from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="Topsis_Riddhi_102103282",
    version="1.0.13",
    author="Riddhi Garg",
    author_email="rgarg2_be21@thapar.com",
    url="https://github.com/Riddhi12349/topsis_102103282",
    description="A python package for implementing topsis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["pandas", "numpy"],
    entry_points={"console_scripts": ["Topsis_Riddhi_102103282 = Topsis_Riddhi_102103282.main:main"]},
)
