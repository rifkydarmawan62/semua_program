import tkinter.filedialog, csv, os, typing, base64, binascii
from tkinter.filedialog import askopenfilename, askdirectory
from typing import Literal
import unicode_standar
from unicode_standar import *
try:
    def menu_encode_dan_decode_unicode_standar():
        os.system("cls")
        print("beranda > kriptografi > unicode standar\n")
        print("Instagram : @rifkydarmawan62")
        print("GitHub : rifkydarmawan62\n")
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
                os.system("cls")
                print("beranda > kriptografi > unicode standar > bantuan\n")
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
        os.system("cls")
        print("beranda > kriptografi > python base64\n")
        print("Instagram : @rifkydarmawan62")
        print("GitHub : rifkydarmawan62\n")
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
                print("beranda > kriptografi > python base64 > bantuan\n")
                print("Instagram : @rifkydarmawan62")
                print("GitHub : rifkydarmawan62\n")
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
        os.system("cls")
        print("beranda > kriptografi\n")
        print("Instagram : @rifkydarmawan62")
        print("GitHub : rifkydarmawan62\n")
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
    def beranda():
        os.system("cls")
        print("Script Program Python\n")
        print("Instagram : @rifkydarmawan62")
        print("GitHub : rifkydarmawan62\n")
        print("Tanggal pembaruan : 9 November 2023\n")
        print("Daftar Menu")
        print("[1] kriptografi")
        print("[2] bersihkan")
        print("[3] keluar (Ctrl + C)\n")
        def pilih_menu():
            menu_yang_dipilih = input("Pilih menu : ")
            if menu_yang_dipilih.lower() == "1" or menu_yang_dipilih.lower() == "kriptografi":
                menu_kriptografi()
            elif menu_yang_dipilih.lower() == "2" or menu_yang_dipilih.lower() == "bersihkan":
                beranda()
            elif menu_yang_dipilih.lower() == "3" or menu_yang_dipilih.lower() == "keluar":
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