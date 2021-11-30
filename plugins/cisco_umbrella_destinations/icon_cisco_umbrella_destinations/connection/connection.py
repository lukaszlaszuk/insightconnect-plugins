import insightconnect_plugin_runtime
import requests

from .schema import ConnectionSchema, Input
# Custom imports below


class Connection(insightconnect_plugin_runtime.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.test_url = "https://management.api.umbrella.com/v1"
        self.test_url2 = 'https://management.api.umbrella.com/v1/organizations/2372338/users'

    def connect(self, params=None):
        self.logger.info("Connect: Connecting...")
        if params is None:
            params = {}
        self.logger.info("Connect: Connecting..")
        key = params.get("api_key").get("secretKey")
        if not key:
            self.logger.error("Connection: connect: Empty key")
            raise Exception("Connection: connect: Empty key")

    def test(self):
        headers = {"Authorization": "Bearer " + self.key}
        response = requests.get(self.test_url, headers=headers)

        if response.status_code == 200:
            return True
        elif response.status_code == 401:
            raise Exception("Error: Invalid API key credentials")
        elif response.status_code == 404:
            raise False
