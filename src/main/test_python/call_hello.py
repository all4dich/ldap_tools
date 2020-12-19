import re
import os
import logging

from ldap_tools.common import LDAPClient

logger = logging.getLogger("add-lge-users-to-nexus")

if __name__ == "__main__":
    host = "156.147.162.251"
    username = "lge\\allessunjoo.park"
    password = input("Password: ")

    a = LDAPClient(host, username, password)
    a.search_root = 'ou=LGE Users,dc=lge,dc=net'
    try:
        lge_department_name = "TV DevOps개발"
    except:
        lge_department_name = input("LGE department name: ")
    r = a.get_members(lge_department_name)
    for member in r:
        user_cn = str(member.cn)
        user_mail = str(member.mail)
        print(user_mail)

