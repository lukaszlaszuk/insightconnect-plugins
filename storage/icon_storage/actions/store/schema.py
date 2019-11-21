# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Store a variable in cache"


class Input:
    VARIABLE_NAME = "variable_name"
    VARIABLE_VALUE = "variable_value"
    

class Output:
    SUCCESS = "success"
    

class StoreInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "variable_name": {
      "type": "string",
      "title": "Variable Name",
      "description": "Name of the variable to store",
      "order": 1
    },
    "variable_value": {
      "type": "string",
      "title": "Variable Value",
      "description": "Value of the variable to store",
      "order": 2
    }
  },
  "required": [
    "variable_name",
    "variable_value"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class StoreOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "Was operation successful",
      "order": 1
    }
  },
  "required": [
    "success"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)