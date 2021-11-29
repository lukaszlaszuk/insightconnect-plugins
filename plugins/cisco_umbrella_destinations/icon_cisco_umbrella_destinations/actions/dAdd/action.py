import insightconnect_plugin_runtime
from .schema import DAddInput, DAddOutput, Input, Output, Component
# Custom imports below


class DAdd(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='dAdd',
                description=Component.DESCRIPTION,
                input=DAddInput(),
                output=DAddOutput())

    def run(self, params={}):
        # TODO: Implement run function
        return {}
