# wp-directory-buster-poc
Skrip Python otomatisasi dir buster dan dokumentasi celah keamanan web
# Custom WordPress Directory Buster & Vulnerability Research

Skrip otomatisasi pengintaian direktori web berbasis Python yang dirancang untuk memeriksa respon server, menangani standar pengodean (UTF-8), dan melacak perilaku pengalihan HTTP (Status Code `301`/`302`) untuk mengidentifikasi celah keamanan pada sistem web.

##  Fitur Utama
- **Automated Wordlist**: Mengunduh daftar kata sandi dan direktori populer secara otomatis dari repositori open-source tepercaya.
- **Redirection Tracking**: Memeriksa header HTTP `Location` untuk membedakan antara proteksi Firewall global dengan folder tersembunyi yang asli.
- **Log System**: Menyimpan hasil temuan secara otomatis ke dalam file teks dengan dukungan enkripsi UTF-8 untuk mencegah crash pada Windows.

##  Studi Kasus: Penemuan Celah Keamanan (Vulnerability Chaining)
Melalui uji coba simulasi keamanan pada lingkungan web target (`https://target.com`), alat ini berhasil memvalidasi dua celah keamanan sekaligus (Medium Severity):

1. **Username Enumeration via Author Tracking**: Server membocorkan nama pengguna (username) administrator yang valid ketika mendeteksi pencarian parameter `?author=1`.
2. **Missing Rate Limiting (Brute Force Vulnerability)**: Formulir login panel admin (`/wp-login.php`) menerima puluhan percobaan kata sandi salah secara berturut-turut tanpa memicu blokir IP atau tantangan CAPTCHA.

> **Catatan Etika**: Penelitian ini mengikuti panduan *Responsible Disclosure*. Semua nama domain asli, parameter sensitif, dan kredensial telah disamarkan sepenuhnya dalam dokumentasi publik ini.
