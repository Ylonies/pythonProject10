from flask import Flask, render_template
from werkzeug.utils import redirect

from data import db_session
from data.users import User
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars_explorer.db")
    app.run()

if __name__ == '__main__':
    main()

