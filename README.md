# **wikilink** [![version][23]][24] [![Downloads][25]][26] [![HitCount][21]][22] [![star this repo][27]][28] [![fork this repo][29]][30]
[21]: http://hits.dwyl.io/tranlyvu/wiki-link.svg
[22]: http://hits.dwyl.io/tranlyvu/wiki-link
[23]: https://img.shields.io/pypi/v/wikilink.svg
[24]: https://pypi.org/project/wikilink/
[25]: https://pepy.tech/badge/wikilink
[26]: https://pepy.tech/project/wikilink
[27]: http://githubbadges.com/star.svg?user=tranlyvu&repo=wiki-link&style=default
[28]: https://github.com/tranlyvu/wiki-link
[29]: http://githubbadges.com/fork.svg?user=tranlyvu&repo=wiki-link&style=default
[30]: https://github.com/tranlyvu/wiki-link/fork

A web-scraping application to find the minimum number of links between 2 given wiki pages.


| Build | [![Build Status][3]][4] | [![Coverage Status][5]][6] | 
| :--- | :--- | :---  |
| **Quality** | [![Maintainability][13]][14] | [![Requirements Status][19]][20] |
| **Support** | [![Join the chat][17]][18] | [![blog][1]][2] |

[3]: https://travis-ci.org/tranlyvu/wiki-link.svg?branch=dev
[4]: https://travis-ci.org/tranlyvu/wiki-link 
[5]: https://coveralls.io/repos/github/tranlyvu/wiki-link/badge.svg
[6]: https://coveralls.io/github/tranlyvu/wiki-link

[13]: https://api.codeclimate.com/v1/badges/8679cde6756683bd787d/maintainability
[14]: https://codeclimate.com/github/tranlyvu/wiki-link/maintainability

[17]: https://badges.gitter.im/find-link/Lobby.svg
[18]: https://gitter.im/find-link/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge
[1]: https://img.shields.io/badge/docs-on%20blog-brightgreen.svg
[2]: https://tranlyvu.github.io/algorithms/BFS-and-a-simple-application/

[19]: https://requires.io/github/tranlyvu/wiki-link/requirements.svg?branch=dev
[20]: https://requires.io/github/tranlyvu/wiki-link/requirements/?branch=dev

<img src="img/link.jpg" width="480" alt="Combined Image" />

---
Table of contents
---

1. [Usage](#Usage)
2. [Contribution](#Contribution) 
3. [Project Architecture](#Project-Architecture)
4. [Release History](#Release-History)
5. [Contact](#Contact)
6. [License](#License)

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

---
Contribution [![Open Source Helpers][7]][8]
---
[7]: https://www.codetriage.com/tranlyvu/wiki-link/badges/users.svg
[8]: https://www.codetriage.com/tranlyvu/wiki-link

### How to contribute

Please follow our contribution convention at [contribution instructions](https://github.com/tranlyvu/wiki-link/blob/dev/CONTRIBUTING.md) and [code of conduct](https://github.com/tranlyvu/wiki-link/blob/dev/CODE-OF-CONDUCT.md).

To set up development environment, simply run:

```
$ pip install -r requirements.txt
```

### List of issues

1. Implement function to print path ([#16](https://github.com/tranlyvu/wiki-link/issues/16))
2. Update unit test ([#11](https://github.com/tranlyvu/wiki-link/issues/11))

### Appreciation

Feel free to add your name into the [list of contributors](https://github.com/tranlyvu/wiki-link/blob/dev/CONTRIBUTORS.md). You will automatically be inducted into Hall of Fame as a way to show my appreciation for your contributions.

#### Hall of Fame

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

If you like my project, feel fee to leave a few words of appreciation here [![Say Thanks!](https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg)](https://saythanks.io/to/tranlyvu)

---
License
---

See the [LICENSE](https://github.com/tranlyvu/wiki-link/blob/master/LICENSE) file for license rights and limitations (Apache License 2.0).

