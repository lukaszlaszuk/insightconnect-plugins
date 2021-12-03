import base64
import requests
import insightconnect_plugin_runtime
from ..util.api import CiscoUmbrellaManagementAPI

from .schema import ConnectionSchema, Input


# Custom imports below


class Connection(insightconnect_plugin_runtime.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.test_url = f"https://management.api.umbrella.com/v1/organizations/{self.orgId}/destinationlists"
        self.apiKey = None
        self.apiSecretKey = None
        self.combinedKey = None
        self.encodedKey = None
        self.orgId = None
        self.client = None

    def connect(self, params={}):
        self.logger.info("Connect: Connecting...")
        self.client = CiscoUmbrellaManagementAPI(
            params.get(Input.API_KEY).get("api_key"),
            params.get(Input.API_SECRET).get("api_secret"),
            params.get(Input.ORGANIZATION_ID).get("organization_id"),
            self.logger,
        )

    def test(self, params={}):
        # Encode to base64 | Combine api_key & secret_key with ':' and encode
        self.apiKey = params.get(Input.API_KEY)
        self.apiSecretKey = params.get(Input.API_SECRET)
        self.combinedKey = self.apiKey + ":" + self.apiSecretKey
        self.encodedKey = base64.b64encode(self.combinedKey.encode("utf-8")).decode('utf-8')

        headers = {"Authorization": f"Basic {self.encodedKey}", "Content-Type": "application/json"}
        response = requests.get(self.test_url, headers=headers)

        if response.status_code == 200:
            return True
        elif response.status_code == 402:
            raise Exception("Invalid API Authentication")
        elif response.status_code == 404:
            raise Exception("Not found")
        elif response.status_code == 429:
            raise Exception("Rate Limit reached")
        else:
            return False
