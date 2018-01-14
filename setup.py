"""
WikiLink
-----
	WikiLink is web-scraping application to find minimum number of links between two given wiki pages. It's extensively documented
    and follows best practice patterns.
    
	:copyright: (c) 2017 by Tran Ly VU.
    :license: Apache License 2.0, see LICENSE for more details.
"""
from setuptools import setup


setup(
	name='WikiLink',
	description='A web-scraping application to find the minimum number of links between 2 given wiki pages',
	author='Tran Ly Vu',
	author_email='vutransingapore@gmail.com',
	license='Apache License 2.0',
	classifiers=[
		'Development Status :: 3 - Alpha',
		'Intended Audience :: Science/Research',
		'Framework :: IPython'
		'Topic :: Scientific/Engineering :: Artificial Intelligence',
		'Programming Language :: Python :: 3.6',
		'Operating System :: Microsoft :: Windows :: Windows 10',
		'Natural Language :: English',
		'License :: OSI Approved :: Apache License 2.0',
	],
	keywords='web-scraping',
	packages=['wiki-link'],
	install_requires=[
		'beautifulsoup4'
		'bs4',
		'SQLAlchemy'
		'requests'
		]
				
)