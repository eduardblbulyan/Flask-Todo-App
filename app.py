from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///flask_todo.db"
db = SQLAlchemy(app)
#app.app_context().push()

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return f"Task {self.id}"


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        pass
    else:
        #return render_template('index.html')
        pass

if __name__ == "__main__":
    app.run()
