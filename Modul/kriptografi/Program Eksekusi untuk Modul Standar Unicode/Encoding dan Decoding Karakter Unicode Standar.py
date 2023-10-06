import kriptografi.unicode_standar, tkinter.filedialog, csv

__version__ = "1.1.0"

print("Kriptografi Unicode Standar\n")

encode_atau_decode = input("[encode/decode] : ")
if encode_atau_decode.lower() == "encode":
    direktori_file_txt = tkinter.filedialog.askopenfilename(defaultextension = ".txt", filetypes = [("Dokumen Teks", "*txt")])
    if direktori_file_txt:
        encoded_data = []
        with open(direktori_file_txt, "r") as file_txt:
            print("Melakukan encoding file ...")
            for data in file_txt:
                encoded_data.extend(kriptografi.unicode_standar.encoding_biner(data, False))
        print("Data setelah di encode : ")
        print(encoded_data)
        direktori_folder = tkinter.filedialog.askdirectory()
        if direktori_folder:
            with open(f"{direktori_folder}/{input('Masukkan nama file [.csv] : ')}.csv", "x") as file_baru:
                tulis_file = csv.writer(file_baru)
                tulis_file.writerow(encoded_data)
            
elif encode_atau_decode.lower() == "decode":
    direktori_file_csv = tkinter.filedialog.askopenfilename(defaultextension = ".csv", filetypes = [("Comma Separate Value (encoded)", "*csv")])
    if direktori_file_csv:
        with open(direktori_file_csv, "r") as file_csv:
            file_csv = csv.reader(file_csv)
            decoded_data = ""
            for data_per_baris in file_csv:
                print("Data sebelum di decode : ")
                print(data_per_baris)
                decoded_data = kriptografi.unicode_standar.decoding_biner(data_per_baris)
                break
            print("Data setelah di decode : ")
            print(decoded_data)
            direktori_folder = tkinter.filedialog.askdirectory()
            if direktori_folder:
                with open(f"{direktori_folder}/{input('Masukkan nama file [.txt] : ')}.txt", "x") as file_baru:
                    file_baru.write(decoded_data)
