import platform

from Cython.Build import cythonize
from setuptools import setup

ext_modules = []

if platform.python_implementation() == "CPython":
    ext_modules.append(cythonize(["django/db/models/query.py"]))

setup(
    name="Django",
    ext_modules=ext_modules,
)
