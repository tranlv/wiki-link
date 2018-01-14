# **wiki-link**

A web-scraping application to find the minimum number of links between 2 given wiki pages.

[![Build Status](https://travis-ci.org/tranlyvu/wiki-link.svg?branch=master)](https://travis-ci.org/tranlyvu/wiki-link) [![Code Health](https://landscape.io/github/tranlyvu/wiki-link/master/landscape.svg?style=flat)](https://landscape.io/github/tranlyvu/wiki-link/master)

<img src="img/link.jpg" width="480" alt="Combined Image" />

---
Usage
---

- Set up database management, as of 14 January 2018, Wiki-link has been tested with [Mysql](https://www.mysql.com/downloads/). Alternatively, for quick development setup, I strongly recommend to setup database with [Docker](https://www.docker.com/).

- Download a [release](https://github.com/tranlyvu/wiki-link/releases) or fork the source code 

```
$git clone https://github.com/tranlyvu/wiki-link.git
```

- Modify the configuration file for database connection

```
$vi wiki-link/conf.ini
```

- The simplest way is to run the [Sample file](https://github.com/tranlyvu/wiki-link/tree/master/sample) with your desired wiki links.

---
Development Setup
---

Wiki-link was developed using python 3.6 ,simply run the following on your development environment

```
$pip install -r requirements.txt
```

---
Project Architecture
---

To do

---
Release History
---

* 1.0.1 - Jan 14, 2016
	*Fix database connection bug

* 1.0.0 - Nov 7, 2016 
    * The first official release

---
Contribution
---

For bug reports or requests please submit an [issue](https://github.com/tranlyvu/wiki-link/issues).

For new features contribution, please follow the following instruction:

```
1. Fork the source code (`$git clone https://github.com/tranlyvu/wiki-link.git`)
2. Create your feature branch (`$git checkout -b new/your-feature`)
3. Commit your changes (`$git commit -am 'Add some new feature'`)
4. Push to the branch (`$git push origin new/your-feature`)
5. Create a new [Pull Request](https://github.com/tranlyvu/wiki-link/pulls)
```

---
Contact
---

Feel free to contact me to discuss any issues, questions, or comments.
*  Email: vutransingapore@gmail.com
*  Twitter: [@vutransingapore](https://twitter.com/vutransingapore)
*  GitHub: [Tran Ly Vu](https://github.com/tranlyvu)

---
License
---

See the [LICENSE](https://github.com/tranlyvu/wiki-link/blob/master/LICENSE) file for license rights and limitations (Apache License 2.0).

