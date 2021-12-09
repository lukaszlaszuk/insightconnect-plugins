import insightconnect_plugin_runtime
from .schema import DlDeleteInput, DlDeleteOutput, Input, Output, Component
# Custom imports below


class DlDelete(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='dlDelete',
                description=Component.DESCRIPTION,
                input=DlDeleteInput(),
                output=DlDeleteOutput())

    def run(self, params={}):
        # TODO: Implement run function
        return {}