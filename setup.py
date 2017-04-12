"""
FindLink
-----

	Findlink is web-scraping application to find minimum number of links between two given wiki pages. It's extensively documented
    and follows best practice patterns.
	For more than you ever wanted to know about find-link, see the documentation:

    :copyright: (c) 2017 by Tran Ly VU.
    :license: Apache License 2.0, see LICENSE for more details.


Findlink is Fun
````````````
Save in a hello.py:
.. code:: python
    from find_link import FindLink
    app = Flask(__name__)
    @app.route("/")
    def hello():
        return "Hello World!"
    if __name__ == "__main__":
        app.run()

"""


from setuptools import setup,find_packages



setup(
    name='findLink',
	description='A web-scraping project to find the links between 2 given wiki pages',
	author='Tran Ly Vu',
	author_email='vutransingapore@gmail.com',
    license='Apache License 2.',
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
		'sqlalchemy'
		'urllib2'
		]
				
)