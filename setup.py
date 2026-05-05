#!/usr/bin/env python3

"""Chewie setup script"""

import sys

from setuptools import setup

if sys.version_info < (3, 10):
    print(
        """You are trying to install chewie on python {py}

chewie is not compatible with python earlier than 3.10, please upgrade.""".format(
            py=".".join([str(v) for v in sys.version_info[:3]])
        ),
        file=sys.stderr,
    )
    sys.exit(1)

setup(
    name="chewie",
    setup_requires=["pbr>=1.9", "setuptools>=17.1"],
    python_requires=">=3.10",
    pbr=True,
)
