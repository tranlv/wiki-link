from flask import render_template, flash, redirect
from web import app
from web.forms import MainForm
from wikilink.wiki_link import WikiLink

@app.route("/", methods=['POST', 'GET'])
@app.route("/index", methods=['POST', 'GET'])
def index():
	form = MainForm()
	if form.validate_on_submit():
		starting_url, ending_url = str(form.starting_link), str(form.ending_link)
		model = WikiLink(starting_url, ending_url)
		if model.search() is not None: 
			answer = "Smallest number of separation is " + str(model.search())		
			flash(answer)
		else:
			flash("no answer")
	return render_template('index.html', form=form)