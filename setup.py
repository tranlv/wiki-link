from setuptools import setup,find_packages

setup(
    name='findLink',
	description='A web-scraping project to find the links between 2 given wiki pages',
	author='Tran Ly Vu',
	author_email='vutransingapore@gmail.com',
    license='MIT',
    classifiers=[
		'Development Status :: 3 - Alpha',
		'Intended Audience :: Science/Research',
		'Framework :: IPython'
		'Topic :: Scientific/Engineering :: Artificial Intelligence',
		'Programming Language :: Python :: 2.7',
		'Operating System :: Microsoft :: Windows :: Windows 7',
		'Natural Language :: English',
		'License :: OSI Approved :: MIT License',
	],
	keywords='web-scraping',
	packages=['findLink'],
	install_requires=[
		'bs4',
		'MySQLdb'
		'urllib2'
		]
				
)