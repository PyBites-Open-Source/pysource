import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name="pybites-pysource",
    version="1.0.1",
    description="Read Python source code from the command line",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/PyBites-Open-Source/pysource",
    author="PyBites",
    author_email="support@pybit.es",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    packages=["src"],
    include_package_data=True,
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    entry_points={
        "console_scripts": [
            "pysource=src.__main__:main",
        ]
    },
)
