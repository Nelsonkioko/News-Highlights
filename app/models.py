class News:


	'''
	News class to define News Objects
	'''
	def __init__(self, id, name, description, url, category):


		self.id = id
		self.name = name
		self.description = description
		self.url = url
		self.category = category



class Article:
	def __init__(self,source,urlToImage,author,title,description,publishedAt,url):

		self.source = source
		self.author = author
		self.title = title
		self.description = description
		self.publishedAt = publishedAt
		self.urlToImage = urlToImage
		self.url = url