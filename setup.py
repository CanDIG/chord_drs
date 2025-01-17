#!/usr/bin/env python

import configparser
import os
import setuptools

with open("README.md", "r") as rf:
    long_description = rf.read()

config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(os.path.realpath(__file__)), "chord_drs", "package.cfg"))

setuptools.setup(
    name=config["package"]["name"],
    version=config["package"]["version"],

    python_requires=">=3.6",
    install_requires=[
        "boto3>=1.17.96,<1.18",
        "bento_lib[flask]==2.2.1",
        "Flask>=1.1.2,<2.0",
        "Flask-SQLAlchemy>=2.5.1,<3.0",
        "Flask-Migrate>=3.0.1,<3.1",
        "prometheus_flask_exporter>=0.14.1,<0.15",
        "python-dotenv>=0.17.1,<0.18",
        "SQLAlchemy>=1.4.18,<1.5"
    ],

    author=config["package"]["authors"],
    author_email=config["package"]["author_emails"],

    description="An implementation of a data repository system (as per GA4GH's specs) for the Bento platform.",
    long_description=long_description,
    long_description_content_type="text/markdown",

    packages=setuptools.find_packages(),
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "ingest=chord_drs.commands:ingest"
        ],
    },

    url="https://github.com/c3g/chord_drs",
    license="LGPLv3",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Operating System :: OS Independent"
    ]
)
