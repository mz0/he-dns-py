from setuptools import setup
from setuptools import find_packages


version = '1.0.0'

install_requires = [
    'setuptools',

    'requests',
    'lxml',
    'six',
    'bs4',
]

with open('README.rst') as in_file:
    long_description = in_file.read()

setup(
    name='certbot-dns-he',
    version=version,
    description='Hurricane Electric DNS Authenticator plugin for Certbot',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    url='https://github.com/TSaaristo/certbot-dns-he',
    author='TSaaristo',
    author_email='tero.saaristo@gmail.com',
    license='MIT',
    python_requires='>3.5',
    classifiers=[
        'Environment :: Plugins',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Security',
        'Topic :: System :: Installation/Setup',
        'Topic :: System :: Networking',
        'Topic :: System :: Systems Administration',
        'Topic :: Utilities',
    ],
    keywords='certbot dns hurricane-electric dns-01 authenticator api',

    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    entry_points={
        'certbot.plugins': [
            'dns-he = certbot_dns_he.dns_he:Authenticator',
        ],
    }
)
