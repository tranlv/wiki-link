"""
	wikilink
	~~~~~~~~

	wikilink is a multiprocessing web-scraping application to scrape wiki pages and 
	find minimum number of links between two given wiki pages.
    
    :copyright: (c) 2016 - 2019 by Tran Ly VU. All Rights Reserved.
    :license: Apache License 2.0.
"""
from setuptools import setup, find_packages
from re import search, MULTILINE

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
	name="wikilink",
	version="0.3.0.post1",
	author="Tran Ly Vu",
	author_email="vutransingapore@gmail.com",
	maintainer="Tran Ly Vu <vutransingapore@gmail.com>",
	maintainer_email="vutransingapore@gmail.com",
	description="A multiprocessing web-scraping application to scrape wiki pages and find minimum number of links between two given wiki pages.",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/tranlyvu/wiki-link",
	packages=find_packages(exclude=("*.tests", "*.tests.*", "tests.*", "tests", "docs")),
	license="Apache License 2.0",
	zip_safe=False,
	include_package_data=True,
	platforms="any",
	classifiers=[
		"Programming Language :: Python :: 3",
		"Programming Language :: Python :: 3.6",
		"Programming Language :: Python :: 3.7",
		"License :: OSI Approved :: Apache Software License ",
		"Operating System :: POSIX",
		"Operating System :: POSIX :: BSD",
		"Operating System :: POSIX :: Linux",
		"Operating System :: Unix",
		"Development Status :: 4 - Beta",
		"Natural Language :: English",
		"Environment :: Console",
		"Intended Audience :: Education",
		"Intended Audience :: End Users/Desktop",
		"Intended Audience :: Information Technology",
		"Intended Audience :: Science/Research",
		"Topic :: Scientific/Engineering :: Artificial Intelligence",
		"Topic :: Scientific/Engineering :: Information Analysis",
		"Topic :: Education",
		"Programming Language :: Python :: Implementation :: CPython",
		"Programming Language :: Python :: Implementation :: PyPy",
		"Framework :: Pytest",
		"Framework :: Flake8"
	],
	keywords=["Web Scraping", "Artificial Intelligence", "Breadth First Search", "Graph", "Data Science", "Web Extracting", "Information Analysis"],
	project_urls={
    "Source": "https://github.com/tranlyvu/wiki-link",
    "Tracker": "https://github.com/tranlyvu/wiki-link/issues",
    "Chat: Gitter": "https://gitter.im/find-link/Lobby",
    "CI: Travis": "https://travis-ci.org/tranlyvu/wiki-link",
    "Coverage: coveralls": "https://coveralls.io/github/tranlyvu/wiki-link",
	},
	py_modules=["six"],
	install_requires=[
		"beautifulsoup4>=4.7.1",
		"requests>=2.21.0",
		"SQLAlchemy-Utils>=0.33.11",
		"mysqlclient>=1.4.2.post1"
	],
	python_requires=">=3.0, <4",
	tests_require = [
    	"pytest",
    	"python-coveralls"
    ]	
)