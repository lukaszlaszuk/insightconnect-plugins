import insightconnect_plugin_runtime
from .schema import GetOnCallsInput, GetOnCallsOutput, Input, Output, Component
# Custom imports below


class GetOnCalls(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_on_calls',
                description=Component.DESCRIPTION,
                input=GetOnCallsInput(),
                output=GetOnCallsOutput())

    def run(self, params={}):
        # TODO: Implement run function
        return {}
