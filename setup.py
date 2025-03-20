from Cython.Build import cythonize
from setuptools import setup

setup(
    name="Django",
    ext_modules=cythonize(["django/db/models/query.py"]),
)
