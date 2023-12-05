import subprocess
__NAMA_PROSES = "CompatTelRunner"
try:
    __PERINTAH = f"Stop-Process -Name \"{__NAMA_PROSES}\""
    print(f"Menghentikan proses {__NAMA_PROSES}.exe ...")
    print(__PERINTAH)
    subprocess.check_call(["PowerShell", __PERINTAH], shell = True)
except subprocess.CalledProcessError:
    print(f"Proses {__NAMA_PROSES}.exe tidak ditemukan")
except:
    print(f"Proses {__NAMA_PROSES}.exe gagal dihentikan atau tidak ditemukan")
else:
    print(f"Proses {__NAMA_PROSES}.exe berhasil dihentikan")
finally:
    input("Tekan Enter atau Ctrl + C untuk keluar")