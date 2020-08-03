
from flask import Flask, render_template, url_for , request , redirect
app = Flask(__name__)


@app.route('/')
def hp():
    return render_template('index.html')



@app.route('/works.html')
def hp1():
    return render_template('work.html')


@app.route('/about.html')
def hp2():
    return render_template('about.html')

@app.route('/contact.html')
def hp3():
    return render_template('contact.html')

@app.route('/components.html')
def hp4():
    return render_template('components.html')


# method to write in a python file #
def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email=data["name"]
        subject=data["subject"]
        message=data["message"]
        file=database.write(f'\n{email},{subject},{message}')

@app.route('/submit_form', methods=['POST','GET'])
def submits_form():
    if request.method =='POST':
        data = request.form.to_dict()
        write_to_file(data)
    return render_template("thanks.html")