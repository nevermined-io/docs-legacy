---
title: Marketplace API v0.1.0
language_tabs:
  - shell: Shell
  - http: HTTP
  - javascript: JavaScript
  - ruby: Ruby
  - python: Python
  - php: PHP
  - java: Java
  - go: Go
toc_footers: []
includes: []
search: true
highlight_theme: darkula
headingLevel: 2

---

<!-- Generator: Widdershins v4.0.1 -->

<h1 id="marketplace-api">Marketplace API v0.1.0</h1>

> Scroll down for code samples, example requests and responses. Select a language for code samples from the tabs above or the mobile navigation menu.

Base URLs:

<h1 id="marketplace-api-asset">Asset</h1>

## AssetController_createAsset

<a id="opIdAssetController_createAsset"></a>

> Code samples

```shell
# You can also use wget
curl -X POST /api/v1/metadata/assets/ddo \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
POST /api/v1/metadata/assets/ddo HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "@context": "https://w3id.org/did/v1",
  "id": "did:nv:0c184915b07b44c888d468be85a9b28253e80070e5294b1aaed81c2f0264e429",
  "created": "2019-02-08T08:13:49Z",
  "updated": "2019-02-08T08:13:49Z",
  "authentication": [
    {
      "publicKey": "did:nv:0c184915b07b44c888d468be85a9b28253e80070e5294b1aaed81c2f0264e430",
      "type": "RsaSignatureAuthentication2018"
    }
  ],
  "proof": {
    "created": "2022-01-08T16:02:20Z",
    "creator": "2022-01-08T16:02:20Z",
    "signatureValue": "0xbd7b46b3ac664167bc70ac211b1a1da0baed9ead91613a5f02dfc25c1bb6e3ff40861b455017e8a587fd4e37b703436072598c3a81ec88be28bfe33b61554a471b",
    "type": "DDOIntegritySignature"
  },
  "publicKey": [
    {
      "id": "did:nv:0c184915b07b44c888d468be85a9b28253e80070e5294b1aaed81c2f0264e430",
      "owner": "0x00Bd138aBD70e2F00903268F3Db08f2D25677C9e",
      "type": "EthereumECDSAKey"
    }
  ],
  "service": [
    {
      "index": 0,
      "service": "SecretStore",
      "serviceEndpoint": "http://localhost:12001",
      "type": "authorization"
    },
    {
      "index": 1,
      "purchaseEndpoint": "http://localhost:8030/api/v1/gateway/services/access/initialize",
      "serviceEndpoint": "http://localhost:8030/api/v1/gateway/services/consume",
      "type": "access"
    },
    {
      "attributes": {
        "additionalInformation": {
          "copyrightHolder": "Met Office",
          "description": "Weather information of UK including temperature and humidity",
          "inLanguage": "en",
          "links": [
            {
              "name": "Sample of Asset Data",
              "type": "sample",
              "url": "https://foo.com/sample.csv"
            }
          ],
          "tags": [
            "weather",
            "uk",
            "2011",
            "temperature",
            "humidity"
          ],
          "workExample": "stationId,latitude,longitude,datetime, temperature,humidity/n423432fsd,51.509865,-0.118092, 2011-01-01T10:55:11+00:00,7.2,68"
        },
        "curation": {
          "numVotes": 123,
          "rating": 0.93,
          "schema": "Binary Voting"
        },
        "main": {
          "author": "Met Office",
          "dateCreated": "2012-02-01T10:55:11Z",
          "encryptedFiles": "0x098213xzckasdf089723hjgdasfkjgasfv",
          "files": [
            {
              "compression": "zip",
              "contentLength": "4535431",
              "contentType": "text/csv",
              "encoding": "UTF-8",
              "index": 0,
              "resourceId": "access-log2018-02-13-15-17-29-18386C502CAEA932"
            }
          ],
          "license": "CC-BY",
          "name": "UK Weather information 2011",
          "price": "10",
          "type": "dataset"
        }
      },
      "index": 2,
      "serviceEndpoint": "http://mymetadata.org/api/v1/provider/assets/metadata/did:nv:0c184915b07b44c888d468be85a9b28253e80070e5294b1aaed81c2f0264e430",
      "type": "metadata"
    }
  ]
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/api/v1/metadata/assets/ddo',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.post '/api/v1/metadata/assets/ddo',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/api/v1/metadata/assets/ddo', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/api/v1/metadata/assets/ddo', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/v1/metadata/assets/ddo");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/api/v1/metadata/assets/ddo", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /api/v1/metadata/assets/ddo`

Create a asset entry

> Body parameter

```json
{
  "@context": "https://w3id.org/did/v1",
  "id": "did:nv:0c184915b07b44c888d468be85a9b28253e80070e5294b1aaed81c2f0264e429",
  "created": "2019-02-08T08:13:49Z",
  "updated": "2019-02-08T08:13:49Z",
  "authentication": [
    {
      "publicKey": "did:nv:0c184915b07b44c888d468be85a9b28253e80070e5294b1aaed81c2f0264e430",
      "type": "RsaSignatureAuthentication2018"
    }
  ],
  "proof": {
    "created": "2022-01-08T16:02:20Z",
    "creator": "2022-01-08T16:02:20Z",
    "signatureValue": "0xbd7b46b3ac664167bc70ac211b1a1da0baed9ead91613a5f02dfc25c1bb6e3ff40861b455017e8a587fd4e37b703436072598c3a81ec88be28bfe33b61554a471b",
    "type": "DDOIntegritySignature"
  },
  "publicKey": [
    {
      "id": "did:nv:0c184915b07b44c888d468be85a9b28253e80070e5294b1aaed81c2f0264e430",
      "owner": "0x00Bd138aBD70e2F00903268F3Db08f2D25677C9e",
      "type": "EthereumECDSAKey"
    }
  ],
  "service": [
    {
      "index": 0,
      "service": "SecretStore",
      "serviceEndpoint": "http://localhost:12001",
      "type": "authorization"
    },
    {
      "index": 1,
      "purchaseEndpoint": "http://localhost:8030/api/v1/gateway/services/access/initialize",
      "serviceEndpoint": "http://localhost:8030/api/v1/gateway/services/consume",
      "type": "access"
    },
    {
      "attributes": {
        "additionalInformation": {
          "copyrightHolder": "Met Office",
          "description": "Weather information of UK including temperature and humidity",
          "inLanguage": "en",
          "links": [
            {
              "name": "Sample of Asset Data",
              "type": "sample",
              "url": "https://foo.com/sample.csv"
            }
          ],
          "tags": [
            "weather",
            "uk",
            "2011",
            "temperature",
            "humidity"
          ],
          "workExample": "stationId,latitude,longitude,datetime, temperature,humidity/n423432fsd,51.509865,-0.118092, 2011-01-01T10:55:11+00:00,7.2,68"
        },
        "curation": {
          "numVotes": 123,
          "rating": 0.93,
          "schema": "Binary Voting"
        },
        "main": {
          "author": "Met Office",
          "dateCreated": "2012-02-01T10:55:11Z",
          "encryptedFiles": "0x098213xzckasdf089723hjgdasfkjgasfv",
          "files": [
            {
              "compression": "zip",
              "contentLength": "4535431",
              "contentType": "text/csv",
              "encoding": "UTF-8",
              "index": 0,
              "resourceId": "access-log2018-02-13-15-17-29-18386C502CAEA932"
            }
          ],
          "license": "CC-BY",
          "name": "UK Weather information 2011",
          "price": "10",
          "type": "dataset"
        }
      },
      "index": 2,
      "serviceEndpoint": "http://mymetadata.org/api/v1/provider/assets/metadata/did:nv:0c184915b07b44c888d468be85a9b28253e80070e5294b1aaed81c2f0264e430",
      "type": "metadata"
    }
  ]
}
```

<h3 id="assetcontroller_createasset-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[CreateAssetDto](#schemacreateassetdto)|true|none|

> Example responses

> 201 Response

```json
{
  "@context": "https://w3id.org/did/v1",
  "authentication": [
    {
      "publicKey": "did:nv:0c184915b07b44c888d468be85a9b28253e80070e5294b1aaed81c2f0264e430",
      "type": "RsaSignatureAuthentication2018"
    }
  ],
  "created": "2021-02-01T10:55:11Z",
  "updated": "2021-02-01T10:55:11Z",
  "id": "did:nv:0c184915b07b44c888d468be85a9b28253e80070e5294b1aaed81c2f0264e429",
  "proof": {
    "created": "2022-01-08T16:02:20Z",
    "creator": "2022-01-08T16:02:20Z",
    "signatureValue": "0xbd7b46b3ac664167bc70ac211b1a1da0baed9ead91613a5f02dfc25c1bb6e3ff40861b455017e8a587fd4e37b703436072598c3a81ec88be28bfe33b61554a471b",
    "type": "DDOIntegritySignature"
  },
  "publicKey": [
    {
      "id": "did:nv:0c184915b07b44c888d468be85a9b28253e80070e5294b1aaed81c2f0264e430",
      "owner": "0x00Bd138aBD70e2F00903268F3Db08f2D25677C9e",
      "type": "EthereumECDSAKey"
    }
  ],
  "service": [
    {
      "index": 0,
      "service": "SecretStore",
      "serviceEndpoint": "http://localhost:12001",
      "type": "authorization"
    },
    {
      "index": 1,
      "purchaseEndpoint": "http://localhost:8030/api/v1/gateway/services/access/initialize",
      "serviceEndpoint": "http://localhost:8030/api/v1/gateway/services/consume",
      "type": "access"
    },
    {
      "attributes": {
        "additionalInformation": {
          "copyrightHolder": "Met Office",
          "description": "Weather information of UK including temperature and humidity",
          "inLanguage": "en",
          "links": [
            {
              "name": "Sample of Asset Data",
              "type": "sample",
              "url": "https://foo.com/sample.csv"
            }
          ],
          "tags": [
            "weather",
            "uk",
            "2011",
            "temperature",
            "humidity"
          ],
          "workExample": "stationId,latitude,longitude,datetime, temperature,humidity/n423432fsd,51.509865,-0.118092, 2011-01-01T10:55:11+00:00,7.2,68"
        },
        "curation": {
          "numVotes": 123,
          "rating": 0.93,
          "schema": "Binary Voting"
        },
        "main": {
          "author": "Met Office",
          "dateCreated": "2012-02-01T10:55:11Z",
          "encryptedFiles": "0x098213xzckasdf089723hjgdasfkjgasfv",
          "files": [
            {
              "compression": "zip",
              "contentLength": "4535431",
              "contentType": "text/csv",
              "encoding": "UTF-8",
              "index": 0,
              "resourceId": "access-log2018-02-13-15-17-29-18386C502CAEA932"
            }
          ],
          "license": "CC-BY",
          "name": "UK Weather information 2011",
          "price": "10",
          "type": "dataset"
        }
      },
      "index": 2,
      "serviceEndpoint": "http://mymetadata.org/api/v1/provider/assets/metadata/did:nv:0c184915b07b44c888d468be85a9b28253e80070e5294b1aaed81c2f0264e430",
      "type": "metadata"
    }
  ]
}
```

<h3 id="assetcontroller_createasset-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|asset is created|[GetAssetDto](#schemagetassetdto)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Bad Request|None|

<aside class="success">
This operation does not require authentication
</aside>

## AssetController_getDDOAllAssets

<a id="opIdAssetController_getDDOAllAssets"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /api/v1/metadata/assets/ddo \
  -H 'Accept: application/json'

```

```http
GET /api/v1/metadata/assets/ddo HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/api/v1/metadata/assets/ddo',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/api/v1/metadata/assets/ddo',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/api/v1/metadata/assets/ddo', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/v1/metadata/assets/ddo', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/v1/metadata/assets/ddo");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/v1/metadata/assets/ddo", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /api/v1/metadata/assets/ddo`

Get DDO of all assets

<h3 id="assetcontroller_getddoallassets-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|query|query|string|false|execute directly queries to elasticsearch from the client|
|text|query|string|false|Text to search|
|offset|query|string|false|Page Size|
|page|query|string|false|Page to retrieve|
|sort|query|string|false|sort the response by specified parameter|

> Example responses

> 200 Response

```json
[
  {
    "@context": "https://w3id.org/did/v1",
    "authentication": [
      {
        "publicKey": "did:nv:0c184915b07b44c888d468be85a9b28253e80070e5294b1aaed81c2f0264e430",
        "type": "RsaSignatureAuthentication2018"
      }
    ],
    "created": "2021-02-01T10:55:11Z",
    "updated": "2021-02-01T10:55:11Z",
    "id": "did:nv:0c184915b07b44c888d468be85a9b28253e80070e5294b1aaed81c2f0264e429",
    "proof": {
      "created": "2022-01-08T16:02:20Z",
      "creator": "2022-01-08T16:02:20Z",
      "signatureValue": "0xbd7b46b3ac664167bc70ac211b1a1da0baed9ead91613a5f02dfc25c1bb6e3ff40861b455017e8a587fd4e37b703436072598c3a81ec88be28bfe33b61554a471b",
      "type": "DDOIntegritySignature"
    },
    "publicKey": [
      {
        "id": "did:nv:0c184915b07b44c888d468be85a9b28253e80070e5294b1aaed81c2f0264e430",
        "owner": "0x00Bd138aBD70e2F00903268F3Db08f2D25677C9e",
        "type": "EthereumECDSAKey"
      }
    ],
    "service": [
      {
        "index": 0,
        "service": "SecretStore",
        "serviceEndpoint": "http://localhost:12001",
        "type": "authorization"
      },
      {
        "index": 1,
        "purchaseEndpoint": "http://localhost:8030/api/v1/gateway/services/access/initialize",
        "serviceEndpoint": "http://localhost:8030/api/v1/gateway/services/consume",
        "type": "access"
      },
      {
        "attributes": {
          "additionalInformation": {
            "copyrightHolder": "Met Office",
            "description": "Weather information of UK including temperature and humidity",
            "inLanguage": "en",
            "links": [
              {
                "name": "Sample of Asset Data",
                "type": "sample",
                "url": "https://foo.com/sample.csv"
              }
            ],
            "tags": [
              "weather",
              "uk",
              "2011",
              "temperature",
              "humidity"
            ],
            "workExample": "stationId,latitude,longitude,datetime, temperature,humidity/n423432fsd,51.509865,-0.118092, 2011-01-01T10:55:11+00:00,7.2,68"
          },
          "curation": {
            "numVotes": 123,
            "rating": 0.93,
            "schema": "Binary Voting"
          },
          "main": {
            "author": "Met Office",
            "dateCreated": "2012-02-01T10:55:11Z",
            "encryptedFiles": "0x098213xzckasdf089723hjgdasfkjgasfv",
            "files": [
              {
                "compression": "zip",
                "contentLength": "4535431",
                "contentType": "text/csv",
                "encoding": "UTF-8",
                "index": 0,
                "resourceId": "access-log2018-02-13-15-17-29-18386C502CAEA932"
              }
            ],
            "license": "CC-BY",
            "name": "UK Weather information 2011",
            "price": "10",
            "type": "dataset"
          }
        },
        "index": 2,
        "serviceEndpoint": "http://mymetadata.org/api/v1/provider/assets/metadata/did:nv:0c184915b07b44c888d468be85a9b28253e80070e5294b1aaed81c2f0264e430",
        "type": "metadata"
      }
    ]
  }
]
```

<h3 id="assetcontroller_getddoallassets-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Assets Ids|Inline|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Bad Request|None|

<h3 id="assetcontroller_getddoallassets-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[GetAssetDto](#schemagetassetdto)]|false|none|none|
|» @context|string|true|none|Context of the asset|
|» authentication|[[AuthenticationDto](#schemaauthenticationdto)]|true|none|Authentication used in the asset|
|»» publicKey|string|true|none|Public key of ddo|
|»» type|string|true|none|Type of the signature|
|» created|string|true|none|Date when the asset is created|
|» updated|string|true|none|Date when the asset is created|
|» id|string|true|none|ID of the asset|
|» proof|[ProofDto](#schemaproofdto)|true|none|Proof data|
|»» created|string|true|none|Date of the proof|
|»» creator|string|true|none|Wallet address who created the proof signature|
|»» signatureValue|string|true|none|Value of the signature|
|»» type|string|true|none|Type of the proof|
|» publicKey|[[PublicKeyDto](#schemapublickeydto)]|true|none|Public keys that contains the asset|
|»» id|string|true|none|Id of the public key|
|»» owner|string|true|none|Wallet address who own the public key|
|»» type|string|true|none|Type of the public key|
|» service|[[ServiceDto](#schemaservicedto)]|true|none|Services that contains the asset|
|»» index|number|true|none|index of the service|
|»» serviceEndpoint|string|true|none|Url of the service endpoint|
|»» type|string|true|none|Service type|
|»» service|string|false|none|Service name|
|»» purchaseEndpoint|string|false|none|Url to purchase asset|
|»» attributes|[AttributesDto](#schemaattributesdto)|false|none|Attribute of the metadata|
|»»» additionalInformation|object|false|none|Aditional information of the asset|
|»»» curation|[CurationDto](#schemacurationdto)|true|none|popularity of the asset|
|»»»» numVotes|number|true|none|Number of votes. 0 is the default value|
|»»»» rating|number|true|none|Decimal value between 0 and 1. 0 is the default value|
|»»»» schema|string|false|none|Schema applied to calculate the rating|
|»»»» isListed|boolean|false|none|Flag unsuitable content. False by default. If it's true, the content must not be returned|
|»»» main|[MainDto](#schemamaindto)|true|none|Main data of the asset|
|»»»» author|string|true|none|Name of the entity generating this data (e.g. Tfl, Disney Corp, etc.)|
|»»»» dateCreated|string|true|none|The date on which the asset was created by the originator.ISO 8601 format, Coordinated Universal Time, e.g. 2019-01-31T08:38:32Z|
|»»»» datePublished|string|false|none|The date on which the asset DDO is registered into the metadata store|
|»»»» encryptedFiles|string|true|none|files encrytion signature|
|»»»» files|[[FileDto](#schemafiledto)]|true|none|Array of File objects including the encrypted file urls. Further metadata about each file is stored|
|»»»»» checksum|string|false|none|Checksum of the file using your preferred format (i.e. MD5). Format specified in checksumType.If it's not provided can't be validated if the file was not modified after registering|
|»»»»» url|string|false|none|Content URL. Omitted from the remote metadata. Supports http(s):// and ipfs:// URLs|
|»»»»» checksumType|string|false|none|Format of the provided checksum. Can vary according to server (i.e Amazon vs. Azure)|
|»»»»» name|string|false|none|File name|
|»»»»» compression|string|false|none|File compression (e.g. no, gzip, bzip2, etc)|
|»»»»» contentLength|string|false|none|Size of the file in bytes|
|»»»»» contentType|string|true|none|File format|
|»»»»» encoding|string|false|none|File encoding (e.g. UTF-8)|
|»»»»» index|number|true|none|Index of the file|
|»»»»» resourceId|string|false|none|Remote identifier of the file in the external provider. It is typically the remote id in the cloud provider|
|»»»»» encrypted|boolean|false|none|Boolean. Is the file encrypted? If is not set is assumed the file is not encrypted|
|»»»»» encryptionMode|string|false|none|Encryption mode used. Just valid if encrypted=true|
|»»»» license|number|true|none|Short name referencing the license of the asset (e.g. Public Domain, CC-0, CC-BY, No License Specified, etc.). If it's not specified, the following value will be added: "No License Specified|
|»»»» name|string|true|none|Descriptive name or title of the asset|
|»»»» price|string|true|none|Price of the asset. It must be an integer encoded as a string, e.g. "123000000000000000000"|
|»»»» type|string|true|none|Type of the asset. Helps to filter by the type of asset. It could be for example ("dataset", "algorithm")|
|»»»» algorithm|[AlgorithmDto](#schemaalgorithmdto)|true|none|Algorithm used in the asset|
|»»»»» language|string|false|none|Language used to implement the software|
|»»»»» format|string|false|none|Packaging format of the software|
|»»»»» version|string|false|none|Version of the software|
|»»»»» container|[[ContainerDto](#schemacontainerdto)]|true|none|Object describing the Docker container image|
|»»»»»» entrypoint|string|false|none|The command to execute, or script to run inside the Docker image|
|»»»»»» image|string|false|none|Name of the Docker image|
|»»»»»» tag|string|false|none|Tag of the Docker image|
|»»» serviceAgreementTemplate|[ServiceAgreementTemplateDto](#schemaserviceagreementtemplatedto)|false|none|Service agreement template|
|»»»» conditionDependency|[[ConditionDependencyDto](#schemaconditiondependencydto)]|true|none|none|
|»»»»» access|[string]|true|none|Access|
|»»»»» escrowPayment|[string]|true|none|Escrow Payment|
|»»»»» execCompute|[string]|true|none|Exec Compute|
|»»»»» lockPayment|[string]|true|none|Lock Payment|
|»»»» conditions|[[ConditionDto](#schemaconditiondto)]|true|none|Conditions|
|»»»»» contractName|string|true|none|Contract name|
|»»»»» functionName|string|true|none|Function name|
|»»»»» name|string|true|none|Function name|
|»»»»» events|[[EventDto](#schemaeventdto)]|true|none|Events|
|»»»»»» actionType|string|true|none|Action Type|
|»»»»»» handler|[HandlerDto](#schemahandlerdto)|true|none|Handler event|
|»»»»»»» functionName|string|true|none|Function name|
|»»»»»»» moduleName|string|true|none|Module name|
|»»»»»»» version|string|true|none|Version of the handler|
|»»»»»» name|string|true|none|Name of the event|
|»»»»» parameters|[[ParameterDto](#schemaparameterdto)]|true|none|Parameters|
|»»»»»» name|string|true|none|Parameter name|
|»»»»»» type|string|true|none|Parameter type|
|»»»»»» value|object|true|none|Parameter value|
|»»»»» timelock|number|true|none|Time lock|
|»»»»» timeout|number|true|none|Time out|
|»»»» contractName|number|true|none|Contract Name|
|»»»» events|[[EventDto](#schemaeventdto)]|true|none|Events|
|»»»» fulfillmentOrder|string|false|none|Fulfillment order|

<aside class="success">
This operation does not require authentication
</aside>

## AssetController_deleteAllDDOs

<a id="opIdAssetController_deleteAllDDOs"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE /api/v1/metadata/assets/ddo

```

```http
DELETE /api/v1/metadata/assets/ddo HTTP/1.1

```

```javascript

fetch('/api/v1/metadata/assets/ddo',
{
  method: 'DELETE'

})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

result = RestClient.delete '/api/v1/metadata/assets/ddo',
  params: {
  }

p JSON.parse(result)

```

```python
import requests

r = requests.delete('/api/v1/metadata/assets/ddo')

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('DELETE','/api/v1/metadata/assets/ddo', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/v1/metadata/assets/ddo");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "/api/v1/metadata/assets/ddo", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`DELETE /api/v1/metadata/assets/ddo`

Retire metadata of all assets

<h3 id="assetcontroller_deleteallddos-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Deleted all DDOs from marketplace|None|

<aside class="success">
This operation does not require authentication
</aside>

## AssetController_getAllAssetIds

<a id="opIdAssetController_getAllAssetIds"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /api/v1/metadata/assets \
  -H 'Accept: application/json'

```

```http
GET /api/v1/metadata/assets HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/api/v1/metadata/assets',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/api/v1/metadata/assets',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/api/v1/metadata/assets', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/v1/metadata/assets', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/v1/metadata/assets");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/v1/metadata/assets", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /api/v1/metadata/assets`

Get all asset Ids

<h3 id="assetcontroller_getallassetids-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|query|query|string|false|execute directly queries to elasticsearch from the client|
|text|query|string|false|Text to search|
|offset|query|string|false|Page Size|
|page|query|string|false|Page to retrieve|
|sort|query|string|false|sort the response by specified parameter|

> Example responses

> 200 Response

```json
[
  "did:nv:0c184915b07b44c888d468be85a9b28253e80070e5294b1aaed81c2f0264e430"
]
```

<h3 id="assetcontroller_getallassetids-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Assets Ids|Inline|

<h3 id="assetcontroller_getallassetids-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## AssetController_listDDObyQuery

<a id="opIdAssetController_listDDObyQuery"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /api/v1/metadata/assets/ddo/query \
  -H 'Accept: application/json'

```

```http
GET /api/v1/metadata/assets/ddo/query HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/api/v1/metadata/assets/ddo/query',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/api/v1/metadata/assets/ddo/query',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/api/v1/metadata/assets/ddo/query', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/v1/metadata/assets/ddo/query', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/v1/metadata/assets/ddo/query");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/v1/metadata/assets/ddo/query", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /api/v1/metadata/assets/ddo/query`

Get a list of DDOs that match with the given text

<h3 id="assetcontroller_listddobyquery-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|query|query|string|false|execute directly queries to elasticsearch from the client|
|text|query|string|false|Text to search|
|offset|query|string|false|Page Size|
|page|query|string|false|Page to retrieve|
|sort|query|string|false|sort the response by specified parameter|

> Example responses

> 200 Response

```json
[
  {
    "@context": "https://w3id.org/did/v1",
    "authentication": [
      {
        "publicKey": "did:nv:0c184915b07b44c888d468be85a9b28253e80070e5294b1aaed81c2f0264e430",
        "type": "RsaSignatureAuthentication2018"
      }
    ],
    "created": "2021-02-01T10:55:11Z",
    "updated": "2021-02-01T10:55:11Z",
    "id": "did:nv:0c184915b07b44c888d468be85a9b28253e80070e5294b1aaed81c2f0264e429",
    "proof": {
      "created": "2022-01-08T16:02:20Z",
      "creator": "2022-01-08T16:02:20Z",
      "signatureValue": "0xbd7b46b3ac664167bc70ac211b1a1da0baed9ead91613a5f02dfc25c1bb6e3ff40861b455017e8a587fd4e37b703436072598c3a81ec88be28bfe33b61554a471b",
      "type": "DDOIntegritySignature"
    },
    "publicKey": [
      {
        "id": "did:nv:0c184915b07b44c888d468be85a9b28253e80070e5294b1aaed81c2f0264e430",
        "owner": "0x00Bd138aBD70e2F00903268F3Db08f2D25677C9e",
        "type": "EthereumECDSAKey"
      }
    ],
    "service": [
      {
        "index": 0,
        "service": "SecretStore",
        "serviceEndpoint": "http://localhost:12001",
        "type": "authorization"
      },
      {
        "index": 1,
        "purchaseEndpoint": "http://localhost:8030/api/v1/gateway/services/access/initialize",
        "serviceEndpoint": "http://localhost:8030/api/v1/gateway/services/consume",
        "type": "access"
      },
      {
        "attributes": {
          "additionalInformation": {
            "copyrightHolder": "Met Office",
            "description": "Weather information of UK including temperature and humidity",
            "inLanguage": "en",
            "links": [
              {
                "name": "Sample of Asset Data",
                "type": "sample",
                "url": "https://foo.com/sample.csv"
              }
            ],
            "tags": [
              "weather",
              "uk",
              "2011",
              "temperature",
              "humidity"
            ],
            "workExample": "stationId,latitude,longitude,datetime, temperature,humidity/n423432fsd,51.509865,-0.118092, 2011-01-01T10:55:11+00:00,7.2,68"
          },
          "curation": {
            "numVotes": 123,
            "rating": 0.93,
            "schema": "Binary Voting"
          },
          "main": {
            "author": "Met Office",
            "dateCreated": "2012-02-01T10:55:11Z",
            "encryptedFiles": "0x098213xzckasdf089723hjgdasfkjgasfv",
            "files": [
              {
                "compression": "zip",
                "contentLength": "4535431",
                "contentType": "text/csv",
                "encoding": "UTF-8",
                "index": 0,
                "resourceId": "access-log2018-02-13-15-17-29-18386C502CAEA932"
              }
            ],
            "license": "CC-BY",
            "name": "UK Weather information 2011",
            "price": "10",
            "type": "dataset"
          }
        },
        "index": 2,
        "serviceEndpoint": "http://mymetadata.org/api/v1/provider/assets/metadata/did:nv:0c184915b07b44c888d468be85a9b28253e80070e5294b1aaed81c2f0264e430",
        "type": "metadata"
      }
    ]
  }
]
```

<h3 id="assetcontroller_listddobyquery-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|list of DDOs|Inline|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Bad Request|None|

<h3 id="assetcontroller_listddobyquery-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[GetAssetDto](#schemagetassetdto)]|false|none|none|
|» @context|string|true|none|Context of the asset|
|» authentication|[[AuthenticationDto](#schemaauthenticationdto)]|true|none|Authentication used in the asset|
|»» publicKey|string|true|none|Public key of ddo|
|»» type|string|true|none|Type of the signature|
|» created|string|true|none|Date when the asset is created|
|» updated|string|true|none|Date when the asset is created|
|» id|string|true|none|ID of the asset|
|» proof|[ProofDto](#schemaproofdto)|true|none|Proof data|
|»» created|string|true|none|Date of the proof|
|»» creator|string|true|none|Wallet address who created the proof signature|
|»» signatureValue|string|true|none|Value of the signature|
|»» type|string|true|none|Type of the proof|
|» publicKey|[[PublicKeyDto](#schemapublickeydto)]|true|none|Public keys that contains the asset|
|»» id|string|true|none|Id of the public key|
|»» owner|string|true|none|Wallet address who own the public key|
|»» type|string|true|none|Type of the public key|
|» service|[[ServiceDto](#schemaservicedto)]|true|none|Services that contains the asset|
|»» index|number|true|none|index of the service|
|»» serviceEndpoint|string|true|none|Url of the service endpoint|
|»» type|string|true|none|Service type|
|»» service|string|false|none|Service name|
|»» purchaseEndpoint|string|false|none|Url to purchase asset|
|»» attributes|[AttributesDto](#schemaattributesdto)|false|none|Attribute of the metadata|
|»»» additionalInformation|object|false|none|Aditional information of the asset|
|»»» curation|[CurationDto](#schemacurationdto)|true|none|popularity of the asset|
|»»»» numVotes|number|true|none|Number of votes. 0 is the default value|
|»»»» rating|number|true|none|Decimal value between 0 and 1. 0 is the default value|
|»»»» schema|string|false|none|Schema applied to calculate the rating|
|»»»» isListed|boolean|false|none|Flag unsuitable content. False by default. If it's true, the content must not be returned|
|»»» main|[MainDto](#schemamaindto)|true|none|Main data of the asset|
|»»»» author|string|true|none|Name of the entity generating this data (e.g. Tfl, Disney Corp, etc.)|
|»»»» dateCreated|string|true|none|The date on which the asset was created by the originator.ISO 8601 format, Coordinated Universal Time, e.g. 2019-01-31T08:38:32Z|
|»»»» datePublished|string|false|none|The date on which the asset DDO is registered into the metadata store|
|»»»» encryptedFiles|string|true|none|files encrytion signature|
|»»»» files|[[FileDto](#schemafiledto)]|true|none|Array of File objects including the encrypted file urls. Further metadata about each file is stored|
|»»»»» checksum|string|false|none|Checksum of the file using your preferred format (i.e. MD5). Format specified in checksumType.If it's not provided can't be validated if the file was not modified after registering|
|»»»»» url|string|false|none|Content URL. Omitted from the remote metadata. Supports http(s):// and ipfs:// URLs|
|»»»»» checksumType|string|false|none|Format of the provided checksum. Can vary according to server (i.e Amazon vs. Azure)|
|»»»»» name|string|false|none|File name|
|»»»»» compression|string|false|none|File compression (e.g. no, gzip, bzip2, etc)|
|»»»»» contentLength|string|false|none|Size of the file in bytes|
|»»»»» contentType|string|true|none|File format|
|»»»»» encoding|string|false|none|File encoding (e.g. UTF-8)|
|»»»»» index|number|true|none|Index of the file|
|»»»»» resourceId|string|false|none|Remote identifier of the file in the external provider. It is typically the remote id in the cloud provider|
|»»»»» encrypted|boolean|false|none|Boolean. Is the file encrypted? If is not set is assumed the file is not encrypted|
|»»»»» encryptionMode|string|false|none|Encryption mode used. Just valid if encrypted=true|
|»»»» license|number|true|none|Short name referencing the license of the asset (e.g. Public Domain, CC-0, CC-BY, No License Specified, etc.). If it's not specified, the following value will be added: "No License Specified|
|»»»» name|string|true|none|Descriptive name or title of the asset|
|»»»» price|string|true|none|Price of the asset. It must be an integer encoded as a string, e.g. "123000000000000000000"|
|»»»» type|string|true|none|Type of the asset. Helps to filter by the type of asset. It could be for example ("dataset", "algorithm")|
|»»»» algorithm|[AlgorithmDto](#schemaalgorithmdto)|true|none|Algorithm used in the asset|
|»»»»» language|string|false|none|Language used to implement the software|
|»»»»» format|string|false|none|Packaging format of the software|
|»»»»» version|string|false|none|Version of the software|
|»»»»» container|[[ContainerDto](#schemacontainerdto)]|true|none|Object describing the Docker container image|
|»»»»»» entrypoint|string|false|none|The command to execute, or script to run inside the Docker image|
|»»»»»» image|string|false|none|Name of the Docker image|
|»»»»»» tag|string|false|none|Tag of the Docker image|
|»»» serviceAgreementTemplate|[ServiceAgreementTemplateDto](#schemaserviceagreementtemplatedto)|false|none|Service agreement template|
|»»»» conditionDependency|[[ConditionDependencyDto](#schemaconditiondependencydto)]|true|none|none|
|»»»»» access|[string]|true|none|Access|
|»»»»» escrowPayment|[string]|true|none|Escrow Payment|
|»»»»» execCompute|[string]|true|none|Exec Compute|
|»»»»» lockPayment|[string]|true|none|Lock Payment|
|»»»» conditions|[[ConditionDto](#schemaconditiondto)]|true|none|Conditions|
|»»»»» contractName|string|true|none|Contract name|
|»»»»» functionName|string|true|none|Function name|
|»»»»» name|string|true|none|Function name|
|»»»»» events|[[EventDto](#schemaeventdto)]|true|none|Events|
|»»»»»» actionType|string|true|none|Action Type|
|»»»»»» handler|[HandlerDto](#schemahandlerdto)|true|none|Handler event|
|»»»»»»» functionName|string|true|none|Function name|
|»»»»»»» moduleName|string|true|none|Module name|
|»»»»»»» version|string|true|none|Version of the handler|
|»»»»»» name|string|true|none|Name of the event|
|»»»»» parameters|[[ParameterDto](#schemaparameterdto)]|true|none|Parameters|
|»»»»»» name|string|true|none|Parameter name|
|»»»»»» type|string|true|none|Parameter type|
|»»»»»» value|object|true|none|Parameter value|
|»»»»» timelock|number|true|none|Time lock|
|»»»»» timeout|number|true|none|Time out|
|»»»» contractName|number|true|none|Contract Name|
|»»»» events|[[EventDto](#schemaeventdto)]|true|none|Events|
|»»»» fulfillmentOrder|string|false|none|Fulfillment order|

<aside class="success">
This operation does not require authentication
</aside>

## AssetController_listDDObyQueryPost

<a id="opIdAssetController_listDDObyQueryPost"></a>

> Code samples

```shell
# You can also use wget
curl -X POST /api/v1/metadata/assets/ddo/query \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
POST /api/v1/metadata/assets/ddo/query HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "query": {
    "match_all": {}
  },
  "text": "Eius vel alias.",
  "offset": 100,
  "page": 0,
  "sort": {
    "created": "asc"
  }
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/api/v1/metadata/assets/ddo/query',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.post '/api/v1/metadata/assets/ddo/query',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/api/v1/metadata/assets/ddo/query', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/api/v1/metadata/assets/ddo/query', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/v1/metadata/assets/ddo/query");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/api/v1/metadata/assets/ddo/query", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /api/v1/metadata/assets/ddo/query`

Get a list of DDOs that match with the executed query.

> Body parameter

```json
{
  "query": {
    "match_all": {}
  },
  "text": "Eius vel alias.",
  "offset": 100,
  "page": 0,
  "sort": {
    "created": "asc"
  }
}
```

<h3 id="assetcontroller_listddobyquerypost-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[QueryBodyDDOdto](#schemaquerybodyddodto)|true|none|

> Example responses

> 200 Response

```json
[
  {
    "@context": "https://w3id.org/did/v1",
    "authentication": [
      {
        "publicKey": "did:nv:0c184915b07b44c888d468be85a9b28253e80070e5294b1aaed81c2f0264e430",
        "type": "RsaSignatureAuthentication2018"
      }
    ],
    "created": "2021-02-01T10:55:11Z",
    "updated": "2021-02-01T10:55:11Z",
    "id": "did:nv:0c184915b07b44c888d468be85a9b28253e80070e5294b1aaed81c2f0264e429",
    "proof": {
      "created": "2022-01-08T16:02:20Z",
      "creator": "2022-01-08T16:02:20Z",
      "signatureValue": "0xbd7b46b3ac664167bc70ac211b1a1da0baed9ead91613a5f02dfc25c1bb6e3ff40861b455017e8a587fd4e37b703436072598c3a81ec88be28bfe33b61554a471b",
      "type": "DDOIntegritySignature"
    },
    "publicKey": [
      {
        "id": "did:nv:0c184915b07b44c888d468be85a9b28253e80070e5294b1aaed81c2f0264e430",
        "owner": "0x00Bd138aBD70e2F00903268F3Db08f2D25677C9e",
        "type": "EthereumECDSAKey"
      }
    ],
    "service": [
      {
        "index": 0,
        "service": "SecretStore",
        "serviceEndpoint": "http://localhost:12001",
        "type": "authorization"
      },
      {
        "index": 1,
        "purchaseEndpoint": "http://localhost:8030/api/v1/gateway/services/access/initialize",
        "serviceEndpoint": "http://localhost:8030/api/v1/gateway/services/consume",
        "type": "access"
      },
      {
        "attributes": {
          "additionalInformation": {
            "copyrightHolder": "Met Office",
            "description": "Weather information of UK including temperature and humidity",
            "inLanguage": "en",
            "links": [
              {
                "name": "Sample of Asset Data",
                "type": "sample",
                "url": "https://foo.com/sample.csv"
              }
            ],
            "tags": [
              "weather",
              "uk",
              "2011",
              "temperature",
              "humidity"
            ],
            "workExample": "stationId,latitude,longitude,datetime, temperature,humidity/n423432fsd,51.509865,-0.118092, 2011-01-01T10:55:11+00:00,7.2,68"
          },
          "curation": {
            "numVotes": 123,
            "rating": 0.93,
            "schema": "Binary Voting"
          },
          "main": {
            "author": "Met Office",
            "dateCreated": "2012-02-01T10:55:11Z",
            "encryptedFiles": "0x098213xzckasdf089723hjgdasfkjgasfv",
            "files": [
              {
                "compression": "zip",
                "contentLength": "4535431",
                "contentType": "text/csv",
                "encoding": "UTF-8",
                "index": 0,
                "resourceId": "access-log2018-02-13-15-17-29-18386C502CAEA932"
              }
            ],
            "license": "CC-BY",
            "name": "UK Weather information 2011",
            "price": "10",
            "type": "dataset"
          }
        },
        "index": 2,
        "serviceEndpoint": "http://mymetadata.org/api/v1/provider/assets/metadata/did:nv:0c184915b07b44c888d468be85a9b28253e80070e5294b1aaed81c2f0264e430",
        "type": "metadata"
      }
    ]
  }
]
```

<h3 id="assetcontroller_listddobyquerypost-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|list of DDOs|Inline|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Bad Request|None|

<h3 id="assetcontroller_listddobyquerypost-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[GetAssetDto](#schemagetassetdto)]|false|none|none|
|» @context|string|true|none|Context of the asset|
|» authentication|[[AuthenticationDto](#schemaauthenticationdto)]|true|none|Authentication used in the asset|
|»» publicKey|string|true|none|Public key of ddo|
|»» type|string|true|none|Type of the signature|
|» created|string|true|none|Date when the asset is created|
|» updated|string|true|none|Date when the asset is created|
|» id|string|true|none|ID of the asset|
|» proof|[ProofDto](#schemaproofdto)|true|none|Proof data|
|»» created|string|true|none|Date of the proof|
|»» creator|string|true|none|Wallet address who created the proof signature|
|»» signatureValue|string|true|none|Value of the signature|
|»» type|string|true|none|Type of the proof|
|» publicKey|[[PublicKeyDto](#schemapublickeydto)]|true|none|Public keys that contains the asset|
|»» id|string|true|none|Id of the public key|
|»» owner|string|true|none|Wallet address who own the public key|
|»» type|string|true|none|Type of the public key|
|» service|[[ServiceDto](#schemaservicedto)]|true|none|Services that contains the asset|
|»» index|number|true|none|index of the service|
|»» serviceEndpoint|string|true|none|Url of the service endpoint|
|»» type|string|true|none|Service type|
|»» service|string|false|none|Service name|
|»» purchaseEndpoint|string|false|none|Url to purchase asset|
|»» attributes|[AttributesDto](#schemaattributesdto)|false|none|Attribute of the metadata|
|»»» additionalInformation|object|false|none|Aditional information of the asset|
|»»» curation|[CurationDto](#schemacurationdto)|true|none|popularity of the asset|
|»»»» numVotes|number|true|none|Number of votes. 0 is the default value|
|»»»» rating|number|true|none|Decimal value between 0 and 1. 0 is the default value|
|»»»» schema|string|false|none|Schema applied to calculate the rating|
|»»»» isListed|boolean|false|none|Flag unsuitable content. False by default. If it's true, the content must not be returned|
|»»» main|[MainDto](#schemamaindto)|true|none|Main data of the asset|
|»»»» author|string|true|none|Name of the entity generating this data (e.g. Tfl, Disney Corp, etc.)|
|»»»» dateCreated|string|true|none|The date on which the asset was created by the originator.ISO 8601 format, Coordinated Universal Time, e.g. 2019-01-31T08:38:32Z|
|»»»» datePublished|string|false|none|The date on which the asset DDO is registered into the metadata store|
|»»»» encryptedFiles|string|true|none|files encrytion signature|
|»»»» files|[[FileDto](#schemafiledto)]|true|none|Array of File objects including the encrypted file urls. Further metadata about each file is stored|
|»»»»» checksum|string|false|none|Checksum of the file using your preferred format (i.e. MD5). Format specified in checksumType.If it's not provided can't be validated if the file was not modified after registering|
|»»»»» url|string|false|none|Content URL. Omitted from the remote metadata. Supports http(s):// and ipfs:// URLs|
|»»»»» checksumType|string|false|none|Format of the provided checksum. Can vary according to server (i.e Amazon vs. Azure)|
|»»»»» name|string|false|none|File name|
|»»»»» compression|string|false|none|File compression (e.g. no, gzip, bzip2, etc)|
|»»»»» contentLength|string|false|none|Size of the file in bytes|
|»»»»» contentType|string|true|none|File format|
|»»»»» encoding|string|false|none|File encoding (e.g. UTF-8)|
|»»»»» index|number|true|none|Index of the file|
|»»»»» resourceId|string|false|none|Remote identifier of the file in the external provider. It is typically the remote id in the cloud provider|
|»»»»» encrypted|boolean|false|none|Boolean. Is the file encrypted? If is not set is assumed the file is not encrypted|
|»»»»» encryptionMode|string|false|none|Encryption mode used. Just valid if encrypted=true|
|»»»» license|number|true|none|Short name referencing the license of the asset (e.g. Public Domain, CC-0, CC-BY, No License Specified, etc.). If it's not specified, the following value will be added: "No License Specified|
|»»»» name|string|true|none|Descriptive name or title of the asset|
|»»»» price|string|true|none|Price of the asset. It must be an integer encoded as a string, e.g. "123000000000000000000"|
|»»»» type|string|true|none|Type of the asset. Helps to filter by the type of asset. It could be for example ("dataset", "algorithm")|
|»»»» algorithm|[AlgorithmDto](#schemaalgorithmdto)|true|none|Algorithm used in the asset|
|»»»»» language|string|false|none|Language used to implement the software|
|»»»»» format|string|false|none|Packaging format of the software|
|»»»»» version|string|false|none|Version of the software|
|»»»»» container|[[ContainerDto](#schemacontainerdto)]|true|none|Object describing the Docker container image|
|»»»»»» entrypoint|string|false|none|The command to execute, or script to run inside the Docker image|
|»»»»»» image|string|false|none|Name of the Docker image|
|»»»»»» tag|string|false|none|Tag of the Docker image|
|»»» serviceAgreementTemplate|[ServiceAgreementTemplateDto](#schemaserviceagreementtemplatedto)|false|none|Service agreement template|
|»»»» conditionDependency|[[ConditionDependencyDto](#schemaconditiondependencydto)]|true|none|none|
|»»»»» access|[string]|true|none|Access|
|»»»»» escrowPayment|[string]|true|none|Escrow Payment|
|»»»»» execCompute|[string]|true|none|Exec Compute|
|»»»»» lockPayment|[string]|true|none|Lock Payment|
|»»»» conditions|[[ConditionDto](#schemaconditiondto)]|true|none|Conditions|
|»»»»» contractName|string|true|none|Contract name|
|»»»»» functionName|string|true|none|Function name|
|»»»»» name|string|true|none|Function name|
|»»»»» events|[[EventDto](#schemaeventdto)]|true|none|Events|
|»»»»»» actionType|string|true|none|Action Type|
|»»»»»» handler|[HandlerDto](#schemahandlerdto)|true|none|Handler event|
|»»»»»»» functionName|string|true|none|Function name|
|»»»»»»» moduleName|string|true|none|Module name|
|»»»»»»» version|string|true|none|Version of the handler|
|»»»»»» name|string|true|none|Name of the event|
|»»»»» parameters|[[ParameterDto](#schemaparameterdto)]|true|none|Parameters|
|»»»»»» name|string|true|none|Parameter name|
|»»»»»» type|string|true|none|Parameter type|
|»»»»»» value|object|true|none|Parameter value|
|»»»»» timelock|number|true|none|Time lock|
|»»»»» timeout|number|true|none|Time out|
|»»»» contractName|number|true|none|Contract Name|
|»»»» events|[[EventDto](#schemaeventdto)]|true|none|Events|
|»»»» fulfillmentOrder|string|false|none|Fulfillment order|

<aside class="success">
This operation does not require authentication
</aside>

## AssetController_getDDO

<a id="opIdAssetController_getDDO"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /api/v1/metadata/assets/ddo/{did} \
  -H 'Accept: application/json'

```

```http
GET /api/v1/metadata/assets/ddo/{did} HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/api/v1/metadata/assets/ddo/{did}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/api/v1/metadata/assets/ddo/{did}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/api/v1/metadata/assets/ddo/{did}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/v1/metadata/assets/ddo/{did}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/v1/metadata/assets/ddo/{did}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/v1/metadata/assets/ddo/{did}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /api/v1/metadata/assets/ddo/{did}`

Get DDO of a particular asset

<h3 id="assetcontroller_getddo-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|did|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "@context": "https://w3id.org/did/v1",
  "authentication": [
    {
      "publicKey": "did:nv:0c184915b07b44c888d468be85a9b28253e80070e5294b1aaed81c2f0264e430",
      "type": "RsaSignatureAuthentication2018"
    }
  ],
  "created": "2021-02-01T10:55:11Z",
  "updated": "2021-02-01T10:55:11Z",
  "id": "did:nv:0c184915b07b44c888d468be85a9b28253e80070e5294b1aaed81c2f0264e429",
  "proof": {
    "created": "2022-01-08T16:02:20Z",
    "creator": "2022-01-08T16:02:20Z",
    "signatureValue": "0xbd7b46b3ac664167bc70ac211b1a1da0baed9ead91613a5f02dfc25c1bb6e3ff40861b455017e8a587fd4e37b703436072598c3a81ec88be28bfe33b61554a471b",
    "type": "DDOIntegritySignature"
  },
  "publicKey": [
    {
      "id": "did:nv:0c184915b07b44c888d468be85a9b28253e80070e5294b1aaed81c2f0264e430",
      "owner": "0x00Bd138aBD70e2F00903268F3Db08f2D25677C9e",
      "type": "EthereumECDSAKey"
    }
  ],
  "service": [
    {
      "index": 0,
      "service": "SecretStore",
      "serviceEndpoint": "http://localhost:12001",
      "type": "authorization"
    },
    {
      "index": 1,
      "purchaseEndpoint": "http://localhost:8030/api/v1/gateway/services/access/initialize",
      "serviceEndpoint": "http://localhost:8030/api/v1/gateway/services/consume",
      "type": "access"
    },
    {
      "attributes": {
        "additionalInformation": {
          "copyrightHolder": "Met Office",
          "description": "Weather information of UK including temperature and humidity",
          "inLanguage": "en",
          "links": [
            {
              "name": "Sample of Asset Data",
              "type": "sample",
              "url": "https://foo.com/sample.csv"
            }
          ],
          "tags": [
            "weather",
            "uk",
            "2011",
            "temperature",
            "humidity"
          ],
          "workExample": "stationId,latitude,longitude,datetime, temperature,humidity/n423432fsd,51.509865,-0.118092, 2011-01-01T10:55:11+00:00,7.2,68"
        },
        "curation": {
          "numVotes": 123,
          "rating": 0.93,
          "schema": "Binary Voting"
        },
        "main": {
          "author": "Met Office",
          "dateCreated": "2012-02-01T10:55:11Z",
          "encryptedFiles": "0x098213xzckasdf089723hjgdasfkjgasfv",
          "files": [
            {
              "compression": "zip",
              "contentLength": "4535431",
              "contentType": "text/csv",
              "encoding": "UTF-8",
              "index": 0,
              "resourceId": "access-log2018-02-13-15-17-29-18386C502CAEA932"
            }
          ],
          "license": "CC-BY",
          "name": "UK Weather information 2011",
          "price": "10",
          "type": "dataset"
        }
      },
      "index": 2,
      "serviceEndpoint": "http://mymetadata.org/api/v1/provider/assets/metadata/did:nv:0c184915b07b44c888d468be85a9b28253e80070e5294b1aaed81c2f0264e430",
      "type": "metadata"
    }
  ]
}
```

<h3 id="assetcontroller_getddo-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Get a DDO|[GetAssetDto](#schemagetassetdto)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|None|

<aside class="success">
This operation does not require authentication
</aside>

## AssetController_updateDDO

<a id="opIdAssetController_updateDDO"></a>

> Code samples

```shell
# You can also use wget
curl -X PUT /api/v1/metadata/assets/ddo/{did} \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
PUT /api/v1/metadata/assets/ddo/{did} HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "@context": "https://w3id.org/did/v1",
  "updated": "2019-02-08T08:13:49Z",
  "authentication": [
    {
      "publicKey": "did:nv:0c184915b07b44c888d468be85a9b28253e80070e5294b1aaed81c2f0264e430",
      "type": "RsaSignatureAuthentication2018"
    }
  ],
  "proof": {
    "created": "2022-01-08T16:02:20Z",
    "creator": "2022-01-08T16:02:20Z",
    "signatureValue": "0xbd7b46b3ac664167bc70ac211b1a1da0baed9ead91613a5f02dfc25c1bb6e3ff40861b455017e8a587fd4e37b703436072598c3a81ec88be28bfe33b61554a471b",
    "type": "DDOIntegritySignature"
  },
  "publicKey": [
    {
      "id": "did:nv:0c184915b07b44c888d468be85a9b28253e80070e5294b1aaed81c2f0264e430",
      "owner": "0x00Bd138aBD70e2F00903268F3Db08f2D25677C9e",
      "type": "EthereumECDSAKey"
    }
  ],
  "service": [
    {
      "index": 0,
      "service": "SecretStore",
      "serviceEndpoint": "http://localhost:12001",
      "type": "authorization"
    },
    {
      "index": 1,
      "purchaseEndpoint": "http://localhost:8030/api/v1/gateway/services/access/initialize",
      "serviceEndpoint": "http://localhost:8030/api/v1/gateway/services/consume",
      "type": "access"
    },
    {
      "attributes": {
        "additionalInformation": {
          "copyrightHolder": "Met Office",
          "description": "Weather information of UK including temperature and humidity",
          "inLanguage": "en",
          "links": [
            {
              "name": "Sample of Asset Data",
              "type": "sample",
              "url": "https://foo.com/sample.csv"
            }
          ],
          "tags": [
            "weather",
            "uk",
            "2011",
            "temperature",
            "humidity"
          ],
          "workExample": "stationId,latitude,longitude,datetime, temperature,humidity/n423432fsd,51.509865,-0.118092, 2011-01-01T10:55:11+00:00,7.2,68"
        },
        "curation": {
          "numVotes": 123,
          "rating": 0.93,
          "schema": "Binary Voting"
        },
        "main": {
          "author": "Met Office",
          "dateCreated": "2012-02-01T10:55:11Z",
          "encryptedFiles": "0x098213xzckasdf089723hjgdasfkjgasfv",
          "files": [
            {
              "compression": "zip",
              "contentLength": "4535431",
              "contentType": "text/csv",
              "encoding": "UTF-8",
              "index": 0,
              "resourceId": "access-log2018-02-13-15-17-29-18386C502CAEA932"
            }
          ],
          "license": "CC-BY",
          "name": "UK Weather information 2011",
          "price": "10",
          "type": "dataset"
        }
      },
      "index": 2,
      "serviceEndpoint": "http://mymetadata.org/api/v1/provider/assets/metadata/did:nv:0c184915b07b44c888d468be85a9b28253e80070e5294b1aaed81c2f0264e430",
      "type": "metadata"
    }
  ]
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/api/v1/metadata/assets/ddo/{did}',
{
  method: 'PUT',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.put '/api/v1/metadata/assets/ddo/{did}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.put('/api/v1/metadata/assets/ddo/{did}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('PUT','/api/v1/metadata/assets/ddo/{did}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/v1/metadata/assets/ddo/{did}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PUT");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PUT", "/api/v1/metadata/assets/ddo/{did}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`PUT /api/v1/metadata/assets/ddo/{did}`

Update DDO of an existing asset

> Body parameter

```json
{
  "@context": "https://w3id.org/did/v1",
  "updated": "2019-02-08T08:13:49Z",
  "authentication": [
    {
      "publicKey": "did:nv:0c184915b07b44c888d468be85a9b28253e80070e5294b1aaed81c2f0264e430",
      "type": "RsaSignatureAuthentication2018"
    }
  ],
  "proof": {
    "created": "2022-01-08T16:02:20Z",
    "creator": "2022-01-08T16:02:20Z",
    "signatureValue": "0xbd7b46b3ac664167bc70ac211b1a1da0baed9ead91613a5f02dfc25c1bb6e3ff40861b455017e8a587fd4e37b703436072598c3a81ec88be28bfe33b61554a471b",
    "type": "DDOIntegritySignature"
  },
  "publicKey": [
    {
      "id": "did:nv:0c184915b07b44c888d468be85a9b28253e80070e5294b1aaed81c2f0264e430",
      "owner": "0x00Bd138aBD70e2F00903268F3Db08f2D25677C9e",
      "type": "EthereumECDSAKey"
    }
  ],
  "service": [
    {
      "index": 0,
      "service": "SecretStore",
      "serviceEndpoint": "http://localhost:12001",
      "type": "authorization"
    },
    {
      "index": 1,
      "purchaseEndpoint": "http://localhost:8030/api/v1/gateway/services/access/initialize",
      "serviceEndpoint": "http://localhost:8030/api/v1/gateway/services/consume",
      "type": "access"
    },
    {
      "attributes": {
        "additionalInformation": {
          "copyrightHolder": "Met Office",
          "description": "Weather information of UK including temperature and humidity",
          "inLanguage": "en",
          "links": [
            {
              "name": "Sample of Asset Data",
              "type": "sample",
              "url": "https://foo.com/sample.csv"
            }
          ],
          "tags": [
            "weather",
            "uk",
            "2011",
            "temperature",
            "humidity"
          ],
          "workExample": "stationId,latitude,longitude,datetime, temperature,humidity/n423432fsd,51.509865,-0.118092, 2011-01-01T10:55:11+00:00,7.2,68"
        },
        "curation": {
          "numVotes": 123,
          "rating": 0.93,
          "schema": "Binary Voting"
        },
        "main": {
          "author": "Met Office",
          "dateCreated": "2012-02-01T10:55:11Z",
          "encryptedFiles": "0x098213xzckasdf089723hjgdasfkjgasfv",
          "files": [
            {
              "compression": "zip",
              "contentLength": "4535431",
              "contentType": "text/csv",
              "encoding": "UTF-8",
              "index": 0,
              "resourceId": "access-log2018-02-13-15-17-29-18386C502CAEA932"
            }
          ],
          "license": "CC-BY",
          "name": "UK Weather information 2011",
          "price": "10",
          "type": "dataset"
        }
      },
      "index": 2,
      "serviceEndpoint": "http://mymetadata.org/api/v1/provider/assets/metadata/did:nv:0c184915b07b44c888d468be85a9b28253e80070e5294b1aaed81c2f0264e430",
      "type": "metadata"
    }
  ]
}
```

<h3 id="assetcontroller_updateddo-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|did|path|string|true|none|
|body|body|[UpdateAssetDto](#schemaupdateassetdto)|true|none|

> Example responses

> 200 Response

```json
{
  "@context": "https://w3id.org/did/v1",
  "authentication": [
    {
      "publicKey": "did:nv:0c184915b07b44c888d468be85a9b28253e80070e5294b1aaed81c2f0264e430",
      "type": "RsaSignatureAuthentication2018"
    }
  ],
  "created": "2021-02-01T10:55:11Z",
  "updated": "2021-02-01T10:55:11Z",
  "id": "did:nv:0c184915b07b44c888d468be85a9b28253e80070e5294b1aaed81c2f0264e429",
  "proof": {
    "created": "2022-01-08T16:02:20Z",
    "creator": "2022-01-08T16:02:20Z",
    "signatureValue": "0xbd7b46b3ac664167bc70ac211b1a1da0baed9ead91613a5f02dfc25c1bb6e3ff40861b455017e8a587fd4e37b703436072598c3a81ec88be28bfe33b61554a471b",
    "type": "DDOIntegritySignature"
  },
  "publicKey": [
    {
      "id": "did:nv:0c184915b07b44c888d468be85a9b28253e80070e5294b1aaed81c2f0264e430",
      "owner": "0x00Bd138aBD70e2F00903268F3Db08f2D25677C9e",
      "type": "EthereumECDSAKey"
    }
  ],
  "service": [
    {
      "index": 0,
      "service": "SecretStore",
      "serviceEndpoint": "http://localhost:12001",
      "type": "authorization"
    },
    {
      "index": 1,
      "purchaseEndpoint": "http://localhost:8030/api/v1/gateway/services/access/initialize",
      "serviceEndpoint": "http://localhost:8030/api/v1/gateway/services/consume",
      "type": "access"
    },
    {
      "attributes": {
        "additionalInformation": {
          "copyrightHolder": "Met Office",
          "description": "Weather information of UK including temperature and humidity",
          "inLanguage": "en",
          "links": [
            {
              "name": "Sample of Asset Data",
              "type": "sample",
              "url": "https://foo.com/sample.csv"
            }
          ],
          "tags": [
            "weather",
            "uk",
            "2011",
            "temperature",
            "humidity"
          ],
          "workExample": "stationId,latitude,longitude,datetime, temperature,humidity/n423432fsd,51.509865,-0.118092, 2011-01-01T10:55:11+00:00,7.2,68"
        },
        "curation": {
          "numVotes": 123,
          "rating": 0.93,
          "schema": "Binary Voting"
        },
        "main": {
          "author": "Met Office",
          "dateCreated": "2012-02-01T10:55:11Z",
          "encryptedFiles": "0x098213xzckasdf089723hjgdasfkjgasfv",
          "files": [
            {
              "compression": "zip",
              "contentLength": "4535431",
              "contentType": "text/csv",
              "encoding": "UTF-8",
              "index": 0,
              "resourceId": "access-log2018-02-13-15-17-29-18386C502CAEA932"
            }
          ],
          "license": "CC-BY",
          "name": "UK Weather information 2011",
          "price": "10",
          "type": "dataset"
        }
      },
      "index": 2,
      "serviceEndpoint": "http://mymetadata.org/api/v1/provider/assets/metadata/did:nv:0c184915b07b44c888d468be85a9b28253e80070e5294b1aaed81c2f0264e430",
      "type": "metadata"
    }
  ]
}
```

<h3 id="assetcontroller_updateddo-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Get a updated DDO|[GetAssetDto](#schemagetassetdto)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Bad Request|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|None|

<aside class="success">
This operation does not require authentication
</aside>

## AssetController_deleteDDO

<a id="opIdAssetController_deleteDDO"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE /api/v1/metadata/assets/ddo/{did}

```

```http
DELETE /api/v1/metadata/assets/ddo/{did} HTTP/1.1

```

```javascript

fetch('/api/v1/metadata/assets/ddo/{did}',
{
  method: 'DELETE'

})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

result = RestClient.delete '/api/v1/metadata/assets/ddo/{did}',
  params: {
  }

p JSON.parse(result)

```

```python
import requests

r = requests.delete('/api/v1/metadata/assets/ddo/{did}')

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('DELETE','/api/v1/metadata/assets/ddo/{did}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/v1/metadata/assets/ddo/{did}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "/api/v1/metadata/assets/ddo/{did}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`DELETE /api/v1/metadata/assets/ddo/{did}`

<h3 id="assetcontroller_deleteddo-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|did|path|string|true|none|

<h3 id="assetcontroller_deleteddo-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Deleted DDO|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|None|
|default|Default|Retire metadata of an asset|None|

<aside class="success">
This operation does not require authentication
</aside>

## AssetController_getDDOMetadata

<a id="opIdAssetController_getDDOMetadata"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /api/v1/metadata/assets/metadata/{did} \
  -H 'Accept: application/json'

```

```http
GET /api/v1/metadata/assets/metadata/{did} HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/api/v1/metadata/assets/metadata/{did}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/api/v1/metadata/assets/metadata/{did}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/api/v1/metadata/assets/metadata/{did}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/v1/metadata/assets/metadata/{did}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/v1/metadata/assets/metadata/{did}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/v1/metadata/assets/metadata/{did}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /api/v1/metadata/assets/metadata/{did}`

<h3 id="assetcontroller_getddometadata-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|did|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "additionalInformation": {},
  "curation": {
    "numVotes": 123,
    "rating": 0.93,
    "schema": "Binary Voting",
    "isListed": false
  },
  "main": {
    "author": "Met Office",
    "dateCreated": "2021-02-01T10:55:11Z",
    "datePublished": "2021-02-01T10:55:11Z",
    "encryptedFiles": "0x098213xzckasdf089723hjgdasfkjgasfv",
    "files": [
      {
        "checksum": "efb2c764274b745f5fc37f97c6b0e761",
        "url": "https://raw.githubusercontent.com/tbertinmahieux/MSongsDB/master/Tasks_Demos/CoverSongs/shs_dataset_test.txt",
        "checksumType": "md5",
        "name": "data.txt",
        "compression": "zip",
        "contentLength": "4535431",
        "contentType": "text/csv",
        "encoding": "UTF-8",
        "index": 0,
        "resourceId": "access-log2018-02-13-15-17-29-18386C502CAEA932",
        "encrypted": false,
        "encryptionMode": "gpg"
      }
    ],
    "license": "CC-BY",
    "name": "UK Weather information 2011",
    "price": "10",
    "type": "dataset",
    "algorithm": {
      "language": "scala",
      "format": "docker-image",
      "version": "0.1",
      "container": [
        {
          "entrypoint": "node $ALGO",
          "image": "node",
          "tag": "10"
        }
      ]
    }
  },
  "serviceAgreementTemplate": {
    "conditionDependency": [
      {
        "access": [],
        "escrowPayment": [
          "lockPayment",
          "access"
        ],
        "execCompute": [],
        "lockPayment": []
      }
    ],
    "conditions": [
      {
        "contractName": "LockPaymentCondition",
        "functionName": "fulfill",
        "name": "lockPayment",
        "events": [
          {
            "actionType": "publisher",
            "handler": {
              "functionName": "fulfill",
              "moduleName": "lockPaymentConditon",
              "version": "0.1"
            },
            "name": "Fulfilled"
          }
        ],
        "parameters": [
          {
            "name": "_rewardAddress",
            "type": "address",
            "value": "0x886dE2b3F8F27eEd43bA2FD4bC2AabDc14E0d9dD"
          }
        ],
        "timelock": 0,
        "timeout": 0
      }
    ],
    "contractName": "EscrowAccessSecretStoreTemplate",
    "events": [
      {
        "actionType": "publisher",
        "handler": {
          "functionName": "fulfill",
          "moduleName": "lockPaymentConditon",
          "version": "0.1"
        },
        "name": "Fulfilled"
      }
    ],
    "fulfillmentOrder": [
      "lockPayment.fulfill",
      "access.fulfill",
      "escrowPayment.fulfill"
    ]
  }
}
```

<h3 id="assetcontroller_getddometadata-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Get a metadata from asset|[AttributesDto](#schemaattributesdto)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|None|
|default|Default|Get metadata of a particular asset|None|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="marketplace-api-bookmark">Bookmark</h1>

## BookmarkController_createBookmark

<a id="opIdBookmarkController_createBookmark"></a>

> Code samples

```shell
# You can also use wget
curl -X POST /api/v1/ugc/bookmarks \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
POST /api/v1/ugc/bookmarks HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "did": "did:12345",
  "userId": "u-12345",
  "description": "I am interesting in this asset"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/api/v1/ugc/bookmarks',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.post '/api/v1/ugc/bookmarks',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/api/v1/ugc/bookmarks', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/api/v1/ugc/bookmarks', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/v1/ugc/bookmarks");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/api/v1/ugc/bookmarks", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /api/v1/ugc/bookmarks`

Create a bookmark entry

> Body parameter

```json
{
  "did": "did:12345",
  "userId": "u-12345",
  "description": "I am interesting in this asset"
}
```

<h3 id="bookmarkcontroller_createbookmark-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[CreateBookmarkDto](#schemacreatebookmarkdto)|true|none|

> Example responses

> 201 Response

```json
{
  "id": "b-123434",
  "did": "did:12345",
  "userId": "u-12345",
  "description": "I am interesting in this asset",
  "createdAt": "2022-03-18T13:44:00.931Z"
}
```

<h3 id="bookmarkcontroller_createbookmark-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Bookmark is created|[GetBookmarkDto](#schemagetbookmarkdto)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Bad Request|None|

<aside class="success">
This operation does not require authentication
</aside>

## BookmarkController_getBookmarkById

<a id="opIdBookmarkController_getBookmarkById"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /api/v1/ugc/bookmarks/{id} \
  -H 'Accept: application/json'

```

```http
GET /api/v1/ugc/bookmarks/{id} HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/api/v1/ugc/bookmarks/{id}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/api/v1/ugc/bookmarks/{id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/api/v1/ugc/bookmarks/{id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/v1/ugc/bookmarks/{id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/v1/ugc/bookmarks/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/v1/ugc/bookmarks/{id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /api/v1/ugc/bookmarks/{id}`

Get a bookmark entry

<h3 id="bookmarkcontroller_getbookmarkbyid-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "id": "b-123434",
  "did": "did:12345",
  "userId": "u-12345",
  "description": "I am interesting in this asset",
  "createdAt": "2022-03-18T13:44:00.931Z"
}
```

<h3 id="bookmarkcontroller_getbookmarkbyid-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Return a bookmark user|[GetBookmarkDto](#schemagetbookmarkdto)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|None|

<aside class="success">
This operation does not require authentication
</aside>

## BookmarkController_updateBookmarkById

<a id="opIdBookmarkController_updateBookmarkById"></a>

> Code samples

```shell
# You can also use wget
curl -X PUT /api/v1/ugc/bookmarks/{id} \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
PUT /api/v1/ugc/bookmarks/{id} HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "description": "I am interesting in this asset"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/api/v1/ugc/bookmarks/{id}',
{
  method: 'PUT',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.put '/api/v1/ugc/bookmarks/{id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.put('/api/v1/ugc/bookmarks/{id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('PUT','/api/v1/ugc/bookmarks/{id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/v1/ugc/bookmarks/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PUT");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PUT", "/api/v1/ugc/bookmarks/{id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`PUT /api/v1/ugc/bookmarks/{id}`

Update an existing bookmark

> Body parameter

```json
{
  "description": "I am interesting in this asset"
}
```

<h3 id="bookmarkcontroller_updatebookmarkbyid-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string|true|none|
|body|body|[UpdateBookmarkDto](#schemaupdatebookmarkdto)|true|none|

> Example responses

> 200 Response

```json
{
  "id": "b-123434",
  "did": "did:12345",
  "userId": "u-12345",
  "description": "I am interesting in this asset",
  "createdAt": "2022-03-18T13:44:00.931Z"
}
```

<h3 id="bookmarkcontroller_updatebookmarkbyid-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Return a updated bookmark|[GetBookmarkDto](#schemagetbookmarkdto)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Bad Request|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|None|

<aside class="success">
This operation does not require authentication
</aside>

## BookmarkController_deleteBookmarkById

<a id="opIdBookmarkController_deleteBookmarkById"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE /api/v1/ugc/bookmarks/{id}

```

```http
DELETE /api/v1/ugc/bookmarks/{id} HTTP/1.1

```

```javascript

fetch('/api/v1/ugc/bookmarks/{id}',
{
  method: 'DELETE'

})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

result = RestClient.delete '/api/v1/ugc/bookmarks/{id}',
  params: {
  }

p JSON.parse(result)

```

```python
import requests

r = requests.delete('/api/v1/ugc/bookmarks/{id}')

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('DELETE','/api/v1/ugc/bookmarks/{id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/v1/ugc/bookmarks/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "/api/v1/ugc/bookmarks/{id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`DELETE /api/v1/ugc/bookmarks/{id}`

Delete a bookmark

<h3 id="bookmarkcontroller_deletebookmarkbyid-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string|true|none|

<h3 id="bookmarkcontroller_deletebookmarkbyid-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|return bookmark deleted|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|None|

<aside class="success">
This operation does not require authentication
</aside>

## BookmarkController_getBookmarksByUserId

<a id="opIdBookmarkController_getBookmarksByUserId"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /api/v1/ugc/bookmarks/user/{userId} \
  -H 'Accept: application/json'

```

```http
GET /api/v1/ugc/bookmarks/user/{userId} HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/api/v1/ugc/bookmarks/user/{userId}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/api/v1/ugc/bookmarks/user/{userId}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/api/v1/ugc/bookmarks/user/{userId}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/v1/ugc/bookmarks/user/{userId}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/v1/ugc/bookmarks/user/{userId}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/v1/ugc/bookmarks/user/{userId}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /api/v1/ugc/bookmarks/user/{userId}`

Get all the user bookmarks

<h3 id="bookmarkcontroller_getbookmarksbyuserid-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|userId|path|string|true|none|
|query|query|string|false|execute directly queries to elasticsearch from the client|
|text|query|string|false|Text to search|
|offset|query|string|false|Page Size|
|page|query|string|false|Page to retrieve|
|sort|query|string|false|sort the response by specified parameter|

> Example responses

> 200 Response

```json
[
  {
    "id": "b-123434",
    "did": "did:12345",
    "userId": "u-12345",
    "description": "I am interesting in this asset",
    "createdAt": "2022-03-18T13:44:00.931Z"
  }
]
```

<h3 id="bookmarkcontroller_getbookmarksbyuserid-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Return all bookmark from a user|Inline|

<h3 id="bookmarkcontroller_getbookmarksbyuserid-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[GetBookmarkDto](#schemagetbookmarkdto)]|false|none|none|
|» id|string|true|none|The identifier of the bookmark|
|» did|string|true|none|The identifier of the asset|
|» userId|string|true|none|The userId who created the bookmark|
|» description|string|true|none|Description given by the user|
|» createdAt|string(date-time)|true|none|When the UGC was created|

<aside class="success">
This operation does not require authentication
</aside>

# Schemas

<h2 id="tocS_AuthenticationDto">AuthenticationDto</h2>
<!-- backwards compatibility -->
<a id="schemaauthenticationdto"></a>
<a id="schema_AuthenticationDto"></a>
<a id="tocSauthenticationdto"></a>
<a id="tocsauthenticationdto"></a>

```json
{
  "publicKey": "did:nv:0c184915b07b44c888d468be85a9b28253e80070e5294b1aaed81c2f0264e430",
  "type": "RsaSignatureAuthentication2018"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|publicKey|string|true|none|Public key of ddo|
|type|string|true|none|Type of the signature|

<h2 id="tocS_ProofDto">ProofDto</h2>
<!-- backwards compatibility -->
<a id="schemaproofdto"></a>
<a id="schema_ProofDto"></a>
<a id="tocSproofdto"></a>
<a id="tocsproofdto"></a>

```json
{
  "created": "2022-01-08T16:02:20Z",
  "creator": "2022-01-08T16:02:20Z",
  "signatureValue": "0xbd7b46b3ac664167bc70ac211b1a1da0baed9ead91613a5f02dfc25c1bb6e3ff40861b455017e8a587fd4e37b703436072598c3a81ec88be28bfe33b61554a471b",
  "type": "DDOIntegritySignature"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|created|string|true|none|Date of the proof|
|creator|string|true|none|Wallet address who created the proof signature|
|signatureValue|string|true|none|Value of the signature|
|type|string|true|none|Type of the proof|

<h2 id="tocS_PublicKeyDto">PublicKeyDto</h2>
<!-- backwards compatibility -->
<a id="schemapublickeydto"></a>
<a id="schema_PublicKeyDto"></a>
<a id="tocSpublickeydto"></a>
<a id="tocspublickeydto"></a>

```json
{
  "id": "did:nv:0c184915b07b44c888d468be85a9b28253e80070e5294b1aaed81c2f0264e430",
  "owner": "0x00Bd138aBD70e2F00903268F3Db08f2D25677C9e",
  "type": "EthereumECDSAKey"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string|true|none|Id of the public key|
|owner|string|true|none|Wallet address who own the public key|
|type|string|true|none|Type of the public key|

<h2 id="tocS_CurationDto">CurationDto</h2>
<!-- backwards compatibility -->
<a id="schemacurationdto"></a>
<a id="schema_CurationDto"></a>
<a id="tocScurationdto"></a>
<a id="tocscurationdto"></a>

```json
{
  "numVotes": 123,
  "rating": 0.93,
  "schema": "Binary Voting",
  "isListed": false
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|numVotes|number|true|none|Number of votes. 0 is the default value|
|rating|number|true|none|Decimal value between 0 and 1. 0 is the default value|
|schema|string|false|none|Schema applied to calculate the rating|
|isListed|boolean|false|none|Flag unsuitable content. False by default. If it's true, the content must not be returned|

<h2 id="tocS_FileDto">FileDto</h2>
<!-- backwards compatibility -->
<a id="schemafiledto"></a>
<a id="schema_FileDto"></a>
<a id="tocSfiledto"></a>
<a id="tocsfiledto"></a>

```json
{
  "checksum": "efb2c764274b745f5fc37f97c6b0e761",
  "url": "https://raw.githubusercontent.com/tbertinmahieux/MSongsDB/master/Tasks_Demos/CoverSongs/shs_dataset_test.txt",
  "checksumType": "md5",
  "name": "data.txt",
  "compression": "zip",
  "contentLength": "4535431",
  "contentType": "text/csv",
  "encoding": "UTF-8",
  "index": 0,
  "resourceId": "access-log2018-02-13-15-17-29-18386C502CAEA932",
  "encrypted": false,
  "encryptionMode": "gpg"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|checksum|string|false|none|Checksum of the file using your preferred format (i.e. MD5). Format specified in checksumType.If it's not provided can't be validated if the file was not modified after registering|
|url|string|false|none|Content URL. Omitted from the remote metadata. Supports http(s):// and ipfs:// URLs|
|checksumType|string|false|none|Format of the provided checksum. Can vary according to server (i.e Amazon vs. Azure)|
|name|string|false|none|File name|
|compression|string|false|none|File compression (e.g. no, gzip, bzip2, etc)|
|contentLength|string|false|none|Size of the file in bytes|
|contentType|string|true|none|File format|
|encoding|string|false|none|File encoding (e.g. UTF-8)|
|index|number|true|none|Index of the file|
|resourceId|string|false|none|Remote identifier of the file in the external provider. It is typically the remote id in the cloud provider|
|encrypted|boolean|false|none|Boolean. Is the file encrypted? If is not set is assumed the file is not encrypted|
|encryptionMode|string|false|none|Encryption mode used. Just valid if encrypted=true|

<h2 id="tocS_ContainerDto">ContainerDto</h2>
<!-- backwards compatibility -->
<a id="schemacontainerdto"></a>
<a id="schema_ContainerDto"></a>
<a id="tocScontainerdto"></a>
<a id="tocscontainerdto"></a>

```json
{
  "entrypoint": "node $ALGO",
  "image": "node",
  "tag": "10"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|entrypoint|string|false|none|The command to execute, or script to run inside the Docker image|
|image|string|false|none|Name of the Docker image|
|tag|string|false|none|Tag of the Docker image|

<h2 id="tocS_AlgorithmDto">AlgorithmDto</h2>
<!-- backwards compatibility -->
<a id="schemaalgorithmdto"></a>
<a id="schema_AlgorithmDto"></a>
<a id="tocSalgorithmdto"></a>
<a id="tocsalgorithmdto"></a>

```json
{
  "language": "scala",
  "format": "docker-image",
  "version": "0.1",
  "container": [
    {
      "entrypoint": "node $ALGO",
      "image": "node",
      "tag": "10"
    }
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|language|string|false|none|Language used to implement the software|
|format|string|false|none|Packaging format of the software|
|version|string|false|none|Version of the software|
|container|[[ContainerDto](#schemacontainerdto)]|true|none|Object describing the Docker container image|

<h2 id="tocS_MainDto">MainDto</h2>
<!-- backwards compatibility -->
<a id="schemamaindto"></a>
<a id="schema_MainDto"></a>
<a id="tocSmaindto"></a>
<a id="tocsmaindto"></a>

```json
{
  "author": "Met Office",
  "dateCreated": "2021-02-01T10:55:11Z",
  "datePublished": "2021-02-01T10:55:11Z",
  "encryptedFiles": "0x098213xzckasdf089723hjgdasfkjgasfv",
  "files": [
    {
      "checksum": "efb2c764274b745f5fc37f97c6b0e761",
      "url": "https://raw.githubusercontent.com/tbertinmahieux/MSongsDB/master/Tasks_Demos/CoverSongs/shs_dataset_test.txt",
      "checksumType": "md5",
      "name": "data.txt",
      "compression": "zip",
      "contentLength": "4535431",
      "contentType": "text/csv",
      "encoding": "UTF-8",
      "index": 0,
      "resourceId": "access-log2018-02-13-15-17-29-18386C502CAEA932",
      "encrypted": false,
      "encryptionMode": "gpg"
    }
  ],
  "license": "CC-BY",
  "name": "UK Weather information 2011",
  "price": "10",
  "type": "dataset",
  "algorithm": {
    "language": "scala",
    "format": "docker-image",
    "version": "0.1",
    "container": [
      {
        "entrypoint": "node $ALGO",
        "image": "node",
        "tag": "10"
      }
    ]
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|author|string|true|none|Name of the entity generating this data (e.g. Tfl, Disney Corp, etc.)|
|dateCreated|string|true|none|The date on which the asset was created by the originator.ISO 8601 format, Coordinated Universal Time, e.g. 2019-01-31T08:38:32Z|
|datePublished|string|false|none|The date on which the asset DDO is registered into the metadata store|
|encryptedFiles|string|true|none|files encrytion signature|
|files|[[FileDto](#schemafiledto)]|true|none|Array of File objects including the encrypted file urls. Further metadata about each file is stored|
|license|number|true|none|Short name referencing the license of the asset (e.g. Public Domain, CC-0, CC-BY, No License Specified, etc.). If it's not specified, the following value will be added: "No License Specified|
|name|string|true|none|Descriptive name or title of the asset|
|price|string|true|none|Price of the asset. It must be an integer encoded as a string, e.g. "123000000000000000000"|
|type|string|true|none|Type of the asset. Helps to filter by the type of asset. It could be for example ("dataset", "algorithm")|
|algorithm|[AlgorithmDto](#schemaalgorithmdto)|true|none|Algorithm used in the asset|

<h2 id="tocS_ConditionDependencyDto">ConditionDependencyDto</h2>
<!-- backwards compatibility -->
<a id="schemaconditiondependencydto"></a>
<a id="schema_ConditionDependencyDto"></a>
<a id="tocSconditiondependencydto"></a>
<a id="tocsconditiondependencydto"></a>

```json
{
  "access": [],
  "escrowPayment": [
    "lockPayment",
    "access"
  ],
  "execCompute": [],
  "lockPayment": []
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|access|[string]|true|none|Access|
|escrowPayment|[string]|true|none|Escrow Payment|
|execCompute|[string]|true|none|Exec Compute|
|lockPayment|[string]|true|none|Lock Payment|

<h2 id="tocS_HandlerDto">HandlerDto</h2>
<!-- backwards compatibility -->
<a id="schemahandlerdto"></a>
<a id="schema_HandlerDto"></a>
<a id="tocShandlerdto"></a>
<a id="tocshandlerdto"></a>

```json
{
  "functionName": "fulfill",
  "moduleName": "lockPaymentConditon",
  "version": "0.1"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|functionName|string|true|none|Function name|
|moduleName|string|true|none|Module name|
|version|string|true|none|Version of the handler|

<h2 id="tocS_EventDto">EventDto</h2>
<!-- backwards compatibility -->
<a id="schemaeventdto"></a>
<a id="schema_EventDto"></a>
<a id="tocSeventdto"></a>
<a id="tocseventdto"></a>

```json
{
  "actionType": "publisher",
  "handler": {
    "functionName": "fulfill",
    "moduleName": "lockPaymentConditon",
    "version": "0.1"
  },
  "name": "Fulfilled"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|actionType|string|true|none|Action Type|
|handler|[HandlerDto](#schemahandlerdto)|true|none|Handler event|
|name|string|true|none|Name of the event|

<h2 id="tocS_ParameterDto">ParameterDto</h2>
<!-- backwards compatibility -->
<a id="schemaparameterdto"></a>
<a id="schema_ParameterDto"></a>
<a id="tocSparameterdto"></a>
<a id="tocsparameterdto"></a>

```json
{
  "name": "_rewardAddress",
  "type": "address",
  "value": "0x886dE2b3F8F27eEd43bA2FD4bC2AabDc14E0d9dD"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|name|string|true|none|Parameter name|
|type|string|true|none|Parameter type|
|value|object|true|none|Parameter value|

<h2 id="tocS_ConditionDto">ConditionDto</h2>
<!-- backwards compatibility -->
<a id="schemaconditiondto"></a>
<a id="schema_ConditionDto"></a>
<a id="tocSconditiondto"></a>
<a id="tocsconditiondto"></a>

```json
{
  "contractName": "LockPaymentCondition",
  "functionName": "fulfill",
  "name": "lockPayment",
  "events": [
    {
      "actionType": "publisher",
      "handler": {
        "functionName": "fulfill",
        "moduleName": "lockPaymentConditon",
        "version": "0.1"
      },
      "name": "Fulfilled"
    }
  ],
  "parameters": [
    {
      "name": "_rewardAddress",
      "type": "address",
      "value": "0x886dE2b3F8F27eEd43bA2FD4bC2AabDc14E0d9dD"
    }
  ],
  "timelock": 0,
  "timeout": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|contractName|string|true|none|Contract name|
|functionName|string|true|none|Function name|
|name|string|true|none|Function name|
|events|[[EventDto](#schemaeventdto)]|true|none|Events|
|parameters|[[ParameterDto](#schemaparameterdto)]|true|none|Parameters|
|timelock|number|true|none|Time lock|
|timeout|number|true|none|Time out|

<h2 id="tocS_ServiceAgreementTemplateDto">ServiceAgreementTemplateDto</h2>
<!-- backwards compatibility -->
<a id="schemaserviceagreementtemplatedto"></a>
<a id="schema_ServiceAgreementTemplateDto"></a>
<a id="tocSserviceagreementtemplatedto"></a>
<a id="tocsserviceagreementtemplatedto"></a>

```json
{
  "conditionDependency": [
    {
      "access": [],
      "escrowPayment": [
        "lockPayment",
        "access"
      ],
      "execCompute": [],
      "lockPayment": []
    }
  ],
  "conditions": [
    {
      "contractName": "LockPaymentCondition",
      "functionName": "fulfill",
      "name": "lockPayment",
      "events": [
        {
          "actionType": "publisher",
          "handler": {
            "functionName": "fulfill",
            "moduleName": "lockPaymentConditon",
            "version": "0.1"
          },
          "name": "Fulfilled"
        }
      ],
      "parameters": [
        {
          "name": "_rewardAddress",
          "type": "address",
          "value": "0x886dE2b3F8F27eEd43bA2FD4bC2AabDc14E0d9dD"
        }
      ],
      "timelock": 0,
      "timeout": 0
    }
  ],
  "contractName": "EscrowAccessSecretStoreTemplate",
  "events": [
    {
      "actionType": "publisher",
      "handler": {
        "functionName": "fulfill",
        "moduleName": "lockPaymentConditon",
        "version": "0.1"
      },
      "name": "Fulfilled"
    }
  ],
  "fulfillmentOrder": [
    "lockPayment.fulfill",
    "access.fulfill",
    "escrowPayment.fulfill"
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|conditionDependency|[[ConditionDependencyDto](#schemaconditiondependencydto)]|true|none|none|
|conditions|[[ConditionDto](#schemaconditiondto)]|true|none|Conditions|
|contractName|number|true|none|Contract Name|
|events|[[EventDto](#schemaeventdto)]|true|none|Events|
|fulfillmentOrder|string|false|none|Fulfillment order|

<h2 id="tocS_AttributesDto">AttributesDto</h2>
<!-- backwards compatibility -->
<a id="schemaattributesdto"></a>
<a id="schema_AttributesDto"></a>
<a id="tocSattributesdto"></a>
<a id="tocsattributesdto"></a>

```json
{
  "additionalInformation": {},
  "curation": {
    "numVotes": 123,
    "rating": 0.93,
    "schema": "Binary Voting",
    "isListed": false
  },
  "main": {
    "author": "Met Office",
    "dateCreated": "2021-02-01T10:55:11Z",
    "datePublished": "2021-02-01T10:55:11Z",
    "encryptedFiles": "0x098213xzckasdf089723hjgdasfkjgasfv",
    "files": [
      {
        "checksum": "efb2c764274b745f5fc37f97c6b0e761",
        "url": "https://raw.githubusercontent.com/tbertinmahieux/MSongsDB/master/Tasks_Demos/CoverSongs/shs_dataset_test.txt",
        "checksumType": "md5",
        "name": "data.txt",
        "compression": "zip",
        "contentLength": "4535431",
        "contentType": "text/csv",
        "encoding": "UTF-8",
        "index": 0,
        "resourceId": "access-log2018-02-13-15-17-29-18386C502CAEA932",
        "encrypted": false,
        "encryptionMode": "gpg"
      }
    ],
    "license": "CC-BY",
    "name": "UK Weather information 2011",
    "price": "10",
    "type": "dataset",
    "algorithm": {
      "language": "scala",
      "format": "docker-image",
      "version": "0.1",
      "container": [
        {
          "entrypoint": "node $ALGO",
          "image": "node",
          "tag": "10"
        }
      ]
    }
  },
  "serviceAgreementTemplate": {
    "conditionDependency": [
      {
        "access": [],
        "escrowPayment": [
          "lockPayment",
          "access"
        ],
        "execCompute": [],
        "lockPayment": []
      }
    ],
    "conditions": [
      {
        "contractName": "LockPaymentCondition",
        "functionName": "fulfill",
        "name": "lockPayment",
        "events": [
          {
            "actionType": "publisher",
            "handler": {
              "functionName": "fulfill",
              "moduleName": "lockPaymentConditon",
              "version": "0.1"
            },
            "name": "Fulfilled"
          }
        ],
        "parameters": [
          {
            "name": "_rewardAddress",
            "type": "address",
            "value": "0x886dE2b3F8F27eEd43bA2FD4bC2AabDc14E0d9dD"
          }
        ],
        "timelock": 0,
        "timeout": 0
      }
    ],
    "contractName": "EscrowAccessSecretStoreTemplate",
    "events": [
      {
        "actionType": "publisher",
        "handler": {
          "functionName": "fulfill",
          "moduleName": "lockPaymentConditon",
          "version": "0.1"
        },
        "name": "Fulfilled"
      }
    ],
    "fulfillmentOrder": [
      "lockPayment.fulfill",
      "access.fulfill",
      "escrowPayment.fulfill"
    ]
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|additionalInformation|object|false|none|Aditional information of the asset|
|curation|[CurationDto](#schemacurationdto)|true|none|popularity of the asset|
|main|[MainDto](#schemamaindto)|true|none|Main data of the asset|
|serviceAgreementTemplate|[ServiceAgreementTemplateDto](#schemaserviceagreementtemplatedto)|false|none|Service agreement template|

<h2 id="tocS_ServiceDto">ServiceDto</h2>
<!-- backwards compatibility -->
<a id="schemaservicedto"></a>
<a id="schema_ServiceDto"></a>
<a id="tocSservicedto"></a>
<a id="tocsservicedto"></a>

```json
{
  "index": 0,
  "serviceEndpoint": "http://localhost:8030/api/v1/gateway/services/consume",
  "type": "access",
  "service": "SecretStore",
  "purchaseEndpoint": "http://localhost:8030/api/v1/gateway/services/access/initialize",
  "attributes": {
    "additionalInformation": {},
    "curation": {
      "numVotes": 123,
      "rating": 0.93,
      "schema": "Binary Voting",
      "isListed": false
    },
    "main": {
      "author": "Met Office",
      "dateCreated": "2021-02-01T10:55:11Z",
      "datePublished": "2021-02-01T10:55:11Z",
      "encryptedFiles": "0x098213xzckasdf089723hjgdasfkjgasfv",
      "files": [
        {
          "checksum": "efb2c764274b745f5fc37f97c6b0e761",
          "url": "https://raw.githubusercontent.com/tbertinmahieux/MSongsDB/master/Tasks_Demos/CoverSongs/shs_dataset_test.txt",
          "checksumType": "md5",
          "name": "data.txt",
          "compression": "zip",
          "contentLength": "4535431",
          "contentType": "text/csv",
          "encoding": "UTF-8",
          "index": 0,
          "resourceId": "access-log2018-02-13-15-17-29-18386C502CAEA932",
          "encrypted": false,
          "encryptionMode": "gpg"
        }
      ],
      "license": "CC-BY",
      "name": "UK Weather information 2011",
      "price": "10",
      "type": "dataset",
      "algorithm": {
        "language": "scala",
        "format": "docker-image",
        "version": "0.1",
        "container": [
          {
            "entrypoint": "node $ALGO",
            "image": "node",
            "tag": "10"
          }
        ]
      }
    },
    "serviceAgreementTemplate": {
      "conditionDependency": [
        {
          "access": [],
          "escrowPayment": [
            "lockPayment",
            "access"
          ],
          "execCompute": [],
          "lockPayment": []
        }
      ],
      "conditions": [
        {
          "contractName": "LockPaymentCondition",
          "functionName": "fulfill",
          "name": "lockPayment",
          "events": [
            {
              "actionType": "publisher",
              "handler": {
                "functionName": "fulfill",
                "moduleName": "lockPaymentConditon",
                "version": "0.1"
              },
              "name": "Fulfilled"
            }
          ],
          "parameters": [
            {
              "name": "_rewardAddress",
              "type": "address",
              "value": "0x886dE2b3F8F27eEd43bA2FD4bC2AabDc14E0d9dD"
            }
          ],
          "timelock": 0,
          "timeout": 0
        }
      ],
      "contractName": "EscrowAccessSecretStoreTemplate",
      "events": [
        {
          "actionType": "publisher",
          "handler": {
            "functionName": "fulfill",
            "moduleName": "lockPaymentConditon",
            "version": "0.1"
          },
          "name": "Fulfilled"
        }
      ],
      "fulfillmentOrder": [
        "lockPayment.fulfill",
        "access.fulfill",
        "escrowPayment.fulfill"
      ]
    }
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|index|number|true|none|index of the service|
|serviceEndpoint|string|true|none|Url of the service endpoint|
|type|string|true|none|Service type|
|service|string|false|none|Service name|
|purchaseEndpoint|string|false|none|Url to purchase asset|
|attributes|[AttributesDto](#schemaattributesdto)|false|none|Attribute of the metadata|

<h2 id="tocS_CreateAssetDto">CreateAssetDto</h2>
<!-- backwards compatibility -->
<a id="schemacreateassetdto"></a>
<a id="schema_CreateAssetDto"></a>
<a id="tocScreateassetdto"></a>
<a id="tocscreateassetdto"></a>

```json
{
  "@context": "https://w3id.org/did/v1",
  "id": "did:nv:0c184915b07b44c888d468be85a9b28253e80070e5294b1aaed81c2f0264e429",
  "created": "2019-02-08T08:13:49Z",
  "updated": "2019-02-08T08:13:49Z",
  "authentication": [
    {
      "publicKey": "did:nv:0c184915b07b44c888d468be85a9b28253e80070e5294b1aaed81c2f0264e430",
      "type": "RsaSignatureAuthentication2018"
    }
  ],
  "proof": {
    "created": "2022-01-08T16:02:20Z",
    "creator": "2022-01-08T16:02:20Z",
    "signatureValue": "0xbd7b46b3ac664167bc70ac211b1a1da0baed9ead91613a5f02dfc25c1bb6e3ff40861b455017e8a587fd4e37b703436072598c3a81ec88be28bfe33b61554a471b",
    "type": "DDOIntegritySignature"
  },
  "publicKey": [
    {
      "id": "did:nv:0c184915b07b44c888d468be85a9b28253e80070e5294b1aaed81c2f0264e430",
      "owner": "0x00Bd138aBD70e2F00903268F3Db08f2D25677C9e",
      "type": "EthereumECDSAKey"
    }
  ],
  "service": [
    {
      "index": 0,
      "service": "SecretStore",
      "serviceEndpoint": "http://localhost:12001",
      "type": "authorization"
    },
    {
      "index": 1,
      "purchaseEndpoint": "http://localhost:8030/api/v1/gateway/services/access/initialize",
      "serviceEndpoint": "http://localhost:8030/api/v1/gateway/services/consume",
      "type": "access"
    },
    {
      "attributes": {
        "additionalInformation": {
          "copyrightHolder": "Met Office",
          "description": "Weather information of UK including temperature and humidity",
          "inLanguage": "en",
          "links": [
            {
              "name": "Sample of Asset Data",
              "type": "sample",
              "url": "https://foo.com/sample.csv"
            }
          ],
          "tags": [
            "weather",
            "uk",
            "2011",
            "temperature",
            "humidity"
          ],
          "workExample": "stationId,latitude,longitude,datetime, temperature,humidity/n423432fsd,51.509865,-0.118092, 2011-01-01T10:55:11+00:00,7.2,68"
        },
        "curation": {
          "numVotes": 123,
          "rating": 0.93,
          "schema": "Binary Voting"
        },
        "main": {
          "author": "Met Office",
          "dateCreated": "2012-02-01T10:55:11Z",
          "encryptedFiles": "0x098213xzckasdf089723hjgdasfkjgasfv",
          "files": [
            {
              "compression": "zip",
              "contentLength": "4535431",
              "contentType": "text/csv",
              "encoding": "UTF-8",
              "index": 0,
              "resourceId": "access-log2018-02-13-15-17-29-18386C502CAEA932"
            }
          ],
          "license": "CC-BY",
          "name": "UK Weather information 2011",
          "price": "10",
          "type": "dataset"
        }
      },
      "index": 2,
      "serviceEndpoint": "http://mymetadata.org/api/v1/provider/assets/metadata/did:nv:0c184915b07b44c888d468be85a9b28253e80070e5294b1aaed81c2f0264e430",
      "type": "metadata"
    }
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|@context|string|true|none|Context of the asset|
|id|string|true|none|ID of the asset|
|created|string|false|none|ID of the asset|
|updated|string|false|none|ID of the asset|
|authentication|[[AuthenticationDto](#schemaauthenticationdto)]|true|none|Authentication used in the asset|
|proof|[ProofDto](#schemaproofdto)|true|none|Proof data|
|publicKey|[[PublicKeyDto](#schemapublickeydto)]|true|none|Public keys that contains the asset|
|service|[[ServiceDto](#schemaservicedto)]|true|none|Services that contains the asset|

<h2 id="tocS_GetAssetDto">GetAssetDto</h2>
<!-- backwards compatibility -->
<a id="schemagetassetdto"></a>
<a id="schema_GetAssetDto"></a>
<a id="tocSgetassetdto"></a>
<a id="tocsgetassetdto"></a>

```json
{
  "@context": "https://w3id.org/did/v1",
  "authentication": [
    {
      "publicKey": "did:nv:0c184915b07b44c888d468be85a9b28253e80070e5294b1aaed81c2f0264e430",
      "type": "RsaSignatureAuthentication2018"
    }
  ],
  "created": "2021-02-01T10:55:11Z",
  "updated": "2021-02-01T10:55:11Z",
  "id": "did:nv:0c184915b07b44c888d468be85a9b28253e80070e5294b1aaed81c2f0264e429",
  "proof": {
    "created": "2022-01-08T16:02:20Z",
    "creator": "2022-01-08T16:02:20Z",
    "signatureValue": "0xbd7b46b3ac664167bc70ac211b1a1da0baed9ead91613a5f02dfc25c1bb6e3ff40861b455017e8a587fd4e37b703436072598c3a81ec88be28bfe33b61554a471b",
    "type": "DDOIntegritySignature"
  },
  "publicKey": [
    {
      "id": "did:nv:0c184915b07b44c888d468be85a9b28253e80070e5294b1aaed81c2f0264e430",
      "owner": "0x00Bd138aBD70e2F00903268F3Db08f2D25677C9e",
      "type": "EthereumECDSAKey"
    }
  ],
  "service": [
    {
      "index": 0,
      "service": "SecretStore",
      "serviceEndpoint": "http://localhost:12001",
      "type": "authorization"
    },
    {
      "index": 1,
      "purchaseEndpoint": "http://localhost:8030/api/v1/gateway/services/access/initialize",
      "serviceEndpoint": "http://localhost:8030/api/v1/gateway/services/consume",
      "type": "access"
    },
    {
      "attributes": {
        "additionalInformation": {
          "copyrightHolder": "Met Office",
          "description": "Weather information of UK including temperature and humidity",
          "inLanguage": "en",
          "links": [
            {
              "name": "Sample of Asset Data",
              "type": "sample",
              "url": "https://foo.com/sample.csv"
            }
          ],
          "tags": [
            "weather",
            "uk",
            "2011",
            "temperature",
            "humidity"
          ],
          "workExample": "stationId,latitude,longitude,datetime, temperature,humidity/n423432fsd,51.509865,-0.118092, 2011-01-01T10:55:11+00:00,7.2,68"
        },
        "curation": {
          "numVotes": 123,
          "rating": 0.93,
          "schema": "Binary Voting"
        },
        "main": {
          "author": "Met Office",
          "dateCreated": "2012-02-01T10:55:11Z",
          "encryptedFiles": "0x098213xzckasdf089723hjgdasfkjgasfv",
          "files": [
            {
              "compression": "zip",
              "contentLength": "4535431",
              "contentType": "text/csv",
              "encoding": "UTF-8",
              "index": 0,
              "resourceId": "access-log2018-02-13-15-17-29-18386C502CAEA932"
            }
          ],
          "license": "CC-BY",
          "name": "UK Weather information 2011",
          "price": "10",
          "type": "dataset"
        }
      },
      "index": 2,
      "serviceEndpoint": "http://mymetadata.org/api/v1/provider/assets/metadata/did:nv:0c184915b07b44c888d468be85a9b28253e80070e5294b1aaed81c2f0264e430",
      "type": "metadata"
    }
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|@context|string|true|none|Context of the asset|
|authentication|[[AuthenticationDto](#schemaauthenticationdto)]|true|none|Authentication used in the asset|
|created|string|true|none|Date when the asset is created|
|updated|string|true|none|Date when the asset is created|
|id|string|true|none|ID of the asset|
|proof|[ProofDto](#schemaproofdto)|true|none|Proof data|
|publicKey|[[PublicKeyDto](#schemapublickeydto)]|true|none|Public keys that contains the asset|
|service|[[ServiceDto](#schemaservicedto)]|true|none|Services that contains the asset|

<h2 id="tocS_QueryBodyDDOdto">QueryBodyDDOdto</h2>
<!-- backwards compatibility -->
<a id="schemaquerybodyddodto"></a>
<a id="schema_QueryBodyDDOdto"></a>
<a id="tocSquerybodyddodto"></a>
<a id="tocsquerybodyddodto"></a>

```json
{
  "query": {
    "match_all": {}
  },
  "text": "Eius vel alias.",
  "offset": 100,
  "page": 0,
  "sort": {
    "created": "asc"
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|query|object|false|none|execute directly queries to elasticsearch from the client|
|text|string|false|none|Text to search|
|offset|string|false|none|Page Size|
|page|string|false|none|Page to retrieve|
|sort|object|false|none|sort the response by specified parameter|

<h2 id="tocS_UpdateAssetDto">UpdateAssetDto</h2>
<!-- backwards compatibility -->
<a id="schemaupdateassetdto"></a>
<a id="schema_UpdateAssetDto"></a>
<a id="tocSupdateassetdto"></a>
<a id="tocsupdateassetdto"></a>

```json
{
  "@context": "https://w3id.org/did/v1",
  "updated": "2019-02-08T08:13:49Z",
  "authentication": [
    {
      "publicKey": "did:nv:0c184915b07b44c888d468be85a9b28253e80070e5294b1aaed81c2f0264e430",
      "type": "RsaSignatureAuthentication2018"
    }
  ],
  "proof": {
    "created": "2022-01-08T16:02:20Z",
    "creator": "2022-01-08T16:02:20Z",
    "signatureValue": "0xbd7b46b3ac664167bc70ac211b1a1da0baed9ead91613a5f02dfc25c1bb6e3ff40861b455017e8a587fd4e37b703436072598c3a81ec88be28bfe33b61554a471b",
    "type": "DDOIntegritySignature"
  },
  "publicKey": [
    {
      "id": "did:nv:0c184915b07b44c888d468be85a9b28253e80070e5294b1aaed81c2f0264e430",
      "owner": "0x00Bd138aBD70e2F00903268F3Db08f2D25677C9e",
      "type": "EthereumECDSAKey"
    }
  ],
  "service": [
    {
      "index": 0,
      "service": "SecretStore",
      "serviceEndpoint": "http://localhost:12001",
      "type": "authorization"
    },
    {
      "index": 1,
      "purchaseEndpoint": "http://localhost:8030/api/v1/gateway/services/access/initialize",
      "serviceEndpoint": "http://localhost:8030/api/v1/gateway/services/consume",
      "type": "access"
    },
    {
      "attributes": {
        "additionalInformation": {
          "copyrightHolder": "Met Office",
          "description": "Weather information of UK including temperature and humidity",
          "inLanguage": "en",
          "links": [
            {
              "name": "Sample of Asset Data",
              "type": "sample",
              "url": "https://foo.com/sample.csv"
            }
          ],
          "tags": [
            "weather",
            "uk",
            "2011",
            "temperature",
            "humidity"
          ],
          "workExample": "stationId,latitude,longitude,datetime, temperature,humidity/n423432fsd,51.509865,-0.118092, 2011-01-01T10:55:11+00:00,7.2,68"
        },
        "curation": {
          "numVotes": 123,
          "rating": 0.93,
          "schema": "Binary Voting"
        },
        "main": {
          "author": "Met Office",
          "dateCreated": "2012-02-01T10:55:11Z",
          "encryptedFiles": "0x098213xzckasdf089723hjgdasfkjgasfv",
          "files": [
            {
              "compression": "zip",
              "contentLength": "4535431",
              "contentType": "text/csv",
              "encoding": "UTF-8",
              "index": 0,
              "resourceId": "access-log2018-02-13-15-17-29-18386C502CAEA932"
            }
          ],
          "license": "CC-BY",
          "name": "UK Weather information 2011",
          "price": "10",
          "type": "dataset"
        }
      },
      "index": 2,
      "serviceEndpoint": "http://mymetadata.org/api/v1/provider/assets/metadata/did:nv:0c184915b07b44c888d468be85a9b28253e80070e5294b1aaed81c2f0264e430",
      "type": "metadata"
    }
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|@context|string|true|none|Context of the asset|
|updated|string|false|none|ID of the asset|
|authentication|[[AuthenticationDto](#schemaauthenticationdto)]|true|none|Authentication used in the asset|
|proof|[ProofDto](#schemaproofdto)|true|none|Proof data|
|publicKey|[[PublicKeyDto](#schemapublickeydto)]|true|none|Public keys that contains the asset|
|service|[[ServiceDto](#schemaservicedto)]|true|none|Services that contains the asset|

<h2 id="tocS_CreateBookmarkDto">CreateBookmarkDto</h2>
<!-- backwards compatibility -->
<a id="schemacreatebookmarkdto"></a>
<a id="schema_CreateBookmarkDto"></a>
<a id="tocScreatebookmarkdto"></a>
<a id="tocscreatebookmarkdto"></a>

```json
{
  "did": "did:12345",
  "userId": "u-12345",
  "description": "I am interesting in this asset"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|did|string|true|none|The identifier of the asset|
|userId|string|true|none|The userId who created the bookmark|
|description|string|true|none|Description given by the user|

<h2 id="tocS_GetBookmarkDto">GetBookmarkDto</h2>
<!-- backwards compatibility -->
<a id="schemagetbookmarkdto"></a>
<a id="schema_GetBookmarkDto"></a>
<a id="tocSgetbookmarkdto"></a>
<a id="tocsgetbookmarkdto"></a>

```json
{
  "id": "b-123434",
  "did": "did:12345",
  "userId": "u-12345",
  "description": "I am interesting in this asset",
  "createdAt": "2022-03-18T13:44:00.931Z"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string|true|none|The identifier of the bookmark|
|did|string|true|none|The identifier of the asset|
|userId|string|true|none|The userId who created the bookmark|
|description|string|true|none|Description given by the user|
|createdAt|string(date-time)|true|none|When the UGC was created|

<h2 id="tocS_UpdateBookmarkDto">UpdateBookmarkDto</h2>
<!-- backwards compatibility -->
<a id="schemaupdatebookmarkdto"></a>
<a id="schema_UpdateBookmarkDto"></a>
<a id="tocSupdatebookmarkdto"></a>
<a id="tocsupdatebookmarkdto"></a>

```json
{
  "description": "I am interesting in this asset"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|description|string|true|none|Description given by the user|

