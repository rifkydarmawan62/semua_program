"Menyediakan fungsi matematika yang tersedia"
from typing import Iterable, overload

PEMBARUAN_TERAKHIR : str = "23 November 2023"
"Tanggal program terakhir kali diperbarui"

NILAI_PI = 3.14
"Nilai π untuk lingkaran"
__JUMLAH_SISI_PERSEGI = 4
SATU_PER_DUA, SETENGAH = 0.5, 0.5
PERSEN, PER_SERATUS = 100, 100
"Nilai 100%"

def balikkan_bilangan(__dari_angka : int | float | Iterable[int | float]) -> int | float | list[int | float]:
    "Membalikan bilangan positif menjadi bilangan negatif atau membalikan bilangan bilangan negatif menjadi bilangan positif"
    def proses_pembalikan_bilangan(__angka : int | float) -> int | float:
        if __angka > 0:
            return -(__angka)
        elif __angka < 0:
            return __angka * -1
        else:
            return __angka
    if isinstance(__dari_angka, int | float):
        return proses_pembalikan_bilangan(__dari_angka)
    else:
        item_hasil : list = []
        for item_angka in __dari_angka:
            item_hasil.append(proses_pembalikan_bilangan(item_angka))
        return item_hasil
def adalah_bilangan_positif(__angka : int | float | Iterable[int | float]) -> bool | list[bool]:
    "Mengembalikan True jika angka adalah bilangan positif mengembalikan False jika tidak"
    def proses_bilangan_postif(__angka : int | float) -> bool:
        if __angka > 0:
            return True
        else:
            return False
    if isinstance(__angka, int | float):
        return proses_bilangan_postif(__angka)
    else:
        item_hasil : list = []
        for item_angka in __angka:
            item_hasil.append(proses_bilangan_postif(item_angka))
        return item_hasil
def adalah_bilangan_negatif(__angka : int | float | Iterable[int | float]) -> bool | list[bool]:
    "Mengembalikan True jika angka adalah bilangan negatif mengembalikan False jika tidak"
    def proses_bilangan_negatif(__angka : int | float) -> bool:
        if __angka < 0:
            return True
        else:
            return False
    if isinstance(__angka, int | float):
        return proses_bilangan_negatif(__angka)
    else:
        item_hasil : list = []
        for item_angka in __angka:
            item_hasil.append(proses_bilangan_negatif(item_angka))
        return item_hasil
def adalah_bilangan_genap(__angka : int | Iterable[int]) -> bool | list[bool]:
    def pembagian_bilangan_genap(__angka : int) -> bool:
        if __angka == 0:
            return True
        elif __angka < 0:
            __angka = balikkan_bilangan(__angka)
        if __angka % 2 == 0:
            return True
        else:
            return False
    if isinstance(__angka, int):
        return pembagian_bilangan_genap(__angka)
    else:
        item_hasil = []
        for item_angka in __angka:
            item_hasil.append(pembagian_bilangan_genap(item_angka))
        return item_hasil
def adalah_bilangan_ganjil(__angka : int | Iterable[int]) -> bool | list[bool]:
    def pembagian_bilangan_ganjil(__angka : int) -> bool:
        if __angka == 0:
            return False
        elif __angka < 0:
            __angka = balikkan_bilangan(__angka)
        if __angka % 2 == 0:
            return False
        else:
            return True
    if isinstance(__angka, int):
        return pembagian_bilangan_ganjil(__angka)
    else:
        item_hasil = []
        for item_angka in __angka:
            item_hasil.append(pembagian_bilangan_ganjil(item_angka))
        return item_hasil
def hasil_faktorial(__dari_bilangan : int | Iterable[int]) -> int | list[bool]:
    """
    Mengembalikan bilangan hasil dari faktorial\n
    AssertionError dihasilkan jika tidak dapat mengembalikan hasil dari faktorial
    """
    def proses_hasil_faktorial(__angka : int) -> int:
        assert __angka >= 1, f"Tidak dapat melakukan operasi hasil faktorial dari argumen {__dari_bilangan}"
        if __angka > 1:
            return __angka * hasil_faktorial(__angka - 1)
        else:
            return __angka
    if isinstance(__dari_bilangan, int):
        return proses_hasil_faktorial(__dari_bilangan)
    else:
        item_hasil : list = []
        for item_angka in __dari_bilangan:
            item_hasil.append(proses_hasil_faktorial(item_angka))
        return item_hasil
def deret_bilangan_prima(__maksimum_angka : int, __tuple_output : bool = False) -> list[int] | tuple[int]:
    "Fungsi untuk membuat deret bilangan prima. AssertionError dihasilkan jika argumen angka tidak valid untuk membuat deret bilangan prima"
    assert __maksimum_angka > 1, f"Tidak dapat membuat deret bilangan prima dari argumen angka maksimum {__maksimum_angka}"
    __maksimum_angka += 1
    bilangan_prima : list = []
    for deret_bilangan in range(2, __maksimum_angka):
        for nilai_pembagian in range(2, deret_bilangan):
            if deret_bilangan % nilai_pembagian == 0:
                break
        else:
            bilangan_prima.append(deret_bilangan)
    if __tuple_output:
        return tuple(bilangan_prima)
    else:
        return bilangan_prima
def adalah_bilangan_prima(__angka : int | Iterable[int]) -> bool | list[bool]:
    "Mengembalikan True jika argumen angka adalah bilangan prima. Mengembalikan False jika argumen angka bukan bilangan prima"
    def pembagian_bilangan_prima(__angka : int) -> bool:
        if __angka > 1:
            for nilai_pembagian in range(2, __angka):
                if __angka % nilai_pembagian == 0:
                    return False
            else:
                return True
        else:
            return False
    if isinstance(__angka, int):
        return pembagian_bilangan_prima(__angka)
    else:
        item_hasil = []
        for item_angka in __angka:
            item_hasil.append(pembagian_bilangan_prima(item_angka))
        return item_hasil
def adalah_habis_dibagi(__angka : int | float | Iterable[int | float], *, dibagi_dengan : int | float) -> bool | list[bool]:
    "Mengembalikan True jika angka habis dibagi, mengembalikan False jika tidak\n\nAssertionError dihasilkan jika argumen dibagi bernilai 0"
    assert dibagi_dengan != 0, "Pembagian Nol Tidak Valid Dalam Operasi Matematika"
    def proses_pembagian(__angka : int | float) -> bool:
        if __angka % dibagi_dengan == 0:
            return True
        else:
            return False
    if isinstance(__angka, int | float):
        return proses_pembagian(__angka)
    else:
        item_hasil : list = []
        for item_angka in __angka:
            item_hasil.append(proses_pembagian(item_angka))
        return item_hasil
@overload
def hasil_keliling_lingkaran(*, jari_jari : int | float | Iterable[int | float], bagian_lingkaran : int = 1) -> int | float | list[int | float]:
    "Rumus keliling lingkaran K = 2 x π x r"
    PESAN_ERROR = f"Tidak dapat melakukan operasi hasil keliling lingkaran dengan jari-jari lingkaran {jari_jari} dan jumlah bagian lingkaran {bagian_lingkaran}"
    assert bagian_lingkaran > 0, PESAN_ERROR
    def hasil_akhir(__jari_jari_lingkaran : int | float) -> int | float:
        assert __jari_jari_lingkaran > 0, PESAN_ERROR
        return 2 * NILAI_PI * __jari_jari_lingkaran / bagian_lingkaran
    if isinstance(jari_jari, int | float):
        return hasil_akhir(jari_jari)
    else:
        item_hasil : list = []
        for item_jari_jari_lingkaran in jari_jari:
            item_hasil.append(hasil_akhir(item_jari_jari_lingkaran))
        return item_hasil
@overload
def hasil_keliling_lingkaran(*, diameter : int | float | Iterable[int | float], bagian_lingkaran : int = 1) -> int | float | list[int | float]:
    "Rumus keliling lingkaran K = π x d"
    PESAN_ERROR = f"Tidak dapat melakukan operasi hasil keliling lingkaran dengan diameter {diameter} dan jumlah bagian lingkaran {bagian_lingkaran}"
    assert bagian_lingkaran > 0, PESAN_ERROR
    def hasil_akhir(__diameter_lingkaran : int | float) -> int | float:
        assert __diameter_lingkaran > 0, PESAN_ERROR
        return NILAI_PI * __diameter_lingkaran / bagian_lingkaran
    if isinstance(diameter, int | float):
        return hasil_akhir(diameter)
    else:
        item_hasil : list = []
        for item_diameter in diameter:
            item_hasil.append(hasil_akhir(item_diameter))
        return item_hasil
def hasil_luas_lingkaran(jari_jari : int | float | Iterable[int | float], *, bagian_lingkaran : int = 1) -> int | float | list[int | float]:
    "Rumus luas lingkaran L = π x r x r"
    PESAN_ERROR = f"Tidak dapat melakukan operasi hasil luas lingkaran dengan jari-jari lingkaran {jari_jari} dan jumlah bagian lingkaran {bagian_lingkaran}"
    assert bagian_lingkaran > 0, PESAN_ERROR
    def hasil_akhir(__jari_jari : int | float) -> int | float:
        assert __jari_jari > 0, PESAN_ERROR
        return NILAI_PI * __jari_jari * __jari_jari / bagian_lingkaran
    if isinstance(jari_jari, int | float):
        return hasil_akhir(jari_jari)
    else:
        item_hasil : list = []
        for item_jari_jari_lingkaran in jari_jari:
            item_hasil.append(hasil_akhir(item_jari_jari_lingkaran))
        return item_hasil
def hasil_keliling_persegi(sisi : int | float | Iterable[int | float]) -> int | float | list[int | float]:
    "Rumus keliling persegi K = sisi x 4"
    PESAN_ERROR = f"Tidak dapat melakukan operasi matematika keliling persegi dengan nilai sisi {sisi}"
    if isinstance(sisi, int | float):
        assert sisi > 0, PESAN_ERROR
        return sisi * __JUMLAH_SISI_PERSEGI
    else:
        item_hasil : list = []
        for item_sisi in sisi:
            assert item_sisi > 0, PESAN_ERROR
            item_hasil.append(item_sisi * __JUMLAH_SISI_PERSEGI)
        return item_hasil
def hasil_luas_persegi(sisi : int | float | Iterable[int | float]) -> int | float | list[int | float]:
    "Rumus luas persegi L = sisi x sisi"
    PESAN_ERROR = f"Tidak dapat melakukan operasi matematika luas persegi dengan nilai sisi {sisi}"
    if isinstance(sisi, int | float):
        assert sisi > 0, PESAN_ERROR
        return sisi * sisi
    else:
        item_hasil : list = []
        for item_sisi in sisi:
            assert item_sisi > 0, PESAN_ERROR
            item_hasil.append(item_sisi * item_sisi)
        return item_hasil
def hasil_keliling_persegi_panjang(*, panjang : int | float | Iterable[int | float], lebar : int | float | Iterable[int | float]) -> int | float | list[int | float]:
    "Rumus keliling persegi panjang K = (2 x panjang) + (2 x lebar)"
    PESAN_ERROR = f"Tidak dapat melakukan operasi matematika keliling persegi panjang dari panjang {panjang} dan lebar {lebar}"
    def hasil(__panjang : int | float, __lebar : int | float) -> int | float:
        syarat_operasi = __panjang >= 0 and __lebar >= 0
        assert syarat_operasi, PESAN_ERROR
        return (2 * __panjang) + (2 * __lebar)
    if isinstance(panjang, int | float) and (isinstance(lebar, int | float)):
        return hasil(panjang, lebar)
    else:
        panjang = list(panjang)
        lebar = list(lebar)
    syarat_operasi = (len(panjang) > 0 and len(lebar) > 0) and (len(panjang) == len(lebar))
    assert syarat_operasi, PESAN_ERROR
    item_hasil = []
    for indeks in range(len(panjang)):
        item_hasil.append(hasil(panjang[indeks], lebar[indeks]))
    return item_hasil
def hasil_keliling_segitiga(sisi_1 : int | float | Iterable[int | float], sisi_2 : int | float | Iterable[int | float], sisi_3 : int | float | Iterable[int | float]) -> int | float | list[int | float]:
    "Rumus keliling segitiga K = s + s + s"
    PESAN_ERROR = f"Tidak dapat melakukan operasi matematika keliling segitiga dengan K = {sisi_1} + {sisi_2} + {sisi_3}"
    def hasil(__sisi_1 : int | float, __sisi_2 : int | float, __sisi_3 : int | float) -> int | float:
        syarat_operasi = __sisi_1 >= 0 and __sisi_2 >= 0 and __sisi_3 >= 0
        assert syarat_operasi, PESAN_ERROR
        return __sisi_1 + __sisi_2 + __sisi_3
    if isinstance(sisi_1, int | float) and isinstance(sisi_2, int | float) and isinstance(sisi_3, int | float):
        return hasil(sisi_1, sisi_2, sisi_3)
    else:
        sisi_1 = list(sisi_1)
        sisi_2 = list(sisi_2)
        sisi_3 = list(sisi_3)
    syarat_operasi = (len(sisi_1) > 0 and len(sisi_2) > 0 and len(sisi_3) > 0) and (len(sisi_1) == len(sisi_2) and len(sisi_1) == len(sisi_3) and len(sisi_2) == len(sisi_3))
    assert syarat_operasi, PESAN_ERROR
    item_hasil = []
    for indeks in range(len(sisi_1)):
        item_hasil.append(hasil(sisi_1[indeks], sisi_2[indeks], sisi_3[indeks]))
    return item_hasil
def hasil_luas_segitiga(*, alas : int | float | Iterable[int | float], tinggi : int | float | Iterable[int | float]) -> int | float | list[int | float]:
    "Rumus luas segitiga L = ½ x a x t"
    PESAN_ERROR = f"Tidak dapat melakukan operasi matematika luas segitiga dengan alas {alas} dan tinggi {tinggi}"
    def hasil(__alas : int | float, __tinggi : int | float) -> int | float:
        syarat_operasi = __alas > 0 and __tinggi > 0
        assert syarat_operasi, PESAN_ERROR
        return SATU_PER_DUA * __alas * __tinggi
    if isinstance(alas, int | float) and isinstance(tinggi, int | float):
        return hasil(alas, tinggi)
    else:
        alas = list(alas)
        tinggi = list(tinggi)
    syarat_operasi = (len(alas) > 0 and len(tinggi) > 0) and (len(alas) == len(tinggi))
    assert syarat_operasi, PESAN_ERROR
    item_hasil : list = []
    for indeks in range(len(alas)):
        item_hasil.append(hasil(alas[indeks], tinggi[indeks]))
    return item_hasil
def hasil_pangkat(angka : int | Iterable[int], *, pangkat : int) -> int | list[int]:
    "Fungsi perpangkatan secara rekursif"
    def proses_pangkat(__angka : int, __pangkat : int) -> int:
        syarat_operasi = __angka > 0 and __pangkat > 0
        assert syarat_operasi, f"Tidak dapat melakukan operasi perpangkatan dari angka {__angka} pangkat {__pangkat}"
        if __pangkat == 1:
            return __angka
        else:
            return __angka * proses_pangkat(__angka, __pangkat - 1)
    if isinstance(angka, int):
        return proses_pangkat(angka, pangkat)
    else:
        item_hasil : list = []
        for item_angka in angka:
            item_hasil.append(proses_pangkat(item_angka, pangkat))
        return item_hasil
def hasil_persen(__persen : int = PERSEN, *, dari_angka : int | float | Iterable[int | float]) -> int | float | list[int | float]:
    assert __persen > 0, f"Tidak dapat melakukan operasi hasil {__persen}% dari {dari_angka}"
    def hasil(__dari_angka : int | float) -> int | float:
        return __dari_angka * __persen / PER_SERATUS
    if isinstance(dari_angka, int | float):
        return hasil(dari_angka)
    else:
        item_hasil = []
        for dari_item_angka in dari_angka:
            item_hasil.append(hasil(dari_item_angka))
        return item_hasil
