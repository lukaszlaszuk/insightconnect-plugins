# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Close existing alert from OpsGenie"


class Input:
    IDENTIFIER = "identifier"
    IDENTIFIERTYPE = "identifierType"
    NOTE = "note"
    SOURCE = "source"
    USER = "user"
    

class Output:
    REQUESTID = "requestId"
    RESULT = "result"
    TOOK = "took"
    

class CloseAlertInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "identifier": {
      "type": "string",
      "title": "Alert ID",
      "description": "Identifier of the alert",
      "order": 1
    },
    "identifierType": {
      "type": "string",
      "title": "Identifier Type",
      "description": "Type of the identifier that is provided as an in-line parameter. Possible values are id, tiny and alias. Default value is id",
      "default": "id",
      "enum": [
        "id",
        "tiny",
        "alias"
      ],
      "order": 2
    },
    "note": {
      "type": "string",
      "title": "Note",
      "description": "Additional alert note to add",
      "order": 5
    },
    "source": {
      "type": "string",
      "title": "Source",
      "description": "Display name of the request source",
      "order": 4
    },
    "user": {
      "type": "string",
      "title": "User",
      "description": "Display name of the request owner",
      "order": 3
    }
  },
  "required": [
    "identifier"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class CloseAlertOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "requestId": {
      "type": "string",
      "title": "Request ID",
      "description": "ID of a executed API request",
      "order": 3
    },
    "result": {
      "type": "string",
      "title": "Result",
      "description": "Result message from API",
      "order": 1
    },
    "took": {
      "type": "number",
      "title": "Took",
      "description": "Time took to execute API",
      "order": 2
    }
  },
  "required": [
    "requestId",
    "result",
    "took"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
