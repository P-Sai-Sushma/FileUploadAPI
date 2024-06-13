from setuptools import setup, find_packages

setup(
    name="FileUploadAPI",
    version="1.0",
    author=" Sushma",
    author_email="saisushma.patange@gmail.com",
    description="This API is used to accept file uploads from end users.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/P-Sai-Sushma/demoAPI.git",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    
)