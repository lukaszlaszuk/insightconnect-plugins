# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Update the status of a scan"


class Input:
    ID = "id"
    STATUS = "status"
    

class Output:
    LINKS = "links"
    

class UpdateScanStatusInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "id": {
      "type": "integer",
      "title": "ID",
      "description": "Scan ID",
      "order": 1
    },
    "status": {
      "type": "string",
      "title": "Status",
      "description": "Status to which the scan should be set (stop, resume, pause)",
      "default": "stop",
      "enum": [
        "stop",
        "resume",
        "pause"
      ],
      "order": 2
    }
  },
  "required": [
    "id",
    "status"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class UpdateScanStatusOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "links": {
      "type": "array",
      "title": "Links",
      "description": "Hypermedia links to corresponding or related resources",
      "items": {
        "$ref": "#/definitions/link"
      },
      "order": 1
    }
  },
  "required": [
    "links"
  ],
  "definitions": {
    "link": {
      "type": "object",
      "title": "link",
      "properties": {
        "href": {
          "type": "string",
          "title": "URL",
          "description": "A hypertext reference, which is either a URI (see RFC 3986) or URI template (see RFC 6570)",
          "order": 1
        },
        "rel": {
          "type": "string",
          "title": "Rel",
          "description": "Link relation type following RFC 5988",
          "order": 2
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)