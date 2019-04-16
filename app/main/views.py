from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_news,get_article



@main.route('/general')
def general():
	'''
	View root page function that returns the index page and its data
	'''

	general_news = get_news('general')
	title = 'general-news Page - Get The latest News Online'
	return render_template('general.html',title = title,general=general_news)

@main.route('/sport')
def sport():
	'''
	View root page function that returns the index page and its data
	'''

	general_news = get_news('sports')
	title = 'general-news Page - Get The latest News Online'
	return render_template('sports.html',title = title,sports=general_news)

@main.route('/tech')
def tech():
	'''
	View root page function that returns the index page and its data
	'''

	general_news = get_news('technology')
	title = 'general-news Page - Get The latest News Online'
	return render_template('tech.html',title = title,technology=general_news)

@main.route('/business')
def business():
	'''
	View root page function that returns the index page and its data
	'''

	general_news = get_news('business')
	title = 'general-news Page - Get The latest News Online'
	return render_template('business.html',title = title,business=general_news)

@main.route('/entertainment')
def entertainment():
	'''
	View root page function that returns the index page and its data
	'''
	# Getting popular news
	general_news = get_news('entertainment')
	title = 'general-news Page - Get The latest News Online'
	return render_template('entertainment.html',title = title,entertainment=general_news)


@main.route('/')
def index():

    news_article = get_article('bitcoin')
    title = 'Home Page - Get The latest News Online'
    return render_template('index.html',title = title, article=news_article)