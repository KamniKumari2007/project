from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>I am Home page</h1>
    <h2>I am running in flask</h2>
    """
@app.route("/about")
def abouta():
    return """
    <h1>I am about page</h1>
    <h2>I am running in flask</h2>
    """
if __name__=='__main__':
    app.run(debug=True)