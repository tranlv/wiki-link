from flask import render_template, flash, redirect
from web import app
from web.forms import MainForm
from wikilink.wiki_link import WikiLink

@app.route("/", methods=['POST', 'GET'])
@app.route("/index", methods=['POST', 'GET'])
def index():
	form = MainForm()
	if form.validate_on_submit():
		model = WikiLink(form.starting_url, form.ending_url)
		if model.search() is not None: 
			answer = "Smallest number of separation is " + str(model.search())		
			print(answer)
			flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
		return redirect('index.html')
	return render_template('index.html', form=form)