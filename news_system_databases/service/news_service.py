from db.news_dao import NewsDao
from db.redis_dao import RedisNewsDao
from db.mongo_news_dao import MongoNewsDao


class NewsService():
    __news_dao = NewsDao()
    __redis_news_dao = RedisNewsDao()
    __mongo_news_dao = MongoNewsDao()

    # search unreviewed news list
    def search_unreview_list(self, page):
        res = self.__news_dao.search_unreview_list(page)
        return res

    # get page of pending news
    def search_unreview_count_page(self):
        page = self.__news_dao.search_unreview_count_page()
        return page

    # change unreviewed news to approved
    def update_unreview_news(self, id):
        self.__news_dao.update_unreview_news(id)

    # search all news list
    def search_list(self, page):
        news_list = self.__news_dao.search_list(page)
        return news_list

    # get page of all news
    def search_count_page(self):
        count_page = self.__news_dao.search_count_page()
        return count_page

    # delete news
    def delete_by_id(self, id):
        content_id = self.__news_dao.search_content_id(id)
        self.__news_dao.delete_by_id(id)
        self.__mongo_news_dao.delete_by_id(content_id)

    # add news
    def insert_news(self, title, editor_id, type_id, content, is_top):
        self.__mongo_news_dao.insert_to_M(title, content)
        content_id = self.__mongo_news_dao.search_id(title)
        self.__news_dao.insert_news(title, editor_id, type_id, content_id, is_top)

    # search user's record of cache
    def search_cache(self, id):
        result = self.__news_dao.search_cache(id)
        return result

    # save cache news
    def cache_news(self, id, title, username, type, content, is_top, create_time):
        self.__redis_news_dao.insertToRedis(id, title, username, type, content, is_top, create_time)

    # delete news in cache
    def delete_cache(self, id):
        self.__redis_news_dao.deleteFromRedis(id)

    # search news by id
    def search_by_id(self, id):
        result = self.__news_dao.search_by_id(id)
        return result

    # update news
    def update_news(self, id, title, type_id, content, is_top):
        content_id = self.__news_dao.search_content_id(id)
        self.__mongo_news_dao.update_to_M(content_id, title, content)
        self.__news_dao.update_news(id, title, type_id, content_id, is_top)
        # delete cache of that news
        self.delete_cache(id)

    # search news' content by id
    def search_content_by_id(self, id):
        content = self.__mongo_news_dao.search_content_by_id(id)
        return content
