from typing import Iterable

#PORT
PORT_FTP = 20, 21
"Port File Transfer Protocol"
PORT_SSH = 22
"Port Secure Shell"
PORT_TELNET = 23
PORT_SMTP = 25
"Port Simple Mail Transfer Protocol"
PORT_DNS = 53
"Port Domain Name System"
PORT_DHCP_SERVER = 67
"Port Dynamic Host Configuration Protocol untuk server"
PORT_DHCP_KLIEN = 68
"Port Dynamic Host Configuration Protocol untuk klien"
PORT_HTTP = 80
"Port Hyper Text Transfer Protocol"
PORT_POP3_NON_ENKRIPSI = 110
"Port Post Office Protocol tanpa enkripsi"
PORT_IMAP = 143
"Port Internet Message Access Protocol"
PORT_HTTPS = 443
"Port Hyper Text Transfer Protocol Secure"
PORT_POP3_TERENKRIPSI = 995
"Port Post Office Protocol dengan enkripsi SSL/TLS"
PORT_PROXY = 3128, 8080

#IPV4
IPV4_KELAS_A = "255.0.0.0"
"Netmask kelas a"
IPV4_KELAS_B = "255.255.0.0"
"Netmask kelas b"
IPV4_KELAS_C = "255.255.255.0"
"Netmask kelas c"

IPV4_KELAS_A_BINER = "11111111.00000000.00000000.00000000"
"Netmask kelas a dalam bilangan biner"
IPV4_KELAS_B_BINER = "11111111.11111111.00000000.00000000"
"Netmask kelas b dalam bilangan biner"
IPV4_KELAS_C_BINER = "11111111.11111111.11111111.00000000"
"Netmask kelas c dalam bilangan biner"

CIDR_KELAS_A = "/8"
"Classless Inter-Domain Routing kelas a"
CIDR_KELAS_B = "/16"
"Classless Inter-Domain Routing kelas b"
CIDR_KELAS_C = "/24"
"Classless Inter-Domain Routing kelas c"

TOTAL_NETWORK_IPV4_KELAS_A = 256
"Jumlah network atau jaringan dalam netmask kelas a"
TOTAL_NETWORK_IPV4_KELAS_B = 65536
"Jumlah network atau jaringan dalam netmask kelas b"
TOTAL_NETWORK_IPV4_KELAS_C = 16777216
"Jumlah network atau jaringan dalam netmask kelas c"

MAKSIMUM_HOST_IPV4_KELAS_A = 16777214
"Jumlah host atau perangkat maksimal yang dapat terhubung ke internet dalam netmask kelas a"
MAKSIMUM_HOST_IPV4_KELAS_B = 65534
"Jumlah host atau perangkat maksimal yang dapat terhubung ke internet dalam netmask kelas b"
MAKSIMUM_HOST_IPV4_KELAS_C = 254
"Jumlah host atau perangkat maksimal yang dapat terhubung ke internet dalam netmask kelas c"

def adalah_ipv4(__alamat_ip : str | Iterable[str]) -> bool | list[bool]:
    "Mengembalikan True jika alamat IPv4 valid, mengembalikan False jika tidak"
    def hasil_pemeriksaan(__alamat_ip : str) -> bool:
        __alamat_ip.strip()
        if __alamat_ip.count(".") == 3:
            for nilai_desimal in __alamat_ip.split("."):
                if nilai_desimal.isdigit():
                    if int(nilai_desimal) >= 0 and int(nilai_desimal) <= 255:
                        continue
                    else:
                        return False
                else:
                    return False
            return True
        else:
            return False
    if isinstance(__alamat_ip, str):
        return hasil_pemeriksaan(__alamat_ip)
    else:
        hasil : list = []
        for item_alamat_ip in __alamat_ip:
            hasil.append(hasil_pemeriksaan(item_alamat_ip))
        return hasil
def adalah_mac(__alamat_mac : str | Iterable[str]) -> bool | list[bool]:
    "Mengembalikan True jika alamat MAC valid, mengembalikan False jika tidak"
    def hasil_pemeriksaan(__alamat_mac : str) -> bool:
        __alamat_mac.strip()
        if __alamat_mac.count(":") == 5:
            for nilai_heksadesimal in __alamat_mac.split(":"):
                if len(nilai_heksadesimal) <= 0 or len(nilai_heksadesimal) > 2:
                    return False
                elif len(nilai_heksadesimal) == 1:
                    nilai_heksadesimal = "0" + nilai_heksadesimal
                try:
                    nilai_desimal = int("0x" + nilai_heksadesimal, base = 0)
                except:
                    return False
                else:
                    if nilai_desimal >= 0 and nilai_desimal <= 255:
                        continue
                    else:
                        return False
            return True
        else:
            return False
    if isinstance(__alamat_mac, str):
        return hasil_pemeriksaan(__alamat_mac)
    else:
        hasil : list = []
        for item_alamat_mac in __alamat_mac:
            hasil.append(hasil_pemeriksaan(item_alamat_mac))
        return hasil