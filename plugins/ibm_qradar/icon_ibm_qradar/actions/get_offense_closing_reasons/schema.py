# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Get Offense's Closing Reasons"


class Input:
    FIELDS = "fields"
    FILTER = "filter"
    INCLUDE_DELETED = "include_deleted"
    INCLUDE_RESERVED = "include_reserved"
    RANGE = "range"
    

class Output:
    DATA = "data"
    

class GetOffenseClosingReasonsInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "fields": {
      "type": "string",
      "title": "Fields",
      "description": "Specify which fields you would like to get back in the response. Fields that are not named are excluded. Specify subfields in brackets and multiple fields in the same object are separated by commas",
      "order": 3
    },
    "filter": {
      "type": "string",
      "title": "Filter",
      "description": "Restrict the elements in a list based on the contents of various fields",
      "order": 2
    },
    "include_deleted": {
      "type": "boolean",
      "title": "Include Deleted",
      "description": "If true, deleted closing reasons are included in the response. Defaults to false. Deleted closing reasons cannot be used to close an offense",
      "order": 4
    },
    "include_reserved": {
      "type": "boolean",
      "title": "Include Reserved",
      "description": "If true, reserved closing reasons are included in the response. Defaults to false. Reserved closing reasons cannot be used to close an offense",
      "order": 5
    },
    "range": {
      "type": "string",
      "title": "Range",
      "description": "Restrict the number of returned elements to a range, eg. 0-10, with 0 being the first index",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetOffenseClosingReasonsOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "data": {
      "type": "array",
      "title": "Offense Closing Reasons",
      "description": "JSON data of the Offense Closing Reasons",
      "items": {
        "$ref": "#/definitions/closing_reason"
      },
      "order": 1
    }
  },
  "definitions": {
    "closing_reason": {
      "type": "object",
      "title": "closing_reason",
      "properties": {
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "ID",
          "order": 1
        },
        "is_deleted": {
          "type": "boolean",
          "title": "Is Deleted",
          "description": "Is deleted",
          "order": 2
        },
        "is_reserved": {
          "type": "boolean",
          "title": "Is Reserved",
          "description": "Is reserved",
          "order": 3
        },
        "text": {
          "type": "string",
          "title": "Text",
          "description": "text",
          "order": 4
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)