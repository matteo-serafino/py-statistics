from setuptools import setup, find_packages

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
    name='py-statistics',
    version='0.0.0',
    description='Statistics basics with Python',
    long_description=long_description,
    packages=find_packages(include=['src']),
    python_requires='>=3.10',
    install_requires=[
        'pandas>=2.2.3',
        'scipy>=1.15.0'
    ],
)
