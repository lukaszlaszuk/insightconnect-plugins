# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Publish an event"


class Input:
    EVENT = "event"
    

class Output:
    PUBLISHED = "published"
    

class PublishInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "event": {
      "type": "string",
      "title": "Event",
      "description": "Search by event ID",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class PublishOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "published": {
      "$ref": "#/definitions/published",
      "title": "Published",
      "description": "Info on published event",
      "order": 1
    }
  },
  "definitions": {
    "published": {
      "type": "object",
      "title": "published",
      "properties": {
        "id": {
          "type": "string",
          "title": "ID",
          "order": 4
        },
        "message": {
          "type": "string",
          "title": "Message",
          "order": 2
        },
        "name": {
          "type": "string",
          "title": "Name",
          "order": 1
        },
        "url": {
          "type": "string",
          "title": "URL",
          "order": 3
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
