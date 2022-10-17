# signxml
Container Assinador de XML configurado para IPC-Brasil

## Libs utilizadas
https://github.com/XML-Security/signxml

## Passo a passo para transformar certificado .pfx em .pem com chave .key :
```
[https://stackoverflow.com/questions/15413646/converting-pfx-to-pem-using-openssl]
Second case: To convert a PFX file to separate public and private key PEM files:
Extracts the private key form a PFX to a PEM file:

openssl pkcs12 -in filename.pfx -nocerts -out key.pem
Exports the certificate (includes the public key only):

openssl pkcs12 -in filename.pfx -clcerts -nokeys -out cert.pem
Removes the password (paraphrase) from the extracted private key (optional):

openssl rsa -in key.pem -out server.key
```
