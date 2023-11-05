import tkinter, tkinter.filedialog, os
from tkinter import messagebox

JENDELA = tkinter.Tk()
"Jendela Utama"
JENDELA.title("Manager File txt")
#JENDELA.geometry("430x110+600+50")
JENDELA.configure(background="#dddddd")

def baca_file():
    "Membaca file sumber"
    with open(direktori_yang_dibuka, "r") as file:
        DATA_DIMUAT = [dns.strip() for dns in file]
        return DATA_DIMUAT
def hapus_data_file(*data_yang_akan_dihapus : str):
    indeks = -1
    tipe_list = []
    for bagian_data in data_yang_akan_dihapus:
        indeks += 1
        if bagian_data in baca_file():
            data_saat_ini = baca_file()
            data_saat_ini.remove(bagian_data)
            with open(direktori_yang_dibuka, "w") as file:
                for item in data_saat_ini:
                    file.write(str(item) + "\n")
            if tipe_list == []:
                tipe_list = list([data_yang_akan_dihapus[indeks]])
            elif tipe_list != []:
                tipe_list += list([data_yang_akan_dihapus[indeks]])
    if len(tipe_list) == 1:
        return tipe_list[0]
    elif len(tipe_list) > 1:
        return " dan ".join(tipe_list)
def muat_daftar_data():
    "Memuat atau memperbarui data dalam listbox"
    DAFTAR_DATA.configure(cursor = "hand2", state = "normal")
    DAFTAR_DATA.delete(first = 0, last = tkinter.END)
    for bagian_daftar_data in baca_file():
        DAFTAR_DATA.insert(tkinter.END, bagian_daftar_data)
    DAFTAR_DATA.select_clear(0, tkinter.END)
    #BILAH_GESER_HORIZONTAL.focus_set()

def tombol_menu_file_baru():
    DIREKTORI_YANG_DIPILIH = tkinter.filedialog.askdirectory()
    if DIREKTORI_YANG_DIPILIH:
        def aktifkan_jendela_utama():
            "Mengaktifkan jendela utama sekaligus menutup jendela tambahan"
            JENDELA_TAMBAHAN.destroy()
            JENDELA.attributes("-disabled", False)
            JENDELA.tkraise()
        def buka_file_yang_baru_dibuat():
            aktifkan_jendela_utama()
            MENU_FILE.entryconfigure(index = 2, state = "normal")
            MENU_FILE.entryconfigure(index = 3, state = "normal")
            INPUT_DATA["state"] = "normal"
            LOKASI_FILE["text"] = direktori_yang_dibuka
            INPUT_DATA.focus_force()
            muat_daftar_data()
            aktifkan_tombol_menu_opsi()
        def buat_file():
            global direktori_yang_dibuka
            if INPUT_NAMA_FILE.get() == "" or INPUT_NAMA_FILE.get() == None:
                messagebox.showwarning("Input Tidak Valid", "Input Kosong!")
                JENDELA_TAMBAHAN.tkraise(JENDELA)
            elif "|" in INPUT_NAMA_FILE.get() or "<" in INPUT_NAMA_FILE.get() or ">" in INPUT_NAMA_FILE.get() or '"' in INPUT_NAMA_FILE.get() or "?" in INPUT_NAMA_FILE.get() or "*" in INPUT_NAMA_FILE.get() or ":" in INPUT_NAMA_FILE.get() or "/" in INPUT_NAMA_FILE.get() or "\\" in INPUT_NAMA_FILE.get():
                messagebox.showerror("Nama File Tidak Valid", 'Karakter nama file tidak boleh \\ / : * ? " < > |')
                JENDELA_TAMBAHAN.tkraise(JENDELA)
            elif INPUT_NAMA_FILE.get()[-4:].lower() == ".txt":
                with open(f"{DIREKTORI_YANG_DIPILIH}/{INPUT_NAMA_FILE.get()}", mode = "w") as file_baru:
                    file_baru.write("")
                KONFIRMASI_BUKA_FILE_BARU = messagebox.askyesno(title = "File Dibuat", message = f"File {INPUT_NAMA_FILE.get()} dibuat!\n\nBuka file yang baru dibuat?")
                if KONFIRMASI_BUKA_FILE_BARU:
                    direktori_yang_dibuka = f"{DIREKTORI_YANG_DIPILIH}/{INPUT_NAMA_FILE.get()}"
                    if direktori_yang_dibuka:
                        buka_file_yang_baru_dibuat()
                else:
                    aktifkan_jendela_utama()
            else:
                with open(f"{DIREKTORI_YANG_DIPILIH}/{INPUT_NAMA_FILE.get()}.txt", mode = "w") as file_baru:
                    file_baru.write("")
                KONFIRMASI_BUKA_FILE_BARU = messagebox.askyesno(title = "File Dibuat", message = f"File {INPUT_NAMA_FILE.get()}.txt dibuat!\n\nBuka file yang baru dibuat?")
                if KONFIRMASI_BUKA_FILE_BARU:
                    direktori_yang_dibuka = f"{DIREKTORI_YANG_DIPILIH}/{INPUT_NAMA_FILE.get()}.txt"
                    if direktori_yang_dibuka:
                        buka_file_yang_baru_dibuat()
                else:
                    aktifkan_jendela_utama()

        JENDELA_TAMBAHAN = tkinter.Toplevel(JENDELA)
        JENDELA.attributes("-disabled", True)
        JENDELA_TAMBAHAN.title("File Baru")
        JENDELA_TAMBAHAN.protocol("WM_DELETE_WINDOW", aktifkan_jendela_utama)

        LABEL_NAMA_FILE = tkinter.Label(JENDELA_TAMBAHAN, text = "Nama File", foreground = "#000000")
        TITIK_DUA_NAMA_FILE = tkinter.Label(JENDELA_TAMBAHAN, text = ":", foreground = "#000000")
        INPUT_NAMA_FILE = tkinter.Entry(JENDELA_TAMBAHAN, foreground = "#000000")
        TOMBOL_BUAT = tkinter.Button(JENDELA_TAMBAHAN, text = "Buat", foreground = "#000000", cursor = "hand2", command = buat_file)

        LABEL_NAMA_FILE.grid(column = 0, row = 0)
        TITIK_DUA_NAMA_FILE.grid(column = 1, row = 0)
        INPUT_NAMA_FILE.grid(column = 2, row = 0)
        TOMBOL_BUAT.grid(column = 3, row = 0)
def tombol_menu_file_buka():
    global direktori_yang_dibuka
    direktori_yang_dibuka = tkinter.filedialog.askopenfilename(defaultextension = ".txt", filetypes = [("Dokumen Teks", "*.txt")])
    if direktori_yang_dibuka:
        MENU_FILE.entryconfigure(index = 2, state = "normal")
        MENU_FILE.entryconfigure(index = 3, state = "normal")
        INPUT_DATA["state"] = "normal"
        LOKASI_FILE["text"] = direktori_yang_dibuka
        muat_daftar_data()
        aktifkan_tombol_menu_opsi()
def tombol_menu_file_hapus():
    KONFIRMASI = messagebox.askyesno(title = "Hapus File", message = f"Apakah anda ingin menghapus file ini di lokasi {direktori_yang_dibuka}?")
    if KONFIRMASI:
        if os.path.exists(path = direktori_yang_dibuka):
            os.remove(path = direktori_yang_dibuka)
            messagebox.showinfo(title = "File di Hapus", message = f"File di lokasi {direktori_yang_dibuka} dihapus!")
            tombol_menu_file_tutup()
        else:
            messagebox.showerror(title = "File Tidak Ditemukan", message = f"File di lokasi {direktori_yang_dibuka} tidak ditemukan!")
def tombol_menu_file_tutup():
    MENU_FILE.entryconfigure(index = 2, state = "disabled")
    MENU_FILE.entryconfigure(index = 3, state = "disabled")
    INPUT_DATA.delete(0, tkinter.END)
    INPUT_DATA.configure(state = "disabled")
    LOKASI_FILE.configure(text = "Tidak Dipilih")
    nonaktifkan_tombol_menu_opsi()
    DAFTAR_DATA.delete(first = 0, last = tkinter.END)
    DAFTAR_DATA.configure(cursor = "arrow", state = "disabled")
def tombol_menu_opsi_cari():
    "Mencari data dari file sumber"
    if INPUT_DATA.get() == "" or INPUT_DATA.get() == None:
        KOTAK_OUTPUT.configure(text = "Input Data Kosong!")
    elif INPUT_DATA.get() in baca_file():
        indeks = -1
        for data in baca_file():
            indeks += 1
            if INPUT_DATA.get() == data:
                KOTAK_OUTPUT.configure(text=INPUT_DATA.get() + " ditemukan!")
                DAFTAR_DATA.select_clear(first = 0, last = tkinter.END)
                DAFTAR_DATA.select_set(indeks)
                DAFTAR_DATA.see(indeks)
    else:
        KOTAK_OUTPUT.configure(text=INPUT_DATA.get() + " tidak ditemukan!")
def tombol_menu_opsi_urutkan_data_dari_yang_terkecil():
    KONFIRMASI = messagebox.askyesno("Konfirmasi Untuk Urutkan Data", "Apakah anda yakin untuk mengurutkan data dari yang terkecil?")
    if KONFIRMASI:
        DATA = baca_file()
        DATA.sort()
        with open(direktori_yang_dibuka, "w") as data_diurutkan:
            for data_satuan in DATA:
                data_diurutkan.write(data_satuan + "\n")
        KOTAK_OUTPUT.configure(text = "Data telah diurutkan dari yang terkecil")
        muat_daftar_data()
def tombol_menu_opsi_urutkan_data_dari_yang_terbesar():
    KONFIRMASI = messagebox.askyesno("Konfirmasi Untuk Urutkan Data", "Apakah anda yakin untuk mengurutkan data dari yang terbesar?")
    if KONFIRMASI:
        DATA = baca_file()
        DATA.sort(reverse = True)
        with open(direktori_yang_dibuka, "w") as data_diurutkan:
            for data_satuan in DATA:
                data_diurutkan.write(data_satuan + "\n")
        KOTAK_OUTPUT.configure(text = "Data telah diurutkan dari yang terbesar")
        muat_daftar_data()
def tombol_menu_opsi_tambah():
    "Menambahkan data ke file sumber"
    if INPUT_DATA.get() in baca_file():
        KOTAK_OUTPUT.configure(text = "Telah ada " + INPUT_DATA.get())
    elif INPUT_DATA.get() == "" or INPUT_DATA.get() == None:
        KOTAK_OUTPUT.configure(text = "Input Data Kosong!")
    else:
        with open(direktori_yang_dibuka, "a") as file:
            file.write(INPUT_DATA.get() + "\n")
        KOTAK_OUTPUT.configure(text = INPUT_DATA.get() + " ditambahkan!")
        muat_daftar_data()
def tombol_menu_opsi_hapus():
    "Menghapus data dari file sumber"
    if INPUT_DATA.get() == "" and not DAFTAR_DATA.curselection():
        KOTAK_OUTPUT.configure(text="Input data kosong!")
    elif DAFTAR_DATA.curselection() and INPUT_DATA.get() in baca_file():
        daftar_data_yang_dipilih = DAFTAR_DATA.get(int(DAFTAR_DATA.curselection()[0]))
        KONFIRMASI = messagebox.askyesno(title = "Konfirmasi Hapus", message = f"Apakah anda ingin menghapus {INPUT_DATA.get()} dan {DAFTAR_DATA.get(int(DAFTAR_DATA.curselection()[0]))}?")
        if KONFIRMASI:
            KOTAK_OUTPUT.configure(text = f"{hapus_data_file(INPUT_DATA.get(), DAFTAR_DATA.get(int(DAFTAR_DATA.curselection()[0])))} dihapus!")
            muat_daftar_data()
    elif INPUT_DATA.get() in baca_file():
        KONFIRMASI = messagebox.askyesno(title = "Konfirmasi Hapus", message = f"Apakah anda ingin menghapus {INPUT_DATA.get()}?")
        if KONFIRMASI:
            KOTAK_OUTPUT.configure(text = f"{hapus_data_file(INPUT_DATA.get())} dihapus!")
            muat_daftar_data()
    elif DAFTAR_DATA.curselection():
        daftar_data_yang_dipilih = DAFTAR_DATA.get(int(DAFTAR_DATA.curselection()[0]))
        KONFIRMASI = messagebox.askyesno(title = "Konfirmasi Hapus", message = f"Apakah anda ingin menghapus {DAFTAR_DATA.get(int(DAFTAR_DATA.curselection()[0]))}?")
        if KONFIRMASI:
            KOTAK_OUTPUT.configure(text = f"{hapus_data_file(daftar_data_yang_dipilih)} dihapus!")
            muat_daftar_data()
    else:
        KOTAK_OUTPUT.configure(text = INPUT_DATA.get() + " tidak ditemukan!")
def tombol_menu_opsi_hapus_semua_data():
    "Menghapus seluruh data dalam daftar data"
    konfirmasi = messagebox.askyesno(title = "Hapus Semua Data", message = "Apakah anda yakin untuk menghapus seluruh isi data?")
    if konfirmasi:
        with open(file = direktori_yang_dibuka, mode = "w") as data_kosong:
            data_kosong.write("")
        KOTAK_OUTPUT.configure(text = "Seluruh isi dalam daftar data dihapus!")
        muat_daftar_data()
def tombol_menu_opsi_salin():
    "Menyalin daftar data yang dipilih ke clipboard"
    if DAFTAR_DATA.curselection():
        JENDELA.clipboard_clear()
        JENDELA.clipboard_append(string = DAFTAR_DATA.get(int(DAFTAR_DATA.curselection()[0])))
        KOTAK_OUTPUT["text"] = f"{DAFTAR_DATA.get(int(DAFTAR_DATA.curselection()[0]))} disalin!"
def aktifkan_tombol_menu_opsi():
    MENU_DASAR.entryconfigure("Opsi", state = "normal")
    MENU_OPSI.entryconfigure(0, state = "normal")
    MENU_OPSI.entryconfigure(1, state = "normal")
    MENU_OPSI.entryconfigure(2, state = "normal")
    MENU_OPSI.entryconfigure(3, state = "normal")
    MENU_OPSI.entryconfigure(4, state = "normal")
    MENU_OPSI.entryconfigure(5, state = "normal")
    MENU_OPSI.entryconfigure(6, state = "normal")
def nonaktifkan_tombol_menu_opsi():
    MENU_DASAR.entryconfigure("Opsi", state = "disabled")
    MENU_OPSI.entryconfigure(0, state = "disabled")
    MENU_OPSI.entryconfigure(1, state = "disabled")
    MENU_OPSI.entryconfigure(2, state = "disabled")
    MENU_OPSI.entryconfigure(3, state = "disabled")
    MENU_OPSI.entryconfigure(4, state = "disabled")
    MENU_OPSI.entryconfigure(5, state = "disabled")
    MENU_OPSI.entryconfigure(6, state = "disabled")
def tombol_menu_reset():
    "Mereset input data, label output, dan daftar data yang sedang dipilih"
    INPUT_DATA.delete(first=0, last=tkinter.END)
    KOTAK_OUTPUT.configure(text="")
    DAFTAR_DATA.select_clear(0, tkinter.END)
def tombol_menu_bantuan_petunjuk():
    messagebox.showinfo(title = "Petunjuk", message = "Memanajemen data untuk disimpan dan dikelola dalam format .txt\n\nOpsi\nCari : Mencari data yang ada dalam daftar data\nTambah : Menambahkan data dari input ke daftar data\nHapus : Menghapus daftar data\nHapus Semua Data : Menghapus seluruh daftar data menjadi kosong\nSalin : Menyalin daftar data yang dipilih ke clipboard\n\nReset : Mereset tampilan input data, output, dan daftar data yang dipilih\n\n*Segala perubahan yang dilakukan oleh pengguna akan langsung disimpan")
def tombol_menu_bantuan_informasi_pengembang():
    messagebox.showinfo(title = "Informasi Pengembang", message = "Dikembangkan oleh M Rifky Darmawan dengan Python\n\nDibuat : 8 Agustus 2023\nDiperbarui : 5 November 2023\n\nGitHub : rifkydarmawan62")

variabel_daftar_data = tkinter.StringVar(JENDELA)

MENU_DASAR = tkinter.Menu(JENDELA, cursor = "hand2")
MENU_FILE = tkinter.Menu(MENU_DASAR, tearoff = 0)
MENU_OPSI = tkinter.Menu(MENU_DASAR, tearoff = 0)
MENU_BANTUAN = tkinter.Menu(MENU_DASAR, tearoff = 0)
MENU_DASAR.add_cascade(label = "File", menu = MENU_FILE)
MENU_DASAR.add_cascade(label = "Opsi", menu = MENU_OPSI, state = "disabled")
MENU_DASAR.add_command(label = "Reset", command = tombol_menu_reset)
MENU_DASAR.add_cascade(label = "Bantuan", menu = MENU_BANTUAN)
MENU_FILE.add_command(label = "File Baru", command = tombol_menu_file_baru)
MENU_FILE.add_command(label = "Buka File", command = tombol_menu_file_buka)
MENU_FILE.add_command(label = "Hapus File", command = tombol_menu_file_hapus, state = "disabled")
MENU_FILE.add_command(label = "Tutup File", command = tombol_menu_file_tutup, state = "disabled")
MENU_OPSI.add_command(label = "Cari", command = tombol_menu_opsi_cari, state = "disabled")
MENU_OPSI.add_command(label = "Urutkan Data dari yang Terkecil", command = tombol_menu_opsi_urutkan_data_dari_yang_terkecil, state = "disabled")
MENU_OPSI.add_command(label = "Urutkan Data dari yang Terbesar", command = tombol_menu_opsi_urutkan_data_dari_yang_terbesar, state = "disabled")
MENU_OPSI.add_command(label = "Tambah", command = tombol_menu_opsi_tambah, state = "disabled")
MENU_OPSI.add_command(label = "Hapus", command = tombol_menu_opsi_hapus, state = "disabled")
MENU_OPSI.add_command(label = "Hapus Semua Data", command = tombol_menu_opsi_hapus_semua_data, state = "disabled")
MENU_OPSI.add_command(label = "Salin", command = tombol_menu_opsi_salin, state = "disabled")
MENU_BANTUAN.add_command(label = "Petunjuk", command = tombol_menu_bantuan_petunjuk)
MENU_BANTUAN.add_command(label = "Info Pengembang", command = tombol_menu_bantuan_informasi_pengembang)
JENDELA.configure(menu = MENU_DASAR)

LABEL_INPUT_DATA = tkinter.Label(JENDELA, text = "Input", foreground="#000000", background="#dddddd")
LABEL_LOKASI_FILE = tkinter.Label(JENDELA, text = "Lokasi File", foreground = "#000000", background = "#dddddd")
LABEL_OUTPUT = tkinter.Label(JENDELA, text = "Output", foreground = "#000000", background = "#dddddd")
TITIK_DUA_INPUT_DATA = tkinter.Label(JENDELA, text = ":", foreground = "#000000", background = "#dddddd")
TITIK_DUA_LOKASI_FILE = tkinter.Label(JENDELA, text = ":", foreground = "#000000", background = "#dddddd")
TITIK_DUA_OUTPUT = tkinter.Label(JENDELA, text = ":", foreground = "#000000", background = "#dddddd")
INPUT_DATA = tkinter.Entry(JENDELA, foreground = "#000000", state = "disabled", width = 100)
LOKASI_FILE = tkinter.Label(JENDELA, text = "Tidak Dipilih", foreground = "#000000", background = "#dddddd", width = 100)
KOTAK_OUTPUT = tkinter.Label(JENDELA, text="", foreground="#000000", background="#dddddd", width = 100)
LABEL_DAFTAR_DATA = tkinter.Label(JENDELA, text = "Daftar Data", foreground = "#000000", background = "#dddddd")
DAFTAR_DATA = tkinter.Listbox(JENDELA, activestyle = "dotbox", listvariable = variabel_daftar_data, height = 20, selectmode = "SINGLE", state = "disabled")
BILAH_GESER_HORIZONTAL = tkinter.Scrollbar(JENDELA, orient = "horizontal", command = DAFTAR_DATA.xview)
BILAH_GESER_VERTIKAL = tkinter.Scrollbar(JENDELA, orient = "vertical", command = DAFTAR_DATA.yview)

DAFTAR_DATA.configure(xscrollcommand = BILAH_GESER_HORIZONTAL.set, yscrollcommand = BILAH_GESER_VERTIKAL.set)
#daftar_data.bind("<<ListboxSelect>>")

LABEL_INPUT_DATA.grid(column=0, row=0, sticky="ew")
LABEL_LOKASI_FILE.grid(column = 0, row = 1)
LABEL_OUTPUT.grid(column=0, row = 2, sticky="ew")
TITIK_DUA_INPUT_DATA.grid(column = 1, row = 0)
TITIK_DUA_LOKASI_FILE.grid(column = 1, row = 1)
TITIK_DUA_OUTPUT.grid(column = 1, row = 2)
INPUT_DATA.grid(column= 2, row=0, sticky="ew")
LOKASI_FILE.grid(column = 2, row = 1, sticky = "ew")
KOTAK_OUTPUT.grid(column= 2, row = 2, sticky="ew")
LABEL_DAFTAR_DATA.grid(column = 0, row = 3, columnspan = 3, sticky = "ew")
DAFTAR_DATA.grid(column = 0, row = 4, columnspan = 3, sticky = "nsew")
BILAH_GESER_HORIZONTAL.grid(column = 0, row = 5, columnspan = 3, sticky = "ew")
BILAH_GESER_VERTIKAL.grid(column = 3, row = 4, sticky = "ns")

JENDELA.mainloop()
