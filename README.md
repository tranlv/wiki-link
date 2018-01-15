# **wiki-link**

A web-scraping application to find the minimum number of links between 2 given wiki pages.

[![Build Status](https://travis-ci.org/tranlyvu/wiki-link.svg?branch=master)](https://travis-ci.org/tranlyvu/wiki-link) [![Code Health](https://landscape.io/github/tranlyvu/wiki-link/master/landscape.svg?style=flat)](https://landscape.io/github/tranlyvu/wiki-link/master) [![Join the chat at https://gitter.im/find-link/Lobby](https://badges.gitter.im/find-link/Lobby.svg)](https://gitter.im/find-link/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

<img src="img/link.jpg" width="480" alt="Combined Image" />

---
Usage
---

- Set up database management: as of 14 January 2018, Wiki-link has been tested with [Mysql](https://www.mysql.com/downloads/) and [PostgreSQL](https://www.postgresql.org/) (with psycopg2 adapter). Alternatively, for quick development setup, I strongly recommend to setup database with [Docker](https://www.docker.com/).

- Download a [release](https://github.com/tranlyvu/wiki-link/releases) or fork the repo: 

```
$git clone https://github.com/tranlyvu/wiki-link.git
```

- Modify the configuration file for database connection:

```
$vi wiki-link/conf.ini
```

- The simplest way is to run the [sample file](https://github.com/tranlyvu/wiki-link/blob/master/sample.py) with your desired wiki links:

```
$vi wiki-link/sample.py
$python wiki-link/sample.py
```

---
Development Setup
---

Wiki-link was developed using python 3.6, simply run the following on your development environment:

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

* v1.0.1 - Jan 14, 2018
	* Fix database connection bug
	* Test PostgreSQL database

* v1.0.0 - Nov 7, 2016 
    * First official release

---
Contribution
---

For bug reports or requests please submit an [issue](https://github.com/tranlyvu/wiki-link/issues).

For new features contribution, please follow the following instruction:

```
1. Fork the repo (`$git clone https://github.com/tranlyvu/wiki-link.git`)
2. Create your feature branch (`$git checkout -b new/your-feature`)
3. Commit your changes (`$git commit -am 'Add some new feature'`)
4. Push to the branch (`$git push origin new/your-feature`)
5. Create a new Pull Request at https://github.com/tranlyvu/wiki-link/pulls
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

