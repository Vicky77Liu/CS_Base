import time

from colorama import Fore, Style
# 遮挡用户输入的密码内容
from getpass import getpass
from service.user_service import UserService
from service.news_service import NewsService
from service.role_service import RoleService
from service.type_service import TypeService
import os
import sys

__user_service = UserService()
__news_service = NewsService()
__role_service = RoleService()
__type_service = TypeService()

while True:
    os.system("clear")
    print(Fore.BLUE, "\n\t **************")
    print(Fore.LIGHTBLUE_EX, "\n\tWelcome To News Management System")
    print(Fore.BLUE, "\n\t **************")
    print(Fore.LIGHTGREEN_EX, "\n\t1, login")
    print(Fore.LIGHTGREEN_EX, "\n\t2, exit")
    print(Style.RESET_ALL)

    opt = input("\n\tEnter the operation number: ")
    if opt == "1":
        username = input("\n\tPlease enter username:")
        password = getpass("\n\tPlease enter password:")
        login_res = __user_service.login(username, password)
        # login succeed
        if login_res:
            # search user's role
            role = __user_service.search_user_role(username)
            while True:
                os.system("clear")
                if role == "administer":
                    print(Fore.LIGHTGREEN_EX, "\n\t1,News Management")
                    print(Fore.LIGHTGREEN_EX, "\n\t2,Users Management")
                    print(Fore.LIGHTRED_EX, "\n\tback,exit login")
                    print(Fore.LIGHTRED_EX, "\n\texit,exit system")
                    print(Style.RESET_ALL)
                    opt = input("\n\tEnter the operation number: ")
                    if opt == "1":
                        while True:
                            os.system("clear")
                            print(Fore.LIGHTGREEN_EX, "\n\t1,Approve News")
                            print(Fore.LIGHTGREEN_EX, "\n\t2,Delete News")
                            print(Fore.LIGHTRED_EX, "\n\tback,Back to previous page")
                            print(Style.RESET_ALL)
                            opt = input("\n\tEnter the operation number: ")
                            if opt == "1":
                                page = 1
                                while True:
                                    os.system("clear")
                                    count_page = __news_service.search_unreview_count_page()
                                    result = __news_service.search_unreview_list(page)
                                    for index in range(len(result)):
                                        one = result[index]
                                        print(Fore.BLUE, "\n\t{},{},{},{}".format(index + 1, one[1], one[2], one[3]))
                                    print(Fore.LIGHTGREEN_EX, "\n\t==============================")
                                    print(Fore.LIGHTGREEN_EX, "\n\t{}/{}".format(page, count_page))
                                    print(Fore.LIGHTGREEN_EX, "\n\t==============================")
                                    print(Fore.LIGHTGREEN_EX, "\n\tback,Go back to previous level")
                                    print(Fore.LIGHTGREEN_EX, "\n\tprev,To previous page")
                                    print(Fore.LIGHTGREEN_EX, "\n\tnext,To next page")
                                    print(Style.RESET_ALL)
                                    opt = input("\n\tEnter the operation number: ")
                                    if opt == "back":
                                        break
                                    elif opt == "prev" and page > 1:
                                        page -= 1
                                    elif opt == "next" and page < count_page:
                                        page += 1
                                    elif 1 <= int(opt) <= 10:
                                        news_id = result[int(opt) - 1][0]
                                        __news_service.update_unreview_news(news_id)
                                        result = __news_service.search_cache(news_id)
                                        title = result[0]
                                        username = result[1]
                                        type = result[2]
                                        content_id = result[3]
                                        content = __news_service.search_content_by_id(content_id)
                                        is_top = result[4]
                                        create_time = str(result[5])
                                        __news_service.cache_news(news_id, title, username, type, content,
                                                                  is_top, create_time)


                            elif opt == "2":
                                page = 1
                                while True:
                                    os.system("clear")
                                    count_page = __news_service.search_count_page()
                                    result = __news_service.search_list(page)
                                    for index in range(len(result)):
                                        one = result[index]
                                        print(Fore.LIGHTRED_EX,
                                              "\n\t{},{},{},{},{}".format(index + 1, one[1], one[2], one[3], one[4]))
                                    print(Fore.LIGHTGREEN_EX, "\n\t==============================")
                                    print(Fore.LIGHTGREEN_EX, "\n\t{}/{}".format(page, count_page))
                                    print(Fore.LIGHTGREEN_EX, "\n\t==============================")
                                    print(Fore.LIGHTGREEN_EX, "\n\tback,Go back to previous level")
                                    print(Fore.LIGHTGREEN_EX, "\n\tprev,To previous page")
                                    print(Fore.LIGHTGREEN_EX, "\n\tnext,To next page")
                                    print(Style.RESET_ALL)
                                    opt = input("\n\tEnter the operation number: ")
                                    if opt == "back":
                                        break
                                    elif opt == "prev" and page > 1:
                                        page -= 1
                                    elif opt == "next" and page < count_page:
                                        page += 1
                                    elif 1 <= int(opt) <= 10:
                                        news_id = result[int(opt) - 1][0]
                                        __news_service.delete_by_id(news_id)
                                        __news_service.delete_cache(news_id)

                            elif opt == "back":
                                break
                    elif opt == "2":
                        while True:
                            os.system("clear")
                            print(Fore.LIGHTGREEN_EX, "\n\t1,add user")
                            print(Fore.LIGHTGREEN_EX, "\n\t2,update user")
                            print(Fore.LIGHTGREEN_EX, "\n\t3,delete user")
                            print(Fore.LIGHTRED_EX, "\n\tback,Back to previous page")
                            print(Style.RESET_ALL)
                            opt = input("\n\tEnter the operation number: ")
                            if opt == "1":
                                os.system("clear")
                                username = input("\n\t username: ")
                                password = getpass("\n\t password: ")
                                repassword = getpass("\n\t reenter password: ")
                                if repassword != password:
                                    print("\n\t2 times passwords are different!(back in 2 second)")
                                    time.sleep(2)
                                    continue
                                email = input("\n\t email: ")
                                print(Fore.LIGHTRED_EX, "\n\tenter the id of role name:")
                                res = __role_service.search_list()
                                for index in range(len(res)):
                                    one = res[index]
                                    print(Fore.LIGHTRED_EX, "\n\t{}.{}".format(index + 1, one[1]))
                                print(Style.RESET_ALL)
                                opt = input("\n\t role id: ")
                                role_id = res[int(opt) - 1][0]
                                __user_service.insert(username, password, email, role_id)
                                print("\n\tSUCCEED!(back in 2 second)")
                                time.sleep(2)
                            elif opt == "2":
                                page = 1
                                while True:
                                    os.system("clear")
                                    count_page = __user_service.search_count_page()
                                    result = __user_service.search_list(page)
                                    for index in range(len(result)):
                                        one = result[index]
                                        print(Fore.LIGHTRED_EX, "\n\t{},{},{}".format(index + 1, one[1], one[2]))
                                    print(Fore.LIGHTGREEN_EX, "\n\t==============================")
                                    print(Fore.LIGHTGREEN_EX, "\n\t{}/{}".format(page, count_page))
                                    print(Fore.LIGHTGREEN_EX, "\n\t==============================")
                                    print(Fore.LIGHTGREEN_EX, "\n\tback,Go back to previous level")
                                    print(Fore.LIGHTGREEN_EX, "\n\tprev,To previous page")
                                    print(Fore.LIGHTGREEN_EX, "\n\tnext,To next page")
                                    print(Style.RESET_ALL)
                                    opt = input("\n\tEnter the operation number: ")
                                    if opt == "back":
                                        break
                                    elif opt == "prev" and page > 1:
                                        page -= 1
                                    elif opt == "next" and page < count_page:
                                        page += 1
                                    elif 1 <= int(opt) <= 10:
                                        os.system("clear")
                                        user_id = result[int(opt) - 1][0]
                                        username = input("\n\tnew username: ")
                                        password = getpass("\n\tnew password: ")
                                        repassword = getpass("\n\treenter password: ")
                                        if repassword != password:
                                            print(Fore.LIGHTRED_EX, "\n\t 2 passwords are different (Auto back 2 "
                                                                    "second)")
                                            print(Style.RESET_ALL)
                                            time.sleep(2)
                                            break
                                        email = input("\n\tnew email: ")
                                        print(Fore.LIGHTRED_EX, "\n\tenter the id of role name:")
                                        result = __role_service.search_list()
                                        for index in range(len(result)):
                                            one = result[index]
                                            print(Fore.LIGHTRED_EX, "\n\t{}.{}".format(index + 1, one[1]))
                                        print(Style.RESET_ALL)
                                        opt = input("\n\t new role id: ")
                                        role_id = result[int(opt) - 1][0]
                                        opt = input("\n\t Save Information(Y/N): ")
                                        if opt == "Y" or opt == "y":
                                            __user_service.update(user_id, username, password, email, role_id)
                                            print(Fore.LIGHTRED_EX, "\n\t Information update succeed! (Auto back 2 "
                                                                    "second)")
                                            print(Style.RESET_ALL)
                                            time.sleep(2)
                                            break
                            elif opt == "3":
                                page = 1
                                while True:
                                    os.system("clear")
                                    count_page = __user_service.search_count_page()
                                    result = __user_service.search_list(page)
                                    for index in range(len(result)):
                                        one = result[index]
                                        print(Fore.LIGHTRED_EX, "\n\t{},{},{}".format(index + 1, one[1], one[2]))
                                    print(Fore.LIGHTGREEN_EX, "\n\t==============================")
                                    print(Fore.LIGHTGREEN_EX, "\n\t{}/{}".format(page, count_page))
                                    print(Fore.LIGHTGREEN_EX, "\n\t==============================")
                                    print(Fore.LIGHTGREEN_EX, "\n\tback,Go back to previous level")
                                    print(Fore.LIGHTGREEN_EX, "\n\tprev,To previous page")
                                    print(Fore.LIGHTGREEN_EX, "\n\tnext,To next page")
                                    print(Style.RESET_ALL)
                                    opt = input("\n\tEnter the operation number: ")
                                    if opt == "back":
                                        break
                                    elif opt == "prev" and page > 1:
                                        page -= 1
                                    elif opt == "next" and page < count_page:
                                        page += 1
                                    elif 1 <= int(opt) <= 10:
                                        os.system("clear")
                                        user_id = result[int(opt) - 1][0]
                                        __user_service.delete_by_id(user_id)
                                        print(Fore.LIGHTRED_EX, "\n\t User deletion succeed! (Auto back 2 "
                                                                "second)")
                                        time.sleep(2)
                                        break
                            elif opt == "back":
                                break
                    elif opt == "back":
                        break
                    elif opt == "exit":
                        sys.exit(0)
                elif role == "editor":
                    print(Fore.LIGHTGREEN_EX, "\n\t1,Publish news")
                    print(Fore.LIGHTGREEN_EX, "\n\t2,Edit news")
                    print(Fore.LIGHTRED_EX, "\n\tback,exit login")
                    print(Fore.LIGHTRED_EX, "\n\texit,exit system")
                    print(Style.RESET_ALL)
                    opt = input("\n\tEnter the operation number: ")
                    if opt == "1":
                        os.system("clear")
                        title = input("\n\tEnter Title: ")
                        user_id = __user_service.search_id(username)
                        result = __type_service.search_type_list()
                        for index in range(len(result)):
                            one = result[index]
                            print(Fore.LIGHTRED_EX, "\n\t{}.{}".format(index + 1, one[1]))
                        print(Style.RESET_ALL)
                        opt = input("\n\t Type id:")
                        type_id = result[int(opt) - 1][0]
                        path = input("\n\tfile path:")
                        file = open(path, "r")
                        content = file.read()
                        file.close()
                        is_top = input("\n\t Top level(0-5):")
                        is_commit = input("\n\t Are you ok to submit(Y/N):")
                        if is_commit == "Y" or is_commit == "y":
                            __news_service.insert_news(title, user_id, type_id, content, is_top)
                            print("\n\tSUCCEED!(back in 2 second)")
                            time.sleep(2)
                    elif opt == "2":
                        page = 1
                        while True:
                            os.system("clear")
                            count_page = __news_service.search_count_page()
                            result = __news_service.search_list(page)
                            for index in range(len(result)):
                                one = result[index]
                                print(Fore.LIGHTRED_EX,
                                      "\n\t{},{},{},{},{}".format(index + 1, one[1], one[2], one[3], one[4]))
                            print(Fore.LIGHTGREEN_EX, "\n\t==============================")
                            print(Fore.LIGHTGREEN_EX, "\n\t{}/{}".format(page, count_page))
                            print(Fore.LIGHTGREEN_EX, "\n\t==============================")
                            print(Fore.LIGHTGREEN_EX, "\n\tback,Go back to previous level")
                            print(Fore.LIGHTGREEN_EX, "\n\tprev,To previous page")
                            print(Fore.LIGHTGREEN_EX, "\n\tnext,To next page")
                            print(Style.RESET_ALL)
                            opt = input("\n\tEnter the operation number: ")
                            if opt == "back":
                                break
                            elif opt == "prev" and page > 1:
                                page -= 1
                            elif opt == "next" and page < count_page:
                                page += 1
                            elif 1 <= int(opt) <= 10:
                                os.system("clear")
                                news_id = result[int(opt) - 1][0]
                                result = __news_service.search_by_id(news_id)
                                title = result[0]
                                type = result[1]
                                is_top = result[2]
                                print("\n\tCurrent Title is {}".format(title))
                                new_title = input("\n\t New title:")
                                res = __type_service.search_type_list()
                                for index in range(len(res)):
                                    one = res[index]
                                    print(Fore.LIGHTRED_EX, "\n\t{}.{}".format(index + 1, one[1]))
                                print(Style.RESET_ALL)
                                print("\n\tCurrent type is {}".format(type))
                                opt = input("\n\t New type id:")
                                type_id = res[int(opt) - 1][0]
                                # news content
                                path = input("\n\t file path:")
                                file = open(path, "r")
                                content = file.read()
                                file.close()
                                print("\n\tCurrent top level is {}".format(is_top))
                                new_isTop = input("\n\t New top level(0-5):")
                                is_commit = input("\n\t Are you ok to submit(Y/N):")
                                if is_commit == "Y" or is_commit == "y":
                                    __news_service.update_news(news_id, new_title, type_id, content, new_isTop)
                                    print("\n\tSUCCEED!(back in 2 second)")
                                    time.sleep(2)
                    elif opt == "back":
                        break
                    elif opt == "exit":
                        sys.exit(0)

        else:
            print("\n\t login failed")
            time.sleep(2)

    elif opt == "2":
        # 0代表安全退出
        sys.exit(0)
