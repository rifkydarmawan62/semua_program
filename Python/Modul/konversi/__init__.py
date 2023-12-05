from collections import deque
from typing import Iterable

def desimal_ke_biner(__bilangan_desimal : int | Iterable[int]) -> str | list[str]:
    def hasil_bilangan_biner(__bilangan_desimal : int) -> str:
        assert __bilangan_desimal >= 0, "Operasi hanya mendukung bilangan positif"
        if __bilangan_desimal == 0 or __bilangan_desimal == 1:
            return str(__bilangan_desimal)
        else:
            bilangan_biner = deque()
            sisa_pembagian : int | None = None
            while True:
                sisa_pembagian, __bilangan_desimal = __bilangan_desimal % 2, int(__bilangan_desimal / 2)
                bilangan_biner.appendleft(sisa_pembagian)
                if __bilangan_desimal == 0 or __bilangan_desimal == 1:
                    break
            bilangan_biner.appendleft(__bilangan_desimal)
            hasil : str = ""
            for digit_biner in bilangan_biner:
                hasil += str(digit_biner)
            return hasil
    if isinstance(__bilangan_desimal, int):
        return hasil_bilangan_biner(__bilangan_desimal)
    else:
        hasil : list = []
        for item_bilangan_desimal in __bilangan_desimal:
            hasil.append(hasil_bilangan_biner(item_bilangan_desimal))
        return hasil