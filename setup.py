from setuptools import setup, find_packages


setup(
    name='bothub',
    version='1.0.0',
    packages=find_packages(),
    url='https://github.com/bothub-it/pybothub',
    install_requires=[
        'requests >= 2.0.0, <= 2.22.0',
    ],
    python_requires='>=3.4',
)
