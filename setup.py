import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="django-fixturapp",
    version="1.0",
    url='http://github.com/henriquebastos/django-fixturapp',
    license='BSD',
    description="An utility app that integrates Fixture with Django.",
    long_description=read('README'),

    author='Henrique Bastos',
    author_email='henrique@bastos.net',

    packages=find_packages('src'),
    package_dir={'': 'src'},

    install_requires=['setuptools', 'fixture'],

    classifiers=['Development Status :: 4 - Beta',
                 'Framework :: Django',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: BSD License',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python',
                 'Topic :: Internet :: WWW/HTTP'])
