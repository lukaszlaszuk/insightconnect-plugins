# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Retrieve the value of a variable"


class Input:
    VARIABLE_NAME = "variable_name"
    

class Output:
    VALUE = "value"
    

class RetrieveInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "variable_name": {
      "type": "string",
      "title": "Variable Name",
      "description": "Variable to get value from",
      "order": 1
    }
  },
  "required": [
    "variable_name"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class RetrieveOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "value": {
      "type": "string",
      "title": "Variable Value",
      "description": "Value",
      "order": 1
    }
  },
  "required": [
    "value"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)