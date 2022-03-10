# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Create a MISP event"


class Input:
    ANALYSIS = "analysis"
    DISTRIBUTION = "distribution"
    INFO = "info"
    ORG_ID = "org_id"
    ORGC_ID = "orgc_id"
    PUBLISHED = "published"
    SHARING_GROUP_ID = "sharing_group_id"
    THREAT_LEVEL_ID = "threat_level_id"
    

class Output:
    ATTRIBUTE = "Attribute"
    RELATEDEVENT = "RelatedEvent"
    ANALYSIS = "analysis"
    ATTRIBUTE_COUNT = "attribute_count"
    DATE = "date"
    DISABLE_CORRELATION = "disable_correlation"
    DISTRIBUTION = "distribution"
    EVENT_CREATOR_EMAIL = "event_creator_email"
    ID = "id"
    INFO = "info"
    LOCKED = "locked"
    ORG_ID = "org_id"
    ORGC_ID = "orgc_id"
    PROPOSAL_EMAIL_LOCK = "proposal_email_lock"
    PUBLISH_TIMESTAMP = "publish_timestamp"
    PUBLISHED = "published"
    SHARING_GROUP_ID = "sharing_group_id"
    THREAT_LEVEL_ID = "threat_level_id"
    TIMESTAMP = "timestamp"
    UUID = "uuid"
    

class CreateAnEventInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "analysis": {
      "type": "string",
      "title": "Analysis",
      "description": "The analysis level of the event",
      "default": "0",
      "enum": [
        "2",
        "1",
        "0"
      ],
      "order": 3
    },
    "distribution": {
      "type": "string",
      "title": "Distribution",
      "description": "Distribution type",
      "default": "This Organization",
      "enum": [
        "This Community",
        "This Organization",
        "Connected Communities",
        "All Communities"
      ],
      "order": 1
    },
    "info": {
      "type": "string",
      "title": "Info",
      "description": "Extra event information",
      "order": 4
    },
    "org_id": {
      "type": "string",
      "title": "Organization ID",
      "description": "Organization ID",
      "order": 7
    },
    "orgc_id": {
      "type": "string",
      "title": "Organization C ID",
      "description": "Organization C ID",
      "order": 6
    },
    "published": {
      "type": "boolean",
      "title": "Published",
      "description": "Published event?",
      "default": true,
      "order": 5
    },
    "sharing_group_id": {
      "type": "string",
      "title": "Sharing Group ID",
      "description": "Sharing group ID",
      "order": 8
    },
    "threat_level_id": {
      "type": "string",
      "title": "Threat Level",
      "description": "Importance of the threat",
      "default": "1",
      "enum": [
        "4",
        "3",
        "2",
        "1"
      ],
      "order": 2
    }
  },
  "required": [
    "info",
    "published",
    "threat_level_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class CreateAnEventOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "Attribute": {
      "type": "array",
      "title": "Attribute",
      "description": "Attribute",
      "items": {
        "$ref": "#/definitions/base_output"
      },
      "order": 14
    },
    "RelatedEvent": {
      "type": "array",
      "title": "Related Event",
      "description": "Related event",
      "items": {
        "type": "object"
      },
      "order": 6
    },
    "analysis": {
      "type": "string",
      "title": "Analysis",
      "description": "Analysis",
      "order": 17
    },
    "attribute_count": {
      "type": "string",
      "title": "Attribute Count",
      "description": "Attribute count",
      "order": 15
    },
    "date": {
      "type": "string",
      "title": "Date",
      "displayType": "date",
      "description": "Date",
      "format": "date-time",
      "order": 9
    },
    "disable_correlation": {
      "type": "boolean",
      "title": "Disable Correlation",
      "description": "Disable correlation",
      "order": 10
    },
    "distribution": {
      "type": "string",
      "title": "Distribution",
      "description": "Distribution",
      "order": 19
    },
    "event_creator_email": {
      "type": "string",
      "title": "Email",
      "description": "Event creator's email",
      "order": 4
    },
    "id": {
      "type": "string",
      "title": "ID",
      "description": "Event ID",
      "order": 2
    },
    "info": {
      "type": "string",
      "title": "Info",
      "description": "Info",
      "order": 11
    },
    "locked": {
      "type": "boolean",
      "title": "Locked",
      "description": "Locked",
      "order": 12
    },
    "org_id": {
      "type": "string",
      "title": "Organization ID",
      "description": "Organization ID",
      "order": 16
    },
    "orgc_id": {
      "type": "string",
      "title": "Organization C ID",
      "description": "Organization C ID",
      "order": 1
    },
    "proposal_email_lock": {
      "type": "boolean",
      "title": "Proposal Email Lock",
      "description": "Lock proposal email",
      "order": 20
    },
    "publish_timestamp": {
      "type": "string",
      "title": "Publish Timestamp",
      "description": "Publish timestamp",
      "order": 13
    },
    "published": {
      "type": "boolean",
      "title": "Published",
      "description": "Published",
      "order": 18
    },
    "sharing_group_id": {
      "type": "string",
      "title": "Group ID",
      "description": "Sharing group ID",
      "order": 7
    },
    "threat_level_id": {
      "type": "string",
      "title": "Threat Level ID",
      "description": "Threat level ID",
      "order": 3
    },
    "timestamp": {
      "type": "string",
      "title": "Timestamp",
      "description": "Timestamp",
      "order": 8
    },
    "uuid": {
      "type": "string",
      "title": "UUID",
      "description": "Unique event ID",
      "order": 5
    }
  },
  "definitions": {
    "base_output": {
      "type": "object",
      "title": "base_output",
      "properties": {
        "category": {
          "type": "string",
          "title": "Category",
          "description": "Attribute category",
          "order": 1
        },
        "comment": {
          "type": "string",
          "title": "Comment",
          "description": "Attribute comment",
          "order": 2
        },
        "deleted": {
          "type": "boolean",
          "title": "Deleted",
          "description": "Deleted?",
          "order": 10
        },
        "email": {
          "type": "string",
          "title": "Email",
          "description": "Email address",
          "order": 9
        },
        "event_id": {
          "type": "string",
          "title": "Event ID",
          "description": "Event ID",
          "order": 5
        },
        "event_org_id": {
          "type": "string",
          "title": "Event Organization ID",
          "description": "Organization ID",
          "order": 6
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "Email ID",
          "order": 13
        },
        "old_id": {
          "type": "string",
          "title": "Old ID",
          "description": "Old ID",
          "order": 4
        },
        "timestamp": {
          "type": "string",
          "title": "Timestamp",
          "description": "Time created",
          "order": 11
        },
        "to_ids": {
          "type": "boolean",
          "title": "To IDs",
          "description": "To IDs",
          "order": 7
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Type of email",
          "order": 12
        },
        "uuid": {
          "type": "string",
          "title": "UUID",
          "description": "Unique ID",
          "order": 3
        },
        "value": {
          "type": "string",
          "title": "Value",
          "description": "Value",
          "order": 8
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
