# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Get on-call request is used to retrieve current on-call participants of a specific schedule"


class Input:
    DATE = "date"
    FLAT = "flat"
    SCHEDULEIDENTIFIER = "scheduleIdentifier"
    SCHEDULEIDENTIFIERTYPE = "scheduleIdentifierType"
    

class Output:
    DATA = "data"
    REQUESTID = "requestId"
    TOOK = "took"
    

class GetOnCallsInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "date": {
      "type": "string",
      "title": "Date",
      "displayType": "date",
      "description": "Starting date of the timeline that will be provided in format as (yyyy-MM-dd'T'HH:mm:ssZ) (e.g. 2017-01-15T08:00:00+02:00). Default date is the moment of the time that request is received.",
      "format": "date-time",
      "order": 4
    },
    "flat": {
      "type": "boolean",
      "title": "Flat",
      "description": "When enabled, retrieves user names of all on call participants. Default value is false",
      "order": 3
    },
    "scheduleIdentifier": {
      "type": "string",
      "title": "Schedule Identifier",
      "description": "Identifier of the schedule",
      "order": 1
    },
    "scheduleIdentifierType": {
      "type": "string",
      "title": "Schedule Identifier Type",
      "description": "Type of the schedule identifier that is provided as an in-line parameter. Possible values are id and name. Default value is id",
      "default": "id",
      "enum": [
        "id",
        "name"
      ],
      "order": 2
    }
  },
  "required": [
    "scheduleIdentifier"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetOnCallsOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "data": {
      "type": "object",
      "title": "Data",
      "description": "Response DATA from OpsGenie API",
      "order": 1
    },
    "requestId": {
      "type": "string",
      "title": "Request ID",
      "description": "ID of a executed API request",
      "order": 3
    },
    "took": {
      "type": "number",
      "title": "Took",
      "description": "Time took to execute API",
      "order": 2
    }
  },
  "required": [
    "data",
    "requestId",
    "took"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
