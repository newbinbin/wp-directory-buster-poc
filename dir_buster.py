import requests

def scan_direktori_advanced(url):
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url

    print(f"\n[+] Mengunduh wordlist profesional dari internet...")
    try:
        url_wordlist = "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Discovery/Web-Content/common.txt"
        konten = requests.get(url_wordlist).text
        wordlist = konten.splitlines()[:1000]  # Menguji 1000 kata populer
    except Exception:
        print("[❌] Gagal mengambil wordlist online.")
        return

    print(f"[+] Memulai scanning pada: {url}")
    print(f"Menguji {len(wordlist)} direktori. Hasil akan disimpan ke 'hasil_scan.txt'...\n" + "-"*50)

    # Membuka file teks untuk menulis hasil secara bertahap ('a' artinya append/tambah terus)
    with open("hasil_scan.txt", "a", encoding="utf-8") as file_log:
        file_log.write(f"=== Hasil Scan untuk {url} ===\n")
        
        for folder in wordlist:
            if folder.startswith("#") or not folder.strip():
                continue
                
            target_url = f"{url.rstrip('/')}/{folder.strip()}"
            try:
                respon = requests.get(target_url, timeout=2, allow_redirects=False)
                
                if respon.status_code == 200:
                    hasil = f"[🎉 FOUND] Status 200 OK       -> {target_url}"
                    print(hasil)
                    file_log.write(hasil + "\n")
                    
                elif respon.status_code in [301, 302]:
                    # MENGENDUS KE MANA ARAH PENGALIHANNYA
                    # .get('Location') digunakan untuk mengambil URL tujuan dari server
                    tujuan_redirect = respon.headers.get('Location', 'Tidak diketahui')
                    
                    hasil = f"[转向 REDIRECT] Status {respon.status_code} -> {target_url}\n                ↳ Diperintahkan pindah ke: {tujuan_redirect}"
                    print(hasil)
                    file_log.write(hasil + "\n")
                    
            except requests.exceptions.RequestException:
                pass
                
    print("-" * 50 + "\n[+] Pemindaian selesai! Silakan cek file 'hasil_scan.txt' di folder project-mu.")

target = input("Masukkan domain utama target (contoh: google.com): ")
scan_direktori_advanced(target)