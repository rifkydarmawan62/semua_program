# Author
> rifkydarmawan62

# Alat
> | Nama | Kategori Program |
> | --- | --- |
> | [Program Script Python CLI](https://github.com/rifkydarmawan62/program_publik/blob/Publik/Python/Modul/__main__.py) | Program Python Terminal/Konsol |
> | Metode Peretasan | [Modul Python](https://github.com/rifkydarmawan62/program_publik/tree/Publik/Python/Modul/metode_peretasan)<br>[Modul PHP](https://github.com/rifkydarmawan62/program_publik/tree/Publik/PHP/Modul/metode_peretasan.php) |
> | Fungsi String | [Modul Python](https://github.com/rifkydarmawan62/program_publik/tree/Publik/Python/Modul/fungsi_string)<br>[Modul PHP](https://github.com/rifkydarmawan62/program_publik/tree/Publik/PHP/Modul/fungsi_string.php) |
> | Fungsi Matematika | [Modul Python](https://github.com/rifkydarmawan62/program_publik/blob/Publik/Python/Modul/fungsi_matematika)<br>Modul PHP (segera hadir) |
> | [Manipulasi Data](https://github.com/rifkydarmawan62/program_publik/blob/Publik/Python/Modul/manipulasi_data) | Modul Python |
> ## [Kriptografi](https://github.com/rifkydarmawan62/program_publik/tree/Publik/Python/Modul/kriptografi)
>> | Nama | Kategori Program |
>> | --- | --- |
>> | [Encode and Decode Standard Unicode Character](https://github.com/rifkydarmawan62/program_publik/blob/Publik/Python/Modul/kriptografi/unicode_standar.py) | Modul Python |
> ## [Konfigurasi Jaringan Internet](https://github.com/rifkydarmawan62/program_publik/tree/Publik/Python/Modul/jaringan_internet)
>> | Nama | Kategori Program |
>> | --- | --- |
>> | [port](https://github.com/rifkydarmawan62/program_publik/tree/Publik/Python/Modul/jaringan_internet/port) | Modul Python |
>> | [netmask](https://github.com/rifkydarmawan62/program_publik/tree/Publik/Python/Modul/jaringan_internet/netmask) | Modul Python |
> ## Konfigurasi Waktu
>> | Nama | Kategori Program |
>> | --- | --- |
>> | [waktu_sekarang](https://github.com/rifkydarmawan62/program_publik/blob/Publik/Python/Modul/waktu_sekarang/__init__.py) | Modul Python |
> ## Lainnya
>> | Nama | Kategori Program |
>> | --- | --- |
>> | [manager file txt](https://github.com/rifkydarmawan62/program_publik/tree/Publik/Python/Manager%20File%20txt) | Program Python Aplikasi Desktop |
>> | [Konversi Warna](https://github.com/rifkydarmawan62/program_publik/blob/Publik/Python/Konversi%20Warna.py) | Program Python Aplikasi Desktop |
>> | [Pointer Array Dua Dimensi](https://github.com/rifkydarmawan62/program_publik/blob/Publik/C++/Dasar-Dasar/Pointer%20Array.cpp) | Program C++ Terminal/Konsol |
>> | [static dan non static](https://github.com/rifkydarmawan62/program_publik/blob/Publik/C%2B%2B/Dasar-Dasar/static%20dan%20non%20static.cpp) | Program C++ Terminal/Konsol |
# Disclaimer dan Informasi:
> Program yang dibuat bukan untuk **tujuan ILEGAL apapun**!  
> **Pengembang tidak bertanggung jawab** terhadap **tindakan pengguna yang menggunakan program ini untuk tujuan ilegal!**
# Bantuan
> ## Memulai Dengan Python
>> 1. Download dan Instal Bahasa Pemrograman Python
>>    
>>    Download dan unduh bahasa pemrograman Python dari situs resmi https://www.python.org/downloads/ lalu lakukan instalasi
>> 2. Buka control panel atau panel kontrol
>> 3. Cari variabel dan pilih Edit variabel lingkungan sistem (membutuhkan akses administrator)
>>   
>>    ![aset_gambar_1](https://github.com/rifkydarmawan62/program_publik/blob/Publik/Aset/Gambar/Memulai%20Dengan%20Python/1.png)
>> 4. Pilih environment variables
>>
>>    ![aset_gambar_2](https://github.com/rifkydarmawan62/program_publik/blob/Publik/Aset/Gambar/Memulai%20Dengan%20Python/2.png)
>> 5. Pilih path system variable (untuk seluruh pengguna) atau path user variable (untuk 1 pengguna) lalu tekan Edit > New lalu salin direktori folder Python ke edit environment variable tekan ok untuk semua jendela yang sedang dibuka
>>
>>    ![aset_gambar_3](https://github.com/rifkydarmawan62/program_publik/blob/Publik/Aset/Gambar/Memulai%20Dengan%20Python/3.png)
>> 6. Download IDE (Integrated Development Environment)
>>    
>>    Download Visual Studio Code sebagai IDE utama dari situs resmi https://code.visualstudio.com/download lalu buat file Python dengan format .py dan tulis program
>>    ~~~Python
>>    print("Hello World")
>>    ~~~
>>    Sebagai program pertama Python
>> 7. Pelajari dan kuasai syntax dasar bahasa pemrograman Python
>> 8. Eksplorasi pustaka standar Python
>>
>>    Anda dapat menemukan pustaka standar Python pada situs dokumentasi pemrograman Python di https://docs.python.org/3/
>> 9. Eksplorasi pustaka Python pihak ketiga
>>
>>    Terdapat pustaka Python pihak ketiga seperti NumPy, TensorFlow, Matplotlib, dan lain-lain di situs https://pypi.org/ dan dapat diunduh dan diinstal dengan menginput baris perintah di bawah ini pada PowerShell
>>    ~~~PowerShell
>>    pip install package_name
>>    ~~~
>> 10. Teruslah belajar
> ## Dokumentasi
>> ### Metode Peretasan
>>> - ~~~Python
>>>   PEMBARUAN_TERAKHIR : Literal[str]
>>>   ~~~
>>>   
>>>   Tanggal program terakhir kali diperbarui
>>> #### Exception
>>>> - ~~~Python
>>>>   class exception_karakter_kata_sandi_bukan_ascii
>>>>   ~~~
>>>>   Exception untuk karakter kata sandi non ascii
>>>>   
>>>> - ~~~Python
>>>>   class exception_abjad_tunggal_duplikasi
>>>>   ~~~
>>>>   Exception untuk abjad tunggal yang memiliki duplikasi
>>> #### Fungsi
>>>> - ~~~Python
>>>>   def brute_force_standar(karakter_kata_sandi : str, panjang_kata_sandi : int) -> typing.Iterator[str]
>>>>   ~~~
>>>>   Metode serangan brute force standar.  
>>>>   Kemungkinan exception:
>>>>   ~~~Python
>>>>   raise exception_karakter_kata_sandi_bukan_ascii
>>>>   raise exception_abjad_tunggal_duplikasi
>>>>   ~~~
>>>>   Penggunaan:
>>>>   ~~~Python
>>>>   from metode_peretasan import *
>>>>   
>>>>   for serangan_brute_force in brute_force_standar("abcdefghijklmnopqrstuvwxyz", 2):
>>>>       "Program berbahaya untuk serangan brute force"
>>>>   ~~~
>>>> - ~~~Python
>>>>   def kamus(string_judul = False, string_kapital = False, string_huruf_besar = False, string_huruf_kecil = False, hanya_karakter_ascii = False) -> typing.Iterator[str] | typing.Iterator[typing.Literal[False]]
>>>>   ~~~
>>>>   Metode serangan dictionary.
>>>>   Program akan meminta file txt untuk serangan dictionary.
>>>>   False akan dihasilkan saat Iterator sedang berlangsung jika file tidak dibuka.  
>>>>   Penggunaan :
>>>>   ~~~Python
>>>>   from metode_peretasan import *
>>>>   
>>>>   for serangan_dictionary in kamus():
>>>>       "Program berbahaya untuk serangan dictionary"
>>>>   ~~~
>>>> - ~~~Python
>>>>   def brute_force_heksadesimal(jumlah_digit_heksadesimal : int, output_bawan = True) -> typing.Iterator[str]:
>>>>       assert jumlah_digit_heksadesimal > 0, "Jumlah Digit Harus Lebih Dari Nol!"
>>>>   ~~~
>>>>   Melancarkan serangan brute force heksadesimal.  
>>>>   Penggunaan :
>>>>   ~~~Python
>>>>   from metode_peretasan import *
>>>>   
>>>>   for heksadesimal in brute_force_heksadesimal(jumlah_digit_heksadesimal : 2, output_bawan = True):
>>>>       "Program berbahaya untuk brute force heksadesimal"
>>>>   ~~~
>>>> - ~~~Python
>>>>   def brute_force_pin(jumlah_digit : int, string_output = False) -> typing.Iterator[str] | typing.Iterator[int]:
>>>>       assert jumlah_digit > 0, "Jumlah Digit Harus Lebih Dari Nol!"
>>>>   ~~~
>>>>   Melancarkan serangan brute force pin.  
>>>>   Penggunaan:
>>>>   ~~~Python
>>>>   from metode_peretasan import *
>>>>   
>>>>   for serangan_pin in brute_force_pin(4, True):
>>>>       "Program berbahaya untuk brute force pin"
>>>>   ~~~
>>>> - ~~~Python
>>>>   def brute_force_oktal(jumlah_digit_oktal : int, output_bawaan = True) -> typing.Iterator[str]:
>>>>       assert jumlah_digit_oktal > 0, "Jumlah Digit Oktal Harus Lebih Dari Nol!"
>>>>   ~~~
>>>>   Melancarkan serangan brute force oktal.  
>>>>   Penggunaan:
>>>>   ~~~Python
>>>>   from metode_peretasan import *
>>>>   
>>>>   for serangan_oktal in brute_force_oktal(2):
>>>>       "Program berbahaya untuk brute force oktal"
>>>>   ~~~
>>>> - ~~~Python
>>>>   def brute_force_biner(jumlah_digit_biner : int, tipe_output : typing.Literal["integer", "string", "bawaan"]) -> typing.Iterator[str] | typing.Iterator[int]:
>>>>       assert jumlah_digit_biner > 0, "Jumlah Digit Biner Harus Lebih Dari Nol!"
>>>>   ~~~
>>>>   Melancarkan serangan brute force biner.  
>>>>   Penggunaan:
>>>>   ~~~Python
>>>>   from metode_peretasan import *
>>>>   
>>>>   for serangan_biner in brute_force_biner(8, "string"):
>>>>       "Program berbahaya untuk brute force biner"
>>>>   ~~~
> ## Instalasi
>> 1. Pastikan anda telah menginstal git terlebih dahulu dari https://git-scm.com
>> 2. Ganti direktori file yang akan diunduh
>>    ~~~bash
>>    cd direktori\file\yang\akan\diunduh
>>    ~~~
>> 3. Download repository pemrograman saya
>>    ~~~bash
>>    git clone https://github.com/rifkydarmawan62/program_publik
>>    ~~~
# Media Sosial
> - Instagram : [@rifkydarmawan62](https://www.instagram.com/rifkydarmawan62/)
