#!/usr/bin/env python
import sys
import os
from setuptools import setup, find_packages
from distutils.spawn import find_executable
from trueimager import *
setup(
name = "fbimager",
author_email = "abhashjha16@gmail.com.com",
description = ("Automated phishing attacks against Wi-Fi networks"),
license = "GPL",
packages = find_packages(),
include_package_data = True,
version = "0.1",
install_requires = [
'bs4',
'requests',
'selenium']
)

