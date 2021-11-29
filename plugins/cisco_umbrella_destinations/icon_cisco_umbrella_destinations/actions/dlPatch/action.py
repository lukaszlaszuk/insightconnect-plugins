import insightconnect_plugin_runtime
from .schema import DlPatchInput, DlPatchOutput, Input, Output, Component
# Custom imports below


class DlPatch(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='dlPatch',
                description=Component.DESCRIPTION,
                input=DlPatchInput(),
                output=DlPatchOutput())

    def run(self, params={}):
        # TODO: Implement run function
        return {}
