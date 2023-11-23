"Fungsi tambahan untuk string"
from typing import Iterable

PEMBARUAN_TERAKHIR : str = "23 November 2023"
"Tanggal program terakhir kali diperbarui"

def abjad_tunggal_duplikasi(__string : str | Iterable[str]) -> bool | list[bool]:
    "Memeriksa abjad tunggal apakah terdapat abjad tunggal duplikasi atau tidak.\n\nMengembalikan True jika terdapat abjad tunggal duplikasi, mengembalikan False jika tidak"
    def proses_pemeriksaan_string(__string : str) -> bool:
        for abjad_tunggal in __string:
            if __string.count(abjad_tunggal) > 1:
                return True
        return False
    if isinstance(__string, str):
        return proses_pemeriksaan_string(__string)
    else:
        item_hasil : list = []
        for item_string in __string:
            item_hasil.extend([proses_pemeriksaan_string(item_string)])
        return item_hasil