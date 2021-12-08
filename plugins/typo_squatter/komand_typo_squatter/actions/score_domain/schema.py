# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Get phishing score for a domain. Scores over 65 should be considered likely phishing attempts with scores over 90 being very suspicious"


class Input:
    DOMAIN = "domain"
    

class Output:
    SCORE = "score"
    

class ScoreDomainInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "domain": {
      "type": "string",
      "title": "Domain",
      "description": "Domain to check",
      "default": "example.com",
      "order": 1
    }
  },
  "required": [
    "domain"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ScoreDomainOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "score": {
      "type": "number",
      "title": "Score",
      "description": "Phishing score",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
