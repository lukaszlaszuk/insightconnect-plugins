# GENERATED BY KOMAND SDK - DO NOT EDIT
from setuptools import setup, find_packages


setup(name="string-rapid7-plugin",
      version="1.3.1",
      description="The String plugin provides common programmatic string operations",
      author="rapid7",
      author_email="",
      url="",
      packages=find_packages(),
      install_requires=['insightconnect-plugin-runtime'],  # Add third-party dependencies to requirements.txt, not here!
      scripts=['bin/komand_string']
      )