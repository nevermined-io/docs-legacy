# Secret Store API Reference

Nevermined integrates the Parity Secret Store to support use cases with high
security requirements for the secret management. These secrets are being used
for the encryption and distributed decryption of the access information to user
assets. This module allows the multiparty encryption and decryption of secrets via
Secret Store integration.

The main functions are:

## Encrypt

 Encrypts a document using Secret Store. Parameters:

 * `documentId` the id of the document to encrypt, typically a DID
 * `content` the content to encrypt. It can be any kind of string content
 * `threshold` the minimum number of Secret Store nodes that should build a quorum for decrypting a secret

Example:

```java
String encryptedContent = encrypt("did:nv:1234", "my secret", 3)
```


## Decrypt

Decrypts a document using Secret Store. Parameters:

* `documentId` the id of the document to encrypt, typically a DID
* `encryptedContent` the content to decrypt.

Example:

```java
String decryptedContent = decrypt("did:nv:1234", "0358920a932854984293")
```
