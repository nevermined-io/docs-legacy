# Metadata API queys
Metadata API accepts native elastic search querys in the endpoint: 
`/api/v1/metadata/assets/ddo/query`

To call this endpoint the body should contain a elastic search query in the query field, other fields can be also added to sort the results and use pagination, a body example would be:

```json
{
  "offset": 100,
  "page": 1,
  "query": {
     "bool": { "must": [{ "match": { "service.attributes.additionalInformation.categories": "image"}}]}
  },
  "sort": {
    "value": 1
  }
}
```

To use any other query, the [DSL language](https://elasticsearch-dsl.readthedocs.io/en/latest/) from elastic searc can be used. 

## Examples
##### Filter by partial text in a specific field

```json
{
  "offset": 100,
  "page": 1,
  "query": {
      "bool": { "must": [{ "query_string": { "query": "*text*", "fields": ["service.attributes.main.name"] } }]}
  },
  "sort": {
    "value": 1
  }
}
```

## Examples
##### Multiple filters

```json
{
    "offset": 100,
    "page": 1,
    "query": {
        "bool": {
            "must": [
                {
                    "query_string": {
                        "query": "*uni*",
                        "fields": [
                            "service.attributes.main.name"
                        ]
                    }
                },
                {
                    "match": {
                        "service.attributes.additionalInformation.categories": "image"
                    }
                }
            ]
        }
    },
    "sort": {
        "value": 1
    }
}
```

##### Filter by date range
```json
{
    "offset": 100,
    "page": 1,
    "query": {
        "bool": {
            "must": [
                {
                    "range": {
                        "service.attributes.main.dateCreated": {
                            "time_zone": "+01:00",
                            "gte": "2021-01-21T20:03:12.963",
                            "lte": "2021-10-21T20:03:12.963"
                        }
                    }
                }
            ]
        }
    },
    "sort": {
        "value": 1
    }
}
```