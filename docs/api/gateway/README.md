# Nevermined Gateway

The [Nevermined Gateway](https://github.com/nevermined-io/gateway) is an
Open Source micro-service in the Nevermined ecosystem. The Gateway is the
technical component executed by Data/Compute Providers allowing them to provide
extended data services (e.g. storage and compute). The Nevermined Gateway, as
part of the Publisher ecosystem, includes the credentials to interact with the
infrastructure (initially cloud, but could be on-premise).

The Gateway allows also the encryption and decryption of components using the following mechanisms:

* RSA
* ECDSA
* Parity Secret Store

Nevermined provides the package and automation of the micro-service allowing an
easy integration and deployment in cloud providers and Kubernetes clusters.


## Gateway API Reference

You can find a complete API reference documented in Swagger format in the
[docs folder](https://github.com/nevermined-io/gateway/tree/master/docs) of the
metadata api repository.
