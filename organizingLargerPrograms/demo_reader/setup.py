import setuptools

setuptools.setup(
    name='reader',
    version='1.0.0',
    description='Tools for reading various file formats',
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'}
)
