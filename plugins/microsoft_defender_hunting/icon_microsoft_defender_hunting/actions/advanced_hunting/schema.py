# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Runs advanced hunting query and retrieves the data"


class Input:
    QUERY = "query"
    

class Output:
    COLUMNS = "columns"
    ROWS = "rows"
    

class AdvancedHuntingInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "query": {
      "type": "string",
      "title": "Query",
      "description": "Advanced Hunting query to run",
      "order": 1
    }
  },
  "required": [
    "query"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class AdvancedHuntingOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "columns": {
      "type": "array",
      "title": "Columns",
      "description": "Schema containing response column's name and type",
      "items": {
        "$ref": "#/definitions/column"
      },
      "order": 1
    },
    "rows": {
      "type": "array",
      "title": "Rows",
      "description": "Array of objects containing query response values with keys as specific column name",
      "items": {
        "type": "object"
      },
      "order": 2
    }
  },
  "required": [
    "columns",
    "rows"
  ],
  "definitions": {
    "column": {
      "type": "object",
      "title": "column",
      "properties": {
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Column's name",
          "order": 1
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Column's data type",
          "order": 2
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)