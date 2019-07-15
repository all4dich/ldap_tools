from ldap_tools.common import LDAPClient

if __name__ == "__main__":
    host = "192.168.57.4"
    username = "\\admin"
    password = "admin"

    a = LDAPClient(host,username,password)
    a.search_root = 'dc=tv, dc=sunjoo, dc=org'
    b = a.get_child(oc="person")
    members = list(map(lambda x: x.entry_dn, b))
    print("\n".join(members))
