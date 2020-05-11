from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import DataRequired, ValidationError
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')
    
class CommentForm(FlaskForm):
    comment = StringField('Comment')
    submit = SubmitField('Post')

class Subscribe(FlaskForm):
    submit = SubmitField('Subscribe')
