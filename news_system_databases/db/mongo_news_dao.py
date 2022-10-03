from db.mongo_db import client
from bson.objectid import ObjectId

class MongoNewsDao:
    # add news content into mongodb
    def insert_to_M(self, title, content):
        try:
            client.vega.news.insert_one({"title": title, "content": content})
        except Exception as e:
            print(e)

    # search news' content id from mongodb
    def search_id(self, title):
        try:
            news = client.vega.news.find_one({"title": title})
            return str(news["_id"])
        except Exception as e:
            print(e)

    # update news content
    def update_to_M(self,id,title,content):
        try:
            client.vega.news.update_one({"_id": ObjectId(id)},
                                        {"$set": {"title": title, "content": content}})
        except Exception as e:
            print(e)

    # search news' content by id
    def search_content_by_id(self, id):
        try:
            news = client.vega.news.find_one({"_id": ObjectId(id)})
            return str(news["content"])
        except Exception as e:
            print(e)

    # delete news' content by id
    def delete_by_id(self, id):
        try:
            client.vega.news.delete_one({"_id": ObjectId(id)})
        except Exception as e:
            print(e)