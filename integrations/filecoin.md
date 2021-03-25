# Filecoin Integration

- `POWERGATE_TOKEN`

If the `POWERGATE_TOKEN` env is not set the [filecoin driver](https://github.com/nevermined-io/metadata-driver-filecoin) will create one on the fly.

In certain situations if we try to submit a file to filecoin immediately after creating a new powergate token we may end up in a situation where powergate tries to fund the new address without this address being available yet in which case a job may fail with:

```bash
$ pow storage-jobs list -t 0815dd75-d6cb-4a1a-a77a-7d04b415f5e7
{
  "storageJobs": [
    {
      "id": "8500bf4c-a147-494b-8684-38b318e37152",
      "apiId": "d31a94c4-888e-4f61-8b35-f28881ca7778",
      "cid": "QmaY4mQdPM57zqhZA42yWD1BoiYuRb7DGgHt9XocBDSi1Y",
      "status": "JOB_STATUS_FAILED",
      "errorCause": "executing cold-storage config: all started deals failed",
      "dealInfo": [
        {
          "proposalCid": "bafyreiegd5fd7jpex3gnwbifp3egfahzzuu6bdrw7emktcgwcpm74y3yuu",
          "stateId": "26",
          "stateName": "StorageDealError",
          "miner": "f01000",
          "pieceCid": "baga6ea4seaqal4sh4be7shoqrqfqgjtladj6oii2wniat3gy7ygg65h5fqmkahi",
          "size": "65024",
          "pricePerEpoch": "30517",
          "startEpoch": "0",
          "duration": "521888",
          "dealId": "0",
          "activationEpoch": "0",
          "message": "adding market funds failed: resolve address f3qdva2mds3wmdhercoz6nfyrbwftbxwcbfduvh2ckc7i36zhaawvyvp7zhqzqoad4v7xop4eldkykodoolyoq: actor not found"
        }
      ],
      "dealErrors": [
        {
          "proposalCid": "bafyreiegd5fd7jpex3gnwbifp3egfahzzuu6bdrw7emktcgwcpm74y3yuu",
          "miner": "f01000",
          "message": "adding market funds failed: resolve address f3qdva2mds3wmdhercoz6nfyrbwftbxwcbfduvh2ckc7i36zhaawvyvp7zhqzqoad4v7xop4eldkykodoolyoq: actor not found"
        }
      ],
      "createdAt": "1616609250"
    }
  ],
  "more": false,
  "nextPageToken": ""
}
```

To avoid this scenario is always safer to create a new powergate user and start the nevermined gateway with the `POWERGATE_TOKEN` env set.