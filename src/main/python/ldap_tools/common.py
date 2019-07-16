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
        self._search_attributes = ['name', 'mail', 'mobile', 'cn', 'department', 'description', 'displayNamePrintable', 'displayName']

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

    @property
    def search_attributes(self):
        return self._search_attributes

    @search_attributes.setter
    def search_attributes(self, value):
        self._search_attributes = value

    def get_connection(self):
        """
        Return a connection to LDAP server
        :return: conn
        """
        server = Server(self.host)
        conn = Connection(server, user=self._username, password=self._password, authentication=self.authentication)
        conn.bind()
        return conn

    def get_objects(self, obj_name):
        """
        Return a list of objects with a query 'obj_name'
        'obj_name' is a query statement written by a caller
        Example. cn=John Doe
        :param obj_name:
        :return:
        """
        conn = self.get_connection()
        if self._search_root is None:
            logger.warning("Set 'search_root' and try again")
            return None
        conn.search(self._search_root, f"({obj_name})", attributes=self._search_attributes )
        return conn.entries

    def get_departments(self, dept_name):
        return self.get_objects(f"cn={dept_name}")

    def get_members(self, dept_name):
        """
        Get a list of members who are under 'dept_name'
        :param dept_name: Department name
        :return:
        """
        members = []
        conn  = self.get_connection()
        if self._search_root is None:
            logger.warning("Set 'search_root' and try again")
            return None
        #Get a dapartment object
        depts = self.get_objects(f"&(objectClass=organizationalUnit)(ou=*{dept_name}*)")
        for each_dept in depts:
            member_search_base = each_dept.entry_dn
            conn.search(member_search_base, '(objectClass=person)', attributes=self._search_attributes)
            for each_entry in conn.entries:
                members.append(each_entry)
        return members

    def get_child(self,oc="person"):
        """
        Return all child elements under 'self._search_root'
        :param oc:
        :return:
        """
        if self._search_root is None:
            logger.warning("Set 'search_root' and try again")
            return None
        conn = self.get_connection()
        conn.search(self._search_root, f"(objectClass={oc})", attributes=self._search_attributes)
        return conn.entries

