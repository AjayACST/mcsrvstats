import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mcsrvstats",
    version="0.1.1",
    author="Leon Bowie",
    author_email="leon@bowie-co.nz",
    description="An async wrapper for popular minecraft servers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Obsidion-dev/mcsrvstats",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 2 - Pre-Alpha",
    ],
    python_requires=">=3.6",
    install_requires=["aiohttp", "beautifulsoup4"],
)
