from setuptools import setup, find_packages

curdir = dirname(__file__)
with io.open(join(curdir, "README.md"), encoding="utf-8") as fd:
    readme = fd.read()
with io.open(join(curdir, "CHANGELOG.md"), encoding="utf-8") as fd:
    changelog = fd.read()


setup(
    name='reddit_api',
    version='0.1',
    packages=find_packages(where='src'),
    description='Reddit API for Airflow',
    long_description=readme + "\n\n" + changelog,
    long_description_content_type='text/markdown',
    author='Unknwon',
    install_requires=[
        'praw',
    ],
    extras_require={
        'dev': [
            'pytest',
            'pytest-cov',
            'flake8',
            'black',
            'isort',
            'mypy',
            'pylint',
            'pre-commit',
            'tox',
            'twine',
            'wheel',
        ]
    },
    package_dir={"": "src"},
    entry_points={
        'console_scripts': [
            'airflow_reddit=airflow_reddit.cli:main',
        ],
    },
)
