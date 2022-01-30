from setuptools import setup, find_packages

setup(
    name='ckanext-import-example',
    version='0.0.1',
    description='Example plugin to test blueprint imports',
    url='https://example.com',
    author='Qld Government',
    author_email='qol.development@smartservice.qld.gov.au',

    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext'],

    entry_points='''
    [ckan.plugins]
    import_example=ckanext.import_example.plugin:ImportExamplePlugin
    '''
)

