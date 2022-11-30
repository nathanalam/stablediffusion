from setuptools import setup

setup(
    name='stablediffusion',
    version='0.0.1',
    description='',
    packages=["ldm"],
    install_requires=[
        'torch',
        'numpy',
        'tqdm',
    ],
)
