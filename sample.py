from findlink.find_link import FindLink

def main():
	starting_url = '/wiki/Barack_Obama'
	ending_url = '/wiki/Bill_Clinton'
	model = FindLink(starting_url,ending_url)
	model.search()
	model.print_links()

if __name__ == "__main__":
	main()