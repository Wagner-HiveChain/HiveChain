from setuptools import setup, find_packages
import os

# Read the long description from README.md if available
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, "README.md"), encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="hivechain",
    version="0.1.0",
    author="Laura Wagner",
    author_email="wagner@hivechain.dev", 
    description="HiveChain: A Modular AI Orchestration Framework for Transparent and easy to use.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://www.hivechain.dev",
    # This will include all packages under src, including hivechain and its submodules (e.g., provider_adapters)
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.7",
    install_requires=[
        "openai",
        "python-dotenv",
    ],
    entry_points={
        "console_scripts": [
            "hivechain-run=hivechain.cli:main",
        ]
    },
)
