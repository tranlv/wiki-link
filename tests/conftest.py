import pytest
from wikilink.wiki_link import WikiLink


@pytest.fixture()
def engine():
    return create_engine('postgresql://localhost/test_database')



@pytest.fixture()
def wikilin_db_connection(tmpdir):
	WikiLink.setup_db()
	yield

