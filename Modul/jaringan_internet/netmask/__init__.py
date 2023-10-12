"Modul netmask untuk alamat IPV4"

__all__ = ["KELAS_A", "KELAS_B", "KELAS_C", "KELAS_A_BINER", "KELAS_B_BINER", "KELAS_C_BINER", "TOTAL_NETWORK_KELAS_A", "TOTAL_NETWORK_KELAS_B", "TOTAL_NETWORK_KELAS_C", "CIDR_KELAS_A", "CIDR_KELAS_B", "CIDR_KELAS_C", "HOST_MAKSIMUM_KELAS_A", "HOST_MAKSIMUM_KELAS_B", "HOST_MAKSIMUM_KELAS_C"]

KELAS_A = "255.0.0.0"
"Netmask kelas a"
KELAS_B = "255.255.0.0"
"Netmask kelas b"
KELAS_C = "255.255.255.0"
"Netmask kelas c"

KELAS_A_BINER = "11111111.00000000.00000000.00000000"
"Netmask kelas a dalam bilangan biner"
KELAS_B_BINER = "11111111.11111111.00000000.00000000"
"Netmask kelas b dalam bilangan biner"
KELAS_C_BINER = "11111111.11111111.11111111.00000000"
"Netmask kelas c dalam bilangan biner"

CIDR_KELAS_A = "/8"
"Classless Inter-Domain Routing kelas a"
CIDR_KELAS_B = "/16"
"Classless Inter-Domain Routing kelas b"
CIDR_KELAS_C = "/24"
"Classless Inter-Domain Routing kelas c"

TOTAL_NETWORK_KELAS_A = 256
"Jumlah network atau jaringan dalam netmask kelas a"
TOTAL_NETWORK_KELAS_B = 65536
"Jumlah network atau jaringan dalam netmask kelas b"
TOTAL_NETWORK_KELAS_C = 16777216
"Jumlah network atau jaringan dalam netmask kelas c"

HOST_MAKSIMUM_KELAS_A = 16777214
"Jumlah host atau perangkat maksimal yang dapat terhubung ke internet dalam netmask kelas a"
HOST_MAKSIMUM_KELAS_B = 65534
"Jumlah host atau perangkat maksimal yang dapat terhubung ke internet dalam netmask kelas b"
HOST_MAKSIMUM_KELAS_C = 254
"Jumlah host atau perangkat maksimal yang dapat terhubung ke internet dalam netmask kelas c"
