# **wikilink** [![version][23]][24] [![HitCount][21]][22] [![Downloads][25]][26]
[21]: http://hits.dwyl.io/tranlyvu/wiki-link.svg
[22]: http://hits.dwyl.io/tranlyvu/wiki-link
[23]: https://img.shields.io/pypi/v/wikilink.svg
[24]: https://pypi.org/project/wikilink/
[25]: https://pepy.tech/badge/wikilink
[26]: https://pepy.tech/project/wikilink

A web-scraping application to find the minimum number of links between 2 given wiki pages.


| Build | [![Build Status][3]][4] | [![Coverage Status][5]][6] | | 
| :--- | :--- | :---  | :--- |
| **Quality** | [![Maintainability][13]][14] | [![Known Vulnerabilities][15]][16] | [![Requirements Status][19]][20] |
| **Support** | [![Join the chat at https://gitter.im/find-link/Lobby][17]][18] | [![blog][1]][2] | [![Open Source Helpers][7]][8] | 

[3]: https://travis-ci.org/tranlyvu/wiki-link.svg?branch=dev
[4]: https://travis-ci.org/tranlyvu/wiki-link 
[5]: https://coveralls.io/repos/github/tranlyvu/wiki-link/badge.svg
[6]: https://coveralls.io/github/tranlyvu/wiki-link

[13]: https://api.codeclimate.com/v1/badges/8679cde6756683bd787d/maintainability
[14]: https://codeclimate.com/github/tranlyvu/wiki-link/maintainability
[15]: https://snyk.io/test/github/tranlyvu/wiki-link/badge.svg
[16]: https://snyk.io/test/github/tranlyvu/wiki-link

[17]: https://badges.gitter.im/find-link/Lobby.svg
[18]: https://gitter.im/find-link/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge
[1]: https://img.shields.io/badge/docs-on%20blog-brightgreen.svg
[2]: https://tranlyvu.github.io/algorithms/BFS-and-a-simple-application/

[19]: https://requires.io/github/tranlyvu/wiki-link/requirements.svg?branch=dev
[20]: https://requires.io/github/tranlyvu/wiki-link/requirements/?branch=dev

[7]: https://www.codetriage.com/tranlyvu/wiki-link/badges/users.svg
[8]: https://www.codetriage.com/tranlyvu/wiki-link

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

Download a [release](https://github.com/tranlyvu/wiki-link/releases) or install with pip

```
$ pip install wikilink
```

### Database support

wikilink currently supports [Mysql](https://www.mysql.com/downloads/) and [PostgreSQL](https://www.postgresql.org/)

### API

setup_db(db, username, password, ip, port): to set up database; supported "mysql" and postgresql" for 'db' argument.

min_link(source_url, dest_url, limit = 6): find minimum number of link from source url to destination url within limit (default=6)

### Examples

```
>>> from wikilink import wiki_link
>>> model = wiki_link.WikiLink()
>>> model.setup_db("mysql", "root", "12345", "127.0.0.1", "3306")
>>> model.min_link(source_url, dest_url, 6)
```

Alternatively, you can simply modify starting_url and ending_url in the script [sample.py](https://github.com/tranlyvu/wiki-link) and run:

```
$ python sample.py
```

---
Contribution
---

Please follow [contribution instruction](https://github.com/tranlyvu/wiki-link/blob/dev/CONTRIBUTING.md) and [code of conduct](https://github.com/tranlyvu/wiki-link/blob/dev/CODE-OF-CONDUCT.md)

### Development setup

Wiki-link was developed using python 3.6, simply run the following on your development environment:

```
$ pip install -r requirements.txt
```

Or to set up environment with virtualenv

```
$ cd <path to wikilink project>
$ python3 -m venv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

If you are done working in the virtual environment for the moment, you can deactivate it:

```
$ deactivate
```

### [List of contributors](https://github.com/tranlyvu/wiki-link/blob/dev/CONTRIBUTORS.md)

### Hall of Fame

[![](https://sourcerer.io/fame/tranlyvu/tranlyvu/wiki-link/images/0)](https://sourcerer.io/fame/tranlyvu/tranlyvu/wiki-link/links/0)[![](https://sourcerer.io/fame/tranlyvu/tranlyvu/wiki-link/images/1)](https://sourcerer.io/fame/tranlyvu/tranlyvu/wiki-link/links/1)[![](https://sourcerer.io/fame/tranlyvu/tranlyvu/wiki-link/images/2)](https://sourcerer.io/fame/tranlyvu/tranlyvu/wiki-link/links/2)[![](https://sourcerer.io/fame/tranlyvu/tranlyvu/wiki-link/images/3)](https://sourcerer.io/fame/tranlyvu/tranlyvu/wiki-link/links/3)[![](https://sourcerer.io/fame/tranlyvu/tranlyvu/wiki-link/images/4)](https://sourcerer.io/fame/tranlyvu/tranlyvu/wiki-link/links/4)[![](https://sourcerer.io/fame/tranlyvu/tranlyvu/wiki-link/images/5)](https://sourcerer.io/fame/tranlyvu/tranlyvu/wiki-link/links/5)[![](https://sourcerer.io/fame/tranlyvu/tranlyvu/wiki-link/images/6)](https://sourcerer.io/fame/tranlyvu/tranlyvu/wiki-link/links/6)[![](https://sourcerer.io/fame/tranlyvu/tranlyvu/wiki-link/images/7)](https://sourcerer.io/fame/tranlyvu/tranlyvu/wiki-link/links/7)

---
Project Architecture
---

An overview of the project can be found [here](https://tranlyvu.github.io/BFS-and-a-simple-application/).

---
Release History
---
* v1.2.0 - Jan 23, 2019
	* Re-define API
	* Publish to PyPi

* v1.0.1 - Jan 14, 2018
	* Fix database connection bug
	* Test PostgreSQL database

* v1.0.0 - Nov 7, 2016 
    * First official release

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

