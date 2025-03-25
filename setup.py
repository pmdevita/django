import platform

from Cython.Build import cythonize
from setuptools import setup

ext_modules = None

if platform.python_implementation() == "CPython":
    ext_modules = cythonize(
        ["django/db/models/query.py", "django/db/models/sql/compiler.py"],
        compiler_directives={"language_level": "3"},
    )

setup(
    name="Django",
    ext_modules=ext_modules,
)
