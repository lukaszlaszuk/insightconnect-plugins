import json
import requests
from requests.auth import HTTPBasicAuth
from insightconnect_plugin_runtime.exceptions import PluginException
from logging import Logger
from typing import Optional


class CiscoUmbrellaManagementAPI:
    def __init__(self, api_key: str, api_secret: str, organization_id: int, destination_list_id: int, payload: dict ,logger: Logger):
        self.url = "https://management.api.umbrella.com/v1/"
        self.api_key = api_key
        self.api_secret = api_secret
        self.organization_id = organization_id
        self.destination_list_id = destination_list_id
        self.payload = payload
        self.logger = logger

    # def destinations_most_recent_request(self, domain: str) -> dict:
    #     return self._call_api(
    #         "GET",
    #         f"organizations/{self.organization_id}/destinations/{domain}/activity",
    #         {"limit": 500},
    #     )

    def get_destination_lists(self) -> dict:
        return self._call_api(
            "GET",
            f"organizations/{self.organization_id}/destinationlists",
            {"limit": 500}
        )

    def create_destination_list(self, params={}, data={}) -> dict:
        params['organization_id'] = self.organization_id
        return self._call_api(
            "POST",
            f"organizations/{self.organization_id}/destinationlists",
            None,
            {"payload": data},
        )

    def create_destinations(self, params={}, data={}) -> dict:
        params['organizationId'] = self.organization_id
        params['destinationListId'] = self.destination_list_id
        data['payload'] = self.payload
        return self._call_api(
            "POST",
            f"organizations/{self.organization_id}/destinationlists/{self.destination_list_id}/destinations",
            None,
            {"payload": data},
        )


    def _call_api(
        self,
        method: str,
        path: str,
        json_data: Optional[dict] = None,
        params: Optional[dict] = None,
    ) -> dict:
        response = {"text": ""}

        try:
            response = requests.request(
                method,
                self.url + path,
                json=json_data,
                params=params,
                auth=HTTPBasicAuth(self.api_key, self.api_secret),
            )

            if response.status_code == 401:
                raise PluginException(preset=PluginException.Preset.USERNAME_PASSWORD)
            if response.status_code == 403:
                raise PluginException(preset=PluginException.Preset.UNAUTHORIZED)
            if response.status_code == 404:
                raise PluginException(preset=PluginException.Preset.NOT_FOUND)
            if response.status_code >= 400:
                response_data = response.text
                raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response_data)
            if response.status_code == 201 or response.status_code == 204:
                return {}
            if 200 <= response.status_code < 300:
                return response.json()

            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
        except json.decoder.JSONDecodeError as e:
            self.logger.info(f"Invalid JSON: {e}")
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=response.text)
        except requests.exceptions.HTTPError as e:
            self.logger.info(f"Call to Cisco Umbrella Reporting API failed: {e}")
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
