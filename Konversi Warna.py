import tkinter
from tkinter import messagebox

jendela = tkinter.Tk()
jendela.title("Konversi Warna")
#jendela.geometry("600x100+600+50")
jendela.configure(background="#dddddd")

class bilangan:
    class desimal:
        @staticmethod
        def merah():
            "Bilangan desimal merah"
            return int(bilah_merah.get())
        @staticmethod
        def hijau():
            "bilangan desimal hijau"
            return int(bilah_hijau.get())
        @staticmethod
        def biru():
            "Bilangan desimal biru"
            return int(bilah_biru.get())
    class hex:
        @staticmethod
        def merah():
            "Bilangan heksadesimal merah"
            if hex(int(bilah_merah.get()))[2:] == "0" or hex(int(bilah_merah.get()))[2:] == "1" or hex(int(bilah_merah.get()))[2:] == "2" or hex(int(bilah_merah.get()))[2:] == "3" or hex(int(bilah_merah.get()))[2:] == "4" or hex(int(bilah_merah.get()))[2:] == "5" or hex(int(bilah_merah.get()))[2:] == "6" or hex(int(bilah_merah.get()))[2:] == "7" or hex(int(bilah_merah.get()))[2:] == "8" or hex(int(bilah_merah.get()))[2:] == "9" or hex(int(bilah_merah.get()))[2:] == "a" or hex(int(bilah_merah.get()))[2:] == "b" or hex(int(bilah_merah.get()))[2:] == "c" or hex(int(bilah_merah.get()))[2:] == "d" or hex(int(bilah_merah.get()))[2:] == "e" or hex(int(bilah_merah.get()))[2:] == "f":
                return "0" + hex(int(bilah_merah.get()))[2:]
            else:
                return hex(int(bilah_merah.get()))[2:]
        @staticmethod
        def hijau():
            "Bilangan heksadesimal hijau"
            if hex(int(bilah_hijau.get()))[2:] == "0" or hex(int(bilah_hijau.get()))[2:] == "1" or hex(int(bilah_hijau.get()))[2:] == "2" or hex(int(bilah_hijau.get()))[2:] == "3" or hex(int(bilah_hijau.get()))[2:] == "4" or hex(int(bilah_hijau.get()))[2:] == "5" or hex(int(bilah_hijau.get()))[2:] == "6" or hex(int(bilah_hijau.get()))[2:] == "7" or hex(int(bilah_hijau.get()))[2:] == "8" or hex(int(bilah_hijau.get()))[2:] == "9" or hex(int(bilah_hijau.get()))[2:] == "a" or hex(int(bilah_hijau.get()))[2:] == "b" or hex(int(bilah_hijau.get()))[2:] == "c" or hex(int(bilah_hijau.get()))[2:] == "d" or hex(int(bilah_hijau.get()))[2:] == "e" or hex(int(bilah_hijau.get()))[2:] == "f":
                return "0" + hex(int(bilah_hijau.get()))[2:]
            else:
                return hex(int(bilah_hijau.get()))[2:]
        @staticmethod
        def biru():
            "Bilangan heksadesimal biru"
            if hex(int(bilah_biru.get()))[2:] == "0" or hex(int(bilah_biru.get()))[2:] == "1" or hex(int(bilah_biru.get()))[2:] == "2" or hex(int(bilah_biru.get()))[2:] == "3" or hex(int(bilah_biru.get()))[2:] == "4" or hex(int(bilah_biru.get()))[2:] == "5" or hex(int(bilah_biru.get()))[2:] == "6" or hex(int(bilah_biru.get()))[2:] == "7" or hex(int(bilah_biru.get()))[2:] == "8" or hex(int(bilah_biru.get()))[2:] == "9" or hex(int(bilah_biru.get()))[2:] == "a" or hex(int(bilah_biru.get()))[2:] == "b" or hex(int(bilah_biru.get()))[2:] == "c" or hex(int(bilah_biru.get()))[2:] == "d" or hex(int(bilah_biru.get()))[2:] == "e" or hex(int(bilah_biru.get()))[2:] == "f":
                return "0" + hex(int(bilah_biru.get()))[2:]
            else:
                return hex(int(bilah_biru.get()))[2:]
class konfigurasi:
    @staticmethod
    def nilai_desimal_warna():
        "Menkonfigurasi nilai desimal warna ketika bilah nilai warna digeser"
        nilai_merah.delete(first = 0, last = tkinter.END)
        nilai_hijau.delete(first = 0 ,last = tkinter.END)
        nilai_biru.delete(first=0, last = tkinter.END)
        nilai_merah.insert(index=0, string = str(bilah_merah.get()))
        nilai_hijau.insert(index=0, string = str(bilah_hijau.get()))
        nilai_biru.insert(index=0, string = str(bilah_biru.get()))
    @staticmethod
    def nilai_heksadesimal_warna():
        "Menkonfigurasi label nilai heksadesimal ketika bilah nilai warna digeser"
        input_kode_warna_hex.delete(first = 0, last = tkinter.END)
        input_kode_warna_hex.insert(index = 0, string = f"#{bilangan.hex.merah()}{bilangan.hex.hijau()}{bilangan.hex.biru()}")
        tampilan.configure(background = f"#{bilangan.hex.merah()}{bilangan.hex.hijau()}{bilangan.hex.biru()}")
def bilah_nilai(value):
    "Menkonfigurasi nilai desimal warna merah, hijau, dan biru; dan nilai heksadesimal warna ketika bilah nilai warna merah, hijau, dan biru digeser"
    konfigurasi.nilai_desimal_warna()
    konfigurasi.nilai_heksadesimal_warna()

class tombol:
    class menu:
        @staticmethod
        def pengembang():
            messagebox.showinfo(title = "Informasi Pengembang", message = "Dikembangkan oleh M Rifky Darmawan dengan Python\n\nTanggal dibuat : 4 Agustus 2023\nTanggal diperbarui : 5 November 2023\n\nGitHub : rifkydarmawan62")
    class kurangi:
        @staticmethod
        def bilah_nilai_merah():
            "Mengurangi bilah nilai merah"
            bilah_merah.set(bilah_merah.get()-1)
        @staticmethod
        def bilah_nilai_hijau():
            "Mengurangi bilah nilai hijau"
            bilah_hijau.set(bilah_hijau.get()-1)
        @staticmethod
        def bilah_nilai_biru():
            "Mengurangi bilah nilai biru"
            bilah_biru.set(bilah_biru.get()-1)
    class tambah:
        @staticmethod
        def bilah_nilai_merah():
            "Menambahkan bilah nilai merah"
            bilah_merah.set(bilah_merah.get()+1)
        @staticmethod
        def bilah_nilai_hijau():
            "Menambahkan bilah nilai hijau"
            bilah_hijau.set(bilah_hijau.get()+1)
        @staticmethod
        def bilah_nilai_biru():
            "Menambahkan bilah nilai biru"
            bilah_biru.set(bilah_biru.get()+1)
    class enter: 
        @staticmethod
        def input_bilangan_desimal(event):
            "Menkonfigurasi bilah nilai warna jika nilai angka valid ketika tombol enter ditekan"
            if nilai_merah.get().isdigit() and nilai_hijau.get().isdigit() and nilai_biru.get().isdigit():
                bilah_merah.set(nilai_merah.get())
                bilah_hijau.set(nilai_hijau.get())
                bilah_biru.set(nilai_biru.get())
        @staticmethod
        def input_bilangan_hex(event):
            "Menkonfigurasi bilah nilai dan bilangan desimal merah, hijau, biru ketika tombol enter ditekan"
            bilangan_hex = input_kode_warna_hex.get()
            if bilangan_hex[0] == "#":
                bilangan_hex = bilangan_hex.replace("#", "")
            if len(bilangan_hex) == 6 and bilangan_hex[0] != "#":
                bilah_merah.set(int(bilangan_hex[0:2], base = 16))
                bilah_hijau.set(int(bilangan_hex[2:4], base = 16))
                bilah_biru.set(int(bilangan_hex[4:6], base = 16))
    class salin_teks:
        "Menyalin teks ke clipboard"
        @staticmethod
        def kode_warna_hex():
            jendela.clipboard_append(string = f"#{bilangan.hex.merah()}{bilangan.hex.hijau()}{bilangan.hex.biru()}")

menu_dasar = tkinter.Menu(jendela, cursor = "hand2")
menu_dasar.add_command(label = "Info Pengembang", command = tombol.menu.pengembang)
jendela.configure(menu = menu_dasar)

label_rgb = tkinter.Label(jendela, text="R/G/B", foreground="#000000", background="#dddddd")
label_merah = tkinter.Label(jendela, text="R :", foreground="#000000", background="#ff0000")
label_hijau = tkinter.Label(jendela, text="G :", foreground="#000000", background="#00ff00")
label_biru = tkinter.Label(jendela, text="B :", foreground="#000000", background="#0000ff")
label_bilah = tkinter.Label(jendela, text="Bilah", foreground="#000000", background="#dddddd")
tombol_kurangi_bilah_nilai_merah = tkinter.Button(jendela, text="-", foreground="#000000", cursor="hand2", repeatdelay=500, repeatinterval=100, command=tombol.kurangi.bilah_nilai_merah)
tombol_kurangi_bilah_nilai_hijau = tkinter.Button(jendela, text="-", foreground="#000000", cursor="hand2", repeatdelay=500, repeatinterval=100, command=tombol.kurangi.bilah_nilai_hijau)
tombol_kurangi_bilah_nilai_biru = tkinter.Button(jendela, text="-", foreground="#000000", cursor="hand2", repeatdelay=500, repeatinterval=100, command=tombol.kurangi.bilah_nilai_biru)
bilah_merah = tkinter.Scale(jendela, from_=0, to=255, orient="horizontal", showvalue=False, cursor="hand2", command = bilah_nilai, length=300)
bilah_hijau = tkinter.Scale(jendela, from_=0, to=255, orient="horizontal", showvalue=False, cursor="hand2", command = bilah_nilai, length=300)
bilah_biru = tkinter.Scale(jendela, from_=0, to=255, orient="horizontal", showvalue=False, cursor="hand2", command = bilah_nilai, length=300)
tombol_tambah_nilai_skala_merah = tkinter.Button(jendela, text="+", foreground="#000000", cursor="hand2", repeatdelay=500, repeatinterval=100, command=tombol.tambah.bilah_nilai_merah)
tombol_tambah_nilai_skala_hijau = tkinter.Button(jendela, text="+", foreground="#000000", cursor="hand2", repeatdelay=500, repeatinterval=100, command=tombol.tambah.bilah_nilai_hijau)
tombol_tambah_nilai_skala_biru = tkinter.Button(jendela, text="+", foreground="#000000", cursor="hand2", repeatdelay=500, repeatinterval=100, command=tombol.tambah.bilah_nilai_biru)
label_merah_sama_dengan = tkinter.Label(jendela, text="=")
label_hijau_sama_dengan = tkinter.Label(jendela, text="=")
label_biru_sama_dengan = tkinter.Label(jendela, text="=")
label_nilai_desimal = tkinter.Label(jendela, text="Nilai Desimal", foreground="#000000", background="#dddddd")
nilai_merah = tkinter.Entry(jendela, width=12, foreground="#000000", background = "#fafafa", highlightbackground = "#aaaaaa", highlightcolor = "#000000", highlightthickness = 1)
nilai_hijau = tkinter.Entry(jendela, width=12, foreground="#000000", background = "#fafafa", highlightbackground = "#aaaaaa", highlightcolor = "#000000", highlightthickness = 1)
nilai_biru = tkinter.Entry(jendela, width=12, foreground="#000000", background = "#fafafa", highlightbackground = "#aaaaaa", highlightcolor = "#000000", highlightthickness = 1)
nilai_merah.insert(index = 0, string = "0")
nilai_hijau.insert(index = 0, string = "0")
nilai_biru.insert(index = 0, string = "0")
nilai_merah.bind("<Return>", func=tombol.enter.input_bilangan_desimal)
nilai_hijau.bind("<Return>", func=tombol.enter.input_bilangan_desimal)
nilai_biru.bind("<Return>", func=tombol.enter.input_bilangan_desimal)
label_nilai_hex = tkinter.Label(jendela, text="Nilai HEX", foreground="#000000", background="#dddddd")
input_kode_warna_hex = tkinter.Entry(jendela, foreground = "#000000", background = "#fafafa", highlightbackground = "#aaaaaa", highlightcolor = "#000000", highlightthickness = 1, justify = "center", width = 10)
input_kode_warna_hex.insert(index = 0, string = "#000000")
input_kode_warna_hex.bind("<Return>", func = tombol.enter.input_bilangan_hex)
tombol_salin_kode_warna_hex = tkinter.Button(jendela, text = "Salin", foreground="#000000", cursor="hand2", command=tombol.salin_teks.kode_warna_hex)
label_tampilan = tkinter.Label(jendela, text = "Tampilan", foreground = "#000000", background = "#dddddd")
tampilan = tkinter.Canvas(jendela, background = "#000000", width = 50, height = 70)

label_rgb.grid(column=0, row=0)
label_merah.grid(column=0, row=1, sticky="NSEW")
label_hijau.grid(column=0, row=2, sticky="NSEW")
label_biru.grid(column=0, row=3, sticky="NSEW")
label_bilah.grid(column=1, row=0, columnspan=3, sticky="EW")
tombol_kurangi_bilah_nilai_merah.grid(column=1, row=1)
tombol_kurangi_bilah_nilai_hijau.grid(column=1, row=2)
tombol_kurangi_bilah_nilai_biru.grid(column=1, row=3)
bilah_merah.grid(column=2, row=1)
bilah_hijau.grid(column=2, row=2)
bilah_biru.grid(column=2, row=3)
tombol_tambah_nilai_skala_merah.grid(column=3, row=1)
tombol_tambah_nilai_skala_hijau.grid(column=3, row=2)
tombol_tambah_nilai_skala_biru.grid(column=3, row=3)
label_merah_sama_dengan.grid(column=4, row=1)
label_hijau_sama_dengan.grid(column=4, row=2)
label_biru_sama_dengan.grid(column=4, row=3)
label_nilai_desimal.grid(column=5, row=0)
nilai_merah.grid(column=5, row=1, sticky = "NS")
nilai_hijau.grid(column=5, row=2, sticky = "NS")
nilai_biru.grid(column=5, row=3, sticky = "NS")
label_nilai_hex.grid(column=6, row=0, columnspan = 2)
input_kode_warna_hex.grid(column=6, row=1, rowspan=3, sticky = "NS")
tombol_salin_kode_warna_hex.grid(column=7, row=1, rowspan=3, sticky="NS")
label_tampilan.grid(column = 8, row = 0)
tampilan.grid(column = 8, row = 1, rowspan = 3, sticky = "NS")

jendela.mainloop()