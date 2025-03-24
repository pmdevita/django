import platform

from Cython.Build import cythonize
from setuptools import setup

ext_modules = None

if platform.python_implementation() == "CPython":
    ext_modules = cythonize(["django/db/models/query.py"])

setup(
    name="Django",
    ext_modules=ext_modules,
)
