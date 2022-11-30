from setuptools import setup

setup(
    name='stablediffusion',
    version='0.0.1',
    description='',
    packages=["ldm", "ldm.models.diffusion"],
    install_requires=[
        'torch',
        'numpy',
        'tqdm',
    ],
)
