#4. Create a Flask app with a form that accepts user input and displays it

from flask import Flask , render_template , request , redirect , url_for

app = Flask(__name__)


@app.route('/')
def index1():
    return render_template('index1.html')

@app.route('/submit', methods = ['POST'])
def submit():
    if request.method == 'POST':
        user_input = request.form['user_input']
        return render_template('result.html', user_input=user_input)
    else:
        return redirect(url_for(index1))

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000, debug=True)