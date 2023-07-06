# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Signs the user out of all active application and browser sessions, and prevents the user from signing in any new session. Supported IAM systems - Azure AD and Active Directory (on-premises)"


class Input:
    ACCOUNT_IDENTIFIERS = "account_identifiers"
    

class Output:
    MULTI_RESPONSE = "multi_response"
    

class DisableAccountInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "account_identifiers": {
      "type": "array",
      "title": "Account Identifiers",
      "description": "User Account Identifiers containing account name and description",
      "items": {
        "$ref": "#/definitions/account_identifiers"
      },
      "order": 1
    }
  },
  "required": [
    "account_identifiers"
  ],
  "definitions": {
    "account_identifiers": {
      "type": "object",
      "title": "account_identifiers",
      "properties": {
        "account_name": {
          "type": "string",
          "title": "Account Name",
          "description": "The User account that needs to be acted upon",
          "order": 1
        },
        "description": {
          "type": "string",
          "title": "Description",
          "description": "Description of a response task",
          "order": 2
        }
      },
      "required": [
        "account_name"
      ]
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class DisableAccountOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "multi_response": {
      "type": "array",
      "title": "Multi Response",
      "description": "Disable Account Response Array",
      "items": {
        "$ref": "#/definitions/multi_response"
      },
      "order": 1
    }
  },
  "required": [
    "multi_response"
  ],
  "definitions": {
    "multi_response": {
      "type": "object",
      "title": "multi_response",
      "properties": {
        "status": {
          "type": "integer",
          "title": "Status",
          "description": "Status Code of response",
          "order": 1
        },
        "task_id": {
          "type": "string",
          "title": "Task ID",
          "description": "Task ID in Trend Micro Vision One of the executed action",
          "order": 2
        }
      },
      "required": [
        "status"
      ]
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)