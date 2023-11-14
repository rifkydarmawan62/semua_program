import csv, os, base64, binascii, platform, subprocess, tracemalloc
from tkinter.filedialog import askopenfilename, askdirectory
from typing import Literal
from unicode_standar import *
tracemalloc.start()
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
            match menu_yang_dipilih:
                case "1":
                    pilih_file_unicode_standar("encoding heksadesimal")
                case "2":
                    pilih_file_unicode_standar("encoding desimal")
                case "3":
                    pilih_file_unicode_standar("encoding oktal")
                case "4":
                    pilih_file_unicode_standar("encoding biner")
                case "5":
                    pilih_file_unicode_standar("decoding heksadesimal")
                case "6":
                    pilih_file_unicode_standar("decoding desimal")
                case "7":
                    pilih_file_unicode_standar("decoding oktal")
                case "8":
                    pilih_file_unicode_standar("decoding biner")
                case "9":
                    bersihkan_layar()
                    print("beranda > kriptografi > unicode standar > bantuan\n")
                    cetak_informasi_pengembang()
                    print("Menyediakan keamanan data dan kerahasiaan data file teks dengan kriptografi unicode standar")
                    print("Encode dan decode unicode standar hanya dapat digunakan pada teks karakter unicode yang akan di encode menjadi bilangan heksadesimal, desimal, oktal, dan biner.")
                    print("Sebaliknya data yang telah di encode dapat di decode kembali menjadi teks karakter unicode jika data yang telah di encode adalah valid\n")
                    input("Tekan enter untuk menutup (Ctrl + C untuk keluar)")
                    menu_encode_dan_decode_unicode_standar()
                case "10":
                    menu_encode_dan_decode_unicode_standar()
                case "11":
                    menu_kriptografi()
                case "12":
                    beranda()
                case "13":
                    print("Menutup program ...")
                    exit(0)
                case _:
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
                                match nomor_yang_dipilih:
                                    case "1":
                                        encoded_data = encoded_data + base64.b16encode(data_per_baris)
                                    case "2":
                                        decoded_data = decoded_data + base64.b16decode(data_per_baris)
                                    case "3":
                                        encoded_data = encoded_data + base64.b32encode(data_per_baris)
                                    case "4":
                                        decoded_data = decoded_data + base64.b32decode(data_per_baris)
                                    case "5":
                                        encoded_data = encoded_data + base64.b32hexencode(data_per_baris)
                                    case "6":
                                        decoded_data = decoded_data + base64.b32hexdecode(data_per_baris)
                                    case "7":
                                        encoded_data = encoded_data + base64.b64encode(data_per_baris)
                                    case "8":
                                        decoded_data = decoded_data + base64.b64decode(data_per_baris)
                                    case "9":
                                        encoded_data = encoded_data + base64.standard_b64encode(data_per_baris)
                                    case "10":
                                        decoded_data = decoded_data + base64.standard_b64decode(data_per_baris)
                                    case "11":
                                        encoded_data = encoded_data + base64.a85encode(data_per_baris)
                                    case "12":
                                        decoded_data = decoded_data + base64.a85decode(data_per_baris)
                                    case _:
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
            menu_yang_dipilih = input("Pilih nomor : ")
            match menu_yang_dipilih:
                case "1":
                    menu_encode_dan_decode_unicode_standar()
                case "2":
                    menu_encode_dan_decode_python_base64()
                case "3":
                    menu_kriptografi()
                case "4":
                    beranda()
                case "5":
                    print("Menutup program ...")
                    exit(0)
                case _:
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
                match nomor_yang_dipilih:
                    case "1":
                        bilangan_heksadesimal = input("Masukkan bilangan heksadesimal : ")
                        print(f"Hasil bilangan desimal = {int('0x' + bilangan_heksadesimal, base = 0)}")
                        kembali_ke_menu_konversi_satuan_bilangan()
                    case "2":
                        bilangan_desimal = input("Masukkan bilangan desimal : ")
                        print(f"Hasil bilangan heksadesimal = {hex(int(bilangan_desimal))[2:]}")
                        kembali_ke_menu_konversi_satuan_bilangan()
                    case "3":
                        bilangan_heksadesimal = input("Masukkan bilangan heksadesimal : ")
                        print(f"Hasil bilangan oktal = {oct(int('0x' + bilangan_heksadesimal, base = 0))[2:]}")
                        kembali_ke_menu_konversi_satuan_bilangan()
                    case "4":
                        bilangan_oktal = input("Masukkan bilangan oktal : ")
                        print(f"Hasil bilangan heksadesimal = {hex(int('0o' + bilangan_oktal, base = 0))[2:]}")
                        kembali_ke_menu_konversi_satuan_bilangan()
                    case "5":
                        bilangan_heksadesimal = input("Masukkan bilangan heksadesimal : ")
                        print(f"Hasil bilangan biner = {bin(int('0x' + bilangan_heksadesimal, base = 0))[2:]}")
                        kembali_ke_menu_konversi_satuan_bilangan()
                    case "6":
                        bilangan_biner = input("Masukkan bilangan biner : ")
                        print(f"Hasil bilangan heksadesimal = {hex(int('0b' + bilangan_biner, base = 0))[2:]}")
                        kembali_ke_menu_konversi_satuan_bilangan()
                    case "7":
                        bilangan_desimal = input("Masukkan bilangan desimal : ")
                        print(f"Hasil bilangan oktal = {oct(int(bilangan_desimal))[2:]}")
                        kembali_ke_menu_konversi_satuan_bilangan()
                    case "8":
                        bilangan_oktal = input("Masukkan bilangan oktal : ")
                        print(f"Hasil bilangan desimal = {int('0o' + bilangan_oktal, base = 0)}")
                        kembali_ke_menu_konversi_satuan_bilangan()
                    case "9":
                        bilangan_desimal = input("Masukkan bilangan desimal : ")
                        print(f"Hasil bilangan biner = {bin(int(bilangan_desimal))[2:]}")
                        kembali_ke_menu_konversi_satuan_bilangan()
                    case "10":
                        bilangan_biner = input("Masukkan bilangan biner : ")
                        print(f"Hasil bilangan desimal = {int('0b' + bilangan_biner, base = 0)}")
                        kembali_ke_menu_konversi_satuan_bilangan()
                    case "11":
                        bilangan_oktal = input("Masukkan bilangan oktal : ")
                        print(f"Hasil bilangan biner = {bin(int('0o' + bilangan_oktal, base = 0))[2:]}")
                        kembali_ke_menu_konversi_satuan_bilangan()
                    case "12":
                        bilangan_biner = input("Masukkan bilangan biner : ")
                        print(f"Hasil bilangan oktal = {oct(int('0b' + bilangan_biner, base = 0))[2:]}")
                        kembali_ke_menu_konversi_satuan_bilangan()
                    case "13":
                        menu_konversi_satuan_bilangan()
                    case "14":
                        menu_kalkulator()
                    case "15":
                        beranda()
                    case "16":
                        print("Menutup program ...")
                        exit(0)
                    case _:
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
    def buka_file_teks(integrasi : dict, /):
        print("Tekan ALT + Tab untuk membuka jendela baru untuk memilih file")
        def jalankan_perintah(perintah : Literal["PowerShell", "Command Prompt"], lokasi_file : str):
            with open(lokasi_file, "r") as file_teks:
                for perintah_per_baris in file_teks:
                    if perintah == "PowerShell":
                        print(f"Menjalankan perintah PowerShell {perintah_per_baris.strip()}")
                        subprocess.run(["powershell", perintah_per_baris.strip()])
                    else:
                        print(f"Menjalankan perintah Command Prompt {perintah_per_baris.strip()}")
                        subprocess.run(perintah_per_baris.strip(), shell = True)
        for kunci_dictionary in integrasi.keys():
            match kunci_dictionary:
                case "PowerShell":
                    direktori_file = askopenfilename(title = "File Teks Untuk Menjalankan Baris Perintah Powershell Secara Otomatis", filetypes = (["Dokumen Teks", "*.txt"], ["Log Teks", "*.log"]))
                    if direktori_file:
                        jalankan_perintah("PowerShell", direktori_file)
                    else:
                        print("File Tidak Dibuka!")
                    input("Tekan Enter untuk kembali (Ctrl + C untuk keluar)")
                    menu_perintah_powershell = integrasi.get(kunci_dictionary)
                    match menu_perintah_powershell:
                        case "default":
                            menu_integrasi_powershell()
                        case "winget":
                            menu_powershell_winget()
                case "Command Prompt":
                    direktori_file = askopenfilename(title = "File Teks Untuk Menjalankan Baris Perintah Command Prompt Secara Otomatis", filetypes = (["Dokumen Teks", "*.txt"], ["Log Teks", "*.log"]))
                    if direktori_file:
                        jalankan_perintah("Command Prompt", direktori_file)
                    else:
                        print("File Tidak Dibuka!")
                    input("Tekan Enter untuk kembali (Ctrl + C untuk keluar)")
                    menu_perintah_command_prompt = integrasi.get(kunci_dictionary)
                    match menu_perintah_command_prompt:
                        case "default":
                            menu_integrasi_command_prompt()
                        case "netstat":
                            menu_command_prompt_netstat()
                        case "ipconfig":
                            menu_command_prompt_ipconfig()
                        case "netsh":
                            menu_command_prompt_netsh()
                        case "tasklist":
                            menu_command_prompt_tasklist()
                        case "taskkill":
                            menu_command_prompt_taskkill()
                        case "shutdown":
                            menu_command_prompt_shutdown()
                        case "systeminfo":
                            menu_command_prompt_systeminfo()
                        case "sc":
                            menu_command_prompt_sc()
                case _:
                    break
            break
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
        print("Dokumentasi PowerShell")
        print("- https://learn.microsoft.com/id-id/powershell/scripting/samples/sample-scripts-for-administration?view=powershell-7.3")
        print("\nDaftar menu CLI PowerShell")
        print("[-] bersihkan layar")
        print("[-0] beranda")
        print("[-00] keluar (Ctrl + C)")
        print("[#:] buka file teks untuk menjalankan perintah PowerShell otomatis")
        print("[0] masukkan perintah PowerShell secara manual")
        print("[1] tampilkan direktori saat ini (dir)")
        print("[2] tampilkan seluruh proses aplikasi yang berjalan di latar belakang (ps)")
        print("[3] tampilkan detail versi Windows PowerShell ($PSVersionTable)")
        print("[4] tampilkan versi Windows PowerShell ($PSVersionTable.PSVersion)")
        print("[5] menu perintah winget")
        print("[6] tampilkan topik bantuan (help topic)")
        def pilih_menu():
            menu_yang_dipilih = input("Pilih nomor : ")
            match menu_yang_dipilih:
                case "-":
                    menu_integrasi_powershell()
                case "-0":
                    beranda()
                case "-00":
                    print("Menutup program ...")
                    exit(0)
                case "#:":
                    buka_file_teks({"PowerShell" : "default"})
                case "0":
                    input_perintah_powershell_manual("default")
                case "1":
                    subprocess.run(["powershell", "dir"], shell = True)
                    enter_untuk_kembali_ke_menu_integrasi_powershell()
                case "2":
                    subprocess.run(["powershell", "PS"], shell = True)
                    enter_untuk_kembali_ke_menu_integrasi_powershell()
                case "3":
                    subprocess.run(["powershell", "$PSVersionTable"], shell = True)
                    enter_untuk_kembali_ke_menu_integrasi_powershell()
                case "4":
                    subprocess.run(["powershell", "$PSVersionTable.PSVersion"], shell = True)
                    enter_untuk_kembali_ke_menu_integrasi_powershell()
                case "5":
                    menu_powershell_winget()
                case "6":
                    subprocess.run(["powershell", "help topic"])
                    enter_untuk_kembali_ke_menu_integrasi_powershell()
                case _:
                    print("Input Tidak Valid!")
                    pilih_menu()
        pilih_menu()
    def input_perintah_powershell_manual(__menu_powershell : Literal["default", "winget"]):
        perintah_powershell = input("Masukkan perintah PowerShell : ")
        if perintah_powershell != "":
            subprocess.run(["powershell", f"{perintah_powershell}"], shell = False)
        else:
            print("Input Kosong!")
        input("Tekan Enter untuk kembali (Ctrl + C untuk keluar)")
        match __menu_powershell:
            case "default":
                menu_integrasi_powershell()
            case "winget":
                menu_powershell_winget()
    def menu_powershell_winget():
        bersihkan_layar()
        print("beranda > integrasi CLI Windows PowerShell > perintah PowerShell winget\n")
        cetak_informasi_pengembang()
        print("Perintah winget digunakan untuk melakukan instalasi aplikasi\n")
        print("Daftar menu perintah PowerShell winget")
        print("[-] bersihkan layar")
        print("[-0] kembali")
        print("[-00] beranda")
        print("[-000] keluar (Ctrl + C)")
        print("[#:] buka file teks untuk menjalankan perintah PowerShell otomatis")
        print("[0] masukkan perintah PowerShell secara manual")
        def pilih_menu():
            menu_yang_dipilih = input("Pilih nomor : ")
            match menu_yang_dipilih:
                case "-":
                    menu_powershell_winget()
                case "-0":
                    menu_integrasi_powershell()
                case "-00":
                    beranda()
                case "-000":
                    print("Menutup program ...")
                    exit(0)
                case "#:":
                    buka_file_teks({"PowerShell" : "winget"})
                case "0":
                    input_perintah_powershell_manual("winget")
                case _:
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
        print("Dokumentasi Command Prompt")
        print("- https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/windows-commands")
        print("\nDaftar menu CLI Command Prompt")
        print("[-] bersihkan layar")
        print("[-0] beranda")
        print("[-00] keluar (Ctrl + C)")
        print("[#:] buka file teks untuk menjalankan perintah Command Prompt otomatis")
        print("[0] masukkan perintah Command Prompt secara manual")
        print("[1] tampilkan direktori saat ini (dir)")
        print("[2] petunjuk Command Prompt (help)")
        print("[3] bantuan warna (color help)")
        print("[4] menu perintah Command Prompt netstat")
        print("[5] menu perintah Command Prompt ipconfig")
        print("[6] menu perintah Command Prompt netsh")
        print("[7] menu perintah Command Prompt tasklist")
        print("[8] menu perintah Command Prompt taskkill")
        print("[9] menu perintah Command Prompt shutdown")
        print("[10] menu perintah Command Prompt systeminfo")
        print("[11] menu perintah Command Prompt sc")
        print("[12] bantuan call (call /?)")
        print("[13] bantuan ping (ping)")
        print("[14] bantuan tracert (tracert)")
        print("[15] tampilkan versi Windows (ver)")
        print("[16] bantuan vol (vol /?)")
        print("[17] tampilkan nomor serial disk dan label disk, jika ada (vol)")
        print("[18] bantuan set (set /?)")
        print("[19] tampilkan variabel lingkungan Windows (set)")
        def pilih_menu():
            menu_yang_dipilih = input("Pilih nomor : ")
            match menu_yang_dipilih:
                case "-":
                    menu_integrasi_command_prompt()
                case "-0":
                    beranda()
                case "-00":
                    print("Menutup program ...")
                    exit(0)
                case "#:":
                    buka_file_teks({"Command Prompt" : "default"})
                case "0":
                    input_perintah_command_prompt_manual("default")
                case "1":
                    subprocess.run("dir", shell = True)
                    enter_untuk_kembali_ke_menu_integrasi_command_prompt()
                case "2":
                    subprocess.run("help", shell = True)
                    enter_untuk_kembali_ke_menu_integrasi_command_prompt()
                case "3":
                    subprocess.run("color help", shell = True)
                    enter_untuk_kembali_ke_menu_integrasi_command_prompt()
                case "4":
                    menu_command_prompt_netstat()
                case "5":
                    menu_command_prompt_ipconfig()
                case "6":
                    menu_command_prompt_netsh()
                case "7":
                    menu_command_prompt_tasklist()
                case "9":
                    menu_command_prompt_shutdown()
                case "10":
                    menu_command_prompt_systeminfo()
                case "11":
                    menu_command_prompt_sc()
                case "12":
                    subprocess.run("call /?", shell = True)
                    enter_untuk_kembali_ke_menu_integrasi_command_prompt()
                case "13":
                    subprocess.run("ping", shell = True)
                    enter_untuk_kembali_ke_menu_integrasi_command_prompt()
                case "14":
                    subprocess.run("tracert", shell = True)
                    enter_untuk_kembali_ke_menu_integrasi_command_prompt()
                case "15":
                    subprocess.run("ver", shell = True)
                    enter_untuk_kembali_ke_menu_integrasi_command_prompt()
                case "16":
                    subprocess.run("vol /?", shell = True)
                    enter_untuk_kembali_ke_menu_integrasi_command_prompt()
                case "17":
                    subprocess.run("vol", shell = True)
                    enter_untuk_kembali_ke_menu_integrasi_command_prompt()
                case "18":
                    subprocess.run("set /?", shell = True)
                    enter_untuk_kembali_ke_menu_integrasi_command_prompt()
                case "19":
                    subprocess.run("set", shell = True)
                    enter_untuk_kembali_ke_menu_integrasi_command_prompt()
                case _:
                    print("Input Tidak Valid!")
                    pilih_menu()
        pilih_menu()
    def input_perintah_command_prompt_manual(__menu_command_prompt : Literal["default", "netstat", "ipconfig", "netsh", "tasklist", "taskkill", "shutdown", "systeminfo", "sc"]):
        perintah_command_prompt = input("Masukkan perintah Command Prompt : ")
        subprocess.run(f"{perintah_command_prompt}", shell = True)
        input("Tekan Enter untuk kembali (Ctrl + C untuk keluar)")
        match __menu_command_prompt:
            case "default":
                menu_integrasi_command_prompt()
            case "netstat":
                menu_command_prompt_netstat()
            case "ipconfig":
                menu_command_prompt_ipconfig()
            case "netsh":
                menu_command_prompt_netsh()
            case "tasklist":
                menu_command_prompt_tasklist()
            case "taskkill":
                menu_command_prompt_taskkill()
            case "shutdown":
                menu_command_prompt_shutdown()
            case "systeminfo":
                menu_command_prompt_systeminfo()
            case "sc":
                menu_command_prompt_sc()
    def menu_command_prompt_netstat():
        def enter_untuk_kembali_ke_menu_command_prompt_netstat():
            input("Tekan Enter untuk kembali (Ctrl + C untuk keluar)")
            menu_command_prompt_netstat()
        bersihkan_layar()
        print("beranda > integrasi CLI Windows Command Prompt > perintah Command Prompt netstat\n")
        cetak_informasi_pengembang()
        print("Daftar menu perintah Command Prompt netstat")
        print("[-] bersihkan layar")
        print("[-0] kembali")
        print("[-00] beranda")
        print("[-000] keluar")
        print("[#:] buka file teks untuk menjalankan perintah Command Prompt otomatis")
        print("[0] masukkan perintah Command Prompt manual")
        print("[1] tampilkan koneksi jaringan aktif (netstat)")
        print("[2] tampilkan koneksi jaringan aktif dan port yang terhubung (netstat -a)")
        print("[3] tampilkan tabel router (netstat -r)")
        print("[4] tampilkan statisik jaringan per protokol (netstat -s)")
        print("[5] tampilkan koneksi Ethernet (netstat -e)")
        print("[6] tampilkan koneksi Ethernet dan jaringan per protokol (netstat -e -s)")
        print("[7] tampilkan seluruh koneksi TCP (netstat -y)")
        print("[8] tampilkan koneksi jaringan aktif berdasarkan ID proses (netstat -o)")
        print("[9] tampilkan koneksi jaringan aktif dan port yang terhubung berdasarkan ID proses (netstat -a -o)")
        print("[10] tampilkan bantuan netstat (netstat help)")
        def pilih_menu():
            menu_yang_dipilih = input("Pilih nomor : ")
            match menu_yang_dipilih:
                case "-":
                    menu_command_prompt_netstat()
                case "-0":
                    menu_integrasi_command_prompt()
                case "-00":
                    beranda()
                case "-000":
                    print("Menutup program ...")
                    exit(0)
                case "#:":
                    buka_file_teks({"Command Prompt" : "netstat"})
                case "0":
                    input_perintah_command_prompt_manual("netstat")
                case "1":
                    subprocess.run("netstat", shell = True)
                    enter_untuk_kembali_ke_menu_command_prompt_netstat()
                case "2":
                    subprocess.run("netstat -a", shell = True)
                    enter_untuk_kembali_ke_menu_command_prompt_netstat()
                case "3":
                    subprocess.run("netstat -r", shell = True)
                    enter_untuk_kembali_ke_menu_command_prompt_netstat()
                case "4":
                    subprocess.run("netstat -s", shell = True)
                    enter_untuk_kembali_ke_menu_command_prompt_netstat()
                case "5":
                    subprocess.run("netstat -e", shell = True)
                    enter_untuk_kembali_ke_menu_command_prompt_netstat()
                case "6":
                    subprocess.run("netstat -e -s", shell = True)
                    enter_untuk_kembali_ke_menu_command_prompt_netstat()
                case "7":
                    subprocess.run("netstat -y", shell = True)
                    enter_untuk_kembali_ke_menu_command_prompt_netstat()
                case "8":
                    subprocess.run("netstat -o", shell = True)
                    enter_untuk_kembali_ke_menu_command_prompt_netstat()
                case "9":
                    subprocess.run("netstat -a -o", shell = True)
                    enter_untuk_kembali_ke_menu_command_prompt_netstat()
                case "10":
                    subprocess.run("netstat help", shell = True)
                    enter_untuk_kembali_ke_menu_command_prompt_netstat()
                case _:
                    print("Input Tidak Valid!")
                    pilih_menu()
        pilih_menu()
    def menu_command_prompt_ipconfig():
        def enter_untuk_kembali_ke_menu_command_prompt_ipconfig():
            input("Tekan Enter untuk kembali (Ctrl + C untuk keluar)")
            menu_command_prompt_ipconfig()
        bersihkan_layar()
        print("beranda > integrasi CLI Windows Command Prompt > perintah Command Prompt ipconfig\n")
        cetak_informasi_pengembang()
        print("Daftar menu perintah Command Prompt ipconfig")
        print("[-] bersihkan layar")
        print("[-0] kembali")
        print("[-00] beranda")
        print("[-000] keluar")
        print("[#:] buka file teks untuk menjalankan perintah Command Prompt otomatis")
        print("[0] masukkan perintah Command Prompt manual")
        print("[1] tampilkan konfigurasi alamat IP (ipconfig)")
        print("[2] tampilkan detail konfigurasi alamat IP (ipconfig /all)")
        print("[3] perbarui seluruh adapter jaringan (ipconfig /renew)")
        print("[4] tampilkan informasi tentang semua kompartemen (ipconfig /allcompartments)")
        print("[5] tampilkan detail informasi tentang semua kompartemen (ipconfig /allcompartments /all)")
        print("[6] tampilkan konten DNS Resolver Cache (ipconfig /displaydns)")
        print("[7] bersihkan DNS Resolver Cache (ipconfig /flushdns)")
        print("[8] perbarui semua DHCP dan mendaftarkan kembali nama DNS (ipconfig /registerdns)")
        print("[9] tampilkan semua ID kelas DHCP yang diizinkan untuk adaptor (ipconfig /showclassid")
        print("[10] tampilkan semua ID kelas DHCP IPv6 yang diizinkan untuk adaptor (ipconfig /showclassid6)")
        print("[11] tampilkan bantuan ipconfig (ipconfig /?)")
        def pilih_menu():
            menu_yang_dipilih = input("Pilih nomor : ")
            match menu_yang_dipilih:
                case "-":
                    menu_command_prompt_ipconfig()
                case "-0":
                    menu_integrasi_command_prompt()
                case "-00":
                    beranda()
                case "-000":
                    print("Menutup program ...")
                    exit(0)
                case "#:":
                    buka_file_teks({"Command Prompt" : "ipconfig"})
                case "0":
                    input_perintah_command_prompt_manual("ipconfig")
                case "1":
                    subprocess.run("ipconfig", shell = True)
                    enter_untuk_kembali_ke_menu_command_prompt_ipconfig()
                case "2":
                    subprocess.run("ipconfig /all", shell = True)
                    enter_untuk_kembali_ke_menu_command_prompt_ipconfig()
                case "3":
                    subprocess.run("ipconfig /renew", shell = True)
                    enter_untuk_kembali_ke_menu_command_prompt_ipconfig()
                case "4":
                    subprocess.run("ipconfig /allcompartments", shell = True)
                    enter_untuk_kembali_ke_menu_command_prompt_ipconfig()
                case "5":
                    subprocess.run("ipconfig /allcompartments /all", shell = True)
                    enter_untuk_kembali_ke_menu_command_prompt_ipconfig()
                case "6":
                    subprocess.run("ipconfig /displaydns", shell = True)
                    enter_untuk_kembali_ke_menu_command_prompt_ipconfig()
                case "7":
                    subprocess.run("ipconfig /flushdns", shell = True)
                    enter_untuk_kembali_ke_menu_command_prompt_ipconfig()
                case "8":
                    subprocess.run("ipconfig /registerdns", shell = True)
                    enter_untuk_kembali_ke_menu_command_prompt_ipconfig()
                case "9":
                    subprocess.run("ipconfig /showclassid", shell = True)
                    enter_untuk_kembali_ke_menu_command_prompt_ipconfig()
                case "10":
                    subprocess.run("ipconfig /showclassid6", shell = True)
                    enter_untuk_kembali_ke_menu_command_prompt_ipconfig()
                case "11":
                    subprocess.run("ipconfig /?", shell = True)
                    enter_untuk_kembali_ke_menu_command_prompt_ipconfig()
                case _:
                    print("Input Tidak Valid!")
                    pilih_menu()
        pilih_menu()
    def menu_command_prompt_netsh():
        def enter_untuk_kembali_ke_menu_command_prompt_netsh():
            input("Tekan Enter untuk kembali (Ctrl + C untuk keluar)")
            menu_command_prompt_netsh()
        bersihkan_layar()
        print("beranda > integrasi CLI Windows Command Prompt > perintah Command Prompt netsh\n")
        cetak_informasi_pengembang()
        print("Daftar menu perintah Command Prompt netsh")
        print("[-] bersihkan layar")
        print("[-0] kembali")
        print("[-00] beranda")
        print("[-000] keluar")
        print("[#:] buka file teks untuk menjalankan perintah Command Prompt otomatis")
        print("[0] masukkan perintah Command Prompt manual")
        print("[1] masuk ke baris perintah netsh (netsh)")
        print("[2] bantuan netsh (netsh help)")
        print("[3] bantuan netsh wlan (netsh wlan)")
        print("[4] tampilkan informasi lengkap perangkat nirkabel dan jaringan (netsh wlan show all)")
        print("[5] tampilkan perizinan pengaturan berbagi kredensial pengguna (netsh wlan show allowexplicitcreds)")
        print("[6] tampilkan jaringan nirkabel yang dikonfigurasikan otomatis (netsh wlan show autoconfig)")
        print("[7] tampilkan jaringan yang diblokir (netsh wlan show blockednetworks)")
        print("[8] tampilkan apakah semua orang diizinkan untuk membuat seluruh profil pengguna (netsh wlan show createalluserprofile)")
        print("[9] tampilkan properti jaringan driver nirkabel LAN pada sistem (netsh wlan show drivers)")
        print("[10] tampilkan daftar jaringan yang diblokir dan diizinkan (netsh wlan show filters)")
        print("[11] tampilkan properti dan status jaringan yang dihosting (netsh wlan show hostednetwork)")
        print("[12] tampilkan daftar antarmuka nirkabel LAN pada sistem (netsh wlan show interfaces)")
        print("[13] tampilkan jaringan yang terlihat pada sistem (netsh wlan show networks)")
        print("[14] tampilkan hanya penggunaan profil GP pada pengaturan jaringan yang dikonfigurasi GP (netsh wlan show onlyUseGPProfilesforAllowedNetworks)")
        print("[15] tampilkan profil yang dikonfigurasi pada sistem (netsh wlan show profiles)")
        print("[16] tampilkan apakah alamat MAC acak diaktifkan atau dinonaktifkan (netsh wlan show randomization)")
        print("[17] tampilkan pengaturan global nirkabel LAN (netsh wlan show settings)")
        print("[18] tampilkan apakah penelusuran LAN nirkabel diaktifkan atau dinonaktifkan (netsh wlan show tracing)")
        print("[19] tampilkan kapabilitas nirkabel pada sistem (netsh wlan show wirelesscapabilities)")
        print("[20] buat laporan yang menampilkan informasi sesi nirkabel terkini (netsh wlan show wlanreport)")
        print("[21] tampilkan kata sandi profil Wi-Fi (netsh wlan show profiles {nama_profil_wlan} key=clear)")
        def pilih_menu():
            menu_yang_dipilih = input("Pilih nomor : ")
            match menu_yang_dipilih:
                case "-":
                    menu_command_prompt_netsh()
                case "-0":
                    menu_integrasi_command_prompt()
                case "-00":
                    beranda()
                case "-000":
                    print("Menutup program ...")
                    exit(0)
                case "#:":
                    buka_file_teks({"Command Prompt" : "netsh"})
                case "0":
                    input_perintah_command_prompt_manual("netsh")
                case "1":
                    print("Anda masuk ke baris perintah netsh")
                    subprocess.run("netsh", shell = True)
                    print("Anda keluar dari baris perintah netsh")
                    enter_untuk_kembali_ke_menu_command_prompt_netsh()
                case "2":
                    subprocess.run("netsh help", shell = True)
                    enter_untuk_kembali_ke_menu_command_prompt_netsh()
                case "3":
                    subprocess.run("netsh wlan", shell = True)
                    enter_untuk_kembali_ke_menu_command_prompt_netsh()
                case "4":
                    subprocess.run("netsh wlan show all", shell = True)
                    enter_untuk_kembali_ke_menu_command_prompt_netsh()
                case "5":
                    subprocess.run("netsh wlan show allowexplicitcreds", shell = True)
                    enter_untuk_kembali_ke_menu_command_prompt_netsh()
                case "6":
                    subprocess.run("netsh wlan show autoconfig", shell = True)
                    enter_untuk_kembali_ke_menu_command_prompt_netsh()
                case "7":
                    subprocess.run("netsh wlan show blockednetworks", shell = True)
                    enter_untuk_kembali_ke_menu_command_prompt_netsh()
                case "8":
                    subprocess.run("netsh wlan show createalluserprofile", shell = True)
                    enter_untuk_kembali_ke_menu_command_prompt_netsh()
                case "9":
                    subprocess.run("netsh wlan show drivers", shell = True)
                    enter_untuk_kembali_ke_menu_command_prompt_netsh()
                case "10":
                    subprocess.run("netsh wlan show filters", shell = True)
                    enter_untuk_kembali_ke_menu_command_prompt_netsh()
                case "11":
                    subprocess.run("netsh wlan show hostednetwork", shell = True)
                    enter_untuk_kembali_ke_menu_command_prompt_netsh()
                case "12":
                    subprocess.run("netsh wlan show interfaces", shell = True)
                    enter_untuk_kembali_ke_menu_command_prompt_netsh()
                case "13":
                    subprocess.run("netsh wlan show networks", shell = True)
                    enter_untuk_kembali_ke_menu_command_prompt_netsh()
                case "14":
                    subprocess.run("netsh wlan show onlyUseGPProfilesforAllowedNetworks", shell = True)
                    enter_untuk_kembali_ke_menu_command_prompt_netsh()
                case "15":
                    subprocess.run("netsh wlan show profiles", shell = True)
                    enter_untuk_kembali_ke_menu_command_prompt_netsh()
                case "16":
                    subprocess.run("netsh wlan show randomization", shell = True)
                    enter_untuk_kembali_ke_menu_command_prompt_netsh()
                case "17":
                    subprocess.run("netsh wlan show settings", shell = True)
                    enter_untuk_kembali_ke_menu_command_prompt_netsh()
                case "18":
                    subprocess.run("netsh wlan show tracing", shell = True)
                    enter_untuk_kembali_ke_menu_command_prompt_netsh()
                case "19":
                    subprocess.run("netsh wlan show wirelesscapabilities", shell = True)
                    enter_untuk_kembali_ke_menu_command_prompt_netsh()
                case "20":
                    subprocess.run("netsh wlan show wlanreport", shell = True)
                    enter_untuk_kembali_ke_menu_command_prompt_netsh()
                case "21":
                    nama_profil_wlan = input("Masukkan nama profil wlan : ")
                    subprocess.run(f"netsh wlan show profiles {nama_profil_wlan} key=clear", shell = True)
                    enter_untuk_kembali_ke_menu_command_prompt_netsh()
                case _:
                    print("Input Tidak Valid!")
                    pilih_menu()
        pilih_menu()
    def menu_command_prompt_tasklist():
        def enter_untuk_kembali_ke_menu_command_prompt_tasklist():
            input("Tekan Enter untuk kembali (Ctrl + C untuk keluar)")
            menu_command_prompt_tasklist()
        bersihkan_layar()
        print("beranda > integrasi CLI Windows Command Prompt > perintah Command Prompt tasklist\n")
        cetak_informasi_pengembang()
        print("Tampilkan proses aplikasi dan layanan yang berjalan di latar belakang\n")
        print("Daftar menu perintah Command Prompt tasklist")
        print("[-] bersihkan layar")
        print("[-0] kembali")
        print("[-00] beranda")
        print("[-000] keluar")
        print("[#:] buka file teks untuk menjalankan perintah Command Prompt otomatis")
        print("[0] masukkan perintah Command Prompt manual")
        print("[1] bantuan tasklist (tasklist /?)")
        print("[2] tampilkan proses aplikasi yang berjalan di latar belakang (tasklist)")
        print("[3] tampilkan layanan yang yang dihosting di setiap proses (tasklist /SVC)")
        def pilih_menu():
            menu_yang_dipilih = input("Pilih nomor : ")
            match menu_yang_dipilih:
                case "-":
                    menu_command_prompt_tasklist()
                case "-0":
                    menu_integrasi_command_prompt()
                case "-00":
                    beranda()
                case "-000":
                    print("Menutup program ...")
                    exit(0)
                case "#:":
                    buka_file_teks({"Command Prompt" : "tasklist"})
                case "0":
                    input_perintah_command_prompt_manual("tasklist")
                case "1":
                    subprocess.run("tasklist /?", shell = True)
                    enter_untuk_kembali_ke_menu_command_prompt_tasklist()
                case "2":
                    subprocess.run("tasklist", shell = True)
                    enter_untuk_kembali_ke_menu_command_prompt_tasklist()
                case "3":
                    subprocess.run("tasklist /SVC", shell = True)
                    enter_untuk_kembali_ke_menu_command_prompt_tasklist()
                case _:
                    print("Input Tidak Valid!")
                    pilih_menu()
        pilih_menu()
    def menu_command_prompt_taskkill():
        def enter_untuk_kembali_ke_menu_command_prompt_taskkill():
            input("Tekan Enter untuk kembali (Ctrl + C untuk keluar)")
            menu_command_prompt_taskkill()
        bersihkan_layar()
        print("beranda > integrasi CLI Windows Command Prompt > perintah Command Prompt taskkill\n")
        cetak_informasi_pengembang()
        print("Hentikan proses aplikasi yang sedang berjalan\n")
        print("Daftar menu perintah Command Prompt taskkill")
        print("[-] bersihkan layar")
        print("[-0] kembali")
        print("[-00] beranda")
        print("[-000] keluar")
        print("[#:] buka file teks untuk menjalankan perintah Command Prompt otomatis")
        print("[0] masukkan perintah Command Prompt manual")
        print("[1] bantuan taskkill (taskkill /?)")
        def pilih_menu():
            menu_yang_dipilih = input("Pilih nomor : ")
            match menu_yang_dipilih:
                case "-":
                    menu_command_prompt_taskkill()
                case "-0":
                    menu_integrasi_command_prompt()
                case "-00":
                    beranda()
                case "-000":
                    print("Menutup program ...")
                    exit(0)
                case "#:":
                    buka_file_teks({"Command Prompt" : "taskkill"})
                case "0":
                    input_perintah_command_prompt_manual("taskkill")
                case "1":
                    subprocess.run("taskkill /?", shell = True)
                    enter_untuk_kembali_ke_menu_command_prompt_taskkill()
                case _:
                    print("Input Tidak Valid!")
                    pilih_menu()
        pilih_menu()
    def menu_command_prompt_shutdown():
        def enter_untuk_kembali_ke_menu_command_prompt_shutdown():
            input("Tekan Enter untuk kembali (Ctrl + C untuk keluar)")
            menu_command_prompt_shutdown()
        bersihkan_layar()
        print("beranda > integrasi CLI Windows Command Prompt > perintah Command Prompt shutdown")
        cetak_informasi_pengembang()
        print("Daftar menu perintah Command Prompt shutdown")
        print("[-] bersihkan layar")
        print("[-0] kembali")
        print("[-00] beranda")
        print("[-000] keluar")
        print("[#:] buka file teks untuk menjalankan perintah Command Prompt otomatis")
        print("[0] masukkan perintah Command Prompt manual")
        print("[1] bantuan shutdown (shutdown)")
        print("[2] tampilkan antarmuka pengguna grafis shutdown (shutdown /i)")
        print("[3] tutup seluruh aplikasi yang berjalan dan keluar dari akun pengguna komputer yang digunakan (shutdown /l)")
        print("[4] matikan komputer (shutdown /s)")
        print("[5] matikan komputer. Pada booting berikutnya, jika login mulai ulang otomatis diaktifkan, login otomatis dan kunci interaktif pengguna terakhir.")
        print("    Setelah masuk, memulai ulang beberapa aplikasi yang terdaftar (shutdown /sg)")
        print("[6] matikan dan nyalakan kembali komputer (shutdown /r)")
        print("[7] matikan dan nyalakan kembali komputer. Setelah sistem di reboot, jika login mulai ulang otomatis diaktifkan, login otomatis dan kunci interaktif pengguna terakhir.")
        print("    Setelah masuk, memulai ulang beberapa aplikasi yang terdaftar (shutdown /g)")
        def pilih_menu():
            menu_yang_dipilih = input("Pilih nomor : ")
            match menu_yang_dipilih:
                case "-":
                    menu_command_prompt_shutdown()
                case "-0":
                    menu_integrasi_command_prompt()
                case "-00":
                    beranda()
                case "-000":
                    print("Menutup program ...")
                    exit(0)
                case "#:":
                    buka_file_teks({"Command Prompt" : "shutdown"})
                case "0":
                    input_perintah_command_prompt_manual("shutdown")
                case "1":
                    subprocess.run("shutdown", shell = True)
                    enter_untuk_kembali_ke_menu_command_prompt_shutdown()
                case "2":
                    print("Jendela antarmuka pengguna grafis shutdown dibuka!")
                    subprocess.run("shutdown /i", shell = True)
                    print("Jendela antarmuka pengguna grafis shutdown ditutup!")
                    enter_untuk_kembali_ke_menu_command_prompt_shutdown()
                case "3":
                    subprocess.run("shutdown /l", shell = True)
                    enter_untuk_kembali_ke_menu_command_prompt_shutdown()
                case "4":
                    subprocess.run("shutdown /s", shell = True)
                    enter_untuk_kembali_ke_menu_command_prompt_shutdown()
                case "5":
                    subprocess.run("shutdown /sg", shell = True)
                    enter_untuk_kembali_ke_menu_command_prompt_shutdown()
                case "6":
                    subprocess.run("shutdown /r", shell = True)
                    enter_untuk_kembali_ke_menu_command_prompt_shutdown()
                case "7":
                    subprocess.run("shutdown /g", shell = True)
                    enter_untuk_kembali_ke_menu_command_prompt_shutdown()
                case _:
                    print("Input Tidak Valid!")
                    pilih_menu()
        pilih_menu()
    def menu_command_prompt_systeminfo():
        def enter_untuk_kembali_ke_menu_command_prompt_systeminfo():
            input("Tekan Enter untuk kembali (Ctrl + C untuk keluar)")
            menu_command_prompt_systeminfo()
        bersihkan_layar()
        print("beranda > integrasi CLI Windows Command Prompt > perintah Command Prompt systeminfo\n")
        cetak_informasi_pengembang()
        print("Daftar menu perintah Command Prompt systeminfo")
        print("[-] bersihkan layar")
        print("[-0] kembali")
        print("[-00] beranda")
        print("[-000] keluar")
        print("[#:] buka file teks untuk menjalankan perintah Command Prompt otomatis")
        print("[0] masukkan perintah Command Prompt manual")
        print("[1] bantuan systeminfo (systeminfo /?)")
        print("[2] tampilkan informasi sistem (systeminfo)")
        def pilih_menu():
            menu_yang_dipilih = input("Pilih nomor :")
            match menu_yang_dipilih:
                case "-":
                    menu_command_prompt_systeminfo()
                case "-0":
                    menu_integrasi_command_prompt()
                case "-00":
                    beranda()
                case "-000":
                    print("Menutup program ...")
                    exit(0)
                case "#:":
                    buka_file_teks({"Command Prompt" : "systeminfo"})
                case "0":
                    input_perintah_command_prompt_manual("systeminfo")
                case "1":
                    subprocess.run("systeminfo /?", shell = True)
                    enter_untuk_kembali_ke_menu_command_prompt_systeminfo()
                case "2":
                    subprocess.run("systeminfo", shell = True)
                    enter_untuk_kembali_ke_menu_command_prompt_systeminfo()
                case _:
                    print("Input Tidak Valid!")
                    pilih_menu()
        pilih_menu()
    def menu_command_prompt_sc():
        def enter_untuk_kembali_ke_menu_command_prompt_sc():
            input("Tekan Enter untuk kembali (Ctrl + C untuk keluar)")
            menu_command_prompt_sc()
        bersihkan_layar()
        print("beranda > integrasi CLI Windows Command Prompt > perintah Command Prompt sc\n")
        cetak_informasi_pengembang()
        print("Daftar menu perintah Command Prompt sc")
        print("[-] bersihkan layar")
        print("[-0] kembali")
        print("[-00] beranda")
        print("[-000] keluar")
        print("[#:] buka file teks untuk menjalankan perintah Command Prompt otomatis")
        print("[0] masukkan perintah Command Prompt manual")
        print("[1] bantuan sc (sc)")
        print("[2] tampilkan status layanan & driver yang aktif (sc query)")
        print("[3] tampilkan status layanan log event (sc query eventlog)")
        print("[4] tampilkan status layanan log event yang diperpanjang (sc queryex eventlog)")
        print("[5] tampilkan hanya driver yang aktif (sc query type= driver)")
        print("[6] tampilkan hanya layanan Win32 (sc query type= service)")
        print("[7] tampilkan seluruh driver dan layanan (sc query state= all)")
        print("[8] tampilkan dengan buffer 50 byte (sc query bufsize= 50)")
        print("[9] tampilkan layanan aktif tidak dalam grup (sc queryex group= \"\")")
        print("[10] tampilkan seluruh layanan interaktif (sc query type= interact)")
        print("[11] tampilkan seluruh driver NDIS (sc query type= driver group= NDIS)")
        def pilih_menu():
            menu_yang_dipilih = input("Pilih nomor : ")
            match menu_yang_dipilih:
                case "-":
                    menu_command_prompt_sc()
                case "-0":
                    menu_integrasi_command_prompt()
                case "-00":
                    beranda()
                case "-000":
                    print("Menutup program ...")
                case "#:":
                    buka_file_teks({"Command Prompt" : "sc"})
                case "0":
                    input_perintah_command_prompt_manual("sc")
                case "1":
                    subprocess.run("sc", shell = True)
                    enter_untuk_kembali_ke_menu_command_prompt_sc()
                case "2":
                    subprocess.run("sc query", shell = True)
                    enter_untuk_kembali_ke_menu_command_prompt_sc()
                case "3":
                    subprocess.run("sc query eventlog", shell = True)
                    enter_untuk_kembali_ke_menu_command_prompt_sc()
                case "4":
                    subprocess.run("sc queryex eventlog", shell = True)
                    enter_untuk_kembali_ke_menu_command_prompt_sc()
                case "5":
                    subprocess.run("sc query type= driver", shell = True)
                    enter_untuk_kembali_ke_menu_command_prompt_sc()
                case "6":
                    subprocess.run("sc query type= service", shell = True)
                    enter_untuk_kembali_ke_menu_command_prompt_sc()
                case "7":
                    subprocess.run("sc query state= all", shell = True)
                    enter_untuk_kembali_ke_menu_command_prompt_sc()
                case "8":
                    subprocess.run("sc query bufsize= 50", shell = True)
                    enter_untuk_kembali_ke_menu_command_prompt_sc()
                case "9":
                    subprocess.run("sc queryex group= \"\"", shell = True)
                    enter_untuk_kembali_ke_menu_command_prompt_sc()
                case "10":
                    subprocess.run("sc query type= interact", shell = True)
                    enter_untuk_kembali_ke_menu_command_prompt_sc()
                case "11":
                    subprocess.run("sc query type= driver group= NDIS", shell = True)
                    enter_untuk_kembali_ke_menu_command_prompt_sc()
                case _:
                    print("Input Tidak Valid!")
                    pilih_menu()
        pilih_menu()
    def beranda():
        def enter_untuk_kembali_ke_beranda():
            input("Tekan Enter untuk kembali ke beranda (Ctrl + C untuk keluar)")
            beranda()
        bersihkan_layar()
        print("Python Script Program Command Line Interface (CLI)\n")
        cetak_informasi_pengembang()
        print("Tanggal pembaruan : 14 November 2023\n")
        print("Disclaimer : Beberapa program CLI PowerShell dan Command Prompt dapat merubah fungsi sistem. Kerusakan yang terjadi akibat tindakan pengguna adalah di luar tanggung jawab pengembang\n")
        print("Daftar Menu")
        print("[1] kriptografi")
        print("[2] kalkulator")
        print("[3] tampilkan informasi platform perangkat")
        print("[4] tampilkan versi Python")
        print("[5] integrasi Command Line Interface (CLI) Windows PowerShell")
        print("[6] integrasi Command Line Interface (CLI) Windows Command Prompt")
        print("[7] bersihkan")
        print("[8] keluar (Ctrl + C)\n")
        def pilih_menu():
            menu_yang_dipilih = input("Pilih nomor : ")
            match menu_yang_dipilih:
                case "1":
                    menu_kriptografi()
                case "2":
                    menu_kalkulator()
                case "3":
                    tampilkan_informasi_platform_perangkat()
                case "4":
                    if platform.system() == "Windows":
                        subprocess.run(["powershell", "py --version"], shell = True)
                    else:
                        subprocess.run("python3 --version", shell = True)
                    enter_untuk_kembali_ke_beranda()
                case "5":
                    menu_integrasi_powershell()
                case "6":
                    menu_integrasi_command_prompt()
                case "7":
                    beranda()
                case "8":
                    print("Menutup program ...")
                    exit(0)
                case _:
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
finally:
    print(f"Penggunaan memori di sepanjang program : {tracemalloc.get_tracemalloc_memory()} byte")