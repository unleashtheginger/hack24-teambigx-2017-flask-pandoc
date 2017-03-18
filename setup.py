import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "FlaskPandoc",
    version = "0.0.1",
    author = "Will Ellwood",
    author_email = "fragmad@gmail.com",
    description = ("A python library to convert files with Pandoc"),
    license = "MIT",
    keywords = "pandoc markdown docx hackathon hack24",
    url = "https://github.com/fragmad/hack24-teambigx-2017-flask-pandoc",
    packages=['FlaskPandoc'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
)
