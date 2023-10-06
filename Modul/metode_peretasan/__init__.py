"""
Memperbolehkan anda untuk memilih berbagai metode peretasan yang tersedia.
Namun perlu di ingat ini adalah modul yang tidak dapat digunakan untuk peretasan secara langsung.
Anda harus membuat kode pemrograman untuk peretasan anda sendiri dan pastikan anda tidak menggunakan modul ini untuk tujuan ilegal!
"""
import typing
from tkinter import filedialog

__version__ = "1.2.0"
__all__ = ["exception_karakter_kata_sandi_bukan_ascii", "brute_force", "kamus"]

class exception_karakter_kata_sandi_bukan_ascii(Exception):
    PESAN_ERROR = "Karakter Kata Sandi Bukan ASCII!"
    def __init__(self):
        "Exception untuk karakter kata sandi bukan ascii"
        super().__init__(self.PESAN_ERROR)

def brute_force(karakter_kata_sandi : str, panjang_kata_sandi : typing.Literal[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], cetak = False):
    "Hanya karakter ASCII yang diperbolehkan. Membutuhkan perulangan for untuk memuat serangan brute force jika parameter cetak bernilai False"
    if not karakter_kata_sandi.isascii():
        raise exception_karakter_kata_sandi_bukan_ascii()
    else:
        def loop_kata_sandi(kata_sandi_brute_force : str):
            if len(kata_sandi_brute_force) < digit_brute_force_saat_ini:
                for kata_sandi_tambahan in karakter_kata_sandi:
                    kata_sandi_sekarang = kata_sandi_brute_force + kata_sandi_tambahan
                    if cetak:
                        loop_kata_sandi(kata_sandi_sekarang)
                    else:
                        for yield_kata_sandi_brute_force in loop_kata_sandi(kata_sandi_sekarang):
                            yield yield_kata_sandi_brute_force
            elif cetak:
                return print(kata_sandi_brute_force)
            else:
                yield kata_sandi_brute_force
        kata_sandi_baru = ""
        for digit_brute_force_saat_ini in range(panjang_kata_sandi):
            digit_brute_force_saat_ini += 1
            if cetak:
                loop_kata_sandi(kata_sandi_baru)
            else:
                for yield_kata_sandi_brute_force in loop_kata_sandi(kata_sandi_baru):
                    yield yield_kata_sandi_brute_force
def kamus(string_judul = False, string_kapital = False, string_huruf_besar = False, string_huruf_kecil = False, hanya_karakter_ascii = False, cetak = False):
    "Membutuhkan perulangan for untuk memuat serangan dictionary jika parameter cetak bernilai False. Memerlukan file txt. Mengembalikan False jika file tidak dibuka"
    direktori_file = filedialog.askopenfilename(defaultextension = ".txt", filetypes = [("Dokumen Teks", "*.txt")])
    if direktori_file:
        with open(file = direktori_file, mode = "r") as data_kamus:
            data_kamus_dimuat = [list_data_kamus.strip() for list_data_kamus in data_kamus]
            for data_per_baris in data_kamus_dimuat:
                if hanya_karakter_ascii:
                    if not data_per_baris.isascii():
                        continue
                if cetak:
                    print(data_per_baris)
                    if string_judul: print(data_per_baris.title())
                    if string_kapital: print(data_per_baris.capitalize())
                    if string_huruf_besar: print(data_per_baris.upper())
                    if string_huruf_kecil: print(data_per_baris.lower())
                else:
                    yield data_per_baris
                    if string_judul: yield data_per_baris.title()
                    if string_kapital: yield data_per_baris.capitalize()
                    if string_huruf_besar: yield data_per_baris.upper()
                    if string_huruf_kecil: yield data_per_baris.lower()
    else:
        return False
