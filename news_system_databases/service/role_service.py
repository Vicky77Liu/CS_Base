from db.role_dao import RoleDao


class RoleService:
    __role_service = RoleDao()

    # search list of roles
    def search_list(self):
        res = self.__role_service.search_list()
        return res
