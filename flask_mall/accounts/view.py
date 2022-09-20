import flask
from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import LoginManager, login_required, logout_user, login_user, current_user
from werkzeug.exceptions import abort

from forms import LoginForm, SignupForm, ProfileForm
from models import User, db

accounts = Blueprint('accounts', __name__,
                     template_folder='templates',
                     static_folder='static')
login_manager = LoginManager()


@accounts.route('/', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        email = form.userEmail.data
        password = form.password.data
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page or url_for('index'))
        flask.flash(' *Invalid email or password* ')
        return redirect(url_for('accounts.login'))
    return render_template('login.html', form=form)


@accounts.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@accounts.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = ProfileForm()
    if form.validate_on_submit():
        email = form.userEmail.data
        password = form.password.data
        confirm_password = form.confirm_password.data
        username = form.username.data
        if password != confirm_password:
            flask.flash(' *Passwords need same* ')
        else:
            user = User.query.filter_by(email=email, is_active=True).first()
            if user is None:
                abort(404)
            else:
                user.username = username
                user.email = email
                if user.check_password(password):
                    flask.flash(' *New password is same with old ones *')
                user.set_password(password)
                db.session.add(user)
                db.session.commit()
                flask.flash('Update successfully')
                return redirect(url_for('index'))
    return render_template('profile.html', form=form)


@accounts.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        email = form.userEmail.data
        password = form.password.data
        confirm_password = form.confirm_password.data
        username = form.username.data
        if password != confirm_password:
            flask.flash('*Passwords need same*')
        else:
            user = User.query.filter_by(email=email).first()
            if user is None:
                user = User(email=email, username=username)
                user.set_password(password)
                db.session.add(user)
                db.session.commit()
                login_user(user)
                return redirect(url_for('index'))
            flask.flash('Email has an account')
    return render_template('signup.html', form=form)


@login_manager.user_loader
def load_user(user_id):
    if user_id is not None:
        return User.query.get(user_id)
    return None


@login_manager.unauthorized_handler
def unauthorized():
    flask.flash('You need to log in')
    return redirect(url_for('accounts.login'))
