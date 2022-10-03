from db.user_dao import UserDao


class UserService:
    __user_dao = UserDao()

    # verify user login
    def login(self, username, password):
        res = self.__user_dao.login(username, password)
        return res

    # query user's role name
    def search_user_role(self, username):
        role = self.__user_dao.search_user_role(username)
        return role

    # add a new user
    def insert(self, username, password, email, role_id):
        self.__user_dao.insert(username, password, email, role_id)

    # query all user's page
    def search_count_page(self):
        user_page = self.__user_dao.search_count_page()
        return user_page

    # query all user's info list
    def search_list(self, page):
        res = self.__user_dao.search_list(page)
        return res

    # update user information
    def update(self, id, username, password, email, role_id):
        self.__user_dao.update(id, username, password, email, role_id)

    # delete user
    def delete_by_id(self, id):
        self.__user_dao.delete_by_id(id)

    # search ID by username
    def search_id(self, username):
        user_id = self.__user_dao.search_id(username)
        return user_id