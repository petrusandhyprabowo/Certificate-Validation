import json
import cert_utils

if __name__ == "__main__":

	# buka json file berisi hostname
	file = open('hostname.json')

	# convert json ke dict python
	json_data = json.load(file)

	# get list hostname
	hostname_list = json_data['hostname']

	# looping hostname
	for hostname in hostname_list:
		try:
			certificate = cert_utils.get_certificate_from_hostname(hostname)
			cert_data = cert_utils.read_certificate(certificate)
			print(cert_utils.print_result(f'Get Certificate of {hostname}',cert_data))
		except Exception as e:
			print(hostname, e.strerror)