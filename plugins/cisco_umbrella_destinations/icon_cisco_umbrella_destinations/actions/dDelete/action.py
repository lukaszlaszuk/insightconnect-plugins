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
        # Careful because this works but only because our
        # payload is double wrapped [[ x, y ]]
        # If it is single wrapped you will get type error

        payload = params.get(Input.PAYLOAD)
        return self.connection.client.delete_destinations(data=payload)

