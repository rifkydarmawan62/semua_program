import csv, os, base64, binascii, platform, subprocess, tracemalloc, zipfile
from tkinter.filedialog import askopenfilename, askdirectory
from typing import Literal, overload
try:
    from kriptografi.unicode_standar import *
except ModuleNotFoundError:
    print("Modul unicode_standar tidak ditemukan!")
else:
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
        def tampilkan_penggunaan_memori():
            print(f"{tracemalloc.get_tracemalloc_memory()} byte memori yang digunakan")
        def tampilkan_informasi_platform_perangkat():
            bersihkan_layar()
            print("beranda > tampilkan informasi platform perangkat\n")
            print(f"Direktori saat ini : {os.getcwd()}")
            print(f"Platform : {platform.platform()}")
            print(f"Sistem operasi : {platform.system()}")
            print(f"Versi sistem : {platform.version()}")
            print(f"Prosesor : {platform.processor()}")
            print(f"Jumlah prosesor : {os.cpu_count()}")
            print(f"Mesin : {platform.machine()}")
            print(f"Arsitektur : {platform.architecture()}")
        def tampilkan_variabel_lingkungan_sistem():
            bersihkan_layar()
            print("beranda > tampilkan variabel lingkungan sistem\n")
            print(f"Variabel lingkungan sistem :")
            for kunci, nilai in os.environ.items():
                print(f"{kunci} : {nilai}")
        def tekan_enter_untuk_kembali():
            input("Tekan Enter untuk kembali (Ctrl + C untuk keluar)")
        def tutup_program():
            print("Menutup program ...")
            exit(0)
        def input_tidak_valid():
            print("Input Tidak Valid!")
        while True:
            def jalankan_perintah(perintah : Literal["PowerShell", "Command Prompt"], lokasi_file : str):
                with open(lokasi_file, "r") as file_teks:
                    for perintah_per_baris in file_teks:
                        if perintah == "PowerShell":
                            print(f"Menjalankan perintah PowerShell {perintah_per_baris.strip()}")
                            subprocess.run(["powershell", perintah_per_baris.strip()], shell = True)
                        else:
                            print(f"Menjalankan perintah Command Prompt {perintah_per_baris.strip()}")
                            subprocess.run(perintah_per_baris.strip(), shell = True)
                        try:
                            input(f"Tekan Enter untuk melanjutkan perintah {perintah} (Ctrl + C untuk keluar dari perintah)")
                        except KeyboardInterrupt:
                            break
                print(f"Perintah dari file {lokasi_file} selesai dijalankan!")
            bersihkan_layar()
            print("Python Script Program Command Line Interface (CLI)\n")
            cetak_informasi_pengembang()
            print("Tanggal pembaruan : 17 November 2023\n")
            print("Disclaimer : Beberapa program CLI PowerShell dan Command Prompt dapat merubah fungsi sistem. Kerusakan yang terjadi akibat tindakan pengguna adalah di luar tanggung jawab pengembang")
            print("Daftar Menu")
            print("[%] tampilkan penggunaan memori")
            print("[1] kriptografi")
            print("[2] kalkulator")
            print("[3] tampilkan informasi platform perangkat")
            print("[4] tampilkan variabel lingkungan sistem")
            print("[5] tampilkan versi Python")
            print("[6] integrasi Command Line Interface (CLI) Windows PowerShell")
            print("[7] integrasi Command Line Interface (CLI) Windows Command Prompt")
            print("[8] python zipfile")
            print("[9] bersihkan")
            print("[10] keluar (Ctrl + C)\n")
            while True:
                menu_yang_dipilih = input("Pilih nomor : ")
                match menu_yang_dipilih:
                    case "%":
                        tampilkan_penggunaan_memori()
                        tekan_enter_untuk_kembali()
                    case "1":
                        menu_kriptografi = True
                        while menu_kriptografi:
                            bersihkan_layar()
                            print("beranda > kriptografi\n")
                            cetak_informasi_pengembang()
                            print("Daftar Menu Kriptografi")
                            print("[%] tampilkan penggunaan memori")
                            print("[1] unicode standar")
                            print("[2] python base64")
                            print("[3] bersihkan")
                            print("[4] beranda")
                            print("[5] keluar (Ctrl + C)\n")
                            while True:
                                menu_yang_dipilih = input("Pilih nomor : ")
                                match menu_yang_dipilih:
                                    case "%":
                                        tampilkan_penggunaan_memori()
                                        tekan_enter_untuk_kembali()
                                    case "1":
                                        menu_unicode_standar = True
                                        while menu_unicode_standar:
                                            bersihkan_layar()
                                            print("beranda > kriptografi > unicode standar\n")
                                            cetak_informasi_pengembang()
                                            print("Menyediakan keamanan data dan kerahasiaan data file teks dengan kriptografi unicode standar")
                                            print("Encode dan decode unicode standar hanya dapat digunakan pada teks karakter unicode yang akan di encode menjadi bilangan heksadesimal, desimal, oktal, dan biner.")
                                            print("Memiliki tingkat keamanan kriptografi yang rendah\n")
                                            print("Daftar Menu Encode dan Decode Unicode Standar")
                                            print("[%] tampilkan penggunaan memori")
                                            print("[1] encode heksadesimal")
                                            print("[2] encode desimal")
                                            print("[3] encode oktal")
                                            print("[4] encode biner")
                                            print("[5] decode heksadesimal")
                                            print("[6] decode desimal")
                                            print("[7] decode oktal")
                                            print("[8] decode biner")
                                            print("[9] bersihkan")
                                            print("[10] kembali")
                                            print("[11] beranda")
                                            print("[12] keluar (Ctrl + C)\n")
                                            while True:
                                                def pilih_file_unicode_standar(__encode_atau_decode : Literal["encoding heksadesimal", "encoding desimal", "encoding oktal", "encoding biner", "decoding heksadesimal", "decoding desimal", "decoding oktal", "decoding biner"]):
                                                    print("Tekan ALT + Tab untuk membuka jendela baru untuk memilih file")
                                                    def baca_file(__direktori_file : str):
                                                        if __direktori_file:
                                                            print(f"Direktori file untuk {__encode_atau_decode} {__direktori_file}")
                                                            if ".csv" == __direktori_file[-4:].lower():
                                                                decoded_data : str = ""
                                                                with open(__direktori_file, "r") as file_yang_di_baca:
                                                                    file_csv = csv.reader(file_yang_di_baca)
                                                                    print("Data sebelum di decode : ")
                                                                    for data_per_baris in file_csv:
                                                                        print(data_per_baris)
                                                                        if __encode_atau_decode == "decoding heksadesimal":
                                                                            decoded_data = decoding_heksadesimal(data_per_baris)
                                                                        elif __encode_atau_decode == "decoding desimal":
                                                                            decoded_data = decoding_desimal(data_per_baris)
                                                                        elif __encode_atau_decode == "decoding oktal":
                                                                            decoded_data = decoding_oktal(data_per_baris)
                                                                        elif __encode_atau_decode == "decoding biner":
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
                                                                    #kembali_ke_menu_unicode_standar()
                                                                else:
                                                                    print("Data yang telah di decode tidak disimpan")
                                                                    #kembali_ke_menu_unicode_standar()
                                                            elif ".txt" == __direktori_file[-4:].lower():
                                                                if "encoding" in __encode_atau_decode:
                                                                    encoded_data : list = []
                                                                    with open(__direktori_file, "r") as file_yang_di_baca:
                                                                        print("Melakukan encoding file ...")
                                                                        for data_per_baris in file_yang_di_baca:
                                                                            if __encode_atau_decode == "encoding heksadesimal":
                                                                                encoded_data.extend(encoding_heksadesimal(data_per_baris))
                                                                            elif __encode_atau_decode == "encoding desimal":
                                                                                encoded_data.extend(encoding_desimal(data_per_baris))
                                                                            elif __encode_atau_decode == "encoding oktal":
                                                                                encoded_data.extend(encoding_oktal(data_per_baris))
                                                                            elif __encode_atau_decode == "encoding biner":
                                                                                encoded_data.extend(encoding_biner(data_per_baris))
                                                                    print("Data setelah di encode : ")
                                                                    print(encoded_data)
                                                                    print("Tekan ALT + Tab untuk membuka jendela baru untuk menyimpan data setelah di encode")
                                                                    lokasi_folder_file_yang_di_encode = askdirectory(title = "Pilih Folder Untuk Menyimpan File Yang Di Encode")
                                                                    if lokasi_folder_file_yang_di_encode:
                                                                        nama_file_yang_di_encode = input("*Masukkan nama file (Berikutnya tipe file): ")
                                                                        tipe_file_yang_di_encode = input("*Pilih tipe file [txt/csv]: ")
                                                                        match tipe_file_yang_di_encode.lower():
                                                                            case "csv" | ".csv":
                                                                                tipe_file_yang_di_encode = ".csv"
                                                                                with open(f"{lokasi_folder_file_yang_di_encode}/{nama_file_yang_di_encode}{tipe_file_yang_di_encode}", "x") as file_baru:
                                                                                    file_csv_baru = csv.writer(file_baru)
                                                                                    file_csv_baru.writerow(encoded_data)
                                                                                print(f"File baru dibuat di direktori {lokasi_folder_file_yang_di_encode}/{nama_file_yang_di_encode}{tipe_file_yang_di_encode}")
                                                                            case "txt" | ".txt":
                                                                                tipe_file_yang_di_encode = ".txt"
                                                                                with open(f"{lokasi_folder_file_yang_di_encode}/{nama_file_yang_di_encode}{tipe_file_yang_di_encode}", "x") as file_baru:
                                                                                    for karakter_tunggal_encoded in encoded_data:
                                                                                        file_baru.write(f"{karakter_tunggal_encoded}\n")
                                                                                print(f"File baru dibuat di direktori {lokasi_folder_file_yang_di_encode}/{nama_file_yang_di_encode}{tipe_file_yang_di_encode}")
                                                                            case _:
                                                                                print("Tipe File Tidak Valid!")
                                                                    else:
                                                                        print("Data yang telah di encode tidak disimpan!")
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
                                                                            if __encode_atau_decode == "decoding heksadesimal":
                                                                                decoded_data = decoded_data + decoding_heksadesimal(data_per_baris.strip())
                                                                            elif __encode_atau_decode == "decoding desimal":
                                                                                decoded_data = decoded_data + decoding_desimal(data_per_baris.strip())
                                                                            elif __encode_atau_decode == "decoding oktal":
                                                                                decoded_data = decoded_data + decoding_oktal(data_per_baris.strip())
                                                                            elif __encode_atau_decode == "decoding biner":
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
                                                                    else:
                                                                        print("Data yang telah di decode tidak disimpan!")
                                                        else:
                                                            print("File Tidak Dibuka!")
                                                    if "encoding" in __encode_atau_decode.lower():
                                                        direktori_file = askopenfilename(title = f"Pilih File Untuk {__encode_atau_decode.title()}", filetypes = [("Dokumen Teks", "*.txt")])
                                                        baca_file(direktori_file)
                                                    else:
                                                        direktori_file = askopenfilename(title = f"Pilih File Untuk {__encode_atau_decode.title()}", filetypes = [("Dokumen Teks", "*.txt"), ("Comma Separate Value", "*.csv")])
                                                        baca_file(direktori_file)
                                                menu_yang_dipilih = input("Pilih nomor : ")
                                                match menu_yang_dipilih:
                                                    case "%":
                                                        tampilkan_penggunaan_memori()
                                                        tekan_enter_untuk_kembali()
                                                    case "1":
                                                        pilih_file_unicode_standar("encoding heksadesimal")
                                                        tekan_enter_untuk_kembali()
                                                    case "2":
                                                        pilih_file_unicode_standar("encoding desimal")
                                                        tekan_enter_untuk_kembali()
                                                    case "3":
                                                        pilih_file_unicode_standar("encoding oktal")
                                                        tekan_enter_untuk_kembali()
                                                    case "4":
                                                        pilih_file_unicode_standar("encoding biner")
                                                        tekan_enter_untuk_kembali()
                                                    case "5":
                                                        pilih_file_unicode_standar("decoding heksadesimal")
                                                        tekan_enter_untuk_kembali()
                                                    case "6":
                                                        pilih_file_unicode_standar("decoding desimal")
                                                        tekan_enter_untuk_kembali()
                                                    case "7":
                                                        pilih_file_unicode_standar("decoding oktal")
                                                        tekan_enter_untuk_kembali()
                                                    case "8":
                                                        pilih_file_unicode_standar("decoding biner")
                                                        tekan_enter_untuk_kembali()
                                                    case "9":
                                                        break
                                                    case "10":
                                                        menu_unicode_standar = False
                                                    case "11":
                                                        menu_unicode_standar = False
                                                        menu_kriptografi = False
                                                    case "12":
                                                        tutup_program()
                                                    case _:
                                                        input_tidak_valid()
                                                        continue
                                                break
                                    case "2":
                                        menu_python_base64 = True
                                        while menu_python_base64:
                                            bersihkan_layar()
                                            print("beranda > kriptografi > python base64\n")
                                            cetak_informasi_pengembang()
                                            print("Daftar Menu Encode dan Decode Python Base64")
                                            print("[%] tampilkan penggunaan memori")
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
                                            print("[13] bersihkan")
                                            print("[14] kembali")
                                            print("[15] beranda")
                                            print("[16] keluar (Ctrl + C)")
                                            while True:
                                                menu_yang_dipilih = input("Pilih nomor : ")
                                                match menu_yang_dipilih:
                                                    case "%":
                                                        tampilkan_penggunaan_memori()
                                                        tekan_enter_untuk_kembali()
                                                    case "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" | "10" | "11" | "12":
                                                        print("Tekan ALT + Tab untuk membuka jendela baru untuk memilih file")
                                                        encode_atau_decode : tuple
                                                        match menu_yang_dipilih:
                                                            #Nomor encode
                                                            case "1" | "3" | "5" | "7" | "9" | "11":
                                                                encode_atau_decode = "Encoding", "encode"
                                                            case _:
                                                                encode_atau_decode = "Decoding", "decode"
                                                        direktori_file = askopenfilename(title = f"Pilih File Untuk {encode_atau_decode[0]}", filetypes = [("Dokumen Teks", "*.txt")])
                                                        if direktori_file:
                                                            print(f"Direktori file untuk {encode_atau_decode[0].lower()} {direktori_file}")
                                                            if encode_atau_decode[0] == "Decoding":
                                                                print("Data sebelum di decode : ")
                                                                with open(direktori_file, "r") as file_yang_di_buka:
                                                                    for data_per_baris in file_yang_di_buka:
                                                                        print(data_per_baris.strip())
                                                            data_di_encode : bytes = b""
                                                            data_di_decode : bytes = b""
                                                            print(f"Melakukan {encode_atau_decode[0].lower()} file ...")
                                                            try:
                                                                with open(direktori_file, "rb") as file_yang_di_buka:
                                                                    for data_per_baris in file_yang_di_buka:
                                                                        match menu_yang_dipilih:
                                                                            case "1":
                                                                                data_di_encode = data_di_encode + base64.b16encode(data_per_baris)
                                                                            case "2":
                                                                                data_di_decode = data_di_decode + base64.b16decode(data_per_baris)
                                                                            case "3":
                                                                                data_di_encode = data_di_encode + base64.b32encode(data_per_baris)
                                                                            case "4":
                                                                                data_di_decode = data_di_decode + base64.b32decode(data_per_baris)
                                                                            case "5":
                                                                                data_di_encode = data_di_encode + base64.b32hexencode(data_per_baris)
                                                                            case "6":
                                                                                data_di_decode = data_di_decode + base64.b32hexdecode(data_per_baris)
                                                                            case "7":
                                                                                data_di_encode = data_di_encode + base64.b64encode(data_per_baris)
                                                                            case "8":
                                                                                data_di_decode = data_di_decode + base64.b64decode(data_per_baris)
                                                                            case "9":
                                                                                data_di_encode = data_di_encode + base64.standard_b64encode(data_per_baris)
                                                                            case "10":
                                                                                data_di_decode = data_di_decode + base64.standard_b64decode(data_per_baris)
                                                                            case "11":
                                                                                data_di_encode = data_di_encode + base64.a85encode(data_per_baris)
                                                                            case "12":
                                                                                data_di_decode = data_di_decode + base64.a85decode(data_per_baris)
                                                                            case _:
                                                                                break
                                                            except binascii.Error as ascii_error:
                                                                print(f"Terjadi error saat melakukan {encode_atau_decode[0].lower()} file")
                                                                print(f"Pesan error :\n{ascii_error}")
                                                            else:
                                                                print(f"Data setelah di {encode_atau_decode[1]} : ")
                                                                if encode_atau_decode[1] == "encode":
                                                                    print(data_di_encode)
                                                                else:
                                                                    print(data_di_decode)
                                                                print(f"Tekan ALT + Tab untuk membuka jendela baru untuk menyimpan data setelah di {encode_atau_decode[1]}")
                                                                lokasi_folder_file = askdirectory(title = f"Pilih Folder Untuk Menyimpan Data Yang Di {encode_atau_decode[1].title()}")
                                                                if lokasi_folder_file:
                                                                    nama_file = f"{input('Masukkan nama file (.txt) : ')}.txt"
                                                                    with open(f"{lokasi_folder_file}/{nama_file}", "x") as file_baru:
                                                                        if encode_atau_decode[1] == "encode":
                                                                            file_baru.write(data_di_encode.decode())
                                                                        else:
                                                                            file_baru.write(data_di_decode.decode())
                                                                    print(f"File baru dibuat di direktori {lokasi_folder_file}/{nama_file}")
                                                                else:
                                                                    print(f"Data yang telah di {encode_atau_decode[1]} tidak disimpan!")
                                                        else:
                                                            print("File Tidak Dibuka!")
                                                        tekan_enter_untuk_kembali()
                                                    case "13":
                                                        break
                                                    case "14":
                                                        menu_python_base64 = False
                                                    case "15":
                                                        menu_python_base64 = False
                                                        menu_kriptografi = False
                                                    case "16":
                                                        tutup_program()
                                                    case _:
                                                        input_tidak_valid()
                                                        continue
                                                break
                                    case "3":
                                        break
                                    case "4":
                                        menu_kriptografi = False
                                    case "5":
                                        tutup_program()
                                    case _:
                                        input_tidak_valid()
                                        continue
                                break
                    case "2":
                        menu_kalkulator = True
                        while menu_kalkulator:
                            bersihkan_layar()
                            print("beranda > kalkulator\n")
                            cetak_informasi_pengembang()
                            print("Daftar menu kalkulator")
                            print("[%] tampilkan penggunaan memori")
                            print("[1] kalkulator dasar")
                            print("[2] konversi satuan bilangan")
                            print("[3] bersihkan")
                            print("[4] beranda")
                            print("[5] keluar (Ctrl + C)\n")
                            while True:
                                menu_yang_dipilih = input("Pilih nomor : ")
                                match menu_yang_dipilih:
                                    case "%":
                                        tampilkan_penggunaan_memori()
                                        tekan_enter_untuk_kembali()
                                        break
                                    case "1":
                                        menu_kalkulator_dasar = True
                                        while menu_kalkulator_dasar:
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
                                            while True:
                                                operasi_yang_diinput = input("Masukkan input : ")
                                                match operasi_yang_diinput:
                                                    case "1":
                                                        break
                                                    case "2":
                                                        menu_kalkulator_dasar = False
                                                        break
                                                    case "3":
                                                        menu_kalkulator_dasar = False
                                                        menu_kalkulator = False
                                                        break
                                                    case "4":
                                                        tutup_program()
                                                        break
                                                    case _:
                                                        try:
                                                            operasi_yang_diinput = eval(operasi_yang_diinput)
                                                        except SyntaxError:
                                                            print("Input Operator Tidak Valid!")
                                                        except NameError:
                                                            print("Tidak dapat melakukan operasi terhadap nama variabel, kelas, atau fungsi")
                                                        except ZeroDivisionError:
                                                            print("Pembagian Nol Tidak Valid!")
                                                        else:
                                                            print(f"Hasil = {operasi_yang_diinput}")
                                        break
                                    case "2":
                                        menu_konversi_satuan_bilangan = True
                                        while menu_konversi_satuan_bilangan:
                                            bersihkan_layar()
                                            print("beranda > kalkulator > konversi satuan bilangan\n")
                                            cetak_informasi_pengembang()
                                            print("Daftar menu konversi satuan bilangan")
                                            print("[%] tampilkan penggunaan memori")
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
                                            while True:
                                                nomor_yang_dipilih = input("Pilih nomor : ")
                                                try:
                                                    match nomor_yang_dipilih:
                                                        case "%":
                                                            tampilkan_penggunaan_memori()
                                                            tekan_enter_untuk_kembali()
                                                        case "1":
                                                            bilangan_heksadesimal = input("Masukkan bilangan heksadesimal : ")
                                                            print(f"Hasil bilangan desimal = {int('0x' + bilangan_heksadesimal, base = 0)}")
                                                            tekan_enter_untuk_kembali()
                                                        case "2":
                                                            bilangan_desimal = input("Masukkan bilangan desimal : ")
                                                            print(f"Hasil bilangan heksadesimal = {hex(int(bilangan_desimal))[2:]}")
                                                            tekan_enter_untuk_kembali()
                                                        case "3":
                                                            bilangan_heksadesimal = input("Masukkan bilangan heksadesimal : ")
                                                            print(f"Hasil bilangan oktal = {oct(int('0x' + bilangan_heksadesimal, base = 0))[2:]}")
                                                            tekan_enter_untuk_kembali()
                                                        case "4":
                                                            bilangan_oktal = input("Masukkan bilangan oktal : ")
                                                            print(f"Hasil bilangan heksadesimal = {hex(int('0o' + bilangan_oktal, base = 0))[2:]}")
                                                            tekan_enter_untuk_kembali()
                                                        case "5":
                                                            bilangan_heksadesimal = input("Masukkan bilangan heksadesimal : ")
                                                            print(f"Hasil bilangan biner = {bin(int('0x' + bilangan_heksadesimal, base = 0))[2:]}")
                                                            tekan_enter_untuk_kembali()
                                                        case "6":
                                                            bilangan_biner = input("Masukkan bilangan biner : ")
                                                            print(f"Hasil bilangan heksadesimal = {hex(int('0b' + bilangan_biner, base = 0))[2:]}")
                                                            tekan_enter_untuk_kembali()
                                                        case "7":
                                                            bilangan_desimal = input("Masukkan bilangan desimal : ")
                                                            print(f"Hasil bilangan oktal = {oct(int(bilangan_desimal))[2:]}")
                                                            tekan_enter_untuk_kembali()
                                                        case "8":
                                                            bilangan_oktal = input("Masukkan bilangan oktal : ")
                                                            print(f"Hasil bilangan desimal = {int('0o' + bilangan_oktal, base = 0)}")
                                                            tekan_enter_untuk_kembali()
                                                        case "9":
                                                            bilangan_desimal = input("Masukkan bilangan desimal : ")
                                                            print(f"Hasil bilangan biner = {bin(int(bilangan_desimal))[2:]}")
                                                            tekan_enter_untuk_kembali()
                                                        case "10":
                                                            bilangan_biner = input("Masukkan bilangan biner : ")
                                                            print(f"Hasil bilangan desimal = {int('0b' + bilangan_biner, base = 0)}")
                                                            tekan_enter_untuk_kembali()
                                                        case "11":
                                                            bilangan_oktal = input("Masukkan bilangan oktal : ")
                                                            print(f"Hasil bilangan biner = {bin(int('0o' + bilangan_oktal, base = 0))[2:]}")
                                                            tekan_enter_untuk_kembali()
                                                        case "12":
                                                            bilangan_biner = input("Masukkan bilangan biner : ")
                                                            print(f"Hasil bilangan oktal = {oct(int('0b' + bilangan_biner, base = 0))[2:]}")
                                                            tekan_enter_untuk_kembali()
                                                        case "13":
                                                            break
                                                        case "14":
                                                            menu_konversi_satuan_bilangan = False
                                                        case "15":
                                                            menu_konversi_satuan_bilangan = False
                                                            menu_kalkulator = False
                                                        case "16":
                                                            tutup_program()
                                                        case _:
                                                            input_tidak_valid()
                                                            continue
                                                    break
                                                except ValueError:
                                                    print("Nilai yang diinput tidak valid!")
                                                    continue
                                    case "3":
                                        break
                                    case "4":
                                        menu_kalkulator = False
                                    case "5":
                                        tutup_program()
                                    case _:
                                        input_tidak_valid()
                                        continue
                                break
                    case "3":
                        tampilkan_informasi_platform_perangkat()
                        tekan_enter_untuk_kembali()
                    case "4":
                        tampilkan_variabel_lingkungan_sistem()
                        tekan_enter_untuk_kembali()
                    case "5":
                        if platform.system() == "Windows":
                            subprocess.run("powershell py --version", shell = True)
                        else:
                            subprocess.run("python3 --version", shell = True)
                        tekan_enter_untuk_kembali()
                    case "6":
                        menu_integrasi_powershell = True
                        while menu_integrasi_powershell:
                            bersihkan_layar()
                            print("beranda > integrasi Command Line Interface Windows PowerShell\n")
                            cetak_informasi_pengembang()
                            if platform.system() != "Windows":
                                print("Integrasi CLI PowerShell Hanya Mendukung Sistem Operasi Windows!")
                                print(f"Sistem operasi yang anda gunakan : {platform.system()}")
                                input("Tekan Enter untuk kembali ke beranda (Ctrl + C untuk keluar)")
                                menu_integrasi_powershell = False
                                break
                            def input_perintah_powershell_manual():
                                perintah_powershell = input("Masukkan perintah PowerShell : ")
                                if perintah_powershell != "":
                                    subprocess.run(["powershell", f"{perintah_powershell}"], shell = True)
                                else:
                                    print("Input Kosong!")
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
                            print("[%] tampilkan penggunaan memori")
                            print("[0] masukkan perintah PowerShell secara manual")
                            print("[1] tampilkan direktori saat ini (dir)")
                            print("[2] tampilkan seluruh proses aplikasi yang berjalan di latar belakang (ps)")
                            print("[3] tampilkan detail versi Windows PowerShell ($PSVersionTable)")
                            print("[4] tampilkan versi Windows PowerShell ($PSVersionTable.PSVersion)")
                            print("[5] tampilkan topik bantuan (help topic)")
                            print("[6] tampilkan perintah PowerShell yang tersedia dalam CLI (command)")
                            print("[7] tampilkan perintah PowerShell yang tersedia dalam GUI (show-command)")
                            print("[8] tampilkan alias (alias)")
                            print("[9] buka dan muat file dalam format tabel heksadesimal (Format-Hex \"{direktori file}\")")
                            print("[10] ambil clipboard (Get-Clipboard)")
                            while True:
                                menu_yang_dipilih = input("Pilih nomor : ")
                                match menu_yang_dipilih:
                                    case "-":
                                        break
                                    case "-0":
                                        menu_integrasi_powershell = False
                                    case "-00":
                                        tutup_program()
                                    case "#:":
                                        print("Tekan Alt + Tab untuk membuka jendela baru untuk memilih file")
                                        direktori_file = askopenfilename(title = "File Teks Untuk Menjalankan Baris Perintah Powershell Secara Otomatis", filetypes = (["Dokumen Teks", "*.txt"], ["Log Teks", "*.log"]))
                                        if direktori_file:
                                            jalankan_perintah("PowerShell", direktori_file)
                                        else:
                                            print("File Tidak Dibuka!")
                                        tekan_enter_untuk_kembali()
                                    case "%":
                                        tampilkan_penggunaan_memori()
                                        tekan_enter_untuk_kembali()
                                    case "0":
                                        input_perintah_powershell_manual()
                                        tekan_enter_untuk_kembali()
                                    case "1":
                                        subprocess.run(["powershell", "dir"], shell = True)
                                        tekan_enter_untuk_kembali()
                                    case "2":
                                        subprocess.run(["powershell", "ps"], shell = True)
                                        tekan_enter_untuk_kembali()
                                    case "3":
                                        subprocess.run(["powershell", "$PSVersionTable"], shell = True)
                                        tekan_enter_untuk_kembali()
                                    case "4":
                                        subprocess.run(["powershell", "$PSVersionTable.PSVersion"], shell = True)
                                        tekan_enter_untuk_kembali()
                                    case "5":
                                        subprocess.run(["powershell", "help topic"], shell = True)
                                        tekan_enter_untuk_kembali()
                                    case "6":
                                        subprocess.run(["powershell", "command"], shell = True)
                                        tekan_enter_untuk_kembali()
                                    case "7":
                                        subprocess.run(["powershell", "show-command"], shell = True)
                                        tekan_enter_untuk_kembali()
                                    case "8":
                                        subprocess.run(["powershell", "alias"], shell = True)
                                        tekan_enter_untuk_kembali()
                                    case "9":
                                        print("Tekan Alt + Tab untuk membuka jendela baru untuk memilih file")
                                        direktori_file = askopenfilename(title = "Pilih File Agar Ditampilkan Dalam Format Tabel Heksadesimal")
                                        if direktori_file:
                                            subprocess.run(["powershell", f"format-hex \"{direktori_file}\""], shell = True)
                                        else:
                                            print("File Tidak Di Pilih!")
                                        tekan_enter_untuk_kembali()
                                    case "10":
                                        subprocess.run(["powershell", "Get-Clipboard"], shell = True)
                                        tekan_enter_untuk_kembali()
                                    case _:
                                        input_tidak_valid()
                                        continue
                                break
                    case "7":
                        menu_integrasi_command_prompt = True
                        while menu_integrasi_command_prompt:
                            bersihkan_layar()
                            print("beranda > integrasi CLI Windows Command Prompt\n")
                            cetak_informasi_pengembang()
                            if platform.system() != "Windows":
                                print("Integrasi CLI Command Prompt Hanya Mendukung Sistem Operasi Windows!")
                                print(f"Sistem operasi yang anda gunakan : {platform.system()}")
                                input("Tekan Enter untuk kembali ke beranda (Ctrl + C untuk keluar)")
                                menu_integrasi_command_prompt = False
                                break
                            def input_perintah_command_prompt_manual():
                                perintah_command_prompt = input("Masukkan perintah Command Prompt : ")
                                if perintah_command_prompt != "":
                                    subprocess.run(perintah_command_prompt, shell = True)
                                else:
                                    print("Input Kosong!")
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
                            print("[%] tampilkan penggunaan memori")
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
                            while True:
                                menu_yang_dipilih = input("Pilih nomor : ")
                                match menu_yang_dipilih:
                                    case "-":
                                        break
                                    case "-0":
                                        menu_integrasi_command_prompt = False
                                    case "-00":
                                        tutup_program()
                                    case "#:":
                                        print("Tekan Alt + Tab untuk membuka jendela baru untuk memilih file")
                                        direktori_file = askopenfilename(title = "File Teks Untuk Menjalankan Baris Perintah Command Prompt Secara Otomatis", filetypes = (["Dokumen Teks", "*.txt"], ["Log Teks", "*.log"]))
                                        if direktori_file:
                                            jalankan_perintah("Command Prompt", direktori_file)
                                        else:
                                            print("File Tidak Dibuka!")
                                        tekan_enter_untuk_kembali()
                                    case "%":
                                        tampilkan_penggunaan_memori()
                                        tekan_enter_untuk_kembali()
                                    case "0":
                                        input_perintah_command_prompt_manual()
                                        tekan_enter_untuk_kembali()
                                    case "1":
                                        subprocess.run("dir", shell = True)
                                        tekan_enter_untuk_kembali()
                                    case "2":
                                        subprocess.run("help", shell = True)
                                        tekan_enter_untuk_kembali()
                                    case "3":
                                        subprocess.run("color help", shell = True)
                                        tekan_enter_untuk_kembali()
                                    case _:
                                        input_tidak_valid()
                                        continue
                                break
                    case "9":
                        break
                    case "10":
                        tutup_program()
                        break
                    case _:
                        input_tidak_valid()
                        continue
                break
    except KeyboardInterrupt:
        tutup_program()
        