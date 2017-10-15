from setuptools import setup

setup(
    name='scalrapi',
    version='0.1',
    description='A library providing functions for accessing the Scalr API.',
    url='https://github.build.ge.com/CoreTechAutomation/scalrapi',
    author='Joshua Thornton',
    author_email='joshua.thornton@ge.com',
    packages=['scalrapi'],
    install_requires=[
        'pytz',
        'requests'
    ],
    zip_safe=False
)
