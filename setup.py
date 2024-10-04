from setuptools import setup, find_packages

setup(
    name="search-engine-tool-vito",
    version="0.3.0",
    packages=find_packages(),
    install_requires=[
        "selenium"
    ],

    author="bluefrog",
    author_email="vito95311@gmail.com",
    description="搜索引擎API Bing / Google / Yahoo ",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/freewu/search-engine-tool",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
    ],
)