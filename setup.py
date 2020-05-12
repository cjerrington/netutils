import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="netutil",
    version="0.0.7",
    author="Clayton Errington",
    author_email="me@claytonerrington.com",
    description="Simplified way to get networking port status",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cjerrington/netutils",
    packages=setuptools.find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)