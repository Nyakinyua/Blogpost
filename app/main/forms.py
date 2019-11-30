from flask_wtf import FlaskForm
from wtforms.validators import Required
from wtforms import SubmitField,TextAreaField
from wtforms import StringField,PasswordField,SubmitField,BooleanField,SubmitField,TextAreaField
from wtforms import ValidationError



class BlogForm(FlaskForm):
    title = StringField('Title',validators=[Required()])
    blog_post = TextAreaField('Post',validators=[Required()])
    submit = SubmitField('submit')




class CommentForm(FlaskForm):
	description = TextAreaField('Add comment',validators=[Required()])
	submit = SubmitField()



class UpdateProfile(FlaskForm):
    bio = TextAreaField("Whats New?",validators=[Required()])
    submit = SubmitField("Submit")