# Nevermined Metadata API

The [Nevermined Metadata API](https://github.com/nevermined-io/metadata)
is an Open Source micro-service that allows to store Assets metadata in an
off-chain repository. It provides a plugins system allowing to persist the
Metadata in ElasticSearch. The Metadata API exposes the functionality
 for searching metadata using multiple filters and parameters.

The Metadata API is typically the backend used for Data Marketplaces or Data
Catalogs for storing all the Metadata of a specific domain related to a
Marketplace or Catalog .

Nevermined provides the package and automation of the micro-service allowing an
easy integration and deployment in cloud providers and Kubernetes clusters.


## Metadata API Reference

You can find a complete API reference documented in Swagger format in the
[docs folder](https://github.com/nevermined-io/metadata-api/tree/master/docs/) of the
metadata api repository.

### Queries

Because the Metadata API is using Elastic Search as repository of data, allows
to resolve complex searches a filters on top of the metadata information.

Some of these queries are pre-built into the metadata api, but also the micro-service
exposes via the `/api/v1/metadata/assets/ddo/query` endpoint the possibility of
sending bespoke Elastic Search queries to adapt to different metadata.

To call this endpoint the body should contain a elastic search query in the
query field, other fields can be also added to sort the results and use pagination,
a body example would be:

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

To use any other query, the DSL language from elastic search can be used.

Some more examples can be found in the [documentation](https://github.com/nevermined-io/metadata-api/blob/master/docs/querys.md)
of the Metadata API repository.
