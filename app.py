from flask import *  
from flask import send_file
from pdf_scraping import scrap
from test import printme
from flask import Flask, render_template
from graph import build_graph
from monthAgg import monthExpense
from keywordAgg import keywordExpenses
from summaryGraph import summaryGraph
from flask import Flask, render_template,request
from flask_wtf import FlaskForm
from wtforms import StringField
 
app = Flask(__name__)  
app.config['SECRET_KEY'] ='dev'

class LoginForm(FlaskForm):
	month = StringField('month')
	
class keywordForm(FlaskForm):
	keyword = StringField('keyword')

#@app.route('/form',methods=['POST','GET'])
#def form():
#	form = LoginForm()
	
#	if form.validate_on_submit():
#		name=request.form['username']
#		print(name)
#		return "Hi"+name
		
#	return render_template('forms.html',form=form)
		
@app.route('/monthlyExpenses',methods=['POST','GET'])
def graphs():
    #These coordinates could be stored in DB
	form = LoginForm()
	if form.validate_on_submit():
		name=request.form['month']
		print(name)
		graph1_url = monthExpense(name)
		return render_template('graphs.html',graph1=graph1_url)
	return render_template('forms.html',form=form)

@app.route('/keywordExpenses',methods=['POST','GET'])
def keyword():
	form = keywordForm()
	if form.validate_on_submit():
		name=request.form['keyword']
		print(name)
		graph1_url = keywordExpenses(name)
		return render_template('keywordAgg.html',amount=graph1_url)
	return render_template('keywordForm.html',form=form)
	
	
@app.route('/summaryExpense')
def summary():
    #These coordinates could be stored in DB
    
    graph1_url = summaryGraph('1.0');
   
 
    return render_template('graphs.html',
    graph1=graph1_url)

@app.route('/')  
def upload():  
    return render_template("index.html")  
 
@app.route('/success', methods = ['POST'])  
def success():
	if request.method == 'POST':
		f = request.files['file']
		f.save(f.filename)
		mesg = scrap(f.filename)
		return render_template('success.html', filename=f.filename)
		#scrap(f.filename)
		#render_template("success.html", name = f.filename) 

@app.route('/file-downloads/')
def file_downloads():
	try:
		return render_template('downloads.html')
	except Exception as e:
		return str(e)		
		
@app.route('/return-files/')
def return_files_tut():
	try:
		return send_file('C:\\Users\\nidhi\\Desktop\\UCSC_Spring\\WebScraping\\bankStatements.csv', attachment_filename='bankStatements.csv')
	except Exception as e:
		return str(e)
  
if __name__ == '__main__':  
    app.run(debug = True)  