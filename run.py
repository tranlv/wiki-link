from wikilink.wiki_link import WikiLink

def main():
	starting_url = input("Starting url: ")
	ending_url = input("Ending url: ")
	model = WikiLink(starting_url, ending_url)
	print("Smallest number of separation is " + str(model.search()))

if __name__ == "__main__": 
	main()