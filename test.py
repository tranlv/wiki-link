from wikilink import wiki_link
model = wiki_link.WikiLink()
model.setup_db("mysql", "root", "13061990", "127.0.0.1", "3306")
source_url = "https://en.wikipedia.org/wiki/Cristiano_Ronaldo"
dest_url = "https://en.wikipedia.org/wiki/Software_engineer"
print(model.min_link(source_url, dest_url, 6, 2))