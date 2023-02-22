from datetime import datetime
import OpenSSL # needn install this lib
import ssl
cert=ssl.get_server_certificate(('account-stg.aladinbank.id', 443))
x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
bytes=x509.get_notAfter()
print(bytes)
timestamp = bytes.decode('utf-8')
print (datetime.strptime(timestamp, '%Y%m%d%H%M%S%z').date().isoformat())
