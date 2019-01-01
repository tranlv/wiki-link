# **wiki-link**

A web-scraping application to find the minimum number of links between 2 given wiki pages.

[![Build Status](https://travis-ci.org/tranlyvu/wiki-link.svg?branch=master)](https://travis-ci.org/tranlyvu/wiki-link) [![Code Health](https://landscape.io/github/tranlyvu/wiki-link/master/landscape.svg?style=flat)](https://landscape.io/github/tranlyvu/wiki-link/master) [![Coverage Status](https://coveralls.io/repos/github/tranlyvu/findLink/badge.svg?branch=master)](https://coveralls.io/github/tranlyvu/findLink?branch=master) [![Join the chat at https://gitter.im/find-link/Lobby](https://badges.gitter.im/find-link/Lobby.svg)](https://gitter.im/find-link/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge) [![codecov](https://codecov.io/gh/tranlyvu/wiki-link/branch/dev/graph/badge.svg)](https://codecov.io/gh/tranlyvu/wiki-link)

<img src="img/link.jpg" width="480" alt="Combined Image" />

---
Table of contents
---

1. [Usage](#Usage)
2. [Development Setup](#Development-Setup)
3. [Project Architecture](#Project-Architecture)
4. [Release History](#Release-History)
5. [Contribution](#Contribution)
6. [Contact](#Contact)
7. [License](#License)

---
Usage
---

- Set up database management: as of 14 January 2018, Wiki-link has been tested with [Mysql](https://www.mysql.com/downloads/) and [PostgreSQL](https://www.postgresql.org/) (with psycopg2 adapter). Alternatively, for quick development setup, I strongly recommend to setup database with [Docker](https://www.docker.com/).

- Download a [release](https://github.com/tranlyvu/wiki-link/releases) or fork the repo: 

```
$ git clone https://github.com/tranlyvu/wiki-link.git
```

- Modify the configuration file for database connection:

```
$ vi wiki-link/conf.ini
```

- The simplest way is to run the [sample file](https://github.com/tranlyvu/wiki-link/blob/master/sample.py) with your desired wiki links:

```
$ python wiki-link/run.py
```

---
Development Setup
---

### Packages Installation

Wiki-link was developed using python 3.6, simply run the following on your development environment:

```
$ pip install -r requirements.txt
```


Or to set up environment with virtualenv

```
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

If you are done working in the virtual environment for the moment, you can deactivate it:

```
$ deactivate
```

### Additional Dependency 

For Linux, please run:

```
$ sudo apt-get install libmysqlclient-dev
```

---
Project Architecture
---

An overview of the project can be found [here](https://tranlyvu.github.io/BFS-and-a-simple-application/).

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

For new feature contribution, please follow the following instruction:

1. Fork the repo https://github.com/tranlyvu/wiki-link.git to your own github

2. Clone from your own repo

`$ git clone https://github.com/<your name>/wiki-link.git`

3. Make sure you are at dev branch 

`$ git checkout dev && git pull`

4. Create your feature/bug-fix branch

`$ git checkout -b <feature/bug>/<branch-name>`

5. Commit your changes 

`$ git commit -am 'Add some new feature'`

6. Push to the branch 

`$ git push`

7. Go to your own repo and create a new Pull Request against 'dev' branch

8. To sync your forked repo with my repo

```
$ git remote add upstream https://github.com/tranlyvu/wiki-link.git
$ git checkout master
$ git merge upstream/master
```

---
Contact
---

Feel free to contact me to discuss any issues, questions, or comments.
*  Email: vutransingapore@gmail.com
*  Linkedln: [@vutransingapore](https://www.linkedin.com/in/tranlyvu/)
*  GitHub: [Tran Ly Vu](https://github.com/tranlyvu)
*  Blog: [tranlyvu.github.io](https://tranlyvu.github.io/)

---
License
---

See the [LICENSE](https://github.com/tranlyvu/wiki-link/blob/master/LICENSE) file for license rights and limitations (Apache License 2.0).

