"""
	wikilink
	~~~~~~~~

	wikilink is a web-scraping application to find minimum number 
	of links between two given wiki pages. 
    
    :copyright: (c) 2016 - 2019 by Tran Ly VU. All Rights Reserved.
    :license: Apache License 2.0.
"""
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
	name='wikilink',
	version="1.2.0",
	author='Tran Ly Vu',
	author_email='vutransingapore@gmail.com',
	maintainer='Tran Ly Vu <vutransingapore@gmail.com>',
	maintainer_email='vutransingapore@gmail.com',
	description='A web-scraping application to find the minimum number of links between 2 given wiki pages',
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/tranlyvu/wiki-link",
	packages=find_packages("wikilink"),
	package_dir={'':'wikilink'},
	license='Apache License 2.0',
	classifiers=[
		"Programming Language :: Python :: 3",
		"Programming Language :: Python :: 3.6",
		"License :: OSI Approved :: Apache Software License ",
		"Operating System :: OS Independent",
		"Development Status :: 5 - Production/Stable",
		"Natural Language :: English",
		"Environment :: Console",
		'Intended Audience :: Science/Research',
		'Topic :: Scientific/Engineering :: Artificial Intelligence',
	],
	keywords=["web-scraping", "Artificial Intelligence", "breadth first search", "Graph"],
	project_urls={
    'Source': 'https://github.com/tranlyvu/wiki-link',
    'Tracker': 'https://github.com/tranlyvu/wiki-link/issues',
    'Chat: Gitter': 'https://gitter.im/find-link/Lobby',
    'CI: Travis': 'https://travis-ci.org/tranlyvu/wiki-link',
    'Coverage: coveralls': 'https://coveralls.io/github/tranlyvu/wiki-link',

	},
	install_requires=[
		"beautifulsoup4",
		"requests",
		"SQLAlchemy-Utils"
		],
	python_requires="~=3.6"			
)