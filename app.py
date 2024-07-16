from flask import Flask, render_template_string
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///flask_todo.db"
db = SQLAlchemy(app)

@app.route("/")
def index():
    return render_template_string("<h1>Works</h1>")

if __name__ == "__main__":
    app.run()
