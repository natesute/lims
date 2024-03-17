from setuptools import setup, find_packages

setup(
    name='lims',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
    ],
    author='Nathan Suttie',
    author_email='nathan.suttie@gmail.com',
    description='Lims is an LLM-powered simulation of virtual agents and their social interactions.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/natesute/lims',
    python_requires='>=3.6',
    
)