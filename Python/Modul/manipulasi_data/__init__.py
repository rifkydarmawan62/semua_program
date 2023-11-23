from typing import Collection, Optional, Iterable, Any

PEMBARUAN_TERAKHIR = "23 November 2023"
"Tanggal program terakhir kali diperbarui"

#Program binary search masih terdapat kemungkinan bug
"""
def binary_search(data : Collection[int], __boolean_output : bool = False, *, data_yang_dicari : int):
    data_di_posisi_awal = 1
    data_di_posisi_akhir = len(data) + 1
    ditemukan = False
    while data_di_posisi_awal <= data_di_posisi_akhir and not ditemukan:
        data_di_posisi_tengah = int((data_di_posisi_awal + data_di_posisi_akhir) / 2)
        if data_yang_dicari == data[data_di_posisi_tengah]:
            ditemukan = True
            if __boolean_output:
                return True
            else:
                return True, data_di_posisi_tengah + 1
        elif data_yang_dicari < data[data_di_posisi_tengah]:
            data_di_posisi_akhir = data_di_posisi_tengah - 1
        else:
            data_di_posisi_awal = data_di_posisi_tengah - 1
    else:
        return False
"""
class tumpukan:
    __DATA : list = []
    def __init__(self, tumpukan_baru : Optional[Iterable | Any], *, maks_tumpuk : Optional[int]):
        "Buat objek tumpukan baru"
        assert maks_tumpuk > 0, f"Maks tumpuk {maks_tumpuk} harus lebih dari nol!"
        self.MAKS_TUMPUK = maks_tumpuk
        if tumpukan_baru != None:
            if isinstance(tumpukan_baru, Iterable):
                self.__DATA.extend(tumpukan_baru)
            else:
                self.__DATA.append(tumpukan_baru)
    def adalah_kosong(self) -> bool:
        "Mengembalikan True jika data yang ditumpuk kosong, False jika tidak"
        if len(self.__DATA) == 0:
            return True
        else:
            return False
    def tambah(self, __data_baru : Iterable | Any):
        "Menambah tumpukan yang paling atas"
        if isinstance(__data_baru, Iterable):
            self.__DATA.extend(__data_baru)
        else:
            self.__DATA.append(__data_baru)
    def ambil(self):
        "Mengambil tumpukan yang paling atas\n\nMengembalikan None jika data yang ditumpuk kosong"
        if len(self.__DATA) > 0:
            return self.__DATA.pop()
        else:
            return None
    def ambil_semua(self):
        "Mengambil semua tumpukan"
        return self.__DATA
    def hapus_semua(self):
        "Menghapus semua data yang ditumpuk"
        self.__DATA.clear()
    def ambil_dan_hapus_semua(self):
        "Mengambil lalu menghapus semua data yang ditumpuk"
        __objek_sementara = self.__DATA
        self.__DATA.clear()
        return __objek_sementara
    def jumlah_elemen(self):
        "Mengembalikan jumlah elemen yang ditumpuk"
        return len(len(self.__DATA))