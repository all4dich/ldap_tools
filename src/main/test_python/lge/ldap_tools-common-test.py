from ldap_tools.common import LDAPClient

if __name__ == "__main__":
    a = LDAPClient("156.147.162.251", "\\allessunjoo.park", "Yooahrim1!")
    a.search_root = 'ou=LGE Users, dc=lge, dc=net'
    r = a.get_members("TV선행SW*_grp")
    members_info = list(map(lambda x: x.entry_dn, r))
    print("\n".join(members_info))
