import pytest
from wikilink.wiki_link import WikiLink
import string
from random import randint, SystemRandom

MIN_CHAR = 8
MAX_CHAR = 16
ALL_CHAR = string.ascii_letters + string.punctuation + string.digits


def test_setup_db_mysql(wikilin_db_connection):
	password = "".join(SystemRandom().choice(ALL_CHAR) for x in range(randint(MIN_CHAR, MAX_CHAR)))
	name = "".join(SystemRandom().choice(ALL_CHAR) for x in range(randint(MIN_CHAR, MAX_CHAR)))
	model = WikiLink()
	model.setup_db("mysql", name, password, "127.0.0.1", "3306")

	actual = model.db.connection
	expected = "mysql://" + name + ":" + password + "@" + ip + ":" + port

	assert actual == expected
