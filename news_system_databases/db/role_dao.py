from db.mysql_db import pool

class RoleDao:
    # search list of roles
    def search_list(self):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT id, role FROM t_role"
            cursor.execute(sql)
            res = cursor.fetchall()
            return res
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()