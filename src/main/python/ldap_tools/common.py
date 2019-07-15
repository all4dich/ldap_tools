from ldap3 import Server, Connection, ALL, NTLM
import logging

logger = logging.getLogger()
logger.setLevel(logging.WARN)

formatter = logging.Formatter('%(levelname)7s:%(filename)s:%(lineno)d:%(funcName)10s: %(message)s')

ch = logging.StreamHandler()
ch.setLevel(logging.WARN)
ch.setFormatter(formatter)

logger.addHandler(ch)


class LDAPClient:
    def __init__(self, host, username, password, authentication=NTLM, search_root = None):
        self.host = host
        self._username = username
        self._password = password
        self.authentication = authentication
        self._search_root = search_root

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, val):
        self._username = val

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, val):
        self._password = val

    @property
    def search_root(self):
        return self._search_root

    @search_root.setter
    def search_root(self, value):
        self._search_root = value

    def get_connection(self):
        server = Server(self.host)
        conn = Connection(server, user=self._username, password=self._password, authentication=self.authentication)
        conn.bind()
        return conn

    def get_departments(self, dept_name):
        conn = self.get_connection()
        if self._search_root is None:
            logger.warning("Set 'search_root' and try again")
            return None
        conn.search(self._search_root, '(cn=' + dept_name +')',
                     attributes=[
                         'cn', 'mail', 'displayName',
                         'mobile', 'description',
                     ]
                     )
        return conn.entries

    def get_members(self, dept_name):
        members = []
        conn  = self.get_connection()
        if self._search_root is None:
            logger.warning("Set 'search_root' and try again")
            return None
        #Get a dapartment object
        depts = self.get_departments(dept_name)
        for each_dept in depts:
            member_search_base = each_dept.entry_dn.split(",")[1:]
            conn.search(member_search_base, '(objectClass=person)',
                        attributes=['name', 'mail', 'mobile', 'cn', 'department', 'description',
                                    'displayNamePrintable', 'displayName'])
            for each_entry in conn.entries:
                members.append(each_entry)
        return members

