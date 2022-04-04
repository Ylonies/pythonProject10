from flask import Flask, render_template
from werkzeug.utils import redirect

from data import db_session
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

def main():
    db_session.global_init("db/mars_explorer.db")
    add_user(["Scott", "Ridley", 21, "captain", "research engineer", "module_1", "scott_chief@mars.org", "cap"])
    add_user(["Green", "Lucy", 30, "captain helper", "research engineer", "module_1", "lucy_thebest@mars.org", "best"])
    add_user(["Black", "Saimon", 25, "usual worker", "scientist", "module_1", "black@mars.org", "saimon"])
    add_user(["Gagarina", "Polina", 50, "usual worker", "chief", "module_1", "gagrin@mars.org", "space"])
    app.run()


if __name__ == '__main__':
    main()

