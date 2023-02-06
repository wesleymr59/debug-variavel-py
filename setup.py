from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="debugsPy",
    version="0.0.1",
    author="Wesley M",
    description="Debug for python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["src/debugsPy"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=[],
    dependency_links=['https://github.com/ItanuRomero/talk-in-code']
)