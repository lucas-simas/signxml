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
<?php
header('Content-Type: text/html; charset=UTF-8');

//Inicializando o CURL
$curl = curl_init('http://localhost:6025/xml/assinar');

//Transformando o arquivo em algo enviavel pelo CURL
if (function_exists('curl_file_create')) {

	$cFile 		= curl_file_create('./cert.pem');
	$ckeyFile 	= curl_file_create('./certkey.key');
	$xml 		= curl_file_create('./input.xml');
} 
else { 
	$cFile 		= '@' . realpath('./cert.pem'');
	$ckeyFile 	= '@' . realpath('./certkey.key');
	$xml 		= '@' . realpath('./input.xml');
}

//Opções e informações do CURL
curl_setopt($curl, CURLOPT_HEADER, false);
curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
curl_setopt($curl, CURLOPT_POST, true);
curl_setopt($curl, CURLOPT_CUSTOMREQUEST, "POST");
curl_setopt($curl, CURLOPT_POSTFIELDS, [
	'cert'		=> $cFile,
	'certkey'	=> $ckeyFile,
	'xml'		=> $xml,
]);

$json_response = curl_exec($curl);
$json_response = json_decode($json_response, true);
```
