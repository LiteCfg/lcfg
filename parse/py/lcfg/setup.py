import setuptools

with open("README.md", "r",encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="lcfg",
    version="0.0.1",
    author="Cure-X",
    author_email="admin@cure-x.net",
    description="Convert lcfg to Python object",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Cure-Dev/pylcfg",
    packages=setuptools.find_packages(),
    install_requires=[],
    entry_points={},
    classifiers=(),
)
