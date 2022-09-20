import uuid

from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement='auto')
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    is_active = db.Column(db.Boolean, default=True)

    def set_password(self, password):
        # encrypt password
        self.password = generate_password_hash(password, method='sha256')

    def check_password(self, password):
        # check password
        return check_password_hash(self.password, password)


class Product(db.Model):
    """ products """
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True, autoincrement='auto')
    # UID
    uid = db.Column(db.String(128), nullable=False, default=uuid.uuid4, unique=True)
    # product title
    name = db.Column(db.String(128), nullable=False)
    # product description
    content = db.Column(db.Text, nullable=False)
    # product type
    types = db.Column(db.String(10), nullable=False)
    # price
    price = db.Column(db.Integer, nullable=False)
    # main picture
    img = db.Column(db.String(256), nullable=False)
    # product status
    status = db.Column(db.String(10), nullable=False)
    # product total counts
    sku_count = db.Column(db.Integer, default=0)
    # left counts
    remain_count = db.Column(db.Integer, default=0)
    # logic delete
    is_valid = db.Column(db.Boolean, default=True)
    # order
    reorder = db.Column(db.Integer, default=0)
    # built time
    created_at = db.Column(db.DateTime)
    # last update time
    updated_at = db.Column(db.DateTime)


class Tag(db.Model):
    """ product tag """
    __tablename__ = 'product_tag'
    id = db.Column(db.Integer, primary_key=True, autoincrement='auto')  # 主键
    # UID
    uid = db.Column(db.String(128), nullable=False, default=uuid.uuid4, unique=True)
    # tag name
    name = db.Column(db.String(128), nullable=False)
    # tag description
    desc = db.Column(db.String(256))
    # logic delete
    is_valid = db.Column(db.Boolean, default=True)
    # order
    reorder = db.Column(db.Integer, default=0)
    # create time
    created_at = db.Column(db.DateTime)
    # last update time
    updated_at = db.Column(db.DateTime)


class ProductTags(db.Model):
    """ product and tag relation """
    __tablename__ = 'product_tag_rel'
    id = db.Column(db.Integer, primary_key=True, autoincrement='auto')  # 主键
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    tag_id = db.Column(db.Integer, db.ForeignKey('product_tag.id'))
