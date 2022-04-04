from flask import Flask, render_template
from werkzeug.utils import redirect

from data import db_session
from data.jobs import Jobs
from data.users import User
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def add_user(params):

    user = User()
    user.surname = params[0]
    user.name = params[1]
    user.age = params[2]
    user.position = params[3]
    user.speciality = params[4]
    user.address = params[5]
    user.email = params[6]
    user.hashed_password = params[7]
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()

@app.route("/")
def main():
    db_session.global_init("db/mars_explorer.db")
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return render_template("index.html", jobs = jobs)

if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.2')

