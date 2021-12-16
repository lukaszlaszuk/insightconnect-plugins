import json
import requests
from requests.auth import HTTPBasicAuth
from insightconnect_plugin_runtime.exceptions import PluginException
from logging import Logger
from typing import Optional


class CiscoUmbrellaManagementAPI:
    def __init__(self,
                 api_key: str,
                 api_secret: str,
                 organization_id: int,
                 destination_list_id: int,
                 # logger: Logger
                 ):

        self.url = "https://management.api.umbrella.com/v1/"
        self.api_key = api_key
        self.api_secret = api_secret
        self.organization_id = organization_id
        self.destination_list_id = destination_list_id
        # self.logger = logger

    # DESTINATIONS LIST API

    # GET all destination lists
    # https://developer.cisco.com/docs/cloud-security/#!get-destination-lists
    def get_destination_lists(self) -> dict:
        return self._call_api(
            "GET",
            f"organizations/{self.organization_id}/destinationlists"
        )

    # GET destination list by ID
    # https://developer.cisco.com/docs/cloud-security/#!get-destination-list
    def get_destination_list(self) -> dict:
        return self._call_api(
            "GET",
            f"organizations/{self.organization_id}/destinationlists/{self.destination_list_id}"
        )

    # POST a new destination list
    # https://developer.cisco.com/docs/cloud-security/#!create-destination-list
    def create_destination_list(self, data: dict) -> dict:
        return self._call_api(
            "POST",
            f"organizations/{self.organization_id}/destinationlists",
            None,
            None,
            data=data
        )

    # PATCH (Update) destination list
    # https://developer.cisco.com/docs/cloud-security/#!update-destination-lists
    def update_destination_list(self, data: dict) -> dict:
        return self._call_api(
            "PATCH",
            f"organizations/{self.organization_id}/destinationlists/{self.destination_list_id}",
            None,
            None,
            data=data
        )

    # DELETE destination list
    # https://developer.cisco.com/docs/cloud-security/#!delete-destination-list
    def delete_destination_list(self) -> dict:
        return self._call_api(
            "DELETE",
            f'organizations/{self.organization_id}/destinationlists/{self.destination_list_id}'
        )

    # DESTINATIONS API

    # GET list of destinations related to destination list
    # https://developer.cisco.com/docs/cloud-security/#!get-destinations
    def get_destinations(self) -> dict:
        return self._call_api(
            "GET",
            f"organizations/{self.organization_id}/destinationlists/{self.destination_list_id}/destinations"
        )

    # POST destinations to existing destination list
    # https://developer.cisco.com/docs/cloud-security/#!create-destinations
    def create_destinations(self, data: dict) -> dict:
        return self._call_api(
            "POST",
            f"organizations/{self.organization_id}/destinationlists/{self.destination_list_id}/destinations",
            None,
            None,
            data=data
        )

    # DELETE list of destinations from destination list
    # https://developer.cisco.com/docs/cloud-security/#!delete-destinations
    def delete_destinations(self, data: dict) -> dict:
        return self._call_api(
            "DELETE",
            f"organizations/{self.organization_id}/destinationlists/{self.destination_list_id}/destinations/remove",
            None,
            None,
            data=data
        )

    def _call_api(
            self,
            # method -> GET/POST/etc
            method: str,
            # path -> url
            path: str,
            # json_data -> Json to send in body
            json_data: Optional[dict] = None,
            # Params -> Query (Params) String
            params: Optional[dict] = None,
            # data(payload) -> dict in body
            data: Optional[dict] = None,
    ) -> dict:
        # What does 'response' do?
        # response = {"text": ""}
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

        try:
            # Prevents json.dumps() on 'None' data
            if data is None:
                data_string = None
            else:
                data_string = json.dumps(data)
            response = requests.request(
                method,
                self.url + path,
                json=json_data,
                params=params,
                data=data_string,
                headers=headers,
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
