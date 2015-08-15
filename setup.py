"""\
prepend
~~~~~~~

Prepends a list of files with text.


Links
`````

* `Website <http://github.com/joeyespo/prepend>`_

"""

import os
from setuptools import setup, find_packages


def read(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        return f.read()


setup(
    name='prepend',
    version='1.0.0',
    description='Prepends a list of files with text.',
    long_description=__doc__,
    author='Joe Esposito',
    author_email='joe@joeyespo.com',
    url='http://github.com/joeyespo/prepend',
    license='MIT',
    platforms='any',
    packages=find_packages(),
    install_requires=read('requirements.txt').splitlines(),
    zip_safe=False,
    entry_points={'console_scripts': [
        'prepend = prepend:main',
        'pre = prepend:main',
    ]},
)
