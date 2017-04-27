from setuptools import setup


setup(
    name='agiledoc',
    version='1.0',
    description='Agile Documentation System',
    author='Ludovic Bouguerra',
    author_email='bouguerra.ludovic@gmail.com',
    url='https://www.agile-doc.com/',
    packages=['agiledoc'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)
