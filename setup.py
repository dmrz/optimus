from setuptools import setup, find_packages
from codecs import open
from os import path


here = path.abspath(path.dirname(__file__))


with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    requirements = f.read().split()


setup(
    name='baymax',
    version='0.0.4',
    description='A simple telegram bot framework on top of Python asyncio',
    long_description=long_description,
    url='https://github.com/dmrz/baymax',
    license='MIT',
    author='Dima Moroz',
    author_email='me@dimamoroz.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='telegram bot asyncio',
    packages=find_packages(exclude=['docs', 'tests']),
    install_requires=requirements,
    python_requires='>=3.6',
    package_data={
        'baymax': ['LICENSE']
    }
)
