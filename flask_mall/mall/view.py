from flask import Blueprint, render_template
from flask_login import login_required

mall = Blueprint('mall', __name__,
                 template_folder='templates',
                 static_folder='static')


@mall.route('/')
@login_required
def product():
    return render_template('product.html')
