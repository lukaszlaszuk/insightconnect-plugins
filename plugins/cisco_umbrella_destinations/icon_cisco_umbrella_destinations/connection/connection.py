import base64

import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input
# Custom imports below


class Connection(insightconnect_plugin_runtime.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.test_url = "https://management.api.umbrella.com/v1"

    def connect(self, params):
        self.logger.info("Connect: Connecting...")
        self.apiKey = params.get(Input.API_KEY).get("api_key")
        self.apiSecretKey = params.get(Input.API_SECRET).get("api_secret")
        self.orgId = params.get(Input.ORGANIZATION_ID).get("organization_id")

        #Encode to base64 | Combine api_key & secret_key with ':' and encode
        self.combinedKey = self.apiKey + ":" + self.apiSecretKey
        self.encodedKey = base64.b64encode(self.combinedKey.encode("utf-8"))



    def test(self):
        pass
