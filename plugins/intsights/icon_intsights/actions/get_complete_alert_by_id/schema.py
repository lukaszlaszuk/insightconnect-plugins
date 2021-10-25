# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Get an alert's complete details for a given alert ID"


class Input:
    ALERT_ID = "alert_id"
    

class Output:
    ASSETS = "assets"
    ASSIGNEES = "assignees"
    DETAILS = "details"
    FOUND_DATE = "found_date"
    ID = "id"
    IS_CLOSED = "is_closed"
    IS_FLAGGED = "is_flagged"
    LEAK_NAME = "leak_name"
    TAKEDOWN_STATUS = "takedown_status"
    UPDATE_DATE = "update_date"
    

class GetCompleteAlertByIdInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "alert_id": {
      "type": "string",
      "title": "Alert ID",
      "description": "Alert's unique ID",
      "order": 1
    }
  },
  "required": [
    "alert_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetCompleteAlertByIdOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "assets": {
      "type": "array",
      "title": "Assets",
      "description": "List of assets",
      "items": {
        "type": "string"
      },
      "order": 2
    },
    "assignees": {
      "type": "array",
      "title": "Assignees",
      "description": "List of assignees",
      "items": {
        "type": "string"
      },
      "order": 3
    },
    "details": {
      "type": "object",
      "title": "Details",
      "description": "Alert details",
      "order": 4
    },
    "found_date": {
      "type": "string",
      "title": "Found Date",
      "displayType": "date",
      "description": "Alert found date",
      "format": "date-time",
      "order": 5
    },
    "id": {
      "type": "string",
      "title": "ID",
      "description": "Alert ID",
      "order": 1
    },
    "is_closed": {
      "type": "boolean",
      "title": "Is Closed",
      "description": "Is alert closed",
      "order": 8
    },
    "is_flagged": {
      "type": "boolean",
      "title": "Is Flagged",
      "description": "Is alert flagged",
      "order": 9
    },
    "leak_name": {
      "type": "string",
      "title": "Leak Name",
      "description": "Name of the leak DBs in data leakage alerts",
      "order": 10
    },
    "takedown_status": {
      "type": "string",
      "title": "Takedown Status",
      "description": "Alert remediation status",
      "order": 7
    },
    "update_date": {
      "type": "string",
      "title": "Found Date",
      "displayType": "date",
      "description": "Alert update date",
      "format": "date-time",
      "order": 6
    }
  },
  "required": [
    "assets",
    "assignees",
    "details",
    "found_date",
    "id",
    "is_closed",
    "is_flagged",
    "takedown_status",
    "update_date"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
