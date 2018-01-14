from wikilink.wiki_link import WikiLink

def main():
	starting_url = '/wiki/Barack_Obama'
	ending_url = '/wiki/Bill_Clinton'
	model = WikiLink(starting_url, ending_url)
	print("Smallest number of separation is " + str(model.search()))

if __name__ == "__main__": main()