from db.redis_db import pool
import redis

class RedisNewsDao:
    def insertToRedis(self, id, title, username, type, content, is_top, create_time):
        con = redis.Redis(
            connection_pool=pool
        )
        try:
            con.hset(id, "title", title)
            con.hset(id, "username", username)
            con.hset(id, "type", type)
            con.hset(id, "content", content)
            con.hset(id, "is_top", is_top)
            con.hset(id, "create_time", create_time)
            if is_top == 0:
                con.expire(id, 24*3600)

        except Exception as e:
            print(e)
        finally:
            del con

    def deleteFromRedis(self, id):
        con = redis.Redis(
            connection_pool=pool
        )
        try:
            con.delete(id)
        except Exception as e:
            print(e)
        finally:
            del con

if __name__ == '__main__':
    insert = RedisNewsDao()
    insert.insertToRedis(1,"22","fsd","4","reuh","1","2012-3")