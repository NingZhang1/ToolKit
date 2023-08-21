from setuptools import setup

setup(
    name="ToolKitNZ",
    version="0.1",
    author="Ning Zhang",
    author_email="ningzhang1024@gmail.com",
    description="Test ToolKits written by Ning Zhang (ningzhang1024@gmail.com)",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    # packages=setuptools.find_packages(),
    py_modules=[
        "ToolKitNZ.src.PySCF.MoleInts",
        "ToolKitNZ.src.Slurm.tool",
    ]
)
