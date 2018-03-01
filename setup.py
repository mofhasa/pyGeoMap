import os
from setuptools import setup, find_packages

__version__ = '1.0.0'

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name = 'pyGeoMap',
    version = __version__,
    author = 'Kartik Yadav (mofhasa)',
    author_email = 'moofhasa@gmail.com',
    url = 'https://github.com/mofhasa/pyGeoMap',
    description = 'Interface for plotting geographical maps and exporting them in different formats.',
    long_description=read('README.rst'),
    license='MIT',
    keywords='python wrapper basemap matplotlib maps',
    packages = find_packages(exclude=['docs', 'tests']),
    include_package_data=True,
    install_requires=['matplotlib', 'numpy', 'Pillow'],
#     entry_points={  # Optional
#         'console_scripts': [
#             'externals=pyGeoMap:main',
#         ],
#     }
)