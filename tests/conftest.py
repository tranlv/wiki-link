import pytest
from wikilink.wiki_link import WikiLink


@pytest.fixture()
def engine():
    return create_engine('postgresql://localhost/test_database')
