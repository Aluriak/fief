from setuptools import setup, find_packages
from fief.info import __version__, __name__


setup(
    name = __name__,
    version = __version__,
    packages = find_packages(),

    author = "lucas",
    author_email = "lucas.bourneuf@laposte.net",
    description = "Decorator for effective parameter filtering",
    long_description = "Please see README on https://github.com/Aluriak/fief",
    keywords = "decorator parameter filter",
    url = "https://github.com/Aluriak/fief",

    classifiers = [
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Natural Language :: English",
        "Operating System :: Unix",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)
