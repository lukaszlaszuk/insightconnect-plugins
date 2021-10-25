# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Search indicators in IntSights TIP"


class Input:
    INDICATOR_VALUE = "indicator_value"
    

class Output:
    FIRST_SEEN = "first_seen"
    GEO_LOCATION = "geo_location"
    LAST_SEEN = "last_seen"
    LAST_UPDATE = "last_update"
    RELATED_CAMPAIGNS = "related_campaigns"
    RELATED_MALWARE = "related_malware"
    RELATED_THREAT_ACTORS = "related_threat_actors"
    SCORE = "score"
    SEVERITY = "severity"
    SOURCES = "sources"
    SYSTEM_TAGS = "system_tags"
    TAGS = "tags"
    TYPE = "type"
    VALUE = "value"
    WHITELIST = "whitelist"
    

class GetIndicatorByValueInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "indicator_value": {
      "type": "string",
      "title": "Indicator Value",
      "description": "Value of the indicator",
      "order": 1
    }
  },
  "required": [
    "indicator_value"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetIndicatorByValueOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "first_seen": {
      "type": "string",
      "title": "First Seen",
      "description": "First seen",
      "order": 6
    },
    "geo_location": {
      "type": "string",
      "title": "Geographic Location",
      "description": "Geographic location",
      "order": 9
    },
    "last_seen": {
      "type": "string",
      "title": "Last Seen",
      "description": "Last seen",
      "order": 7
    },
    "last_update": {
      "type": "string",
      "title": "Last Update",
      "description": "Last update",
      "order": 8
    },
    "related_campaigns": {
      "type": "array",
      "title": "Related Campaigns",
      "description": "Related campaigns",
      "items": {
        "type": "string"
      },
      "order": 14
    },
    "related_malware": {
      "type": "array",
      "title": "Related Malware",
      "description": "Related malware",
      "items": {
        "type": "string"
      },
      "order": 13
    },
    "related_threat_actors": {
      "type": "array",
      "title": "Related Threat Actors",
      "description": "Related threat actors",
      "items": {
        "type": "string"
      },
      "order": 15
    },
    "score": {
      "type": "integer",
      "title": "Score",
      "description": "Score",
      "order": 4
    },
    "severity": {
      "type": "string",
      "title": "Severity",
      "description": "Severity",
      "order": 3
    },
    "sources": {
      "type": "array",
      "title": "Sources",
      "description": "Sources",
      "items": {
        "$ref": "#/definitions/source"
      },
      "order": 10
    },
    "system_tags": {
      "type": "array",
      "title": "System Tags",
      "description": "System tags",
      "items": {
        "type": "string"
      },
      "order": 12
    },
    "tags": {
      "type": "array",
      "title": "Tags",
      "description": "Tags",
      "items": {
        "type": "string"
      },
      "order": 11
    },
    "type": {
      "type": "string",
      "title": "Type",
      "description": "Type",
      "order": 2
    },
    "value": {
      "type": "string",
      "title": "Value",
      "description": "Value",
      "order": 1
    },
    "whitelist": {
      "type": "boolean",
      "title": "Whitelist",
      "description": "Whitelist",
      "order": 5
    }
  },
  "required": [
    "related_campaigns",
    "related_malware",
    "related_threat_actors",
    "score",
    "sources",
    "system_tags",
    "tags",
    "whitelist"
  ],
  "definitions": {
    "source": {
      "type": "object",
      "title": "source",
      "properties": {
        "ConfidenceLevel": {
          "type": "integer",
          "title": "Confidence Level",
          "description": "Level of confidence",
          "order": 2
        },
        "Name": {
          "type": "string",
          "title": "Name",
          "description": "Name",
          "order": 1
        }
      },
      "required": [
        "ConfidenceLevel",
        "Name"
      ]
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
