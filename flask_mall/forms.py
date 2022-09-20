from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField, StringField, TextAreaField, SelectField, IntegerField, \
    FileField, BooleanField

import constants


class LoginForm(FlaskForm):
    userEmail = EmailField(
        'Email',
        render_kw={
            'id': 'userEmail',
            'class': 'input',
            'placeholder': 'email@example.com',
            'required': 'required'
        }
    )
    password = PasswordField(
        'Password',
        render_kw={
            'id': 'password',
            'class': 'input',
            'data - type': 'password',
            'required': 'required',
            'placeholder': 'Enter your password'
        }
    )
    submit = SubmitField(
        'Login',
        render_kw={
            'class': 'button'
        }
    )


class SignupForm(FlaskForm):
    userEmail = EmailField(
        'Email',
        render_kw={
            'id': 'userEmail_signup',
            'class': 'input',
            'placeholder': 'email@example.com',
            'required': 'required'
        }
    )
    password = PasswordField(
        'Password',
        render_kw={
            'id': 'password_signup',
            'class': 'input',
            'data - type': 'password',
            'required': 'required',
            'placeholder': 'Enter your password'
        }
    )

    confirm_password = PasswordField(
        'Confirm Password',
        render_kw={
            'id': 'password_signup',
            'class': 'input',
            'data - type': 'password',
            'required': 'required',
            'placeholder': 'Confirm your password'
        }
    )
    username = StringField(
        'Name',
        render_kw={
            'id': 'username',
            'class': 'input',
        }
    )

    submit = SubmitField(
        'SignUp',
        render_kw={
            'class': 'button sign-up-bt'
        }
    )


class ProfileForm(FlaskForm):
    userEmail = EmailField(
        'Email',
        render_kw={
            'id': 'userEmail_signup',
            'class': 'input',
            'required': 'required',
            'placeholder': 'Enter your email'

        }
    )
    password = PasswordField(
        'New Password',
        render_kw={
            'id': 'password_signup',
            'class': 'input',
            'data - type': 'password',
            'required': 'required',
            'placeholder': 'Enter your new password'
        }
    )

    confirm_password = PasswordField(
        'Confirm Password',
        render_kw={
            'id': 'password_signup',
            'class': 'input',
            'data - type': 'password',
            'required': 'required',
            'placeholder': 'Confirm your password'
        }
    )
    username = StringField(
        'Name',
        render_kw={
            'id': 'username',
            'class': 'input',
        }
    )

    submit = SubmitField(
        'Update Account',
        render_kw={
            'class': 'button sign-up-bt'
        }
    )


class ProductEditForm(FlaskForm):
    """ Add new product """
    name = StringField(label='product title',
                       description='title is less than 200 words',
                       render_kw={
                        'class': 'form-control',
                        'placeholder': 'product title'
                    })
    content = TextAreaField(label='product description',
                            render_kw={
                                'class': 'form-control',
                                'placeholder': 'product description'
                            })
    types = SelectField(label='product type',
                            choices=constants.PRODUCT_TYPES,
                            render_kw={
                                'class': 'form-control',
                            })
    price = IntegerField(label='product price',
                            render_kw={
                                'class': 'form-control',
                            })
    img = FileField(label='product image')
    status = SelectField(label='product type',
                         choices=constants.PRODUCT_STATUS,
                            render_kw={
                                'class': 'form-control',
                            })
    sku_count = IntegerField(label='product accounts',
                            render_kw={
                                'class': 'form-control',

                            })

    is_valid = BooleanField(label='logic delete')
    reorder = IntegerField(label='order',
                            render_kw={
                                'class': 'form-control',
                            })
