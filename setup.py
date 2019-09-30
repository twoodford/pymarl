import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pymarl",
    version="0.1.0",
    author="OxWhirl",
    description="Python Multi-Agent Reinforcement Learning framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/twoodford/pymarl",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires='>=3.6',
)
