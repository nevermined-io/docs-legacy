# COMPUTE FL: Nevermined Federated Learning Orchestration

```
shortname:      FL
name:           Nevermined Federated Learning Orchestration
type:           Draft
status:         Valid
version:        0.1
editor:         Rodolphe Marques <rodolphe@keyko.io>
contributors:   Aitor Argomaniz <aitor@keyko.io>,
                Enrique Ruiz <kike@keyko.io>
```


* [COMPUTE FL: Nevermined Federated Learning Orchestration](#compute-fl-nevermined-federated-learning-orchestration)
   * [Federated Learning integration in the Nevermined Data in Situ Computation](#federated-learning-integration-in-the-nevermined-data-in-situ-computation)
   * [Terminology](#terminology)
   * [Motivation](#motivation)
   * [Actors](#actors)
   * [Architecture](#architecture)
      * [Running the Coordinator](#running-the-coordinator)
      * [Flow](#flow)
      * [Running the Participants](#running-the-participants)
      * [Flow](#flow-1)
   * [Federated Learning Session Flow](#federated-learning-session-flow)
   * [Federated Learning DDOs](#federated-learning-ddos)
      * [Coordinator Consumer DDO](#coordinator-consumer-ddo)
      * [Coordinator Provider DDO](#coordinator-provider-ddo)
      * [Participant Consumer DDO](#participant-consumer-ddo)
      * [Participant Provider DDO](#participant-provider-ddo)



---


## Federated Learning integration in the Nevermined Data in Situ Computation

This SPEC introduces the integration pattern for the usage a Federated Learning
backend in the [Nevermined DISC architecture](architecture/specs/compute/README.md).

The Nevermined Data in Situ Computation solution introduces a solution where
different compute backends can be plugged in order to support different remote
computation use cases.   

This spec details how Federated Learning sessions could be executed on
Nevermined.


## Terminology

* **Coordinator**: All the components required to perform the coordination of a
  Federated Learning session. The components provided by the
  [xain-fl](https://github.com/keyko-io/xain-fl) framework (coordinator +
    aggregator)
* **Participant**: Component responsible for interacting with the coordinator
  and executing the machine learning task over the data.
* **Federated Learning Session**: The time from setup of the coordinator to the
  successful execution of the machine learning plan. Typically this involves
  coordinating the participants for a finite number or rounds and then storing
  the resulting model


## Motivation

The main motivations of this SPEC are:

* Identify the actors involved in the execution of a Federated Learning session
  on Nevermined
* Identify the integration points between the xain framework components and the
  Nevermined components
* Detail the execution flow of a Federated Learning session on Nevermined


## Actors

The different actors interacting in this flow are:

* PROVIDERS: Give access to the Compute Services and to the data
* CONSUMERS: Want to make use of the Compute Services and access to data
* MARKETPLACE or DOMAINS: Store the DDO/Metadata related to the Assets/services
* INFRASTRUCTURE: Infrastructure required to run the Nevermined compute stack

Here we may have two types of providers. A normal provider like the one
specified in Data in Situ Computation spec. And another type of provider that only
provides compute but now access to the data (to run the coordinator).

## Architecture

### Running the Coordinator

This section details how a Client/Data Scientist can setup and run a Coordinator
 using Nevermined Compute.

The main requirements are:

* A COMPUTE PROVIDER or PROVIDER defines the conditions that a Compute service
supports. It includes:
  - What kind of image (Docker container) can be deployed in the infrastructure
  - What are the infrastructure resources available (CPU, memory, storage)
  - What is the price of using the infrastructure resources
  - Allow incoming connections for the Participants
* A COMSUMER defines the parameters of the coordinator and creates an execution
  workflow using a predefined coordinator workflow template
  - This is a different type of workflow with no inputs, outputs and access to
  data
* A CONSUMER purchasing a compute service defines which Workflow (DID) is going
to execute


![Setting up the Coordinator](images/fl-setting-up-coordinator.png)


### Flow

1. The CONSUMER / Data Scientist locks the payment for the service
1. The CONSUMER / Data scientist provides a DID for the workflow to execute
   - The gateway could potentially provide specific endpoints for this since the
   workflow is always the same. The only thing that changes is the parameters to
    configure the coordinator
1. The Gateway checks if the CONSUMER / Data scientist as the permissions to
  start a new coordinator
1. The Nevermined compute stack starts a new coordinator
1. The url to connect to the coordinator is published (need to figure out how)
1. In the meantime participants will connect to the coordinator and the coordinator will orchestrate the Federated Learning session
1. After the Federated Learning session is finished the coordinator publishes the resulting trained model and shuts down.


### Running the Participants

This section details how a Client/Data Scientist can setup and run a set of
Participants using Nevermined Compute.

This should be simpler to integrate because it’s very similar to the data in
situ computation use case. The main difference being that the algorithm is actually
wrapped around the xain python sdk and it needs to be able to perform outgoing
network connection to connect to the coordinator.


The main requirements are:

* A PROVIDER defines the conditions that a Compute service supports. It includes:
  - What kind of image (Docker container) can be deployed in the infrastructure
  - What are the infrastructure resources available (CPU, memory, storage)
  - What is the price of using the infrastructure resources
* A COMPUTE PROVIDER defines a Compute Service in the scope of the Asset
  (DID/DDO) of the dataset that can be computed
* A CONSUMER defines the task to execute modeling it in a Workflow (including
  configuration, input, participant)
* In this case the transformation is just the participant code
* It does not need to produce any output since that is handled by the
  coordinator
* A workflow is a new type of Asset. It can be resolvable and be used across
  multiple independent compute services
* A CONSUMER purchasing a compute service defines which Workflow (DID) is going
  to execute


![Running the participants](images/fl-running-participants.png)


### Flow

1. The CONSUMER / Data Scientist locks the payment
1. The CONSUMER / Data Scientist requests the execution of the participant
1. The Gateway checks if the CONSUMER / Data Scientist has the permissions to
   execute the participant on the data
1. The Nevermined compute sets up the environment
1. The participants access the data and performs the machine learning task
1. The participant needs to be able to communicate with the coordinator
   throughout the entire Federated Learning session.
1. The coordinator will be external to the Infrastructure Provider
1. The participant does not need to create a new asset since that is handled by
   the coordinator


## Federated Learning Session Flow

This section details a high level overview of a Federated Learning Session using
 two different data providers.

 ![Federated Learning Session Flow](images/fl-high-level-flow.png)


The Data Scientist starts by finding a provider to run the Coordinator compute
job and the data that it requires (possibly using the marketplace).

The flow is:

1. The Data Scientist starts by setting the execution parameters for the coordinator and publishes it as a workflow/ddo
1. The Data Scientist purchases data in situ computation for both Data Provider X and Y and defines the workflow/ddo with the code that will run the participants
1. The Data Scientist purchases the Coordinator compute service
1. The Data Scientist starts the Coordinator
1. The Data Scientist starts the participants
1. The Participants work together with the coordinator over the course of multiple rounds as defined in point 1.
1. Once all rounds are finished the Coordinator publishes the final trained model
1. The Data Scientist fetches the trained model.


## Federated Learning DDOs

This section details the both the consumer and provider DDOs for coordinator
and participant.


### Coordinator Consumer DDO

```json
{
  "serviceAgreementId": "bb23s87856d59867503f80a690357406857698570b964ac8dcc9d86da4ada010",
  "workflow": {
    "@context": "https://w3id.org/future-method/v1",
    "authentication": [],
    "created": "2019-04-09T19:02:11Z",
    "id": "did:nv:8d1b4d73e7af4634958f071ab8dfe7ab0df14019755e444090fd392c8ec9c3f4",
    "proof": {
      "created": "2019-04-09T19:02:11Z",
      "creator": "0x00Bd138aBD70e2F00903268F3Db08f2D25677C9e",
      "signatureValue": "1cd57300733bcbcda0beb59b3e076de6419c0d7674e7befb77820b53c79e3aa8f1776effc64cf088bad8cb694cc4d71ebd74a13b2f75893df5a53f3f318f6cf828",
      "type": "DDOIntegritySignature"
    },
    "publicKey": [
      {
        "id": "did:nv:8d1b4d73e7af4634958f071ab8dfe7ab0df14019755e444090fd392c8ec9c3f4",
        "owner": "0x00Bd138aBD70e2F00903268F3Db08f2D25677C9e",
        "type": "EthereumECDSAKey"
      }
    ],
    "service": [
      {
        "index": 0,
        "serviceEndpoint": "http://172.15.0.15:5000/api/v1/metadata/assets/ddo/did:nv:8d1b4d73e7af4634958f071ab8dfe7ab0df14019755e444090fd392c8ec9c3f4",
        "type": "metadata",
        "attributes": {
          "main": {
            "dateCreated": "2012-10-10T17:00:00Z",
            "type": "fl-coordinator",
            "datePublished": "2019-04-09T19:02:11Z",
            "parameters": {
              "minParticipants": 1,
              "participantsRatio": 1,
              "rounds": 10,
            }
            "workflow": {
              "stages": [
                {
                  "index": 0,
                  "requirements": {
                    "serverInstances": 1,
                    "container": {
                      "image": "keykoio/xain-fl",
                      "tag": "latest",
                      "checksum": "sha256:cb57ecfa6ebbefd8ffc7f75c0f00e57a7fa739578a429b6f72a0df19315deadc"
                    }
                  }
                }
              ]
            }
          }
        }
      }
    ]
  }
}
```

The main information that needs to be provided is:
- `tag`: The version of the `xain-fl` image to use
- `minParticipants`: The minimum number of participants required by the
  coordinator
- `participantsRation`: The ratio of participants that will be selected in
  every round
- `rounds`: The number of rounds the coordinator should do

> Note that `service.main.type` is set to `fl-coordinator` to indicate this is
> not a normal workflow

### Coordinator Provider DDO

```json
{
  "@context": "https://w3id.org/future-method/v1",
  "authentication": [],
  "created": "2019-04-09T19:02:11Z",
  "id": "did:op:8d1b4d73e7af4634958f071ab8dfe7ab0df14019755e444090fd392c8ec9c3f4",
  "proof": {
    "created": "2019-04-09T19:02:11Z",
    "creator": "0x00Bd138aBD70e2F00903268F3Db08f2D25677C9e",
    "signatureValue": "1cd57300733bcbcda0beb59b3e076de6419c0d7674e7befb77820b53c79e3aa8f1776effc64cf088bad8cb694cc4d71ebd74a13b2f75893df5a53f3f318f6cf828",
    "type": "DDOIntegritySignature"
  },
  "publicKey": [
    {
      "id": "did:op:8d1b4d73e7af4634958f071ab8dfe7ab0df14019755e444090fd392c8ec9c3f4",
      "owner": "0x00Bd138aBD70e2F00903268F3Db08f2D25677C9e",
      "type": "EthereumECDSAKey"
    }
  ],
  "service": [
    {
      "type": "metadata",
      "index": 0,
      "serviceEndpoint": "http://mymetadata-api.org/api/v1/metadata/assets/ddo/{did}",
      "attributes": {
        "main": {},
        "additionalInformation": {}
      }
    },
    {
      "type": "fl-coordinator",
      "index": 2,
      "serviceEndpoint": "http://mygateway.org/api/v1/gateway/services/execute",
      "templateId": "804932804923850985093485039850349850439583409583404534231321131a",
      "attributes": {
        "main": {
          "creator": "0x00Bd138aBD70e2F00903268F3Db08f2D25677C9e",
          "datePublished": "2019-04-09T19:02:11Z",
          "price": "10",
          "timeout": 86400,
          "provider": {
            "type": "Azure",
            "description": "",
            "environment": {
              "cluster": {
                "type": "Kubernetes",
                "url": "http://10.0.0.17/xxx"
              },
              "supportedContainers": [
                {
                  "image": "keykoio/xain-fl",
                  "tag": "latest",
                  "checksum": "sha256:cb57ecfa6ebbefd8ffc7f75c0f00e57a7fa739578a429b6f72a0df19315deadc"
                },
                {
                  "image": "keykoio/xain-fl",
                  "tag": "v1",
                  "checksum": "sha256:cb57ecfa6ebbefd8ffc7f75c0f00e57a7fa739578a429b6f72a0df19315deadc"
                }
              ],
              "supportedServers": [
                {
                  "serverId": "1",
                  "serverType": "xlsize",
                  "price": "50",
                  "cpu": "16",
                  "gpu": "0",
                  "memory": "128gb",
                  "disk": "160gb",
                  "maxExecutionTime": 86400
                },
                {
                  "serverId": "2",
                  "serverType": "medium",
                  "price": "10",
                  "cpu": "2",
                  "gpu": "0",
                  "memory": "8gb",
                  "disk": "80gb",
                  "maxExecutionTime": 86400
                }
              ]
            }
          }
        },
        "additionalInformation": {}
      },
      "serviceAgreementTemplate": {
        "contractName": "ServiceExecutionTemplate",
        "events": [
          {
            "name": "AgreementCreated",
            "actorType": "consumer",
            "handler": {
              "moduleName": "serviceExecutionTemplate",
              "functionName": "fulfillLockRewardCondition",
              "version": "0.1"
            }
          }
        ],
        "fulfillmentOrder": [
          "lockReward.fulfill",
          "serviceExecution.fulfill",
          "escrowReward.fulfill"
        ],
        "conditionDependency": {
          "lockReward": [],
          "serviceExecution": [],
          "releaseReward": [
            "lockReward",
            "serviceExecution"
          ]
        },
        "conditions": [
          {
            "name": "lockReward",
            "timelock": 0,
            "timeout": 0,
            "contractName": "LockRewardCondition",
            "functionName": "fulfill",
            "parameters": [
              {
                "name": "_rewardAddress",
                "type": "address",
                "value": ""
              },
              {
                "name": "_amount",
                "type": "uint256",
                "value": ""
              }
            ],
            "events": [
              {
                "name": "Fulfilled",
                "actorType": "publisher",
                "handler": {
                  "moduleName": "lockRewardCondition",
                  "functionName": "fulfillServiceExecutionCondition",
                  "version": "0.1"
                }
              }
            ]
          },
          {
            "name": "execCompute",
            "timelock": 0,
            "timeout": 0,
            "contractName": "ComputeExecutionCondition",
            "functionName": "fulfill",
            "parameters": [
              {
                "name": "_documentId",
                "type": "bytes32",
                "value": ""
              },
              {
                "name": "_grantee",
                "type": "address",
                "value": ""
              }
            ],
            "events": [
              {
                "name": "Fulfilled",
                "actorType": "publisher",
                "handler": {
                  "moduleName": "execCompute",
                  "functionName": "fulfillServiceExecutionCondition",
                  "version": "0.1"
                }
              },
              {
                "name": "TimedOut",
                "actorType": "consumer",
                "handler": {
                  "moduleName": "execCompute",
                  "functionName": "fulfillServiceExecutionCondition",
                  "version": "0.1"
                }
              }
            ]
          },
          {
            "name": "escrowReward",
            "timelock": 0,
            "timeout": 0,
            "contractName": "EscrowReward",
            "functionName": "fulfill",
            "parameters": [
              {
                "name": "_amount",
                "type": "uint256",
                "value": ""
              },
              {
                "name": "_receiver",
                "type": "address",
                "value": ""
              },
              {
                "name": "_sender",
                "type": "address",
                "value": ""
              },
              {
                "name": "_lockCondition",
                "type": "bytes32",
                "value": ""
              },
              {
                "name": "_releaseCondition",
                "type": "bytes32",
                "value": ""
              }
            ],
            "events": [
              {
                "name": "Fulfilled",
                "actorType": "publisher",
                "handler": {
                  "moduleName": "escrowRewardCondition",
                  "functionName": "verifyRewardTokens",
                  "version": "0.1"
                }
              }
            ]
          }
        ]
      }
    }
  ]
}
```

### Participant Consumer DDO

```json
{
  "serviceAgreementId": "bb23s87856d59867503f80a690357406857698570b964ac8dcc9d86da4ada010",
  "workflow": {
    "@context": "https://w3id.org/did/v1",
    "authentication": [
      {
        "type": "RsaSignatureAuthentication2018",
        "publicKey": "did:nv:0ebed8226ada17fde24b6bf2b95d27f8f05fcce09139ff5cec31f6d81a7cd2ea"
      }
    ],
    "created": "2019-02-08T08:13:49Z",
    "updated": "2019-06-30T14:53:09Z",
    "id": "did:nv:0bc278fee025464f8012b811d1bce8e22094d0984e4e49139df5d5ff7a028bdf",
    "proof": {
      "created": "2019-02-08T08:13:41Z",
      "creator": "0x37BB53e3d293494DE59fBe1FF78500423dcFd43B",
      "signatureValue": "did:nv:0bc278fee025464f8012b811d1bce8e22094d0984e4e49139df5d5ff7a028bdf",
      "type": "DDOIntegritySignature",
      "checksum": {
        "0": "0x52b5c93b82dd9e7ecc3d9fdf4755f7f69a54484941897dc517b4adfe3bbc3377",
        "1": "0x999999952b5c93b82dd9e7ecc3d9fdf4755f7f69a54484941897dc517b4adfe3"
      }
    },
    "publicKey": [
      {
        "id": "did:nv:b6e2eb5eff1a093ced9826315d5a4ef6c5b5c8bd3c49890ee284231d7e1d0aaa#keys-1",
        "type": "RsaVerificationKey2018",
        "owner": "did:nv:6027c1e7cbae06a91fce0557ee53195284825f56a7100be0c53cbf4391aa26cc",
        "publicKeyPem": "-----BEGIN PUBLIC KEY...END PUBLIC KEY-----\r\n"
      },
      {
        "id": "did:nv:b6e2eb5eff1a093ced9826315d5a4ef6c5b5c8bd3c49890ee284231d7e1d0aaa#keys-2",
        "type": "Ed25519VerificationKey2018",
        "owner": "did:nv:4c27a254e607cdf91a1206480e7eb8c74856102316c1a462277d4f21c02373b6",
        "publicKeyBase58": "H3C2AVvLMv6gmMNam3uVAjZpfkcJCwDwnZn6z3wXmqPV"
      },
      {
        "id": "did:nv:b6e2eb5eff1a093ced9826315d5a4ef6c5b5c8bd3c49890ee284231d7e1d0aaa#keys-3",
        "type": "RsaPublicKeyExchangeKey2018",
        "owner": "did:nv:5f6b885202ffb9643874be529302eb00d55e226959f1fbacaeda592c5b5c9484",
        "publicKeyPem": "-----BEGIN PUBLIC KEY...END PUBLIC KEY-----\r\n"
      }
    ],
    "verifiableCredential": [
      {
        "@context": [
          "https://www.w3.org/2018/credentials/v1",
          "https://www.w3.org/2018/credentials/examples/v1"
        ],
        "id": "1872",
        "type": [
          "read",
          "update",
          "deactivate"
        ],
        "issuer": "0x610D9314EDF2ced7681BA1633C33fdb8cF365a12",
        "issuanceDate": "2019-01-01T19:73:24Z",
        "credentialSubject": {
          "id": "0x89328493849328493284932"
        },
        "proof": {
          "type": "RsaSignature2018",
          "created": "2019-01-01T19:73:24Z",
          "proofPurpose": "assertionMethod",
          "signatureValue": "ABCJSDAO23...1tzjn4w=="
        }
      }
    ],
    "service": [
      {
        "index": 0,
        "serviceEndpoint": "http://localhost:5000/api/v1/metadata/assets/ddo/{did}",
        "type": "metadata",
        "attributes": {
          "main": {
            "author": "John Doe",
            "checksum": "0x52b5c93b82dd9e7ecc3d9fdf4755f7f69a54484941897dc517b4adfe3bbc3377",
            "dateCreated": "2019-02-08T08:13:49Z",
            "datePublished": "2019-05-08T08:13:49Z",
            "license": "CC-BY",
            "name": "My workflow",
            "price": "1",
            "type": "workflow",
            "workflow": {
              "stages": [
                {
                  "index": 0,
                  "stageType": "Participant",
                  "requirements": {
                    "container": {
                      "image": "keykoio/xain-participant",
                      "tag": "latest",
                      "checksum": "sha256:cb57ecfa6ebbefd8ffc7f75c0f00e57a7fa739578a429b6f72a0df19315deadc"
                    }
                  },
                  "input": [
                    {
                      "index": 0,
                      "id": "did:nv:12345"
                    }
                  ],
                  "transformation": {
                    "id": "did:nv:abcde"
                  },
                  "output": {
                  }
                }
              ]
            }
          },
          "additionalInformation": {
            "description": "Workflow to aggregate weather information",
            "tags": [
              "weather",
              "uk",
              "2011",
              "workflow",
              "aggregation"
            ],
            "copyrightHolder": "John Doe"
          }
        }
      }
    ]
  }
}
```

This is a normal data in situ computation workflow with one stage, a set of inputs,
one transformation and no output since the participant shouldn't need to
generate any data.

### Participant Provider DDO
