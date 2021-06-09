# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Query email info"


class Input:
    ADDRESS = "address"
    DOMAIN = "domain"
    EMAIL = "email"
    

class Output:
    EMAIL_RESULT = "email_result"
    RISK_SCORE = "risk_score"
    

class EmailLookupInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "address": {
      "type": "string",
      "title": "IP Address",
      "description": "IP address to query",
      "order": 1
    },
    "domain": {
      "type": "string",
      "title": "Email Domain",
      "description": "Domain of email used in transaction",
      "order": 3
    },
    "email": {
      "type": "string",
      "title": "Email Address",
      "description": "Email address used in transaction",
      "order": 2
    }
  },
  "required": [
    "address"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class EmailLookupOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "email_result": {
      "$ref": "#/definitions/email",
      "title": "Email Result",
      "description": "Results for email",
      "order": 1
    },
    "risk_score": {
      "type": "string",
      "title": "Risk Score",
      "description": "Overall risk score",
      "order": 2
    }
  },
  "definitions": {
    "email": {
      "type": "object",
      "title": "email",
      "properties": {
        "is_free": {
          "type": "boolean",
          "title": "Is Free",
          "description": "Is email free",
          "order": 1
        },
        "is_high_risk": {
          "type": "boolean",
          "title": "Is High Risk",
          "description": "Is email high risk",
          "order": 2
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)