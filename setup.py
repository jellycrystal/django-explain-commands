from setuptools import setup

setup(
    name='django-explain-commands',
    version='0.1',
    description='Django app for explaining where commands are coming from.',
    long_description=open('README.rst').read(),
    author='Yury Yurevich',
    author_email='yyurevich@jellycrystal.com',
    url='https://github.com/jellycrystal/django-explain-commands',
    license='BSD',
    include_package_data=True,
    zip_safe=True,
    # Get more strings from http://www.python.org/pypi?:action=list_classifiers
    classifiers=[
            'Development Status :: Beta',
            'Environment :: Web Environment',
            'Framework :: Django',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)


