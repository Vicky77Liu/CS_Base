from db.type_dao import TypeDao


class TypeService:
    __type_dao = TypeDao()

    #search list of type
    def search_type_list(self):
        result = self.__type_dao.search_type_list()
        return result
