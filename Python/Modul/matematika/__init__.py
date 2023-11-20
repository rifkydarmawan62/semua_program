"Menyediakan fungsi matematika yang tersedia"

__version__ = "1.2.0"
__all__ = ["hasil_faktorial", "deret_bilangan_prima", "cek_bilangan_prima"]

class exception_tipe_data_tidak_valid(Exception):
    def __init__(self, pesan_error : None | str):
        "Exception untuk tipe data tidak valid"
        super().__init__(pesan_error)

def hasil_faktorial(bilangan_faktorial : int):
    """
    Mengembalikan hasil dari bilangan faktorial
    """
    if bilangan_faktorial == 1:
        return bilangan_faktorial
    else :
        return bilangan_faktorial * faktorial(bilangan_faktorial - 1)
def deret_bilangan_prima(angka_maksimum : int, mengembalikan_tuple = False):
    "Membuat deret bilangan prima. Mengembalikan False jika parameter angka tidak valid untuk bilangan prima"
    if angka_maksimum > 1:
        angka_maksimum += 1
        bilangan_prima = []
        for deret_bilangan in range(2, angka_maksimum):
            for nilai_pembagian in range(2, deret_bilangan):
                if deret_bilangan % nilai_pembagian == 0:
                    break
            else:
                bilangan_prima.extend([deret_bilangan])
        if mengembalikan_tuple:
            return tuple(bilangan_prima)
        else:
            return bilangan_prima
    else:
        return False
def cek_bilangan_prima(angka : int | list[int] | tuple):
    "Mengembalikan True jika parameter angka adalah bilangan prima. Mengembalikan False jika parameter angka bukan bilangan prima"
    if isinstance(angka, int):
        if angka > 1:
            for nilai_pembagian in range(2, angka):
                if angka % nilai_pembagian == 0:
                    return False
            else:
                return True
    else:
        hasil_item = []
        for item_angka in angka:
            if isinstance(item_angka, int):
                if item_angka > 1:
                    for nilai_pembagian in range(2, item_angka):
                        if item_angka % nilai_pembagian == 0:
                            hasil_item.extend([False])
                            break
                    else:
                        hasil_item.extend([True])
            else:
                raise exception_tipe_data_tidak_valid("Tipe Data yang Diperbolehkan Hanya Berupa Integer!")
        return hasil_item
