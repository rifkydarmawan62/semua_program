import time

__version__ = "1.0.1"
__all__ = ["TAHUN", "bulan", "TANGGAL", "hari", "jam", "menit", "detik"]

TAHUN = time.localtime().tm_year
"Mengembalikan integer tahun"
def bulan(integer_output = False):
    "Mengembalikan nama bulan jika parameter adalah False"
    if integer_output: return time.localtime().tm_mon
    elif time.localtime().tm_mon == 1: return "Januari"
    elif time.localtime().tm_mon == 2: return "Februari"
    elif time.localtime().tm_mon == 3: return "Maret"
    elif time.localtime().tm_mon == 4: return "April"
    elif time.localtime().tm_mon == 5: return "Mei"
    elif time.localtime().tm_mon == 6: return "Juni"
    elif time.localtime().tm_mon == 7: return "Juli"
    elif time.localtime().tm_mon == 8: return "Agustus"
    elif time.localtime().tm_mon == 9: return "September"
    elif time.localtime().tm_mon == 10: return "Oktober"
    elif time.localtime().tm_mon == 11: return "November"
    else : return "Desember"
TANGGAL = time.localtime().tm_mday
"Mengembalikan integer tanggal 1 sampai 31"
def hari(integer_output = False):
    "Mengembalikan nama hari jika parameter adalah False"
    if integer_output: return time.localtime().tm_wday
    elif time.localtime().tm_wday == 0: return "Senin"
    elif time.localtime().tm_wday == 1: return "Selasa"
    elif time.localtime().tm_wday == 2: return "Rabu"
    elif time.localtime().tm_wday == 3: return "Kamis"
    elif time.localtime().tm_wday == 4: return "Jum'at"
    elif time.localtime().tm_wday == 5: return "Sabtu"
    else: return "Minggu"
def jam(integer_output = False):
    "Mengembalikan string dua digit jam jika parameter adalah False"
    if integer_output: return time.localtime().tm_hour
    else: return "0" + str(time.localtime().tm_hour) if len(str(time.localtime().tm_hour)) == 1 else str(time.localtime().tm_hour)
def menit(integer_output = False):
    "Mengembalikan string dua digit menit jika parameter adalah False"
    if integer_output: return time.localtime().tm_min
    elif len(str(time.localtime().tm_min)) == 1: return "0" + str(time.localtime().tm_min)
    else : return str(time.localtime().tm_min)
def detik(integer_output = False):
    "Mengembalikan string dua digit detik jika parameter adalah False"
    if integer_output: return time.localtime().tm_sec
    elif len(str(time.localtime().tm_sec)) == 1: return "0" + str(time.localtime().tm_sec)
    else: return str(time.localtime().tm_sec)