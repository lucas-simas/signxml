# signxml
Container Assinador de XML configurado para IPC-Brasil

## Libs utilizadas
https://github.com/XML-Security/signxml

## Passo a passo para transformar certificado .pfx em .pem com chave .key :
Trecho de: https://stackoverflow.com/questions/15413646/converting-pfx-to-pem-using-openssl
```
Second case: To convert a PFX file to separate public and private key PEM files:
Extracts the private key form a PFX to a PEM file:

openssl pkcs12 -in filename.pfx -nocerts -out key.pem
Exports the certificate (includes the public key only):

openssl pkcs12 -in filename.pfx -clcerts -nokeys -out cert.pem
Removes the password (paraphrase) from the extracted private key (optional):

openssl rsa -in key.pem -out server.key
```

## Como buildar
```
sudo docker build . -t lsignxml

sudo docker run -d -p 6025:6025 --name=LSIGNXML --restart=always lsignxml
```

## Como utilizar
Por padrão este container será criado no localhost com a porta definida para 6025.
Ele funciona como uma API que aceita POSTs
Você deve enviar da seguinte forma, exemplo:
```
URL: http://localhost:6025/xml/assinar'

PostData:
cert - arquivo .pem (certificado)
certkey - arquivo .key (chave)
xml - arquivo .xml para assinar
```
