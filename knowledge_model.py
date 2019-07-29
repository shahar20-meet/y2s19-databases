from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):
	__tablename__ = 'knowledge'
	knowledge_id = Column(Integer, primary_key=True)
	article_name = Column(String)
	message = Column(String)
	article = Column(String)
	rating = Column(Integer)


	def __repr__(self):
		return("{}\n" "{}\n" "{}\n" "rating : {}\n").format(self.article_name,self.message, self.article, self.rating)

shawarma = Knowledge(article_name = "shawarma", message = "If you want to learn about shawarma, you should look at the Wikipedia article called shawarma. We gave this article a rating of 10 out of 10!",  article = "https://en.wikipedia.org/wiki/Shawarma" ,rating = 10)
print(shawarma)
watermelon = Knowledge(article_name = "watermelon", message = "If you want to learn about watermelon, you should look at the Wikipedia article called watermelon. We gave this article a rating of 8 out of 10!", article = "https://en.wikipedia.org/wiki/Watermelon" ,rating = 8)
print(watermelon)
shoko = Knowledge(article_name = "shoko", message = "If you want to learn about shoko, you should look at the Wikipedia article called shoko. We gave this article a rating of 9 out of 10!", article = "https://en.wikipedia.org/wiki/Chocolate_milk" ,rating = 9)
print(shoko)
	# Create a table with 4 columns
	# The first column will be the primary key
	# The second column should be a string representing
	# the name of the Wiki article that you're referencing
	# The third column will be a string representing the 
	# topic of the article. The last column will be
	# an integer, representing your rating of the article.

	