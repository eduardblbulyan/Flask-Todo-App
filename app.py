from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy, session
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
        task_content = request.form['content'] # understand by `id` and `name`
        task = Todo(content=task_content)
        try:
            db.session.add(task)
            db.session.commit()
            return redirect("/")
        except:
            return "An error occured!"
    else:
        tasks = Todo.query.order_by(Todo.date).all()
        return render_template('index.html', tasks=tasks)

@app.route('/delete/<int:id>')
def delete(id):
    task = Todo.query.get_or_404(id)
    try:
        db.session.delete(task)
        db.session.commit()
        return redirect("/")
    except:
        return "An error occured!"

    

if __name__ == "__main__":
    app.run()
