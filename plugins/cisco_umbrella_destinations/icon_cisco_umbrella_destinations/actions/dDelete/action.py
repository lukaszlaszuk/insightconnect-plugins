import insightconnect_plugin_runtime
from .schema import DDeleteInput, DDeleteOutput, Input, Output, Component
# Custom imports below


class DDelete(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='dDelete',
                description=Component.DESCRIPTION,
                input=DDeleteInput(),
                output=DDeleteOutput())

    def run(self, params={}):
        # TODO: Implement run function
        return {}
