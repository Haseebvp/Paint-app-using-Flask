from flask import *
import psycopg2
app=Flask(__name__)
@app.route('/')
def welcome():
	return render_template('welcome.html')
@app.route('/home')
def home():
	return render_template('home.html')

@app.route('/save/<filename>',methods=['POST'])
def save(filename=None):
	con=psycopg2.connect(database='has')
	c=con.cursor()
	c.execute('insert into blog7 (filename,imagedata) values(%s,%s)',[request.form['name'],request.form['data']])
	con.commit()
	return render_template('home.html')
@app.route('/gallery')
def gallery():
	con=psycopg2.connect(database='has')
	c=con.cursor()
	c.execute('select * from blog7 ORDER BY id desc')
	value=[dict(id=i[0],filename=i[1])for i in c.fetchall()]
	return render_template('post.html',value=value)
@app.route('/gallery/<filename>',methods=['GET'])
def load(filename=None):
	con=psycopg2.connect(database='has')
	c=con.cursor()
	c.execute('select * from blog7 where filename=%s ',[filename])
	value1=[dict(id=i[0],filename=i[1],imagedata=i[2])for i in c.fetchall()]
	print value1
	return render_template('load.html',value1=value1)
@app.route('/close')
def close():
	return render_template('welcome.html')

	
	
app.run(debug=True)
