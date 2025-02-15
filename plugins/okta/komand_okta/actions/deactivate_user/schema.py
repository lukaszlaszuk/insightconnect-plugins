# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Deactivate a user"


class Input:
    LOGIN = "login"
    

class Output:
    LOGIN = "login"
    SUCCESS = "success"
    USERID = "userId"
    

class DeactivateUserInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "login": {
      "type": "string",
      "title": "Okta User Login",
      "description": "The login of the employee to deactivate",
      "order": 1
    }
  },
  "required": [
    "login"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class DeactivateUserOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "login": {
      "type": "string",
      "title": "Okta User Login",
      "description": "The login of the Okta user",
      "order": 1
    },
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "Whether deactivation was successful",
      "order": 3
    },
    "userId": {
      "type": "string",
      "title": "Okta User ID",
      "description": "The user ID of the Okta user",
      "order": 2
    }
  },
  "required": [
    "success"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
