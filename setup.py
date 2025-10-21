from setuptools import setup, find_packages

setup(
    name='flask-lab-project',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'Flask==2.3.3',
    ],
    extras_require={
        'test': [
            'pytest==7.4.3',
            'pytest-cov==4.1.0',
        ],
    },
)
