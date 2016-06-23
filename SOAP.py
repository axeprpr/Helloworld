#http://users.skynet.be/pascalbotte/rcx-ws-doc/postxmlpython.htm

#post xml soap message

import sys, httplib
#a "as lighter as possible" soap message:
SM_TEMPLATE = """<?xml version="1.0" encoding="UTF-8"?>
<SOAP-ENV:Envelope
SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"  
xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/">
<SOAP-ENV:Body>
<ns1:readLS xmlns:ns1="http://phonedirlux.homeip.net/types">
<String_1>%s</String_1>
</ns1:readLS>
</SOAP-ENV:Body>
</SOAP-ENV:Envelope>
"""
SoapMessage = SM_TEMPLATE%("Your message or e-mail")
print SoapMessage
#construct and send the header
webservice = httplib.HTTP("www.pascalbotte.be")
webservice.putrequest("POST", "/rcx-ws/rcx")
webservice.putheader("Host", "www.pascalbotte.be")
webservice.putheader("User-Agent", "Python post")
webservice.putheader("Content-type", "text/xml; charset=\"UTF-8\"")
webservice.putheader("Content-length", "%d" % len(SoapMessage))
webservice.putheader("SOAPAction", "\"\"")
webservice.endheaders()
webservice.send(SoapMessage)
# get the response
statuscode, statusmessage, header = webservice.getreply()
print "Response: ", statuscode, statusmessage
print "headers: ", header
res = webservice.getfile().read()
print res
