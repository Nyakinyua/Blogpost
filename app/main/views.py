from . import main
from ..requests import get_quotes
from flask import render_template, request, redirect, url_for

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