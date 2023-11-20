"Fungsi tambahan untuk string"

PEMBARUAN_TERAKHIR : str = "20 November 2023"
"Tanggal program terakhir kali diperbarui"

def abjad_tunggal_duplikasi(__string : str) -> bool:
    "Memeriksa abjad tunggal apakah terdapat abjad tunggal duplikasi atau tidak.\n\nMengembalikan True jika terdapat abjad tunggal duplikasi, mengembalikan False jika tidak"
    for abjad_tunggal in __string:
        if __string.count(abjad_tunggal) > 1:
            return True
    return False