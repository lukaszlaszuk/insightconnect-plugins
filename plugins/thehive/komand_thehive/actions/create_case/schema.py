# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Create a new case"


class Input:
    CUSTOMFIELDS = "customFields"
    DESCRIPTION = "description"
    FLAG = "flag"
    JSONDATA = "jsonData"
    METRICS = "metrics"
    OWNER = "owner"
    PAP = "pap"
    SEVERITY = "severity"
    STARTDATE = "startDate"
    SUMMARY = "summary"
    TAGS = "tags"
    TASKS = "tasks"
    TEMPLATE = "template"
    TITLE = "title"
    TLP = "tlp"
    

class Output:
    CASE = "case"
    

class CreateCaseInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "customFields": {
      "type": "object",
      "title": "Custom Fields",
      "description": "Case custom fields",
      "order": 12
    },
    "description": {
      "type": "string",
      "title": "Case Description",
      "description": "Description of the case, supports markdown",
      "order": 2
    },
    "flag": {
      "type": "boolean",
      "title": "Flag",
      "description": "Case's flag, True to mark case as important",
      "default": false,
      "order": 6
    },
    "jsonData": {
      "type": "object",
      "title": "JSON",
      "description": "If the field is not equal to None, the case is instantiated using the JSON value instead of the arguements",
      "order": 15
    },
    "metrics": {
      "type": "object",
      "title": "Metrics",
      "description": "Case metrics collection. A JSON object where keys are defining metric name, and values are defining metric value",
      "order": 11
    },
    "owner": {
      "type": "string",
      "title": "Owner",
      "description": "Case's assignee",
      "order": 10
    },
    "pap": {
      "type": "integer",
      "title": "PAP",
      "description": "Password Authentication Protocol",
      "default": 2,
      "enum": [
        0,
        1,
        2,
        3
      ],
      "order": 8
    },
    "severity": {
      "type": "integer",
      "title": "Severity",
      "description": "Case severity",
      "default": 2,
      "enum": [
        1,
        2,
        3,
        4
      ],
      "order": 3
    },
    "startDate": {
      "type": "integer",
      "title": "Start Date",
      "description": "Case start date (datetime in ms) (will default to now if left blank)",
      "order": 4
    },
    "summary": {
      "type": "string",
      "title": "Summary",
      "description": "Case summary",
      "order": 9
    },
    "tags": {
      "type": "array",
      "title": "Tags",
      "description": "List of case tags",
      "items": {
        "type": "string"
      },
      "order": 5
    },
    "tasks": {
      "$ref": "#/definitions/itask",
      "title": "Task",
      "description": "Case task",
      "order": 14
    },
    "template": {
      "type": "string",
      "title": "Case Template",
      "description": "Case template's name. If specified then the case is created using the given template",
      "order": 13
    },
    "title": {
      "type": "string",
      "title": "Case Title",
      "description": "Name of the case",
      "order": 1
    },
    "tlp": {
      "type": "integer",
      "title": "TLP",
      "description": "Traffic Light Protocol level",
      "default": 2,
      "enum": [
        0,
        1,
        2,
        3
      ],
      "order": 7
    }
  },
  "required": [
    "title"
  ],
  "definitions": {
    "itask": {
      "type": "object",
      "title": "itask",
      "properties": {
        "description": {
          "type": "string",
          "title": "Description",
          "description": "Task's description",
          "order": 3
        },
        "flag": {
          "type": "boolean",
          "title": "Flag",
          "description": "Task's flag",
          "default": false,
          "order": 5
        },
        "id": {
          "type": "string",
          "title": "Case ID",
          "description": "ID for the case",
          "order": 1
        },
        "owner": {
          "type": "string",
          "title": "Task's assignee",
          "description": "Task owner",
          "order": 6
        },
        "status": {
          "type": "string",
          "title": "Status",
          "description": "Task status",
          "default": "Waiting",
          "enum": [
            "Waiting",
            "InProgress",
            "Completed",
            "Cancel"
          ],
          "order": 4
        },
        "title": {
          "type": "string",
          "title": "Title",
          "description": "Task's title",
          "order": 2
        }
      },
      "required": [
        "description",
        "title"
      ]
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class CreateCaseOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "case": {
      "$ref": "#/definitions/createCase",
      "title": "Case",
      "description": "Create case output",
      "order": 1
    }
  },
  "definitions": {
    "createCase": {
      "type": "object",
      "title": "createCase",
      "properties": {
        "assignee": {
          "type": "string",
          "title": "Assignee",
          "description": "User to assign the case to",
          "order": 12
        },
        "caseTemplate": {
          "type": "string",
          "title": "Case Template",
          "description": "Name or ID of the case template to use",
          "order": 14
        },
        "customFields": {
          "type": "object",
          "title": "Custom Fields",
          "description": "Custom fields",
          "order": 13
        },
        "description": {
          "type": "string",
          "title": "Description",
          "description": "Case description",
          "order": 2
        },
        "endDate": {
          "type": "integer",
          "title": "End Date",
          "description": "Case end date (datetime in ms)",
          "order": 5
        },
        "flag": {
          "type": "boolean",
          "title": "Flag",
          "description": "Case flags",
          "default": false,
          "order": 7
        },
        "observableRule": {
          "type": "string",
          "title": "Observable Rule",
          "description": "Case observable rule",
          "order": 18
        },
        "pap": {
          "type": "integer",
          "title": "Password Authentication Protocol",
          "description": "Case password authentication protocol",
          "default": 2,
          "enum": [
            0,
            1,
            2,
            3
          ],
          "order": 9
        },
        "severity": {
          "type": "integer",
          "title": "Severity",
          "description": "Case severity",
          "default": 2,
          "enum": [
            1,
            2,
            3,
            4
          ],
          "order": 3
        },
        "sharingParameters": {
          "type": "array",
          "title": "Sharing Parameters",
          "description": "Case sharing parameters",
          "items": {
            "type": "string"
          },
          "order": 16
        },
        "startDate": {
          "type": "integer",
          "title": "Start Date",
          "description": "Case start date (datetime in ms)",
          "order": 4
        },
        "status": {
          "type": "string",
          "title": "Status",
          "description": "Case status",
          "default": "New",
          "order": 10
        },
        "summary": {
          "type": "string",
          "title": "Summary",
          "description": "Case summary",
          "order": 11
        },
        "tags": {
          "type": "array",
          "title": "Tags",
          "description": "Case tags",
          "items": {
            "type": "string"
          },
          "order": 6
        },
        "taskRule": {
          "type": "string",
          "title": "Task Rule",
          "description": "Case task rule",
          "order": 17
        },
        "tasks": {
          "type": "array",
          "title": "Tasks",
          "description": "Tasks to create. If null, tasks from the case template will be used",
          "items": {
            "type": "string"
          },
          "order": 15
        },
        "title": {
          "type": "string",
          "title": "Title",
          "description": "Case title",
          "order": 1
        },
        "tlp": {
          "type": "integer",
          "title": "Traffic Light Protocol",
          "description": "Case traffic light protocol",
          "default": 2,
          "enum": [
            0,
            1,
            2,
            3
          ],
          "order": 8
        }
      },
      "required": [
        "description",
        "title"
      ]
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
