# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Extracts all SHA256 Hashes from a string or file"


class Input:
    FILE = "file"
    STR = "str"
    

class Output:
    SHA256 = "sha256"
    

class Sha256ExtractorInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "file": {
      "type": "string",
      "title": "File",
      "displayType": "bytes",
      "description": "Input file as bytes, supports text and binary file types such as PDF, DOCX, XLSX, PPTX, ODT, ODP, ODS",
      "format": "bytes",
      "order": 2
    },
    "str": {
      "type": "string",
      "title": "String",
      "description": "Input string",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class Sha256ExtractorOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "sha256": {
      "type": "array",
      "title": "SHA256 Hash",
      "description": "List of extracted SHA256 Hashes",
      "items": {
        "type": "string"
      },
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
