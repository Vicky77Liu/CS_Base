from db.mysql_db import pool


class TypeDao:
    # search list of type
    def search_type_list(self):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT id ,type FROM t_type ORDER BY id"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()
