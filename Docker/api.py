import json
import os

#Libs para criação de API
from flask import Flask, request
from flask_jsonpify import jsonify
from flask_restful import Api, Resource

from lxml import etree
import signxml


#Desabilitando warning de Post inseguro
import urllib3
urllib3.disable_warnings()


#Classe para tratar requisição
class Assinar_XML_IPC_BRASIL(Resource):
    #Definição de POST apenas para respondermos
	def post(self):
		try:
			xml = request.files['xml']
			cert = request.files['cert']
			certkey = request.files['certkey']
			data = request.form.to_dict()
   
			xml = xml.read()
			cert = cert.read()
			certkey = certkey.read()
			
			root = etree.fromstring(xml)
			signed_root = signxml.XMLSigner(method=signxml.methods.enveloped, digest_algorithm="sha1", signature_algorithm="rsa-sha1", c14n_algorithm="http://www.w3.org/TR/2001/REC-xml-c14n-20010315").sign(root, key=certkey, cert=cert)
			# verified_data = XMLVerifier().verify(signed_root, ca_pem_file=cert).signed_xml

			xmlstr = etree.tostring(signed_root, encoding='utf8', method='xml', pretty_print=True)

			# et = etree.ElementTree(signed_root)
			# et.write('output.xml', pretty_print=True)

			return jsonify({'status': True, 'code': None, 'data': {'xml': xmlstr.decode('utf8')}})
		except Exception as e:
			return jsonify({'status': False, 'message': 'Erro encontrado em: ' + str(e), 'code': None, 'data': []})


#Iniciando API
app = Flask(__name__)
api = Api(app)
api.add_resource(Assinar_XML_IPC_BRASIL, '/xml/assinar')

#Estas portas / host podem ser sobreescritos ao rodar em CMD
if __name__ == '__main__':
	app.run(host='0.0.0.0', port='6025')
