import tkinter
from tkinter import messagebox

JENDELA = tkinter.Tk()
"Jendela utama untuk UI konversi warna"
JENDELA.title("Konversi Warna")
JENDELA.configure(background="#dddddd")

def bilangan_desimal_merah() -> int:
    "Bilangan desimal dari bilah merah"
    return int(BILAH_WARNA_MERAH.get())
def bilangan_desimal_hijau() -> int:
    "Bilangan desimal dari bilah hijau"
    return int(BILAH_WARNA_HIJAU.get())
def bilangan_desimal_biru() -> int:
    "Bilangan desimal dari bilah biru"
    return int(BILAH_WARNA_BIRU.get())

def periksa_bilangan_heksadesimal_warna(__bilangan_heksadesimal_warna : str) -> str:
    "Menambahkan digit \"0\" di depan bilangan heksadesimal jika jumlah digit bilangan heksadesimal adalah 1"
    if len(__bilangan_heksadesimal_warna) == 1:
        return "0" + __bilangan_heksadesimal_warna
    else:
        return __bilangan_heksadesimal_warna
def bilangan_heksadesimal_merah() -> str:
    "Bilangan heksadesimal dari bilah merah"
    return periksa_bilangan_heksadesimal_warna(hex(int(BILAH_WARNA_MERAH.get()))[2:].lower())
def bilangan_heksadesimal_hijau() -> str:
    "Bilangan heksadesimal dari bilah hijau"
    return periksa_bilangan_heksadesimal_warna(hex(int(BILAH_WARNA_HIJAU.get()))[2:].lower())
def bilangan_heksadesimal_biru() -> str:
    "Bilangan heksadesimal dari bilah biru"
    return periksa_bilangan_heksadesimal_warna(hex(int(BILAH_WARNA_BIRU.get()))[2:].lower())

def konfigurasi_nilai_desimal_warna():
    "Menkonfigurasi seluruh nilai desimal warna ketika bilah warna merah, hijau, dan biru di geser"
    NILAI_DESIMAL_WARNA_MERAH.delete(first = 0, last = tkinter.END)
    NILAI_DESIMAL_WARNA_HIJAU.delete(first = 0 ,last = tkinter.END)
    NILAI_DESIMAL_WARNA_BIRU.delete(first = 0, last = tkinter.END)
    NILAI_DESIMAL_WARNA_MERAH.insert(index = 0, string = str(BILAH_WARNA_MERAH.get()))
    NILAI_DESIMAL_WARNA_HIJAU.insert(index = 0, string = str(BILAH_WARNA_HIJAU.get()))
    NILAI_DESIMAL_WARNA_BIRU.insert(index = 0, string = str(BILAH_WARNA_BIRU.get()))
def konfigurasi_nilai_heksadesimal_warna():
    "Menkonfigurasi label nilai heksadesimal warna ketika bilah warna merah, hijau, dan biru di geser"
    NILAI_HEKSADESIMAL_SELURUH_WARNA.delete(first = 0, last = tkinter.END)
    NILAI_HEKSADESIMAL_SELURUH_WARNA.insert(index = 0, string = f"#{bilangan_heksadesimal_merah()}{bilangan_heksadesimal_hijau()}{bilangan_heksadesimal_biru()}")
    TAMPILAN.configure(background = f"#{bilangan_heksadesimal_merah()}{bilangan_heksadesimal_hijau()}{bilangan_heksadesimal_biru()}")
def bilah_warna(value):
    "Menkonfigurasi nilai desimal warna merah, hijau, dan biru; dan nilai heksadesimal seluruh warna ketika bilah warna merah, hijau, dan biru digeser"
    konfigurasi_nilai_desimal_warna()
    konfigurasi_nilai_heksadesimal_warna()

def tombol_menu_pengembang():
    messagebox.showinfo(title = "Informasi Pengembang", message = "Dikembangkan oleh M Rifky Darmawan dengan Python\n\nTanggal dibuat : 4 Agustus 2023\nTanggal diperbarui : 5 November 2023\n\nGitHub : rifkydarmawan62")
def tombol_kurangi_bilah_warna_merah():
    "Mengurangi nilai bilah warna merah"
    BILAH_WARNA_MERAH.set(BILAH_WARNA_MERAH.get() - 1)
def tombol_kurangi_bilah_warna_hijau():
    "Mengurangi nilai bilah warna hijau"
    BILAH_WARNA_HIJAU.set(BILAH_WARNA_HIJAU.get() - 1)
def tombol_kurangi_bilah_warna_biru():
    "Mengurangi nilai bilah warna biru"
    BILAH_WARNA_BIRU.set(BILAH_WARNA_BIRU.get() - 1)
def tombol_tambah_bilah_warna_merah():
    "Menambahkan nilai bilah warna merah"
    BILAH_WARNA_MERAH.set(BILAH_WARNA_MERAH.get() + 1)
def tombol_tambah_bilah_warna_hijau():
    "Menambahkan nilai bilah warna hijau"
    BILAH_WARNA_HIJAU.set(BILAH_WARNA_HIJAU.get() + 1)
def tombol_tambah_bilah_warna_biru():
    "Menambahkan nilai bilah warna biru"
    BILAH_WARNA_BIRU.set(BILAH_WARNA_BIRU.get() + 1)
def tombol_salin_kode_warna_heksadesimal():
    "Menyalin teks kode warna heksadesimal ke clipboard"
    JENDELA.clipboard_append(string = f"#{bilangan_heksadesimal_merah()}{bilangan_heksadesimal_hijau()}{bilangan_heksadesimal_biru()}")

def tombol_enter_keyboard_input_bilangan_desimal_warna(event):
    "Menkonfigurasi bilah warna merah, hijau, dan biru jika nilai desimal valid ketika tombol enter keyboard ditekan"
    if NILAI_DESIMAL_WARNA_MERAH.get().isdigit() and NILAI_DESIMAL_WARNA_HIJAU.get().isdigit() and NILAI_DESIMAL_WARNA_BIRU.get().isdigit():
        BILAH_WARNA_MERAH.set(NILAI_DESIMAL_WARNA_MERAH.get())
        BILAH_WARNA_HIJAU.set(NILAI_DESIMAL_WARNA_HIJAU.get())
        BILAH_WARNA_BIRU.set(NILAI_DESIMAL_WARNA_BIRU.get())
def tombol_enter_keyboard_input_bilangan_heksadesimal_warna(event):
    "Menkonfigurasi bilah warna merah, hijau, dan biru jika nilai heksadesimal valid ketika tombol enter ditekan"
    bilangan_heksadesimal_warna = NILAI_HEKSADESIMAL_SELURUH_WARNA.get()
    if bilangan_heksadesimal_warna[0] == "#":
        bilangan_heksadesimal_warna = bilangan_heksadesimal_warna.replace("#", "")
    if len(bilangan_heksadesimal_warna) == 6 and bilangan_heksadesimal_warna[0] != "#":
        BILAH_WARNA_MERAH.set(int(bilangan_heksadesimal_warna[0:2], base = 16))
        BILAH_WARNA_HIJAU.set(int(bilangan_heksadesimal_warna[2:4], base = 16))
        BILAH_WARNA_BIRU.set(int(bilangan_heksadesimal_warna[4:6], base = 16))

MENU_DASAR = tkinter.Menu(JENDELA, cursor = "hand2")
"UI menu utama"
MENU_DASAR.add_command(label = "Info Pengembang", command = tombol_menu_pengembang)
JENDELA.configure(menu = MENU_DASAR)

LABEL_RGB = tkinter.Label(JENDELA, text="R/G/B", foreground="#000000", background="#dddddd")
"UI label \"R/G/B\""
LABEL_MERAH = tkinter.Label(JENDELA, text="R :", foreground="#000000", background="#ff0000")
"UI label \"R :\""
LABEL_HIJAU = tkinter.Label(JENDELA, text="G :", foreground="#000000", background="#00ff00")
"UI label \"G :\""
LABEL_BIRU = tkinter.Label(JENDELA, text="B :", foreground="#000000", background="#0000ff")
"UI label \"B :\""
LABEL_BILAH = tkinter.Label(JENDELA, text="Bilah", foreground="#000000", background="#dddddd")
"UI label \"Bilah\""
TOMBOL_KURANGI_NILAI_WARNA_MERAH = tkinter.Button(JENDELA, text="-", foreground="#000000", cursor="hand2", repeatdelay=500, repeatinterval=100, command = tombol_kurangi_bilah_warna_merah)
"Tombol untuk mengurangi bilah dan nilai warna merah"
TOMBOL_KURANGI_NILAI_WARNA_HIJAU = tkinter.Button(JENDELA, text="-", foreground="#000000", cursor="hand2", repeatdelay=500, repeatinterval=100, command = tombol_kurangi_bilah_warna_hijau)
"Tombol untuk mengurangi bilah dan nilai warna hijau"
TOMBOL_KURANGI_NILAI_WARNA_BIRU = tkinter.Button(JENDELA, text="-", foreground="#000000", cursor="hand2", repeatdelay=500, repeatinterval=100, command = tombol_kurangi_bilah_warna_biru)
"Tombol untuk mengurangi bilah dan nilai warna biru"
BILAH_WARNA_MERAH = tkinter.Scale(JENDELA, from_=0, to=255, orient="horizontal", showvalue=False, cursor="hand2", command = bilah_warna, length=300)
"Bilah untuk warna merah yang dapat digeser secara horizontal"
BILAH_WARNA_HIJAU = tkinter.Scale(JENDELA, from_=0, to=255, orient="horizontal", showvalue=False, cursor="hand2", command = bilah_warna, length=300)
"Bilah untuk warna hijau yang dapat digeser secara horizontal"
BILAH_WARNA_BIRU = tkinter.Scale(JENDELA, from_=0, to=255, orient="horizontal", showvalue=False, cursor="hand2", command = bilah_warna, length=300)
"Bilah untuk warna biru yang dapat digeser secara horizontal"
TOMBOL_TAMBAH_NILAI_WARNA_MERAH = tkinter.Button(JENDELA, text="+", foreground="#000000", cursor="hand2", repeatdelay=500, repeatinterval=100, command = tombol_tambah_bilah_warna_merah)
"UI tombol untuk menambahkan bilah dan nilai warna merah"
TOMBOL_TAMBAH_NILAI_WARNA_HIJAU = tkinter.Button(JENDELA, text="+", foreground="#000000", cursor="hand2", repeatdelay=500, repeatinterval=100, command = tombol_tambah_bilah_warna_hijau)
"UI tombol untuk menambahkan bilah dan nilai warna hijau"
TOMBOL_TAMBAH_NILAI_WARNA_BIRU = tkinter.Button(JENDELA, text="+", foreground="#000000", cursor="hand2", repeatdelay=500, repeatinterval=100, command = tombol_tambah_bilah_warna_biru)
"UI tombol untuk menambahkan bilah dan nilai warna biru"
LABEL_MERAH_SAMA_DENGAN = tkinter.Label(JENDELA, text="=")
"UI label \"=\""
LABEL_HIJAU_SAMA_DENGAN = tkinter.Label(JENDELA, text="=")
"UI label \"=\""
LABEL_BIRU_SAMA_DENGAN = tkinter.Label(JENDELA, text="=")
"UI label \"=\""
LABEL_NILAI_DESIMAL = tkinter.Label(JENDELA, text="Nilai Desimal", foreground="#000000", background="#dddddd")
"UI label \"Nilai Desimal\""
NILAI_DESIMAL_WARNA_MERAH = tkinter.Entry(JENDELA, width=12, foreground="#000000", background = "#fafafa", highlightbackground = "#aaaaaa", highlightcolor = "#000000", highlightthickness = 1)
"UI input nilai desimal untuk warna merah"
NILAI_DESIMAL_WARNA_HIJAU = tkinter.Entry(JENDELA, width=12, foreground="#000000", background = "#fafafa", highlightbackground = "#aaaaaa", highlightcolor = "#000000", highlightthickness = 1)
"UI input nilai desimal untuk warna hijau"
NILAI_DESIMAL_WARNA_BIRU = tkinter.Entry(JENDELA, width=12, foreground="#000000", background = "#fafafa", highlightbackground = "#aaaaaa", highlightcolor = "#000000", highlightthickness = 1)
"UI input nilai desimal untuk warna biru"
NILAI_DESIMAL_WARNA_MERAH.insert(index = 0, string = "0")
NILAI_DESIMAL_WARNA_HIJAU.insert(index = 0, string = "0")
NILAI_DESIMAL_WARNA_BIRU.insert(index = 0, string = "0")
NILAI_DESIMAL_WARNA_MERAH.bind("<Return>", func = tombol_enter_keyboard_input_bilangan_desimal_warna)
NILAI_DESIMAL_WARNA_HIJAU.bind("<Return>", func = tombol_enter_keyboard_input_bilangan_desimal_warna)
NILAI_DESIMAL_WARNA_BIRU.bind("<Return>", func = tombol_enter_keyboard_input_bilangan_desimal_warna)
LABEL_NILAI_HEX = tkinter.Label(JENDELA, text="Nilai HEX", foreground="#000000", background="#dddddd")
"UI label \"Nilai HEX\""
NILAI_HEKSADESIMAL_SELURUH_WARNA = tkinter.Entry(JENDELA, foreground = "#000000", background = "#fafafa", highlightbackground = "#aaaaaa", highlightcolor = "#000000", highlightthickness = 1, justify = "center", width = 10)
"UI input nilai heksadesimal untuk seluruh warna"
NILAI_HEKSADESIMAL_SELURUH_WARNA.insert(index = 0, string = "#000000")
NILAI_HEKSADESIMAL_SELURUH_WARNA.bind("<Return>", func = tombol_enter_keyboard_input_bilangan_heksadesimal_warna)
TOMBOL_SALIN = tkinter.Button(JENDELA, text = "Salin", foreground="#000000", cursor="hand2", command = tombol_salin_kode_warna_heksadesimal)
"UI tombol untuk menyalin teks kode warna heksadesimal ke clipboard"
LABEL_TAMPILAN = tkinter.Label(JENDELA, text = "Tampilan", foreground = "#000000", background = "#dddddd")
"UI label \"Tampilan\""
TAMPILAN = tkinter.Canvas(JENDELA, background = "#000000", width = 50, height = 70)
"UI tampilan warna"

LABEL_RGB.grid(column=0, row=0)
LABEL_MERAH.grid(column=0, row=1, sticky="NSEW")
LABEL_HIJAU.grid(column=0, row=2, sticky="NSEW")
LABEL_BIRU.grid(column=0, row=3, sticky="NSEW")
LABEL_BILAH.grid(column=1, row=0, columnspan=3, sticky="EW")
TOMBOL_KURANGI_NILAI_WARNA_MERAH.grid(column=1, row=1)
TOMBOL_KURANGI_NILAI_WARNA_HIJAU.grid(column=1, row=2)
TOMBOL_KURANGI_NILAI_WARNA_BIRU.grid(column=1, row=3)
BILAH_WARNA_MERAH.grid(column=2, row=1)
BILAH_WARNA_HIJAU.grid(column=2, row=2)
BILAH_WARNA_BIRU.grid(column=2, row=3)
TOMBOL_TAMBAH_NILAI_WARNA_MERAH.grid(column=3, row=1)
TOMBOL_TAMBAH_NILAI_WARNA_HIJAU.grid(column=3, row=2)
TOMBOL_TAMBAH_NILAI_WARNA_BIRU.grid(column=3, row=3)
LABEL_MERAH_SAMA_DENGAN.grid(column=4, row=1)
LABEL_HIJAU_SAMA_DENGAN.grid(column=4, row=2)
LABEL_BIRU_SAMA_DENGAN.grid(column=4, row=3)
LABEL_NILAI_DESIMAL.grid(column=5, row=0)
NILAI_DESIMAL_WARNA_MERAH.grid(column=5, row=1, sticky = "NS")
NILAI_DESIMAL_WARNA_HIJAU.grid(column=5, row=2, sticky = "NS")
NILAI_DESIMAL_WARNA_BIRU.grid(column=5, row=3, sticky = "NS")
LABEL_NILAI_HEX.grid(column=6, row=0, columnspan = 2)
NILAI_HEKSADESIMAL_SELURUH_WARNA.grid(column=6, row=1, rowspan=3, sticky = "NS")
TOMBOL_SALIN.grid(column=7, row=1, rowspan=3, sticky="NS")
LABEL_TAMPILAN.grid(column = 8, row = 0)
TAMPILAN.grid(column = 8, row = 1, rowspan = 3, sticky = "NS")

JENDELA.mainloop()
