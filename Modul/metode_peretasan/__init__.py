"""
Memperbolehkan anda untuk memilih berbagai metode peretasan yang tersedia.
Ini adalah modul yang tidak dapat digunakan untuk peretasan secara langsung.
Namun anda perlu membuat kode pemrograman anda untuk peretasan anda sendiri sekaligus mengimport modul ini. Dan pastikan anda tidak menggunakan modul ini untuk tujuan ilegal!
"""
import typing
from tkinter import filedialog

__version__ = "1.2.1"
__all__ = ["exception_karakter_kata_sandi_bukan_ascii", "brute_force", "brute_force_pin", "kamus"]

class exception_karakter_kata_sandi_bukan_ascii(Exception):
    PESAN_ERROR = "Karakter Kata Sandi Bukan ASCII!"
    def __init__(self):
        "Exception untuk karakter kata sandi bukan ascii"
        super().__init__(self.PESAN_ERROR)

def brute_force(karakter_kata_sandi : str, panjang_kata_sandi : typing.Literal[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]):
    "Hanya karakter ASCII yang diperbolehkan. Membutuhkan perulangan for untuk memuat serangan brute force"
    if not karakter_kata_sandi.isascii():
        raise exception_karakter_kata_sandi_bukan_ascii()
    else:
        def loop_kata_sandi(kata_sandi_brute_force : str):
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
def brute_force_pin(jumlah_digit : int, string_output = False):
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
def kamus(string_judul = False, string_kapital = False, string_huruf_besar = False, string_huruf_kecil = False, hanya_karakter_ascii = False):
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
        return False
