from setuptools import setup

setup(
    name="pygimp-labs",
    version="0.1.1",
    packages=["pygimp"],
    install_requires=[
        "loguru>=0.7.2",
        "art>=6.2",
    ],
    entry_points={
        "console_scripts": [
            "pygimp-labs=pygimp.cli:main",
        ],
    },
)
