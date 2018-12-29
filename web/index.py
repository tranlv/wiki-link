from flask import Flask, request,render_template
from wikilink.wiki_link import WikiLink

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def main():
	return render_template('hello.html')

@app.route("/", methods=['POST'])
def main_post():
	try :
		starting_link = request.form['Starting wiki link']
		ending_link = request.form['Ending wiki link']
	except:
		#to do

	if request.form('Limit') == ''
		limit ==  6
	else: 
		limit = request.form('Limit')

	model = WikiLink(starting_url, ending_url)
	if model.search() is not None: 
		answer = "Smallest number of separation is " + str(model.search())		
		print(answer)
	return 

if __name__ == "__main__":
    app.run()