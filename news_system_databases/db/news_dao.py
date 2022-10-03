from db.mysql_db import pool


class NewsDao:
    # search unreviewed news
    def search_unreview_list(self, page):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT n.id,n.title,t.type,u.username " \
                  "FROM t_news n JOIN t_type t ON n.type_id=t.id " \
                  "JOIN t_user u ON n.editor_id=u.id " \
                  "WHERE n.state=%s " \
                  "ORDER BY n.create_time DESC " \
                  "LIMIT %s,%s"
            cursor.execute(sql, ("pending", (page - 1) * 10, 10))
            un_review_lst = cursor.fetchall()
            return un_review_lst
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    # get page of pending news
    def search_unreview_count_page(self):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT CEIL(COUNT(*)/10) FROM t_news WHERE state=%s"
            cursor.execute(sql, ["pending"])
            count_page = cursor.fetchone()[0]
            return count_page
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    # change unreviewed news to approved
    def update_unreview_news(self, id):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = "UPDATE t_news SET state=%s WHERE id =%s"
            cursor.execute(sql, ("approved", id))
            con.commit()
        except Exception as e:
            if "con" in dir():
                con.rollback()
            print(e)
        finally:
            if "con" in dir():
                con.close()

    # search all news list
    def search_list(self, page):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT n.id,n.title,t.type,u.username,n.state " \
                  "FROM t_news n JOIN t_type t ON n.type_id=t.id " \
                  "JOIN t_user u ON n.editor_id=u.id " \
                  "ORDER BY n.create_time DESC " \
                  "LIMIT %s,%s"
            cursor.execute(sql, ((page - 1) * 10, 10))
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    # get page of all news
    def search_count_page(self):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT CEIL(COUNT(*)/10) FROM t_news"
            cursor.execute(sql)
            count_page = cursor.fetchone()[0]
            return count_page
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    # delete news
    def delete_by_id(self, id):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            # delete by t_news key id
            sql = "DELETE FROM t_news WHERE id =%s"
            cursor.execute(sql, [id])
            con.commit()
        except Exception as e:
            if "con" in dir():
                con.rollback()
            print(e)
        finally:
            if "con" in dir():
                con.close()

    # add news
    def insert_news(self, title, editor_id, type_id, content_id, is_top):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = "INSERT INTO t_news(title, editor_id, type_id, content_id, is_top,state) " \
                  "VALUES(%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, (title, editor_id, type_id, content_id, is_top, "pending"))
            con.commit()
        except Exception as e:
            if "con" in dir():
                con.rollback()
            print(e)
        finally:
            if "con" in dir():
                con.close()

    # search user's record of cache
    def search_cache(self, id):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT n.title,u.username,t.type,n.content_id," \
                  "n.is_top,n.create_time " \
                  "FROM t_news n " \
                  "JOIN t_type t ON n.type_id=t.id " \
                  "JOIN t_user u ON n.editor_id=u.id " \
                  "WHERE n.id=%s"
            cursor.execute(sql, [id])
            result = cursor.fetchone()
            return result
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    # search news by id
    def search_by_id(self, id):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT n.title,t.type,n.is_top " \
                  "FROM t_news n " \
                  "JOIN t_type t ON n.type_id=t.id " \
                  "WHERE n.id=%s"
            cursor.execute(sql, [id])
            result = cursor.fetchone()
            return result
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    # update news
    def update_news(self, id, title, type_id, content_id, is_top):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = "UPDATE t_news SET " \
                  "title=%s, type_id=%s,content_id=%s, " \
                  "is_top=%s, state=%s, update_time= NOW() " \
                  "WHERE id=%s"
            cursor.execute(sql, (title, type_id, content_id,
                                 is_top, "pending", id))
            con.commit()
        except Exception as e:
            if "con" in dir():
                con.rollback()
            print(e)
        finally:
            if "con" in dir():
                con.close()

    # search content_id by id
    def search_content_id(self, id):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT content_id FROM t_news "\
                  "WHERE id=%s"
            cursor.execute(sql, [id])
            content_id = cursor.fetchone()[0]
            return content_id
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()


if __name__ == '__main__':
    service = NewsDao()
    re = service.search_count_page()
    rs = service.search_content_id(2)
    print(rs)
