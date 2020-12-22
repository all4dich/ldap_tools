import re
import os
import logging

from ldap_tools.common import LDAPClient
import argparse

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-u", dest="username", required=True)
arg_parser.add_argument("-p", dest="password", required=True)
args = arg_parser.parse_args()

if __name__ == "__main__":
    host = "156.147.162.251"
    username = f"lge\\{args.username}"
    password = args.password

    a = LDAPClient(host, username, password)
    a.search_root = 'ou=LGE Users,dc=lge,dc=net'
    try:
        lge_department_name = "TV DevOps개발"
    except:
        lge_department_name = input("LGE department name: ")
    a.find_department(lge_department_name)
