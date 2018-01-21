from flask import Flask, render_template

app = Flask("__name__")
@app.route('/')
def home():
	
	return render_template('amber.html')

if __name__ == "__main__":
    app.secret_key = 'secret123'
    app.run(debug = True)  