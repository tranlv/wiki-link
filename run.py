from wikilink import wiki_link

def main():
	starting_url = "https://en.wikipedia.org/wiki/Cristiano_Ronaldo" 
	ending_url = "https://en.wikipedia.org/wiki/Association_football"
	model = wiki_link.WikiLink()
	model.setup_db("mysql", "root", "12345", "127.0.0.1", "3306")
	print(model.search(starting_url, ending_url, 6))

if __name__ == "__main__":
	main()