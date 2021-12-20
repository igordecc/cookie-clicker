import os

from datetime import datetime

from setuptools import setup, find_packages

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

version = (os.environ.get('VERSION') or datetime.utcnow().strftime("0.0.0%Y%m%d%H%M%S")).lstrip('v')

setup(
    name="cookie-clicker-bot",
    version=version,

    description="",

    long_description=long_description,
    long_description_content_type="text/markdown",

    url="https://github.com/igordecc/cookie-clicker-bot",

    author="igordecc",

    classifiers=[
       "Development Status :: 2 - Pre-Alpha",

        "Programming Language :: Python :: 3",
    ],

    keyworkd="selenium bot clicker gaming",

    project_urls={
        "Issues": "https://github.com/igordecc/cookie-clicker-bot/issues",
    },

    packages=find_packages(exclude=["examples"]),

    install_requires=["selenium"],

    include_package_data=True,

    python_requires=">=3",
)