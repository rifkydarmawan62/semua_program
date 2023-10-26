"Memperbolehkan anda untuk memilih berbagai metode peretasan yang tersedia"
import typing
from tkinter import filedialog

__all__ = ["PEMBARUAN_TERAKHIR", "exception_karakter_kata_sandi_bukan_ascii", "brute_force_standar", "brute_force_heksadesimal", "brute_force_pin", "kamus", "brute_force_oktal", "brute_force_biner"]

PEMBARUAN_TERAKHIR = "26 Oktober 2023"
"Tanggal program terakhir kali diperbarui"

class exception_karakter_kata_sandi_bukan_ascii(Exception):
    def __init__(self):
        "Exception untuk karakter kata sandi bukan ascii"
        super().__init__("Karakter Kata Sandi Bukan ASCII!")

def brute_force_standar(karakter_kata_sandi : str, panjang_kata_sandi : typing.Literal[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) -> typing.Iterator[str]:
    "Hanya karakter ASCII yang diperbolehkan. Membutuhkan perulangan for untuk memuat serangan brute force"
    if not karakter_kata_sandi.isascii():
        raise exception_karakter_kata_sandi_bukan_ascii()
    else:
        def loop_kata_sandi(kata_sandi_brute_force : str) -> typing.Iterator[str]:
            if len(kata_sandi_brute_force) < digit_brute_force_saat_ini:
                for kata_sandi_tambahan in karakter_kata_sandi:
                    kata_sandi_sekarang = kata_sandi_brute_force + kata_sandi_tambahan
                    for yield_kata_sandi_brute_force in loop_kata_sandi(kata_sandi_sekarang):
                        yield yield_kata_sandi_brute_force
            else:
                yield kata_sandi_brute_force
        kata_sandi_baru = ""
        for digit_brute_force_saat_ini in range(panjang_kata_sandi):
            digit_brute_force_saat_ini += 1
            for yield_kata_sandi_brute_force in loop_kata_sandi(kata_sandi_baru):
                yield yield_kata_sandi_brute_force
def kamus(string_judul = False, string_kapital = False, string_huruf_besar = False, string_huruf_kecil = False, hanya_karakter_ascii = False) -> typing.Iterator[str] | typing.Iterator[typing.Literal[False]]:
    "Membutuhkan perulangan for untuk memuat serangan dictionary. Memerlukan file txt. Mengembalikan False jika file tidak dibuka"
    direktori_file = filedialog.askopenfilename(defaultextension = ".txt", filetypes = [("Dokumen Teks", "*.txt")], title = "File Untuk Dictionary Attack")
    if direktori_file:
        with open(file = direktori_file, mode = "r") as data_kamus:
            data_kamus_dimuat = [list_data_kamus.strip() for list_data_kamus in data_kamus]
            for data_per_baris in data_kamus_dimuat:
                if hanya_karakter_ascii:
                    if not data_per_baris.isascii():
                        continue
                yield data_per_baris
                if string_judul: yield data_per_baris.title()
                if string_kapital: yield data_per_baris.capitalize()
                if string_huruf_besar: yield data_per_baris.upper()
                if string_huruf_kecil: yield data_per_baris.lower()
    else:
        yield False
def brute_force_heksadesimal(jumlah_digit_heksadesimal : int, output_bawan = True) -> typing.Iterator[str]:
    "Membutuhkan perulangan for untuk memuat serangan brute force heksadesimal"
    assert jumlah_digit_heksadesimal > 0, "Jumlah Digit Harus Lebih Dari Nol!"
    bilangan_desimal = 0
    while True:
        bilangan_heksadesimal = hex(bilangan_desimal)[2:]
        if output_bawan:
            yield "0x" + bilangan_heksadesimal
        elif not output_bawan:
            yield bilangan_heksadesimal
        if "f" * jumlah_digit_heksadesimal == bilangan_heksadesimal.lower():
            break
        bilangan_desimal += 1
def brute_force_pin(jumlah_digit : int, string_output = False) -> typing.Iterator[str] | typing.Iterator[int]:
    "Membutuhkan perulangan for untuk memuat serangan brute force pin"
    assert jumlah_digit > 0, "Jumlah Digit Harus Lebih Dari Nol!"
    PIN_MAKSIMUM = int("1" + "0" * jumlah_digit)
    for pin_saat_ini in range(PIN_MAKSIMUM):
        if string_output:
            STRING_PIN_MAKSIMUM = str(PIN_MAKSIMUM)
            pin_saat_ini = str(pin_saat_ini)
            while len(pin_saat_ini) < len(STRING_PIN_MAKSIMUM) - 1:
                pin_saat_ini = "0" + pin_saat_ini
            yield pin_saat_ini
        else:
            yield pin_saat_ini
def brute_force_oktal(jumlah_digit_oktal : int, output_bawaan = True) -> typing.Iterator[str]:
    "Membutuhkan perulangan for untuk memuat serangan brute force oktal"
    assert jumlah_digit_oktal > 0, "Jumlah Digit Oktal Harus Lebih Dari Nol!"
    bilangan_desimal = 0
    while True:
        bilangan_oktal = oct(bilangan_desimal)[2:]
        if output_bawaan:
            yield "0o" + bilangan_oktal
        elif not output_bawaan:
            yield bilangan_oktal
        if "7" * jumlah_digit_oktal == bilangan_oktal.lower():
            break
        bilangan_desimal += 1
def brute_force_biner(jumlah_digit_biner : int, tipe_output : typing.Literal["integer", "string", "bawaan"]) -> typing.Iterator[str] | typing.Iterator[int]:
    "Membutuhkan perulangan for untuk memuat serangan brute force biner"
    assert jumlah_digit_biner > 0, "Jumlah Digit Biner Harus Lebih Dari Nol!"
    bilangan_desimal = 0
    while True:
        string_bilangan_biner = bin(bilangan_desimal)[2:]
        if tipe_output == "bawaan":
            yield "0b" + string_bilangan_biner
        elif tipe_output == "string":
            while len(string_bilangan_biner) < jumlah_digit_biner:
                string_bilangan_biner = "0" + string_bilangan_biner
            yield string_bilangan_biner
        elif tipe_output == "integer":
            yield int(string_bilangan_biner)
        if "1" * jumlah_digit_biner == string_bilangan_biner:
            break
        bilangan_desimal += 1
