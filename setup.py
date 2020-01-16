from setuptools import setup, find_packages


setup(
    name='pybothub',
    version='1.0.0',
    packages=find_packages(),
    url='https://github.com/bothub-it/pybothub',
    author='Daniel Yohan',
    author_email='dyohan9@gmail.com',
    install_requires=[
        'requests >= 2.0.0, <= 2.22.0',
    ],
    python_requires='>=3.4',
)
