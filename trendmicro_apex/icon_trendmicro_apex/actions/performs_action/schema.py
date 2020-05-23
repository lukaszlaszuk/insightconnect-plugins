# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "This action performs agent actions such as endpoint isolation, restoration, relocation, and uninstalls"


class Input:
    ACTION = "action"
    ALLOW_MULTIPLE_MATCH = "allow_multiple_match"
    ENTITY_ID = "entity_id"
    HOST_NAME = "host_name"
    IP_ADDRESS = "ip_address"
    MAC_ADDRESS = "mac_address"
    PRODUCT = "product"
    RELOCATE_TO_FOLDER_PATH = "relocate_to_folder_path"
    RELOCATE_TO_SERVER_ID = "relocate_to_server_id"
    SKIP_IDS = "skip_ids"
    

class Output:
    RESULT_CODE = "result_code"
    RESULT_CONTENT = "result_content"
    RESULT_DESCRIPTION = "result_description"
    

class PerformsActionInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "action": {
      "type": "string",
      "title": "Action",
      "description": "Perform action",
      "enum": [
        "Isolate",
        "Restore",
        "Relocate",
        "Uninstall"
      ],
      "order": 1
    },
    "allow_multiple_match": {
      "type": "boolean",
      "title": "Allow Multiple Match",
      "description": "True - Allows multiple matches False - Does not allow multiple matches",
      "default": true,
      "order": 2
    },
    "entity_id": {
      "type": "string",
      "title": "Entity ID",
      "description": "The GUID of the managed product agent. Use to identify the agent(s) on which the action is performed",
      "order": 3
    },
    "host_name": {
      "type": "string",
      "title": "Host Name",
      "description": "The endpoint name of the managed product agent. Use to identify the agent(s) on which the action is performed",
      "order": 4
    },
    "ip_address": {
      "type": "string",
      "title": "IP Address",
      "description": "The IP address of the managed product agent. Use to identify the agent(s) on which the action is performed",
      "order": 5
    },
    "mac_address": {
      "type": "string",
      "title": "MAC Address",
      "description": "The MAC address of the managed product agent. Use to identify the agent(s) on which the action is performed",
      "order": 6
    },
    "product": {
      "type": "string",
      "title": "Product",
      "description": "The Trend Micro product on the server instance. Use to identify the agent(s) on which the action is performed",
      "order": 7
    },
    "relocate_to_folder_path": {
      "type": "string",
      "title": "Relocate to Folder Path",
      "description": "The target directory for the agent",
      "order": 8
    },
    "relocate_to_server_id": {
      "type": "string",
      "title": "Relocate to Server ID",
      "description": "The GUID of the target server for the agent",
      "order": 9
    },
    "skip_ids": {
      "type": "array",
      "title": "Skip Entity ID",
      "description": "Skip entity ids on isolate and uninstall actions",
      "items": {
        "type": "string"
      },
      "order": 10
    }
  },
  "required": [
    "action"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class PerformsActionOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "result_code": {
      "type": "integer",
      "title": "Result Code",
      "description": "The Apex Central Automation API result code",
      "order": 1
    },
    "result_content": {
      "type": "array",
      "title": "Result Content",
      "description": "The Apex Central Automation API result content",
      "items": {
        "$ref": "#/definitions/result_content"
      },
      "order": 2
    },
    "result_description": {
      "type": "string",
      "title": "Result Description",
      "description": "The Apex Central Automation API result description",
      "order": 3
    }
  },
  "definitions": {
    "result_content": {
      "type": "object",
      "title": "result_content",
      "properties": {
        "capabilities": {
          "type": "array",
          "title": "Capabilities",
          "description": "Result capabilities",
          "items": {
            "type": "string"
          },
          "order": 1
        },
        "entity_id": {
          "type": "string",
          "title": "Entity ID",
          "description": "Result entity ID",
          "order": 2
        },
        "folder_path": {
          "type": "string",
          "title": "Folder Path",
          "description": "Result folder path",
          "order": 3
        },
        "host_name": {
          "type": "string",
          "title": "Host Name",
          "description": "Result host name",
          "order": 4
        },
        "ip_address_list": {
          "type": "string",
          "title": "IP Address List",
          "description": "Result IP address list",
          "order": 5
        },
        "isolation_status": {
          "type": "string",
          "title": "Isolation Status",
          "description": "Result isolation status",
          "order": 6
        },
        "mac_address_list": {
          "type": "string",
          "title": "MAC Address List",
          "description": "Result MAC address list",
          "order": 7
        },
        "managing_server_id": {
          "type": "string",
          "title": "Managing Server ID",
          "description": "Result managing server ID",
          "order": 8
        },
        "product": {
          "type": "string",
          "title": "Product",
          "description": "Result product",
          "order": 9
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)