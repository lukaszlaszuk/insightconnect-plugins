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
        orgId = params.get(Input.ORGANIZATIONID)
        destinationlistId = params.get(Input.DESTINATIONLISTID)
        payload = params.get(Input.PAYLOAD)


        return {}
