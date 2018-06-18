# from os import path
from setuptools import setup

# here = path.abspath(path.dirname(__file__))
#
# print("here: {}".format(here))

setup(
    name = 'coub',
    version = '1.0.0',
    description='A sample Python project',
    url='https://github.com/gutsul/fridays-coub',
    author='Yuriy Grigortsevich',
    author_email='GrigortsevichYuriy@gmail.com',
    packages = ['coub'],
    install_requires=[
        'python-dotenv==0.8.2',
        'requests==2.18.4'
    ],
    data_files=[('coubs.db', ['/home/ygrigortsevich/Repository/fridays-coub/data/coubs.db'])],
    entry_points = {
        'console_scripts': [
            'coub = coub.__main__:main'
        ]
    })