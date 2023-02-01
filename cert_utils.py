# kita menggunakan default library dari python, tidak perlu menginstall library apapun
import ssl
import socket
from datetime import datetime


"""
function ini berfungsi untuk menjalin koneksi dengan hostname yang
kita masukan sebagai parameter dan mengambil data certificate
pada hostname tersebut.

socket adalah default library yang membantu kita untuk membuat
koneksi dengan hostname, dan ssl sebagai library yang membantu
kita untuk mendapatkan data dan membaca data pada certificate.
"""
def get_certificate_from_hostname(hostname):
	# initialization
    context = ssl.create_default_context()
    context.check_hostname = False
 
    conn = context.wrap_socket(
        socket.socket(socket.AF_INET),
        server_hostname=hostname,
    )    
    conn.settimeout(5.0)

    # membuat koneksi dengan hostname
    conn.connect((hostname, 443))

    # membaca data certificate
    certificate = conn.getpeercert()

    # melempar data certificate sebagai hasil dari fungsi ini
    return certificate

"""
function ini berfungsi untuk mengestraksi data certificate,
memfilter apa saja yang mau kita tampilkan.
"""
def read_certificate(certificate):
	
	# format string dari notAfter di certificate untuk maping ke datetime
    date_format = r'%b %d %H:%M:%S %Y %Z'
    
    # get string value dari notAfter, dimana ini adalah tanggal expired date dari certificate
    not_after = certificate['notAfter']
    
    # convert notAfter dari string ke datetime
    expire_date = datetime.strptime(not_after, date_format)

    # menghitung sisa hari, berapa hari lagi certificate akan expired
    remaining = expire_date - datetime.now()

    # mengumpulkan data hasil dari ekstraksi di atas
    cert_data = {	'expire_date': expire_date.strftime("%A, %d %B %Y %H:%M:%S"),
    				'remaining_days': remaining.days
    			}

    # melempar cert_data sebagai hasil akhir dari fungsi ini.
    return cert_data


def print_result(title,cert_data):
	result_format = f"""
	{title}\n
	Expired Date\t: {cert_data['expire_date']}
	Remaining Days\t: {cert_data['remaining_days']}\n
	#################################################################\n
	"""

	return result_format