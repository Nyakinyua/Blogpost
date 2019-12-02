from . import main
from ..requests import get_quotes
from flask import render_template, request, redirect, url_for,abort
from flask_login import login_required,current_user
from ..models import User,Blog_post,Comment
from .forms import UpdateProfile, BlogForm
from .. import db,photos

@main.route('/')
def index():
    
    '''
    View root page function that returns the index page and its data
    '''
    
    #Getting random Quotes
    random_quotes=get_quotes()
    print(random_quotes)
    title = "Home- Nyakinyua Blog post"
    
    return render_template('index.html',title=title,random_quotes=random_quotes) 




@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username=uname).first()
    
    if user is None:

        abort(404)
    bloglist = Blog_post.get_blog(user.username)

    return render_template('profile/profile.html', user=user, bloglist=bloglist)


@main.route('/user/<uname>/update',methods=['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username=uname).first()

    if user is None:

        abort(404)

    form = UpdateProfile()
    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()
        
        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form=form)






@main.route('/delete/<int:id>' ,methods=['GET',"POST"])
@login_required
def delete(id):
    blog=Blog_post.query.filter_by(id=id).first()
    Blog_post.delete_blog(blog)
    
    return redirect(url_for('main.profile',uname=current_user.username))


@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/blog/new/<uname>', methods=['GET','POST'])
@login_required
def new_blog(uname):
    user = User.query.filter_by(username=uname).first()
    form = BlogForm()
    if form.validate_on_submit():
        title = form.title.data
        category=form.category.data
        blog_content = form.blog_post.data
        
        new_blog = Blog_post(user =current_user.username, title= title, blog_content=blog_content,category=category)
        category = form.category.data
        db.session.add(new_blog)
        db.session.commit()
        
        return redirect(url_for('.profile',uname=user.username))    
    title = 'new blog'
    
    return render_template('blogs.html',form = form,title=title)
        

