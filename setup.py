from setuptools import find_packages, setup

setup(
    name='flask-boilerplate',
    version='0.1',
    description='Flask Boilerplate',
    author='Shri',
    license = 'MIT',
    packages = find_packages(),
    install_requires = ['Flask==0.12.2'],
)
