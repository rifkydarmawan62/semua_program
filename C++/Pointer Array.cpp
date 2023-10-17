#include <iostream>

using namespace std;
/*Program pointer array dua dimensi*/
int main(void){
    /*Deklarasi pointer array dua dimensi*/
    short **pointer;
    /*Mendeklarasikan 3 baris*/
    pointer = new short *[3];
    /*Deklarasi item array multidimensi sekaligus meminta input dari pengguna*/
    for (short indeks_baris = 0; indeks_baris < 3; indeks_baris++){
        /*Mendeklarasikan 3 kolom untuk masing-masing baris*/
        pointer[indeks_baris] = new short [3];
        for (short indeks_kolom = 0; indeks_kolom < 3; indeks_kolom++){
            cout << "Masukkan nilai pointer[" << indeks_baris << "][" << indeks_kolom << "] : "; cin >> pointer[indeks_baris][indeks_kolom];
        }
    }
    /*Cetak data yang disimpan ke konsol*/
    for (short indeks_baris = 0; indeks_baris < 3; indeks_baris++){
        for (short indeks_kolom = 0; indeks_kolom < 3; indeks_kolom++){
            cout << "Nilai pointer[" << indeks_baris << "][" << indeks_kolom << "] = " << pointer[indeks_baris][indeks_kolom] << endl;
        }
    }
    /*Bebaskan memori*/
    for (short indeks_kolom = 0; indeks_kolom < 3; indeks_kolom++){
        delete[] pointer[indeks_kolom];
    }
    return 0;
}
