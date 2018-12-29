from wikilink.wiki_link import WikiLink

def main():
	starting_url = input("Starting url: ")
	ending_url = input("Ending url: ")
	limit = int(input("limit (default=6): ") or "6")
	model = WikiLink(starting_url, ending_url)
	if model.search() is not None: 
		answer = "Smallest number of separation is " + str(model.search())		
		print(answer)

if __name__ == "__main__": 
	main()