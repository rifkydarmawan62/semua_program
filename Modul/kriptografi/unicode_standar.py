"""Encoding dan Decoding karakter string unicode. Memiliki tingkat keamanan kriptografi password yang rendah"""

__version__ = "1.1.0"
__all__ = ["exception_digit_bilangan_oktal_tidak_valid", "exception_digit_bilangan_biner_tidak_valid", "encoding_heksadesimal", "encoding_desimal", "encoding_oktal", "encoding_biner", "decoding_heksadesimal", "decoding_desimal", "decoding_oktal", "decoding_biner"]

class exception_digit_bilangan_oktal_tidak_valid(Exception):
    PESAN_ERROR = "Digit Bilangan Oktal Hanya Berupa Angka 0 sampai 7"
    def __init__(self):
        "Exception untuk digit bilangan oktal tidak valid"
        super().__init__(self.PESAN_ERROR)
class exception_digit_bilangan_biner_tidak_valid(Exception):
    PESAN_ERROR = "Digit Bilangan Biner Hanya Berupa Angka 0 dan 1!"
    def __init__(self):
        "Exception untuk digit bilangan biner tidak valid"
        super().__init__(self.PESAN_ERROR)

def encoding_heksadesimal(string : str, mengembalikan_tuple = False):
    "Encode string menjadi bilangan heksadesimal"
    if mengembalikan_tuple: return tuple([hex(ord(karakter_tunggal))[2:] for karakter_tunggal in string])
    return [hex(ord(karakter_tunggal))[2:] for karakter_tunggal in string]
def encoding_desimal(string : str, mengembalikan_tuple = False):
    "Encode string menjadi bilangan desimal"
    if mengembalikan_tuple: return tuple([ord(karakter_tunggal) for karakter_tunggal in string])
    return [ord(karakter_tunggal) for karakter_tunggal in string]
def encoding_oktal(string : str, mengembalikan_tuple = False):
    "Encode string menjadi bilangan oktal"
    if mengembalikan_tuple: return tuple([oct(ord(karakter_tunggal))[2:] for karakter_tunggal in string])
    return [oct(ord(karakter_tunggal)) for karakter_tunggal in string]
def encoding_biner(string : str, mengembalikan_tuple = False):
    "Encode string menjadi bilangan biner"
    if mengembalikan_tuple: return tuple([bin(ord(karakter_tunggal))[2:] for karakter_tunggal in string])
    return [bin(ord(karakter_tunggal))[2:] for karakter_tunggal in string]

def decoding_heksadesimal(bilangan_heksadesimal : str | tuple[str] | list[str]):
    "Decode bilangan heksadesimal menjadi string"
    decode_string = ""
    for karakter_tunggal_bilangan_heksadesimal in bilangan_heksadesimal:
        decode_string = decode_string + chr(int("0x" + karakter_tunggal_bilangan_heksadesimal if "0x" != karakter_tunggal_bilangan_heksadesimal[:2] else karakter_tunggal_bilangan_heksadesimal, base = 0))
    return decode_string
def decoding_desimal(bilangan_desimal : int | tuple[int] | list[int]):
    "Decode bilangan desimal menjadi string"
    decode_string = ""
    if not isinstance(bilangan_desimal, int):
        for karakter_tunggal_bilangan_desimal in bilangan_desimal:
            decode_string = decode_string + chr(karakter_tunggal_bilangan_desimal)
        return decode_string
    else:
        return chr(bilangan_desimal)
def decoding_oktal(bilangan_oktal : str | int | tuple[str] | tuple[int] | tuple[str | int] | list[str] | list[int] | list[str | int]):
    "Decode bilangan oktal menjadi string"
    def periksa_digit_oktal(bilangan_oktal : str):
        "Memeriksa masing-masing digit oktal apakah valid atau tidak"
        for digit_oktal in bilangan_oktal:
            if "0" != digit_oktal and "1" != digit_oktal and "2" != digit_oktal and "3" != digit_oktal and "4" != digit_oktal and "5" != digit_oktal and "6" != digit_oktal and "7" != digit_oktal:
                raise exception_digit_bilangan_oktal_tidak_valid()
        return chr(int("0o" + bilangan_oktal, base = 0))
    decode_string = ""
    if isinstance(bilangan_oktal, int):
        bilangan_oktal = str(bilangan_oktal)
    if isinstance(bilangan_oktal, tuple) or isinstance(bilangan_oktal, list):
        for karakter_tunggal_bilangan_oktal in bilangan_oktal:
            if isinstance(karakter_tunggal_bilangan_oktal, int):
                karakter_tunggal_bilangan_oktal = str(karakter_tunggal_bilangan_oktal)
            if karakter_tunggal_bilangan_oktal.isdigit():
                decode_string = decode_string + periksa_digit_oktal(karakter_tunggal_bilangan_oktal)
            else:
                raise exception_digit_bilangan_oktal_tidak_valid()
        return decode_string
    elif bilangan_oktal.isdigit():
        return periksa_digit_oktal(bilangan_oktal)
    else:
        raise exception_digit_bilangan_oktal_tidak_valid()
def decoding_biner(bilangan_biner : str | int | tuple[str] | tuple[int] | tuple[str | int] | list[str] | list[int] | list[str | int]):
    "Decode bilangan biner menjadi string. Bilangan biner hanya terdiri dari angka 0 dan 1"
    def periksa_digit_biner(bilangan_biner : str):
        "Memeriksa masing-masing digit biner apakah valid atau tidak"
        for digit_biner in bilangan_biner:
            if "0" != digit_biner and "1" != digit_biner:
                raise exception_digit_bilangan_biner_tidak_valid()
        return chr(int("0b" + bilangan_biner, base = 0))
    decode_string = ""
    if isinstance(bilangan_biner, int):
        bilangan_biner = str(bilangan_biner)
    if isinstance(bilangan_biner, tuple) or isinstance(bilangan_biner, list):
        for karakter_tunggal_bilangan_biner in bilangan_biner:
            if isinstance(karakter_tunggal_bilangan_biner, int):
                karakter_tunggal_bilangan_biner = str(karakter_tunggal_bilangan_biner)
            if karakter_tunggal_bilangan_biner.isdigit():
                decode_string = decode_string + periksa_digit_biner(karakter_tunggal_bilangan_biner)
            else:
                raise exception_digit_bilangan_biner_tidak_valid()
        return decode_string
    elif bilangan_biner.isdigit():
        return periksa_digit_biner(bilangan_biner)
    else:
        raise exception_digit_bilangan_biner_tidak_valid()