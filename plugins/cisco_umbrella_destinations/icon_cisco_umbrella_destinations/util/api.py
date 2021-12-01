import json
import requests
from requests.auth import HTTPBasicAuth
from logging import Logger
from typing import Optional


class CiscoUmbrellaManagementAPI:
    def __init__(self, api_key: str, api_secret: str, organization_id: str, logger: Logger):
        self.url = "https://management.api.umbrella.com/v1/"
        self.api_secret = api_secret
        self.api_key = api_key
        self.organization_id = organization_id
        self.logger = logger

