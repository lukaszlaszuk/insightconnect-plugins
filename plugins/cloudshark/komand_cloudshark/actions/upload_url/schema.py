# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Upload capture file by URL"


class Input:
    COMMENTS = "comments"
    FILENAME = "filename"
    TAGS = "tags"
    URL = "url"
    

class Output:
    EXCEPTIONS = "exceptions"
    FILENAME = "filename"
    ID = "id"
    STATUS = "status"
    

class UploadUrlInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "comments": {
      "type": "string",
      "title": "Comments",
      "description": "File comments",
      "order": 4
    },
    "filename": {
      "type": "string",
      "title": "Filename",
      "description": "Resulting filename",
      "order": 3
    },
    "tags": {
      "type": "string",
      "title": "Tags",
      "description": "Comma-separated list of tags",
      "order": 2
    },
    "url": {
      "type": "string",
      "title": "Url",
      "description": "URL",
      "order": 1
    }
  },
  "required": [
    "url"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class UploadUrlOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "exceptions": {
      "type": "array",
      "title": "Exceptions",
      "description": "Exceptions",
      "items": {
        "type": "string"
      },
      "order": 4
    },
    "filename": {
      "type": "string",
      "title": "Filename",
      "description": "Filename",
      "order": 2
    },
    "id": {
      "type": "string",
      "title": "Id",
      "description": "Cloud Shark ID",
      "order": 3
    },
    "status": {
      "type": "integer",
      "title": "Status",
      "description": "HTTP Status",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)