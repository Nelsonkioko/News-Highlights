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

@main.route('/sports')
def sport():
	'''
	View root page function that returns the index page and its data
	'''

	general_news = get_news('sports')
	title = 'general-news Page - Get The latest News Online'
	return render_template('sports.html',title = title,sports=general_news)

@main.route('/technology')
def tech():
	'''
	View root page function that returns the index page and its data
	'''

	general_news = get_news('technology')
	title = 'general-news Page - Get The latest News Online'
	return render_template('technology.html',title = title,technology=general_news)

@main.route('/businessNews')
def business():
	'''
	View root page function that returns the index page and its data
	'''

	general_news = get_news('business')
	title = 'general-news Page - Get The latest News Online'
	return render_template('businessNews.html',title = title,businessNews=general_news)

@main.route('/entertainmentNews')
def entertainment():
	'''
	View root page function that returns the index page and its data
	'''
	# Getting popular news
	general_news = get_news('entertainment')
	title = 'general-news Page - Get The latest News Online'
	return render_template('entertainmentNews.html',title = title,entertainment=general_news)


@main.route('/')
def index():

    news_article = get_article('bitcoin')
    title = 'Home Page - Get The latest News Online'
    return render_template('index.html',title = title, article=news_article)