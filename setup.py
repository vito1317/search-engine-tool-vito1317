from setuptools import setup, find_packages

setup(
    name="search-engine-tool-vito1317",
    version="0.6.9",
    packages=find_packages(),
    install_requires=[
        "selenium"
        "BeautifulSoup4"
    ],

    author="vito",
    author_email="vito95311@gmail.com",
    description="搜索引擎API Bing / Google / Yahoo ",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/vito1317/search-engine-tool-vito1317",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
    ],
)