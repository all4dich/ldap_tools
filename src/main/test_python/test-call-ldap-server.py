from ldap_tools.common import LDAPClient
import subprocess
import re
if __name__ == "__main__":
    host = "156.147.162.251"
    username = "lge\\addhost"
    password = input(f"Password for {username}")

    a = LDAPClient(host,username,password)
    a.search_root = 'ou=LGE Users,dc=lge,dc=net'
#    b = a.get_child(oc="posixGroup")
#    print(b)
#    members = list(map(lambda x: x.entry_dn, b))
#    print("\n".join(members))
#    c = a.get_objects("ou=TV SW Engineering")
#    print(c)
#    user = "jaewooki.lee"
#    d = a.get_objects(f"sAMAccountName=*{user}*")
#    for e in d:
#        print(e)
    team = "TV SW CI팀"
    r = a.get_members(team)
    for member in r:
        print(member.cn)
