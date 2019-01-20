# **wiki-link** [![version][23]][24] [![HitCount][21]][22] 
[21]: http://hits.dwyl.io/tranlyvu/wiki-link.svg
[22]: http://hits.dwyl.io/tranlyvu/wiki-link
[23]: https://img.shields.io/badge/latest%20ver-1.0.1-blue.svg
[24]: https://github.com/tranlyvu/wiki-link/releases

A web-scraping application to find the minimum number of links between 2 given wiki pages.


| Build | [![Build Status][3]][4] | [![Coverage Status][5]][6] | [![Code Health][9]][10]| | 
| :--- | :--- | :---  | :--- | :--- |
| **Quality** | [![Maintainability][13]][14] | [![Known Vulnerabilities][15]][16]	||
| **Technology** | [![Requirements Status][19]][20] | | | |
| **Support** | [![Join the chat at https://gitter.im/find-link/Lobby][17]][18] | [![blog][1]][2] | | |

[3]: https://travis-ci.org/tranlyvu/wiki-link.svg?branch=dev
[4]: https://travis-ci.org/tranlyvu/wiki-link 
[5]: https://coveralls.io/repos/github/tranlyvu/findLink/badge.svg?branch=dev
[6]: https://coveralls.io/github/tranlyvu/findLink?branch=dev
[9]: https://landscape.io/github/tranlyvu/wiki-link/dev/landscape.svg?style=flat)
[10]: https://landscape.io/github/tranlyvu/wiki-link/dev

[13]: https://api.codeclimate.com/v1/badges/8679cde6756683bd787d/maintainability
[14]: https://codeclimate.com/github/tranlyvu/wiki-link/maintainability
[15]: https://snyk.io/test/github/tranlyvu/wiki-link/badge.svg
[16]: https://snyk.io/test/github/tranlyvu/Wiki-link

[17]: https://badges.gitter.im/find-link/Lobby.svg
[18]: https://gitter.im/find-link/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge
[1]: https://img.shields.io/badge/docs-on%20blog-brightgreen.svg
[2]: https://tranlyvu.github.io/algorithms/BFS-and-a-simple-application/

[19]: https://requires.io/github/tranlyvu/wiki-link/requirements.svg?branch=master
[20]: https://requires.io/github/tranlyvu/wiki-link/requirements/?branch=master


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

- Database:  Wiki-link currently supports [Mysql](https://www.mysql.com/downloads/) and [PostgreSQL](https://www.postgresql.org/), please use either "mysql" or "postgresql" for setup_db().

- Download a [release](https://github.com/tranlyvu/wiki-link/releases) or install with pip

```
>>> from wikilink import wiki_link
>>> model = wiki_link.WikiLink()
>>> model.setup_db("mysql", "root", "12345", "127.0.0.1", "3306")
>>> model.min_link(source_url, dest_url, 6)
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
$ virtualenv -p python3 env
$ source env/bin/activate
$ pip install -r requirements.txt
```

If you are done working in the virtual environment for the moment, you can deactivate it:

```
$ deactivate
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
s
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

