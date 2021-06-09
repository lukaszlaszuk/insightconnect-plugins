# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Create a new scan configuration"


class Input:
    APP_ID = "app_id"
    ATTACK_TEMPLATE_ID = "attack_template_id"
    CONFIG_DESCRIPTION = "config_description"
    CONFIG_NAME = "config_name"
    

class Output:
    STATUS = "status"
    

class CreateScanConfigInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "app_id": {
      "type": "string",
      "title": "App ID",
      "description": "App UUID",
      "order": 3
    },
    "attack_template_id": {
      "type": "string",
      "title": "Attack Template ID",
      "description": "Attack template UUID",
      "order": 4
    },
    "config_description": {
      "type": "string",
      "title": "Description",
      "description": "The description of the scan configuration",
      "order": 2
    },
    "config_name": {
      "type": "string",
      "title": "Name",
      "description": "The name of the scan configuration",
      "order": 1
    }
  },
  "required": [
    "app_id",
    "attack_template_id",
    "config_name"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class CreateScanConfigOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "status": {
      "type": "integer",
      "title": "Status",
      "description": "Status code of the request",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)