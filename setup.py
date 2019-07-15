from setuptools import setup, find_packages

python_src_root = "src/main/python"
setup(
    name='ldap_tools',
    version='0.1',
    zip_safe=False,
    description='Custom tools for LDAP Client',
    author='Sunjoo Park',
    author_email='all4dich@gmail.com',
    package_dir={'': python_src_root},
    packages=find_packages(where=python_src_root)
)
