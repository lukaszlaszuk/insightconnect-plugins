import insightconnect_plugin_runtime
from ..util.api import CiscoUmbrellaManagementAPI
from insightconnect_plugin_runtime.exceptions import PluginException, ConnectionTestException
from .schema import ConnectionSchema, Input


class Connection(insightconnect_plugin_runtime.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.client = None

    def connect(self, params={}):
        self.logger.info("Connect: Connecting...")
        self.client = CiscoUmbrellaManagementAPI(
            params.get(Input.API_KEY).get("api_key"),
            params.get(Input.API_SECRET).get("api_secret"),
            params.get(Input.ORGANIZATION_ID).get("organization_id"),
            self.logger,
        )

    def test(self):
        try:
            self.client.get_destination_lists()
            return {"success": True}
        except PluginException as e:
            raise ConnectionTestException(cause=e.cause, assistance=e.assistance, data=e.data)