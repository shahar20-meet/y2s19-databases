from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(article_name,message,url,rating):
    new_article = Knowledge(
        article_name=article_name,
        message=message,
        url=url,
        rating=rating)

    session.add(new_article)
    session.commit()


add_article("fries","", "https://en.wikipedia.org/wiki/French_fries", 10)

def query_all_articles():
	articles = session.query(Knowledge).all()
	return articles
print(query_all_articles())

def query_article_by_topic():
	article = session.query(
       Knowledge).filter_by(
       article_name=article_name).first()
	return article


print(query_article_by_topic("shawarma"))


def delete_article_by_topic():
	pass

def delete_all_articles():
	pass

def edit_article_rating():
	pass
