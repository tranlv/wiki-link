# **wikilink**

<p align="center">
	<a href="https://pypi.org/project/wikilink/"><img src="https://img.shields.io/pypi/v/wikilink.svg"></a>
	<a href="https://pepy.tech/project/wikilink"><img src="https://pepy.tech/badge/wikilink"></a>
</p>

---
wikilink is a multiprocessing web-scraping *application* to scrape the wiki pages, extract urls and find the minimum number of links between 2 given wiki pages.

The project is an implementation of 6-degree of separation in wikipedia that mentioned in [Web Scraping with Python](https://www.amazon.com/Web-Scraping-Python-Collecting-Modern/dp/1491985577/ref=pd_sbs_14_1/142-3292117-4986818?_encoding=UTF8&pd_rd_i=1491985577&pd_rd_r=49ea33a0-0484-4844-bab3-9685cf433745&pd_rd_w=2Pza3&pd_rd_wg=GQY3c&pf_rd_p=e20a7044-dca9-4b2c-8da8-05b176efe6fb&pf_rd_r=J1KTRH8PTY7EMB7XYY7B&psc=1&refRID=J1KTRH8PTY7EMB7XYY7B), you can find more details of the project in [my blog](https://distributedsystemsblog.com/posts/shortest-path-problem-unweighted-graph/).

The project is currently at version [v0.3.0.post1](https://github.com/tranlyvu/wiki-link/releases), also see [change log](https://github.com/tranlyvu/wiki-link/blob/master/CHANGELOG.md) for more details on release history. If you like this project, feel fee to leave a few words of appreciation here [![Say Thanks!](https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg)](https://saythanks.io/to/vutransingapore%40gmail.com)

| Build | [![Build Status][3]][4] | [![Coverage Status][5]][6] | 
| :--- | :--- | :---  |
| **Quality** | [![Maintainability][13]][14] | [![Requirements Status][19]][20] |
| **Platform** | [![python version](https://img.shields.io/pypi/pyversions/wikilink.svg)](https://pypi.org/project/wikilink/)| [![implementation](https://img.shields.io/pypi/implementation/wikilink.svg)](https://pypi.org/project/wikilink/) |

[3]: https://travis-ci.org/tranlyvu/wiki-link.svg?branch=master
[4]: https://travis-ci.org/tranlyvu/wiki-link 
[5]: https://coveralls.io/repos/github/tranlyvu/wiki-link/badge.svg
[6]: https://coveralls.io/github/tranlyvu/wiki-link

[13]: https://api.codeclimate.com/v1/badges/8679cde6756683bd787d/maintainability
[14]: https://codeclimate.com/github/tranlyvu/wiki-link/maintainability

[19]: https://requires.io/github/tranlyvu/wiki-link/requirements.svg?branch=master
[20]: https://requires.io/github/tranlyvu/wiki-link/requirements/?branch=master

---
Table of contents
---

1. [Usage](#Usage)
2. [Contribution](#Contribution) 
3. [License](#License)

---
Usage
---

Install with pip

```
$ pip install wikilink
```

### Database support

wikilink needs to access to database to store the extracted urls, it currently supports [Mysql](https://www.mysql.com/downloads/) and [PostgreSQL](https://www.postgresql.org/)

### API

```
setup_db(db, username, password, ip="127.0.0.1", port=3306): set up database

Args:
	db(str): Database engine, currently support "mysql" and "postgresql"
	name(str): database username
	password(str): database password
	ip(str): IP address of database (Default = "127.0.0.1")
	port(str): port that databse is running on (default=3306)

Returns:
	None
```

```
min_link(source, destination, limit=6, multiprocessing=False): find minimum number of link from source url to destination url within limit 

Args:
	source(str): source wiki url, i.e. "https://en.wikipedia.org/wiki/Cristiano_Ronaldo"
	destination(str): Destination wiki url, i.e. "https://en.wikipedia.org/wiki/Cristiano_Ronaldo"
	limit(int): max number of links from the source that will be considered (default=6)
	multiprocessing(boolean): enable/disable multiprocessing mode (default=False)

Returns:
	(int) minimum number of sepration between source and destination urls
	return None and print messages if exceeding limits or no path found

Raises:
	DisconnectionError: error connecting to DB
```

### Examples

```
>>> from wikilink import WikiLink
>>> app = WikiLink()
>>> app.setup_db("mysql", "root", "12345", "127.0.0.1", "3306")
>>> source = "https://en.wikipedia.org/wiki/Cristiano_Ronaldo"
>>> destination = "https://en.wikipedia.org/wiki/Lionel_Messi"
>>> app.min_link(source, destination, 6)
1
```

---
Contribution [![Open Source Helpers][7]][8]
---
[7]: https://www.codetriage.com/tranlyvu/wiki-link/badges/users.svg
[8]: https://www.codetriage.com/tranlyvu/wiki-link

### How to contribute

Please follow our contribution convention at [contribution instructions](https://github.com/tranlyvu/wiki-link/blob/master/CONTRIBUTING.md) and [code of conduct](https://github.com/tranlyvu/wiki-link/blob/master/CODE-OF-CONDUCT.md).

To set up development environment, simply run:

```
$ pip install -r requirements.txt
```

Please check out the [issues](https://github.com/tranlyvu/wiki-link/issues) for list of issues that required helps.


### Appreciation

Feel free to add your name into the [list of contributors](https://github.com/tranlyvu/wiki-link/blob/master/CONTRIBUTORS.md). You will automatically be inducted into Hall of Fame as a way to show my appreciation for your contributions.

#### Hall of Fame

[![](https://sourcerer.io/fame/tranlyvu/tranlyvu/wiki-link/images/0)](https://sourcerer.io/fame/tranlyvu/tranlyvu/wiki-link/links/0)[![](https://sourcerer.io/fame/tranlyvu/tranlyvu/wiki-link/images/1)](https://sourcerer.io/fame/tranlyvu/tranlyvu/wiki-link/links/1)[![](https://sourcerer.io/fame/tranlyvu/tranlyvu/wiki-link/images/2)](https://sourcerer.io/fame/tranlyvu/tranlyvu/wiki-link/links/2)[![](https://sourcerer.io/fame/tranlyvu/tranlyvu/wiki-link/images/3)](https://sourcerer.io/fame/tranlyvu/tranlyvu/wiki-link/links/3)[![](https://sourcerer.io/fame/tranlyvu/tranlyvu/wiki-link/images/4)](https://sourcerer.io/fame/tranlyvu/tranlyvu/wiki-link/links/4)[![](https://sourcerer.io/fame/tranlyvu/tranlyvu/wiki-link/images/5)](https://sourcerer.io/fame/tranlyvu/tranlyvu/wiki-link/links/5)[![](https://sourcerer.io/fame/tranlyvu/tranlyvu/wiki-link/images/6)](https://sourcerer.io/fame/tranlyvu/tranlyvu/wiki-link/links/6)[![](https://sourcerer.io/fame/tranlyvu/tranlyvu/wiki-link/images/7)](https://sourcerer.io/fame/tranlyvu/tranlyvu/wiki-link/links/7)

---
License
---

See the [LICENSE](https://github.com/tranlyvu/wiki-link/blob/master/LICENSE) file for license rights and limitations (Apache License 2.0).

