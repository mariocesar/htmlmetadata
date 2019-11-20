from setuptools import find_packages, setup

setup(
    name="htmlmetadata",
    version="1.0",
    author="M. César Señoranis",
    author_email="mariocesar@humanzilla.com",
    packages=find_packages(),
    install_requires=["beautifulsoup4>=4.8.1", "html5>=0.0.9"],
    extras_require={"develop": ["wheel", "twine"]}
)
