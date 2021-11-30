# Description

This plugin utilizes Cisco Umbrella to get the most complete view of the relationships and evolution of Internet domains, IP addresses, and autonomous systems to pinpoint attackers infrastructures and predict future threats

# Key Features

Identify key features of plugin.

# Requirements

* Example: Requires an API Key from the product
* Example: API must be enabled on the Settings page in the product's user interface

# Supported Product Versions

_There are no supported product versions listed._

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api_key|credential_secret_key|None|True|Cisco Umbrella API key|None|9de5069c5afe602b2ea0a04b66beb2c0|
|api_secret|credential_secret_key|None|True|Cisco Umbrella API secret key|None|9de5069c5afe602b2ea0a04b66beb2c0|
|organization_id|string|None|True|ID of your Cisco Umbrella organization|None|2961483|

Example input:

```
```

## Technical Details

### Actions

#### Destination POST

This action is used to add list of destinations to destination list.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|destinationListId|integer|None|True|Unique ID for destination list|None|None|
|organizationId|integer|None|True|Organisation ID|None|None|
|payload|[]destinationsList|None|True|List of destinations|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|[]dResponse|True||

Example output:

```
```

#### Destination DELETE

This action is used to delete list of destinations from destination list.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|destinationListId|integer|None|True|Unique ID for destination list|None|None|
|organizationId|integer|None|True|Organisation ID|None|None|
|payload|[]destinationsIdsList|None|True|List of destinations|None|None|

Example input:

```
```

##### Output

_This action does not contain any outputs._

#### Destination GET

This action is used to get list of destinations related to destination list.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|destinationListId|integer|None|True|Unique ID for destination list|None|None|
|limit|integer|None|False|Limit for page|None|None|
|organizationId|integer|None|True|Organisation ID|None|None|
|page|integer|None|False|Pagination|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|[]destinationsEntity|True||

Example output:

```
```

#### Destination Lists POST

This action is used to create a destination list.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|organizationId|integer|None|True|Organisation ID|None|None|
|payload|[]dlCreate|None|True|List of destinations|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|[]dlEntity|True||

Example output:

```
```

#### Destination Lists DELETE

This action is used to delete a destination list.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|destinationListId|integer|None|True|Unique ID for destination list|None|None|
|organizationId|integer|None|True|Organisation ID|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|[]dlDelete|False||

Example output:

```
```

#### Destination List GET

This action is used to return a destination list.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|destinationListId|integer|None|True|Unique ID for destination list|None|None|
|organizationId|integer|None|True|Organisation ID|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|[]destinationList|True||

Example output:

```
```

#### Destinations List GET (All)

This action is used to retrieve all destination lists of organisation.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|organizationId|integer|None|True|Organisation ID|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|[]dlCollection|True||

Example output:

```
```

#### Destination Lists PATCH

This action is used to rename a destination list.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|destinationListId|integer|None|True|Unique ID for destination list|None|None|
|organizationId|integer|None|True|Organisation ID|None|None|
|payload|[]dlPatch|None|False|value containing name to change to|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|[]dlEntity|True||

Example output:

```
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

#### dResponse

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Access|string|False|Access can be allow or block. It defines destinationList type, e.g. allow|
|Created At|integer|False|example, 1490206249|
|ID|integer|False|Unique id of the destination list.|
|Is Global|boolean|False|isGlobal can be true or false. There is only one default destination list of type allow or block for an organization.|
|Is MSP Default|boolean|False|example, false|
|Marked For Deletion|boolean|False|example, false|
|Meta Data|[]meta|False|None|
|Modified At|integer|False|example, 1490206249|
|Name|string|False|Name of the DL list|
|Organization Id|integer|False|ID of org, e.g. 2345678|
|Third Party Category Id|integer|False|example, 0|

#### destinationList

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Access|string|False|Access can be allow or block. It defines destinationList type, e.g. allow|
|Created At|integer|False|example, 1490206249|
|ID|integer|False|Unique id of the destination list.|
|Is Global|boolean|False|isGlobal can be true or false. There is only one default destination list of type allow or block for an organization.|
|Is MSP Default|boolean|False|example, false|
|Marked For Deletion|boolean|False|example, false|
|Modified At|integer|False|example, 1490206249|
|Name|string|False|Name of the DL list|
|Organization Id|integer|False|ID of org, e.g. 2345678|
|Third Party Category Id|integer|False|example, 0|

#### destinations

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Comment|string|False|e.g. Added new destination list|
|Destination|string|True|Destination can be domain, url or ip | e.g. <domain_name>|
|Type|string|True|Type can be DOMAIN, URL, IPV4 | e.g. DOMAIN|

#### destinationsEntity

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Comment|string|False|None|
|CreatedAt|string|False|date and time it has been created at, e.g. example 2018-07-23 19:36:45|
|Destination|string|False|Destination can be domain, url, ip|
|Id|string|False|Unique ID of the destination|
|TypeOf|string|False|Type can be DOMAIN, URL, IPV4|

#### destinationsIdsList

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Destinations Ids List|integer|False|example, 1234|

#### destinationsList

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Comment|string|False|Comment for the destination|
|Destination|string|True|Name of the destination|

#### dlCollection

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Access|string|True|Access can be allow or block. It defines destinationList type, e.g. allow|
|Created At|integer|True|example, 1490206249|
|ID|integer|True|Unique id of the destination list.|
|Is Global|boolean|True|isGlobal can be true or false. There is only one default destination list of type allow or block for an organization.|
|Is MSP Default|boolean|True|example, false|
|Marked For Deletion|boolean|True|example, false|
|Meta Data|[]meta|False|None|
|Modified At|integer|True|example, 1490206249|
|Name|string|True|Name of the DL list|
|Organization Id|integer|True|ID of org, e.g. 2345678|
|Third Party Category Id|integer|True|example, 0|

#### dlCreate

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Access|string|True|Access can be allow or block. It defines destinationlist type.|
|Destinations|[]destinations|False|Destinations to add to new list|
|IsGlobal|boolean|True|isGlobal can be true or false. There is only one default destination list of type allow or block for an organization.|
|Name|string|True|example, New Destination List|

#### dlDelete

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Delete|string|False|Delete|

#### dlEntity

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Access|string|False|Access can be allow or block. It defines destinationList type, e.g. allow|
|Created At|integer|False|example, 1490206249|
|ID|integer|False|Unique id of the destination list.|
|Is Global|boolean|False|isGlobal can be true or false. There is only one default destination list of type allow or block for an organization.|
|Is MSP Default|boolean|False|example, false|
|Marked For Deletion|boolean|False|example, false|
|Meta Data|[]meta|False|None|
|Modified At|integer|False|example, 1490206249|
|Name|string|False|Name of the DL list|
|Organization Id|integer|False|ID of org, e.g. 2345678|
|Third Party Category Id|integer|False|example, 0|

#### dlPatch

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Name|string|True|Name of the destination list|

#### meta

|Name|Type|Required|Description|
|----|----|--------|-----------|
|DestinationCount|integer|False|Total number of destinations in a destination list.|
|DomainCount|integer|False|Total number of domains in a destination list. Domains are part of total destinations in a destination lists.|
|Ipv4Count|integer|False|Total number of Ip's in a destination list. Ip's are part of total destinations in a destination lists.|
|UrlCount|integer|False|Total number of Urls in a destination list. Urls are part of total destinations in a destination lists.|


## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.0 - Initial plugin

# Links

## References

* [Cisco Umbrella Destinations](LINK TO PRODUCT/VENDOR WEBSITE)

