from flask import Flask, render_template
from accounts.view import accounts, login_manager
from mall.view import mall
from models import db

app = Flask(__name__)
app.config.from_object('config.Config')
db.init_app(app)
login_manager.init_app(app)
app.register_blueprint(accounts, url_prefix='/accounts')
app.register_blueprint(mall, url_prefix='/mall')


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
