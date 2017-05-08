#    A-John-Shots - Python module/library for saving Security Hash Algorithms into JSON format.
#    Copyright (C) 2017  Funilrys - Funilrys - Nissar Chababy <contact at funilrys dot com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

#    Original Version: https://github.com/funilrys/A-John-Shots

from distutils.core import setup

setup(
    name='a_john_shots',
    version="1.0.1",
    description='Python module/library for saving Security Hash Algorithms into JSON format.',
    long_description=open('README').read(),
    author='funilrys',
    author_email='contact@funilrys.com',
    license='GPL-3.0 https://opensource.org/licenses/GPL-3.0',
    url='https://github.com/funilrys/A-John-Shots',
    platforms=['any'],
    packages=['a_john_shots'],
    keywords=['Python', 'JSON', 'SHA-1',
              'SHA-512', 'SHA-224', 'SHA-384', 'SHA', 'MD5'],
    classifiers=[
        'Environment :: Console',
        'Topic :: Software Development',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)'
    ],
)

'''
test_suite='testsuite',
entry_points="""
[console_scripts]
cmd = package:main
""",
'''
