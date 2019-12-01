from flask_wtf import FlaskForm
from wtforms.validators import Required,Email
from wtforms import SubmitField,TextAreaField
from wtforms import StringField,PasswordField,SubmitField,BooleanField,SubmitField,TextAreaField
from wtforms import ValidationError
from ..models import Subscribe


class BlogForm(FlaskForm):
    category=SelectField(u'Enter Blog Category', choices =[('Lifestyle Blogs','Lifestyle Blogs'),('Entertainment Blogs','Entertainment Blogs'),('Education Blogs','Education Blogs'),('Religious Blogs','Religious Blogs'),('Political Blogs','Political Blogs'),('Fashion Blogs','Fashion Blogs')]
    title = StringField('Title',validators=[Required()])
    blog_post = TextAreaField('Post',validators=[Required()])
    submit = SubmitField('submit')




class CommentForm(FlaskForm):
	description = TextAreaField('Add comment',validators=[Required()])
	submit = SubmitField()



class UpdateProfile(FlaskForm):
    bio = TextAreaField("Whats New?",validators=[Required()])
    submit = SubmitField("Submit")
    
class subscribeForm(FlaskForm):
    
    
    '''
    class that defines how the subscribe form fields to be filled
    '''
    
    email=StringField('Enter your email address',validators=[Required(),Email()])
    submit=SubmitField('Subscirbe')
    

def validate_email(self,data_field):
    '''
    function that validates no email duplicates
    '''
    if Subscribe.query.filter_by(email=data_field.data).first():
      raise ValidationError('That Email is taken.Please use another email')