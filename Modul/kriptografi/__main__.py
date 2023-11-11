import csv, os, base64, binascii, platform, subprocess
from tkinter.filedialog import askopenfilename, askdirectory
from typing import Literal
from unicode_standar import *
try:
    def cetak_informasi_pengembang():
        print("Instagram : @rifkydarmawan62")
        print("GitHub : rifkydarmawan62\n")
    def bersihkan_layar():
        sistem_operasi = platform.system()
        if sistem_operasi == "Windows":
            os.system("cls")
        else:
            os.system("clear")
    def menu_encode_dan_decode_unicode_standar():
        bersihkan_layar()
        print("beranda > kriptografi > unicode standar\n")
        cetak_informasi_pengembang()
        print("Daftar Menu Encode dan Decode Unicode Standar")
        print("[1] encode heksadesimal")
        print("[2] encode desimal")
        print("[3] encode oktal")
        print("[4] encode biner")
        print("[5] decode heksadesimal")
        print("[6] decode desimal")
        print("[7] decode oktal")
        print("[8] decode biner")
        print("[9] bantuan")
        print("[10] bersihkan")
        print("[11] kembali")
        print("[12] beranda")
        print("[13] keluar (Ctrl + C)\n")
        def pilih_menu_encode_dan_decode():
            menu_yang_dipilih = input("Pilih nomor : ")
            if menu_yang_dipilih == "1":
                pilih_file_unicode_standar("encoding heksadesimal")
            elif menu_yang_dipilih == "2":
                pilih_file_unicode_standar("encoding desimal")
            elif menu_yang_dipilih == "3":
                pilih_file_unicode_standar("encoding oktal")
            elif menu_yang_dipilih == "4":
                pilih_file_unicode_standar("encoding biner")
            elif menu_yang_dipilih == "5":
                pilih_file_unicode_standar("decoding heksadesimal")
            elif menu_yang_dipilih == "6":
                pilih_file_unicode_standar("decoding desimal")
            elif menu_yang_dipilih == "7":
                pilih_file_unicode_standar("decoding oktal")
            elif menu_yang_dipilih == "8":
                pilih_file_unicode_standar("decoding biner")
            elif menu_yang_dipilih == "9":
                bersihkan_layar()
                print("beranda > kriptografi > unicode standar > bantuan\n")
                cetak_informasi_pengembang()
                print("Menyediakan keamanan data dan kerahasiaan data file teks dengan kriptografi unicode standar")
                print("Encode dan decode unicode standar hanya dapat digunakan pada teks karakter unicode yang akan di encode menjadi bilangan heksadesimal, desimal, oktal, dan biner.")
                print("Sebaliknya data yang telah di encode dapat di decode kembali menjadi teks karakter unicode jika data yang telah di encode adalah valid\n")
                input("Tekan enter untuk menutup (Ctrl + C untuk keluar)")
                menu_encode_dan_decode_unicode_standar()
            elif menu_yang_dipilih == "10":
                menu_encode_dan_decode_unicode_standar()
            elif menu_yang_dipilih == "11":
                menu_kriptografi()
            elif menu_yang_dipilih == "12":
                beranda()
            elif menu_yang_dipilih == "13":
                print("Menutup program ...")
                exit(0)
            else:
                print("Input Tidak Valid!")
                pilih_menu_encode_dan_decode()
        pilih_menu_encode_dan_decode()
    def pilih_file_unicode_standar(_encode_atau_decode : Literal["encoding heksadesimal", "encoding desimal", "encoding oktal", "encoding biner", "decoding heksadesimal", "decoding desimal", "decoding oktal", "decoding biner"]):
        print("Tekan ALT + Tab untuk membuka jendela baru untuk memilih file")
        def kembali_ke_menu_unicode_standar():
            input("Tekan enter untuk kembali (Ctrl + C untuk keluar)")
            menu_encode_dan_decode_unicode_standar()
        def baca_file(__direktori_file : str):
            if __direktori_file:
                print(f"Direktori file untuk {_encode_atau_decode} {__direktori_file}")
                if ".csv" == __direktori_file[-4:].lower():
                    decoded_data : str = ""
                    with open(__direktori_file, "r") as file_yang_di_baca:
                        file_csv = csv.reader(file_yang_di_baca)
                        print("Data sebelum di decode : ")
                        for data_per_baris in file_csv:
                            print(data_per_baris)
                            if _encode_atau_decode == "decoding heksadesimal":
                                decoded_data = decoding_heksadesimal(data_per_baris)
                            if _encode_atau_decode == "decoding desimal":
                                decoded_data = decoding_desimal(data_per_baris)
                            if _encode_atau_decode == "decoding oktal":
                                decoded_data = decoding_oktal(data_per_baris)
                            if _encode_atau_decode == "decoding biner":
                                decoded_data = decoding_biner(data_per_baris)
                            break
                    print("Data setelah di decode : ")
                    print(decoded_data)
                    print("Tekan ALT + Tab untuk membuka jendela baru untuk menyimpan data setelah di decode")
                    lokasi_folder_file_yang_di_decode = askdirectory(title = "Pilih Folder Untuk Menyimpan File Yang Di Decode")
                    if lokasi_folder_file_yang_di_decode:
                        nama_file_yang_di_decode = f"{input('*Masukkan nama file (txt): ')}.txt"
                        with open(f"{lokasi_folder_file_yang_di_decode}/{nama_file_yang_di_decode}", "x") as file_baru:
                            file_baru.write(decoded_data)
                        print(f"File baru dibuat di direktori {lokasi_folder_file_yang_di_decode}/{nama_file_yang_di_decode}")
                        kembali_ke_menu_unicode_standar()
                    else:
                        print("Data yang telah di decode tidak disimpan")
                        kembali_ke_menu_unicode_standar()
                elif ".txt" == __direktori_file[-4:].lower():
                    if "encoding" in _encode_atau_decode:
                        encoded_data : list = []
                        with open(__direktori_file, "r") as file_yang_di_baca:
                            print("Melakukan encoding file ...")
                            for data_per_baris in file_yang_di_baca:
                                if _encode_atau_decode == "encoding heksadesimal":
                                    encoded_data.extend(encoding_heksadesimal(data_per_baris))
                                elif _encode_atau_decode == "encoding desimal":
                                    encoded_data.extend(encoding_desimal(data_per_baris))
                                elif _encode_atau_decode == "encoding oktal":
                                    encoded_data.extend(encoding_oktal(data_per_baris))
                                elif _encode_atau_decode == "encoding biner":
                                    encoded_data.extend(encoding_biner(data_per_baris))
                        print("Data setelah di encode : ")
                        print(encoded_data)
                        print("Tekan ALT + Tab untuk membuka jendela baru untuk menyimpan data setelah di encode")
                        lokasi_folder_file_yang_di_encode = askdirectory(title = "Pilih Folder Untuk Menyimpan File Yang Di Encode")
                        if lokasi_folder_file_yang_di_encode:
                            nama_file_yang_di_encode = input("*Masukkan nama file (Berikutnya tipe file): ")
                            tipe_file_yang_di_encode = input("*Pilih tipe file [txt/csv]: ")
                            tipe_file : str = ""
                            if tipe_file_yang_di_encode.lower()[-3:] == "csv":
                                tipe_file = ".csv"
                            elif tipe_file_yang_di_encode.lower()[-3:] == "txt":
                                tipe_file = ".txt"
                            else:
                                print("Tipe File Tidak Valid!")
                                kembali_ke_menu_unicode_standar()
                            with open(f"{lokasi_folder_file_yang_di_encode}/{nama_file_yang_di_encode}{tipe_file}", "x") as file_baru:
                                if tipe_file == ".csv":
                                    file_csv_baru = csv.writer(file_baru)
                                    file_csv_baru.writerow(encoded_data)
                                else:
                                    for karakter_tunggal_encoded in encoded_data:
                                        file_baru.write(f"{karakter_tunggal_encoded}\n")
                            print(f"File baru dibuat di direktori {lokasi_folder_file_yang_di_encode}/{nama_file_yang_di_encode}{tipe_file}")
                            kembali_ke_menu_unicode_standar()
                        else:
                            print("Data yang telah di encode tidak disimpan!")
                            kembali_ke_menu_unicode_standar()
                    else:
                        print("Data sebelum di decode : ")
                        #With Pertama
                        with open(__direktori_file, "r") as file_yang_di_baca:
                            #Iterator pertama
                            for data_per_baris in file_yang_di_baca:
                                print(data_per_baris.strip())
                            print("Melakukan decoding file ...")
                            #Iterator untuk membaca file tidak dapat dilakukan sebanyak 2 kali setiap membuka sebuah file dengan fungsi with untuk decoding file
                            #Iterator kedua akan dilanjutkan di fungsi with kedua
                        decoded_data : str = ""
                        #Fungsi with kedua
                        with open(__direktori_file, "r") as file_yang_di_baca:
                            #Iterator kedua
                            for data_per_baris in file_yang_di_baca:
                                if _encode_atau_decode == "decoding heksadesimal":
                                    decoded_data = decoded_data + decoding_heksadesimal(data_per_baris.strip())
                                elif _encode_atau_decode == "decoding desimal":
                                    decoded_data = decoded_data + decoding_desimal(data_per_baris.strip())
                                elif _encode_atau_decode == "decoding oktal":
                                    decoded_data = decoded_data + decoding_oktal(data_per_baris.strip())
                                elif _encode_atau_decode == "decoding biner":
                                    decoded_data = decoded_data + decoding_biner(data_per_baris.strip())
                        print("Data setelah di decode : ")
                        print(decoded_data)
                        print("Tekan ALT + Tab untuk membuka jendela baru untuk menyimpan data setelah di decode")
                        lokasi_folder_file_yang_di_decode = askdirectory(title = "Pilih Folder Untuk Menyimpan Data Yang Di Decode")
                        if lokasi_folder_file_yang_di_decode:
                            nama_file_yang_di_decode = f"{input('*Masukkan nama file (txt): ')}.txt"
                            with open(f"{lokasi_folder_file_yang_di_decode}/{nama_file_yang_di_decode}", "x") as file_baru:
                                file_baru.write(decoded_data)
                            print(f"File baru dibuat di direktori {lokasi_folder_file_yang_di_decode}/{nama_file_yang_di_decode}")
                            kembali_ke_menu_unicode_standar()
                        else:
                            print("Data yang telah di decode tidak disimpan!")
                            kembali_ke_menu_unicode_standar()
            else:
                print("File Tidak Dibuka!")
                kembali_ke_menu_unicode_standar()
        if "encoding" in _encode_atau_decode.lower():
            direktori_file = askopenfilename(title = f"Pilih File Untuk {_encode_atau_decode.title()}", filetypes = [("Dokumen Teks", "*.txt")])
            baca_file(direktori_file)
        else:
            direktori_file = askopenfilename(title = f"Pilih File Untuk {_encode_atau_decode.title()}", filetypes = [("Dokumen Teks", "*.txt"), ("Comma Separate Value", "*.csv")])
            baca_file(direktori_file)
    def menu_encode_dan_decode_python_base64():
        bersihkan_layar()
        print("beranda > kriptografi > python base64\n")
        cetak_informasi_pengembang()
        print("Daftar Menu Encode dan Decode Python Base64")
        print("[1] base 16 encode (ASCII)")
        print("[2] base 16 decode (ASCII)")
        print("[3] base 32 encode (ASCII)")
        print("[4] base 32 decode (ASCII)")
        print("[5] base 32 hex encode (Extended Hex Alphabet)")
        print("[6] base 32 hex decode (Extended Hex Alphabet)")
        print("[7] base 64 encode (ASCII)")
        print("[8] base 64 decode (ASCII)")
        print("[9] standard base 64 encode (ASCII Alphabet)")
        print("[10] standard base 64 decode (ASCII Alphabet)")
        print("[11] base 85 encode (ASCII)")
        print("[12] base 85 decode (ASCII)")
        print("[13] bantuan")
        print("[14] bersihkan")
        print("[15] kembali")
        print("[16] beranda")
        print("[17] keluar (Ctrl + C)")
        def kembali_ke_menu_python_base64():
            input("Tekan enter untuk kembali (Ctrl + C untuk keluar)")
            menu_encode_dan_decode_python_base64()
        def pilih_nomor():
            nomor_yang_dipilih = input("Pilih nomor : ")
            NOMOR_1_SAMPAI_12 = "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"
            NOMOR_ENCODE = "1", "3", "5", "7", "9", "11"
            if nomor_yang_dipilih in NOMOR_1_SAMPAI_12:
                print("Tekan ALT + Tab untuk membuka jendela baru untuk memilih file")
                encode_atau_decode : tuple
                if nomor_yang_dipilih in NOMOR_ENCODE:
                    encode_atau_decode = "Encoding", "encode"
                else:
                    encode_atau_decode = "Decoding", "decode"
                direktori_file = askopenfilename(title = f"Pilih File Untuk {encode_atau_decode[0]}", filetypes = [("Dokumen Teks", "*.txt")])
                if direktori_file:
                    print(f"Direktori file untuk {encode_atau_decode[0].lower()} {direktori_file}")
                    if encode_atau_decode[0] == "Decoding":
                        print("Data sebelum di decode : ")
                        with open(direktori_file, "r") as file_yang_di_buka:
                            for data_per_baris in file_yang_di_buka:
                                print(data_per_baris.strip())
                    encoded_data : bytes = b""
                    decoded_data : bytes = b""
                    print(f"Melakukan {encode_atau_decode[0].lower()} file ...")
                    try:
                        with open(direktori_file, "r") as file_yang_di_buka:
                            for data_per_baris in file_yang_di_buka:
                                data_per_baris = bytes(data_per_baris, "utf-8")
                                if nomor_yang_dipilih == "1":
                                    encoded_data = encoded_data + base64.b16encode(data_per_baris)
                                elif nomor_yang_dipilih == "2":
                                    decoded_data = decoded_data + base64.b16decode(data_per_baris)
                                elif nomor_yang_dipilih == "3":
                                    encoded_data = encoded_data + base64.b32encode(data_per_baris)
                                elif nomor_yang_dipilih == "4":
                                    decoded_data = decoded_data + base64.b32decode(data_per_baris)
                                elif nomor_yang_dipilih == "5":
                                    encoded_data = encoded_data + base64.b32hexencode(data_per_baris)
                                elif nomor_yang_dipilih == "6":
                                    decoded_data = decoded_data + base64.b32hexdecode(data_per_baris)
                                elif nomor_yang_dipilih == "7":
                                    encoded_data = encoded_data + base64.b64encode(data_per_baris)
                                elif nomor_yang_dipilih == "8":
                                    decoded_data = decoded_data + base64.b64decode(data_per_baris)
                                elif nomor_yang_dipilih == "9":
                                    encoded_data = encoded_data + base64.standard_b64encode(data_per_baris)
                                elif nomor_yang_dipilih == "10":
                                    decoded_data = decoded_data + base64.standard_b64decode(data_per_baris)
                                elif nomor_yang_dipilih == "11":
                                    encoded_data = encoded_data + base64.a85encode(data_per_baris)
                                elif nomor_yang_dipilih == "12":
                                    decoded_data = decoded_data + base64.a85decode(data_per_baris)
                                else:
                                    break
                    except binascii.Error as ascii_error:
                        print(f"Terjadi error saat melakukan {encode_atau_decode[0].lower()} file")
                        print(f"Pesan error : {ascii_error}")
                        kembali_ke_menu_python_base64()
                    else:
                        print(f"Data setelah di {encode_atau_decode[1]} : ")
                        if encode_atau_decode[1] == "encode":
                            print(encoded_data)
                        else:
                            print(decoded_data)
                        print(f"Tekan ALT + Tab untuk membuka jendela baru untuk menyimpan data setelah di {encode_atau_decode[1]}")
                        lokasi_folder_file = askdirectory(title = f"Pilih Folder Untuk Menyimpan Data Yang Di {encode_atau_decode[1]}")
                        if lokasi_folder_file:
                            nama_file = f"{input('Masukkan nama file (.txt) : ')}.txt"
                            with open(f"{lokasi_folder_file}/{nama_file}", "x") as file_baru:
                                if encode_atau_decode[1] == "encode":
                                    file_baru.write(encoded_data.decode())
                                else:
                                    file_baru.write(decoded_data.decode())
                            print(f"File baru dibuat di direktori {lokasi_folder_file}/{nama_file}")
                            kembali_ke_menu_python_base64()
                        else:
                            print(f"Data yang telah di {encode_atau_decode[1]} tidak disimpan!")
                            kembali_ke_menu_python_base64()
                else:
                    print("File Tidak Dibuka!")
                    kembali_ke_menu_python_base64()
            elif nomor_yang_dipilih == "13":
                bersihkan_layar()
                print("beranda > kriptografi > python base64 > bantuan\n")
                cetak_informasi_pengembang()
                print("Menyediakan kriptografi yang lebih kompleks dengan pustaka standar python base64 untuk keamanan dan kerahasiaan data file txt")
                print("Namun encoding dan decoding yang salah dapat menyebabkan perubahan data yang tidak benar dan data tidak dapat dibaca")
                input("Tekan enter untuk menutup (Ctrl + C untuk keluar)")
                menu_encode_dan_decode_python_base64()
            elif nomor_yang_dipilih == "14":
                menu_encode_dan_decode_python_base64()
            elif nomor_yang_dipilih == "15":
                menu_kriptografi()
            elif nomor_yang_dipilih == "16":
                beranda()
            elif nomor_yang_dipilih == "17":
                print("Menutup program ...")
                exit(0)
            else:
                print("Input Tidak Valid!")
                pilih_nomor()
        pilih_nomor()
    def menu_kriptografi():
        bersihkan_layar()
        print("beranda > kriptografi\n")
        cetak_informasi_pengembang()
        print("Daftar Menu Kriptografi")
        print("[1] unicode standar")
        print("[2] python base64")
        print("[3] bersihkan")
        print("[4] beranda")
        print("[5] keluar (Ctrl + C)\n")
        def pilih_nomor():
            nomor_yang_dipilih = input("Pilih nomor : ")
            if nomor_yang_dipilih == "1":
                menu_encode_dan_decode_unicode_standar()
            elif nomor_yang_dipilih == "2":
                menu_encode_dan_decode_python_base64()
            elif nomor_yang_dipilih == "3":
                menu_kriptografi()
            elif nomor_yang_dipilih == "4":
                beranda()
            elif nomor_yang_dipilih == "5":
                print("Menutup program ...")
                exit(0)
            else:
                print("Input Tidak Valid!")
                pilih_nomor()
        pilih_nomor()
    def menu_kalkulator():
        bersihkan_layar()
        print("beranda > kalkulator\n")
        cetak_informasi_pengembang()
        print("Daftar menu kalkulator")
        print("[1] kalkulator dasar")
        print("[2] konversi satuan bilangan")
        print("[3] bersihkan")
        print("[4] beranda")
        print("[5] keluar (Ctrl + C)\n")
        def pilih_menu():
            menu_yang_dipilih = input("Pilih nomor : ")
            if menu_yang_dipilih == "1":
                menu_kalkulator_dasar()
            elif menu_yang_dipilih == "2":
                menu_konversi_satuan_bilangan()
            elif menu_yang_dipilih == "3":
                menu_kalkulator()
            elif menu_yang_dipilih == "4":
                beranda()
            elif menu_yang_dipilih == "5":
                print("Menutup program ...")
                exit(0)
            else:
                print("Input Tidak Valid!")
                pilih_menu()
        pilih_menu()
    def menu_kalkulator_dasar():
        bersihkan_layar()
        print("beranda > kalkulator > kalkulator dasar\n")
        cetak_informasi_pengembang()
        print("Daftar menu : ")
        print("[1] bersihkan")
        print("[2] kembali")
        print("[3] beranda")
        print("[4] keluar\n")
        print("Simbol operator : ")
        print("Operator penjumlahan (+)")
        print("Operator pengurangan (-)")
        print("Operator perkalian (*)")
        print("Operator pangkat 2 atau kuadrat (**)")
        print("Operator pembagian (/)")
        print("Operator pembagian dengan hasil tipe data integer (//)")
        print("Operator sisa pembagian (%)\n")
        print("Contoh input : 1+1")
        #print("*Input dapat berupa objek variabel, kelas, atau fungsi")
        def input_operator_atau_pilih_menu():
            operasi_yang_diinput = input("Masukkan input : ")
            if operasi_yang_diinput == "1":
                menu_kalkulator_dasar()
            elif operasi_yang_diinput == "2":
                menu_kalkulator()
            elif operasi_yang_diinput == "3":
                beranda()
            elif operasi_yang_diinput == "4":
                print("Menutup program ...")
                exit(0)
            try:
                operasi_yang_diinput = eval(operasi_yang_diinput)
            except SyntaxError:
                print("Input Operator Tidak Valid!")
                input_operator_atau_pilih_menu()
            except NameError:
                print("Tidak dapat melakukan operasi terhadap nama variabel, kelas, atau fungsi")
                input_operator_atau_pilih_menu()
            except ZeroDivisionError:
                print("Pembagian Nol Tidak Valid!")
                input_operator_atau_pilih_menu()
            else:
                print(f"Hasil = {operasi_yang_diinput}")
                input_operator_atau_pilih_menu()
        input_operator_atau_pilih_menu()
    def menu_konversi_satuan_bilangan():
        bersihkan_layar()
        print("beranda > kalkulator > konversi satuan bilangan\n")
        cetak_informasi_pengembang()
        print("Daftar menu konversi satuan bilangan")
        print("[1] konversi bilangan heksadesimal ke bilangan desimal")
        print("[2] konversi bilangan desimal ke bilangan heksadesimal")
        print("[3] konversi bilangan heksadesimal ke bilangan oktal")
        print("[4] konversi bilangan oktal ke bilangan heksadesimal")
        print("[5] konversi bilangan heksadesimal ke bilangan biner")
        print("[6] konversi bilangan biner ke bilangan heksadesimal")
        print("[7] konversi bilangan desimal ke bilangan oktal")
        print("[8] konversi bilangan oktal ke bilangan desimal")
        print("[9] konversi bilangan desimal ke bilangan biner")
        print("[10] konversi bilangan biner ke bilangan desimal")
        print("[11] konversi bilangan oktal ke bilangan biner")
        print("[12] konversi bilangan biner ke bilangan oktal")
        print("[13] bersihkan")
        print("[14] kembali")
        print("[15] beranda")
        print("[16] keluar (Ctrl + C)")
        def kembali_ke_menu_konversi_satuan_bilangan():
            input("Tekan enter untuk menutup (Ctrl + C untuk keluar)")
            menu_konversi_satuan_bilangan()
        def pilih_menu():
            nomor_yang_dipilih = input("Pilih nomor : ")
            try:
                if nomor_yang_dipilih == "1":
                    bilangan_heksadesimal = input("Masukkan bilangan heksadesimal : ")
                    print(f"Hasil bilangan desimal = {int('0x' + bilangan_heksadesimal, base = 0)}")
                    kembali_ke_menu_konversi_satuan_bilangan()
                elif nomor_yang_dipilih == "2":
                    bilangan_desimal = input("Masukkan bilangan desimal : ")
                    print(f"Hasil bilangan heksadesimal = {hex(int(bilangan_desimal))[2:]}")
                    kembali_ke_menu_konversi_satuan_bilangan()
                elif nomor_yang_dipilih == "3":
                    bilangan_heksadesimal = input("Masukkan bilangan heksadesimal : ")
                    print(f"Hasil bilangan oktal = {oct(int('0x' + bilangan_heksadesimal, base = 0))[2:]}")
                    kembali_ke_menu_konversi_satuan_bilangan()
                elif nomor_yang_dipilih == "4":
                    bilangan_oktal = input("Masukkan bilangan oktal : ")
                    print(f"Hasil bilangan heksadesimal = {hex(int('0o' + bilangan_oktal, base = 0))[2:]}")
                    kembali_ke_menu_konversi_satuan_bilangan()
                elif nomor_yang_dipilih == "5":
                    bilangan_heksadesimal = input("Masukkan bilangan heksadesimal : ")
                    print(f"Hasil bilangan biner = {bin(int('0x' + bilangan_heksadesimal, base = 0))[2:]}")
                    kembali_ke_menu_konversi_satuan_bilangan()
                elif nomor_yang_dipilih == "6":
                    bilangan_biner = input("Masukkan bilangan biner : ")
                    print(f"Hasil bilangan heksadesimal = {hex(int('0b' + bilangan_biner, base = 0))[2:]}")
                    kembali_ke_menu_konversi_satuan_bilangan()
                elif nomor_yang_dipilih == "7":
                    bilangan_desimal = input("Masukkan bilangan desimal : ")
                    print(f"Hasil bilangan oktal = {oct(int(bilangan_desimal))[2:]}")
                    kembali_ke_menu_konversi_satuan_bilangan()
                elif nomor_yang_dipilih == "8":
                    bilangan_oktal = input("Masukkan bilangan oktal : ")
                    print(f"Hasil bilangan desimal = {int('0o' + bilangan_oktal, base = 0)}")
                    kembali_ke_menu_konversi_satuan_bilangan()
                elif nomor_yang_dipilih == "9":
                    bilangan_desimal = input("Masukkan bilangan desimal : ")
                    print(f"Hasil bilangan biner = {bin(int(bilangan_desimal))[2:]}")
                    kembali_ke_menu_konversi_satuan_bilangan()
                elif nomor_yang_dipilih == "10":
                    bilangan_biner = input("Masukkan bilangan biner : ")
                    print(f"Hasil bilangan desimal = {int('0b' + bilangan_biner, base = 0)}")
                    kembali_ke_menu_konversi_satuan_bilangan()
                elif nomor_yang_dipilih == "11":
                    bilangan_oktal = input("Masukkan bilangan oktal : ")
                    print(f"Hasil bilangan biner = {bin(int('0o' + bilangan_oktal, base = 0))[2:]}")
                    kembali_ke_menu_konversi_satuan_bilangan()
                elif nomor_yang_dipilih == "12":
                    bilangan_biner = input("Masukkan bilangan biner : ")
                    print(f"Hasil bilangan oktal = {oct(int('0b' + bilangan_biner, base = 0))[2:]}")
                    kembali_ke_menu_konversi_satuan_bilangan()
                elif nomor_yang_dipilih == "13":
                    menu_konversi_satuan_bilangan()
                elif nomor_yang_dipilih == "14":
                    menu_kalkulator()
                elif nomor_yang_dipilih == "15":
                    beranda()
                elif nomor_yang_dipilih == "16":
                    print("Menutup program ...")
                    exit(0)
                else:
                    print("Input Tidak Valid!")
                    pilih_menu()
            except ValueError:
                print("Nilai yang diinput tidak valid!")
                pilih_menu()
        pilih_menu()
    def tampilkan_informasi_platform_perangkat():
        bersihkan_layar()
        print("beranda > tampilkan informasi platform perangkat\n")
        cetak_informasi_pengembang()
        print(f"Platform : {platform.platform()}")
        print(f"Sistem operasi : {platform.system()}")
        print(f"Versi sistem : {platform.version()}")
        print(f"Prosesor : {platform.processor()}")
        print(f"Mesin : {platform.machine()}")
        print(f"Arsitektur : {platform.architecture()}")
        input("Tekan Enter untuk kembali ke beranda (Ctrl + C untuk keluar)")
        beranda()
    def menu_integrasi_powershell():
        def enter_untuk_kembali_ke_menu_integrasi_powershell():
            input("Tekan Enter untuk kembali (Ctrl + C untuk keluar)")
            menu_integrasi_powershell()
        bersihkan_layar()
        print("beranda > integrasi Command Line Interface Windows PowerShell\n")
        cetak_informasi_pengembang()
        if platform.system() != "Windows":
            print("Integrasi CLI PowerShell Hanya Mendukung Sistem Operasi Windows!")
            print(f"Sistem operasi yang anda gunakan : {platform.system()}")
            input("Tekan Enter untuk kembali ke beranda (Ctrl + C untuk keluar)")
            beranda()
        print("Integrasi CLI PowerShell memperbolehkan pengguna mengakses sumber daya sistem operasi Windows")
        print("Menjalankan PowerShell dengan hak akses administrator atau akun pengguna administrator dapat mengakses sumber daya sistem yang sensitif")
        print("PowerShell memiliki fitur yang lebih kompleks daripada Command Prompt\n")
        print("Daftar menu CLI PowerShell")
        print("[-] bersihkan layar")
        print("[-0] beranda")
        print("[-00] keluar (Ctrl + C)")
        print("[0] masukkan perintah PowerShell secara manual")
        print("[1] tampilkan direktori saat ini (dir)")
        print("[2] tampilkan seluruh proses aplikasi yang berjalan di latar belakang (ps)")
        def pilih_menu():
            menu_yang_dipilih = input("Pilih nomor : ")
            if menu_yang_dipilih == "-":
                menu_integrasi_powershell()
            elif menu_yang_dipilih == "-0":
                beranda()
            elif menu_yang_dipilih == "-00":
                print("Menutup program ...")
                exit(0)
            elif menu_yang_dipilih == "0":
                perintah_powershell = input("Masukkan perintah PowerShell : ")
                if perintah_powershell != "":
                    subprocess.run(["powershell", f"{perintah_powershell}"], shell = False)
                else:
                    print("Input Kosong!")
                enter_untuk_kembali_ke_menu_integrasi_powershell()
            elif menu_yang_dipilih == "1":
                subprocess.run(["powershell", "dir"], shell = True)
                enter_untuk_kembali_ke_menu_integrasi_powershell()
            elif menu_yang_dipilih == "2":
                subprocess.run(["powershell", "PS"], shell = True)
                enter_untuk_kembali_ke_menu_integrasi_powershell()
                """
            elif menu_yang_dipilih == "2":
                pass
            elif menu_yang_dipilih == "3":
                pass
            elif menu_yang_dipilih == "4":
                pass
                """
            else:
                print("Input Tidak Valid!")
                pilih_menu()
        pilih_menu()
    def menu_integrasi_command_prompt():
        def enter_untuk_kembali_ke_menu_integrasi_command_prompt():
            input("Tekan Enter untuk kembali (Ctrl + C untuk keluar)")
            menu_integrasi_command_prompt()
        bersihkan_layar()
        print("beranda > integrasi CLI Windows Command Prompt\n")
        cetak_informasi_pengembang()
        if platform.system() != "Windows":
            print("Integrasi CLI Command Prompt Hanya Mendukung Sistem Operasi Windows!")
            print(f"Sistem operasi yang anda gunakan : {platform.system()}")
            input("Tekan Enter untuk kembali ke beranda (Ctrl + C untuk keluar)")
            beranda()
        print("Integrasi CLI Command Prompt memperbolehkan pengguna mengakses sumber daya sistem operasi Windows")
        print("Menjalankan Command Prompt dengan hak akses administrator atau akun pengguna administrator dapat mengakses sumber daya sistem yang sensitif")
        print("Command Prompt memiliki fitur yang lebih sederhana dan memiliki sumber daya yang mudah dipahami daripada PowerShell\n")
        print("Daftar menu CLI Command Prompt")
        print("[-] bersihkan layar")
        print("[-0] beranda")
        print("[-00] keluar (Ctrl + C)")
        print("[0] masukkan perintah Command Prompt secara manual")
        print("[1] tampilkan direktori saat ini (dir)")
        print("[2] petunjuk Command Prompt (help)")
        print("[3] bantuan warna (color help)")
        print("[4] tampilkan koneksi jaringan aktif (netstat)")
        print("[5] tampilkan koneksi jaringan aktif dan port yang terhubung (netstat -a)")
        print("[6] tampilkan tabel router (netstat -r)")
        print("[7] tampilkan statisik jaringan per protokol (netstat -s)")
        print("[8] tampilkan koneksi Ethernet (netstat -e)")
        print("[9] tampilkan koneksi Ethernet dan jaringan per protokol (netstat -e -s)")
        print("[10] tampilkan seluruh koneksi TCP (netstat -y)")
        print("[11] tampilkan koneksi jaringan aktif berdasarkan ID proses (netstat -o)")
        print("[12] tampilkan koneksi jaringan aktif dan port yang terhubung berdasarkan ID proses (netstat -a -o)")
        print("[13] tampilkan bantuan netstat (netstat help)")
        print("[14] tampilkan konfigurasi alamat IP (ipconfig)")
        print("[15] tampilkan detail konfigurasi alamat IP (ipconfig /all)")
        print("[16] perbarui seluruh adapter jaringan (ipconfig /renew)")
        print("[17] tampilkan informasi tentang semua kompartemen (ipconfig /allcompartments)")
        print("[18] tampilkan detail informasi tentang semua kompartemen (ipconfig /allcompartments /all)")
        print("[19] tampilkan konten DNS Resolver Cache (ipconfig /displaydns)")
        print("[20] bersihkan DNS Resolver Cache (ipconfig /flushdns)")
        print("[21] perbarui semua DHCP dan mendaftarkan kembali nama DNS (ipconfig /registerdns)")
        print("[22] tampilkan semua ID kelas DHCP yang diizinkan untuk adaptor (ipconfig /showclassid)")
        print("[23] tampilkan semua ID kelas DHCP IPv6 yang diizinkan untuk adaptor (ipconfig /showclassid6)")
        print("[24] tampilkan bantuan ipconfig (ipconfig /?)")
        def pilih_menu():
            menu_yang_dipilih = input("Pilih nomor : ")
            if menu_yang_dipilih == "-":
                menu_integrasi_command_prompt()
            elif menu_yang_dipilih == "-0":
                beranda()
            elif menu_yang_dipilih == "-00":
                print("Menutup program ...")
                exit(0)
            elif menu_yang_dipilih == "0":
                perintah_command_prompt = input("Masukkan perintah Command Prompt : ")
                subprocess.run(f"{perintah_command_prompt}", shell = True)
                enter_untuk_kembali_ke_menu_integrasi_command_prompt()
            elif menu_yang_dipilih == "1":
                subprocess.run("dir", shell = True)
                enter_untuk_kembali_ke_menu_integrasi_command_prompt()
            elif menu_yang_dipilih == "2":
                subprocess.run("help", shell = True)
                enter_untuk_kembali_ke_menu_integrasi_command_prompt()
            elif menu_yang_dipilih == "3":
                subprocess.run("color help", shell = True)
                enter_untuk_kembali_ke_menu_integrasi_command_prompt()
            elif menu_yang_dipilih == "4":
                subprocess.run("netstat", shell = True)
                enter_untuk_kembali_ke_menu_integrasi_command_prompt()
            elif menu_yang_dipilih == "5":
                subprocess.run("netstat -a", shell = True)
                enter_untuk_kembali_ke_menu_integrasi_command_prompt()
            elif menu_yang_dipilih == "6":
                subprocess.run("netstat -r", shell = True)
                enter_untuk_kembali_ke_menu_integrasi_command_prompt()
            elif menu_yang_dipilih == "7":
                subprocess.run("netstat -s", shell = True)
                enter_untuk_kembali_ke_menu_integrasi_command_prompt()
            elif menu_yang_dipilih == "8":
                subprocess.run("netstat -e", shell = True)
                enter_untuk_kembali_ke_menu_integrasi_command_prompt()
            elif menu_yang_dipilih == "9":
                subprocess.run("netstat -e -s", shell = True)
                enter_untuk_kembali_ke_menu_integrasi_command_prompt()
            elif menu_yang_dipilih == "10":
                subprocess.run("netstat -y", shell = True)
                enter_untuk_kembali_ke_menu_integrasi_command_prompt()
            elif menu_yang_dipilih == "11":
                subprocess.run("netstat -o", shell = True)
                enter_untuk_kembali_ke_menu_integrasi_command_prompt()
            elif menu_yang_dipilih == "12":
                subprocess.run("netstat -a -o", shell = True)
                enter_untuk_kembali_ke_menu_integrasi_command_prompt()
            elif menu_yang_dipilih == "13":
                subprocess.run("netstat help", shell = True)
                enter_untuk_kembali_ke_menu_integrasi_command_prompt()
            elif menu_yang_dipilih == "14":
                subprocess.run("ipconfig", shell = True)
                enter_untuk_kembali_ke_menu_integrasi_command_prompt()
            elif menu_yang_dipilih == "15":
                subprocess.run("ipconfig /all", shell = True)
                enter_untuk_kembali_ke_menu_integrasi_command_prompt()
            elif menu_yang_dipilih == "16":
                subprocess.run("ipconfig /renew", shell = True)
                enter_untuk_kembali_ke_menu_integrasi_command_prompt()
            elif menu_yang_dipilih == "17":
                subprocess.run("ipconfig /allcompartments", shell = True)
                enter_untuk_kembali_ke_menu_integrasi_command_prompt()
            elif menu_yang_dipilih == "18":
                subprocess.run("ipconfig /allcompartments /all", shell = True)
                enter_untuk_kembali_ke_menu_integrasi_command_prompt()
            elif menu_yang_dipilih == "19":
                subprocess.run("ipconfig /displaydns", shell = True)
                enter_untuk_kembali_ke_menu_integrasi_command_prompt()
            elif menu_yang_dipilih == "20":
                subprocess.run("ipconfig /flushdns", shell = True)
                enter_untuk_kembali_ke_menu_integrasi_command_prompt()
            elif menu_yang_dipilih == "21":
                subprocess.run("ipconfig /registerdns", shell = True)
                enter_untuk_kembali_ke_menu_integrasi_command_prompt()
            elif menu_yang_dipilih == "22":
                subprocess.run("ipconfig /showclassid", shell = True)
                enter_untuk_kembali_ke_menu_integrasi_command_prompt()
            elif menu_yang_dipilih == "23":
                subprocess.run("ipconfig /showclassid6", shell = True)
                enter_untuk_kembali_ke_menu_integrasi_command_prompt()
            elif menu_yang_dipilih == "24":
                subprocess.run("ipconfig /?", shell = True)
                enter_untuk_kembali_ke_menu_integrasi_command_prompt()
            else:
                print("Input Tidak Valid!")
                pilih_menu()
        pilih_menu()
    def beranda():
        bersihkan_layar()
        print("Python Script Program Command Line Interface (CLI)\n")
        cetak_informasi_pengembang()
        print("Tanggal pembaruan : 11 November 2023\n")
        print("Disclaimer : Beberapa program CLI PowerShell dan Command Prompt dapat merubah fungsi sistem. Kerusakan yang terjadi akibat tindakan pengguna adalah di luar tanggung jawab pengembang\n")
        print("Daftar Menu")
        print("[1] kriptografi")
        print("[2] kalkulator")
        print("[3] tampilkan informasi platform perangkat")
        print("[4] integrasi Command Line Interface (CLI) Windows PowerShell")
        print("[5] integrasi Command Line Interface (CLI) Windows Command Prompt")
        print("[6] bersihkan")
        print("[7] keluar (Ctrl + C)\n")
        def pilih_menu():
            menu_yang_dipilih = input("Pilih nomor : ")
            if menu_yang_dipilih == "1":
                menu_kriptografi()
            elif menu_yang_dipilih == "2":
                menu_kalkulator()
            elif menu_yang_dipilih == "3":
                tampilkan_informasi_platform_perangkat()
            elif menu_yang_dipilih == "4":
                menu_integrasi_powershell()
            elif menu_yang_dipilih == "5":
                menu_integrasi_command_prompt()
            elif menu_yang_dipilih == "6":
                beranda()
            elif menu_yang_dipilih == "7":
                print("Menutup program ...")
                exit(0)
            else:
                print("Input Tidak Valid!")
                pilih_menu()
        pilih_menu()
    if __name__ == "__main__":
        beranda()
except KeyboardInterrupt:
    print("Menutup program ...")
    exit(0)
except Exception as global_error:
    print("Terjadi error di sepanjang program")
    print(f"Log Error : {global_error}")