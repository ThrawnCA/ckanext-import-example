import logging

from ckan import plugins

LOG = logging.getLogger(__name__)


class ImportExamplePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IBlueprint, inherit=True)

    def get_blueprint(self):
        LOG.info('Called ExamplePlugin')
        import dataset
        return []

