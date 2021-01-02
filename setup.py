from setuptools import setup, find_packages, Command


__requires__ = ['requests']

setup(
    name='pydzapi',
    version='1.0.1.0',
    packages=find_packages(exclude=("test", )),
    url='',
    license='',
    author='Nona',
    author_email='',
    description='',
    install_requires=__requires__,
    zip_safe=False
)
