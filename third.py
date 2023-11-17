from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to the Flask App with URL Parameters!'

@app.route('/greet')
def greet():
    # Get the 'name' parameter from the URL
    name = request.args.get('name', 'Guest')
    return render_template('greet.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
