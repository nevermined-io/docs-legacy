---
sidebar_position: 1
---

# Getting Started

This section provides information about how to get started with the Nevermined Components Catalog.

## Pre-requisites

The Nevermined Components Catalog is a package built with React and Typescript.
It requires [Node JS](https://nodejs.org/) v14 or higher. You can find online instructions about [How to install Node JS](https://nodejs.dev/learn/how-to-install-nodejs).

## How to install ?

```
yarn add @nevermined-io/components-catalog
or
npm install --save @nevermined-io/components-catalog
```

## How to integrate ?
```typescript
import Catalog from '@nevermined-io/components-catalog';
import App from 'app';
import { Config } from '@nevermined-io/nevermined-sdk-js';

const appConfig: Config = {
  web3Provider: new Web3(window.ethereum),
  nodeUri,
  gatewayUri,
  faucetUri,
  verbose,
  gatewayAddress,
  secretStoreUri,
  graphHttpUri,
  marketplaceAuthToken,
  marketplaceUri,
  artifactsFolder
};

ReactDOM.render(
  <div>
    <Catalog.NeverminedProvider config={appConfig}>
      <App />
    </Catalog.NeverminedProvider>
  </div>,
  document.getElementById('root') as HTMLElement
);
```

## How to use ?

```typescript
const SingleAsset = () => {
  const did = 'did:nv:f8a00...';
  const assetData: AssetState = Catalog.useAsset(did);

  return (
    <>
      <div>Asset {did}:</div>
      <div>{JSON.stringify(assetData.ddo)}</div>
    </>
  );
};

```

For a full [example](https://github.com/nevermined-io/components-catalog/tree/main/example).
