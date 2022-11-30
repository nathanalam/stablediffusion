from setuptools import setup, find_packages

setup(
    name='ldm',
    version='0.1.3',
    description='',
    packages=find_packages(),
    install_requires=[
        'torch',
        'numpy',
        'tqdm',
    ],
)
