from setuptools import setup, find_packages

setup(
    name="FileUploadAPI",
    version="1.0",
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'run_fileUploadAPI=fileUploadAPI.app:main',
        ],
    },
    package_data={
        '': ['templates/*.html', 'uploads/*'],
    },
    author=" Sushma",
    author_email="saisushma.patange@gmail.com",
    description="This API is used to accept file uploads from end users.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/P-Sai-Sushma/demoAPI.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    
)