from findlink.findLink import my_findLink

def main():
	starting_url='/wiki/Barack_Obama'
	ending_url='/wiki/Bill_Clinton'
	model=my_findLink(starting_url,ending_url)
	model.search()
	model.printLinks()

if __name__=="__main__":
	main()