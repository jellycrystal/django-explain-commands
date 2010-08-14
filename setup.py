from setuptools import setup, find_packages

setup(
    name='django-explain-commands',
    version='0.2',
    description='Django app for explaining where commands are coming from.',
    long_description=open('README.md').read(),
    author='Yury Yurevich',
    author_email='yyurevich@jellycrystal.com',
    url='https://github.com/jellycrystal/django-explain-commands',
    license='BSD',
    packages=find_packages(),
    include_package_data=False,
    zip_safe=True,
    # Get more strings from http://www.python.org/pypi?:action=list_classifiers
    classifiers=[
            'Development Status :: 4 - Beta',
            'Environment :: Web Environment',
            'Framework :: Django',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)


