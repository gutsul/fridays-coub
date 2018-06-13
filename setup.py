from setuptools import setup


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
    entry_points = {
        'console_scripts': [
            'coub = coub.__main__:main'
        ]
    })