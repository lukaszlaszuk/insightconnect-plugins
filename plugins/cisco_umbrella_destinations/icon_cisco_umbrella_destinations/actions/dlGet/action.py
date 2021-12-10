import insightconnect_plugin_runtime
from .schema import DlGetInput, DlGetOutput, Input, Output, Component
# Custom imports below


class DlGet(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='dlGet',
                description=Component.DESCRIPTION,
                input=DlGetInput(),
                output=DlGetOutput())

    def run(self, params={}):
        orgid = params.get(Input.ORGANIZATIONID)
        dstid = params.get(Input.DESTINATIONLISTID)
        if orgid and dstid:
            return {
                Output.SUCCESS: self.connection.client.get_destination_list()
            }
        else:
            raise Exception("No organization ID AND destinationList ID provided")
