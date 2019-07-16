from ldap_tools.common import LDAPClient

if __name__ == "__main__":
    a = LDAPClient("156.147.162.251", "\\addhost", "1qaz2wsx")
    a.search_attributes.append("distinguishedName")
    a.search_root = 'ou=LGE Users, dc=lge, dc=net'
    r = a.get_members("TV LCM High UHD Project")
    members_info = list(map(lambda x: x.entry_dn, r))
    print("\n".join(members_info))

    r2 = a.get_objects(f"&(objectClass=organizationalUnit)(ou=*TV선행SW*)")
    print(r2[0].entry_dn)
    a.search_root = r2[0].entry_dn
    r3 = a.get_child(oc="person")
    for each_member in r3:
        print(each_member.entry_dn)
