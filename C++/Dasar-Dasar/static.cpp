#include <iostream>

using namespace std;

class kelas_static{
    public:
        /*Fungsi static memperbolehkan pengguna untuk memanggil fungsi tanpa objek*/
        static void fungsi_static(){
            cout << "Fungsi static dipanggil\n";
        }
};
class kelas_non_static{
    public:
        /*Mencoba memanggil fungsi non static tanpa objek akan menghasilkan error*/
        void fungsi_non_static(){
           cout << "Fungsi non static dipanggil\n";
        }
};

int main(){
    /*fungsi_static dapat dipanggil tanpa objek*/
    kelas_static::fungsi_static();
    /*Membuat objek untuk kelas_non_static*/
    kelas_non_static objek_non_static;
    /*fungsi_non_static hanya dapat dipanggil dengan objek*/
    objek_non_static.fungsi_non_static();
    return 0;
}