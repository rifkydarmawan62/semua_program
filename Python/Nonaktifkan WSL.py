import subprocess
__PERINTAH = "wsl --shutdown"
try:
    print("Menonaktifkan WSL (Windows Subsystem for Linux) ...")
    print(__PERINTAH)
    subprocess.check_call(__PERINTAH)
except FileNotFoundError:
    print("Perintah wsl tidak ditemukan!")
except subprocess.CalledProcessError:
    print("Error saat menjalankan perintah")
    print("WSL gagal dinonaktifkan!")
except KeyboardInterrupt:
    print("Menutup program ...")
    exit(0)
else:
    print("WSL telah dinonaktifkan!")
finally:
    input("Tekan Enter atau Ctrl + C untuk keluar")