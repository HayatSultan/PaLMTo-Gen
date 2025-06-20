from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='Palmto_gen',
    version='0.3a1',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'Palmto_gen': ['data/*'],
    },
    description='Generate synthetic trajectories using PLMs',
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='',
    author='Hayat Sultan',
    author_email='hayatsul@ualberta.ca',
    license='MIT',
    classifiers = classifiers,
    keywords='trajectory generation' 'Probablistic Language Models',
    install_requires= ['geopandas', 'tqdm', 'geopy', 'scipy', 'folium']
)