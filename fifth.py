from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

# Set a secret key for session management
app.secret_key = b'\x95\x86\x89\xfd\x01\xfc\xef2\x00\xa4v\xf5L\xc62\x93[\xc6\x07SY\x1a\xa4\x04'


# Define a route for the home page
@app.route('/')
def home():
    # Check if the user is logged in
    if 'username' in session:
        username = session['username']
        return render_template('home.html', username=username)
    else:
        return redirect(url_for('login'))

# Define a route for the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get the username from the form
        username = request.form['username']
        
        # Store the username in the session
        session['username'] = username

        return redirect(url_for('home'))

    return render_template('login.html')

# Define a route for the logout page
@app.route('/logout')
def logout():
    # Remove the username from the session if it exists
    session.pop('username', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
