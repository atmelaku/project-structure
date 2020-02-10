import setuptools

with open("README.md", "r") as f:
    long_description = f.read()


setuptools.setup(
    name="quiz_project"
    version="0.0.1",
    author="Alebachew Melaku",
    author_email="alebachewtegegne2017@yahoo.com",
    url="https://github.com/atmelaku/project-structure",
    description="a project structure that can run any python code",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=[],
    extras_require=[],
    tests_require=['pytest'],
    python_requires='>=3.6',
)
