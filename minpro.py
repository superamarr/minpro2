from prettytable import PrettyTable

# Database dan list sementara
pengguna = {"admin": "admin123"}
apartemen = [
    {"no": 1, "nama": "Apartemen Grand Kamala Yogyakarta", "harga": 500000, "lantai": [3, 7, 8], "tersedia": True},
    {"no": 2, "nama": "Apartemen Mahakam", "harga": 750000, "lantai": [2, 4, 8], "tersedia": True},
    {"no": 3, "nama": "Apartemen Elit Bontang", "harga": 1000000, "lantai": [5, 9], "tersedia": True},
    {"no": 4, "nama": "Apartemen Mulia", "harga": 600000, "lantai": [9, 10], "tersedia": True},
    {"no": 5, "nama": "Apartemen Borneo", "harga": 800000, "lantai": [1, 2], "tersedia": True},
    {"no": 6, "nama": "Apartemen Surya", "harga": 700000, "lantai": [8, 10, 12], "tersedia": True},
    {"no": 7, "nama": "Apartemen Zamrud", "harga": 900000, "lantai": [1, 2], "tersedia": True},
    {"no": 8, "nama": "Apartemen Nusa Indah", "harga": 650000, "lantai": [8, 11, 14], "tersedia": True},
    {"no": 9, "nama": "Apartemen Samudera", "harga": 950000, "lantai": [4, 7, 10], "tersedia": True},
    {"no": 10, "nama": "Apartemen Pantai", "harga": 850000, "lantai": [15], "tersedia": True}
]

def masuk(): # Fungsi masuk
    nama_pengguna = input("Nama Pengguna: ")
    kata_sandi = input("Kata Sandi: ")
    if nama_pengguna in pengguna and pengguna[nama_pengguna] == kata_sandi: #Memeriksaa nama pengguna dan kata sandi dalam dictionary
        print(f"\nSelamat datang, {'Admin' if nama_pengguna == 'admin' else nama_pengguna}!")
        return nama_pengguna
    else:
        print("Gagal masuk.")
        return None

def daftar(): # Fungsi daftar
    while True:
        nama_pengguna = input("Nama Pengguna Baru: ")
        if nama_pengguna in pengguna:
            print("Nama pengguna sudah digunakan.")
        else:
            pengguna[nama_pengguna] = input("Kata Sandi: ")
            print("Pendaftaran berhasil.")
            break

def tampil_apartemen():
    table = PrettyTable() # Menampilkan Prettytabel
    table.field_names = ["No", "Apartemen", "Harga", "Lantai", "Tersedia"] 
    for apt in apartemen:
        table.add_row([apt["no"], apt["nama"], f"Rp{apt['harga']:,.0f}", ", ".join(map(str, apt["lantai"])), "Ya" if apt["tersedia"] else "Tidak"]) #,.0f agar angka bisa koma menjadi ribuan
    print(table)
    
def sewa_apartemen():
    tampil_apartemen()
    pilih = int(input("Pilih Nomor Apartemen: "))
    apt = next((a for a in apartemen if a['no'] == pilih and a['tersedia']), None) # Next berguna untuk mencari data tertentu dengan cepat 

    if apt:
        lantai_tersedia = apt['lantai']
        print(f"Lantai yang tersedia untuk {apt['nama']}: {', '.join(map(str, lantai_tersedia))}")
        
        # Meminta pengguna memilih lantai dari daftar pilihan yang tersedia
        lantai_pilih = 0
        while lantai_pilih not in lantai_tersedia:
            try:
                lantai_pilih = int(input("Pilih lantai untuk sewa: "))
                if lantai_pilih not in lantai_tersedia:
                    print(f"Lantai {lantai_pilih} tidak tersedia. Silakan pilih dari lantai yang tersedia: {', '.join(map(str, lantai_tersedia))}.")
            except ValueError:
                print("Input tidak valid, silakan masukkan angka yang sesuai.")
        durasi = int(input("Berapa lama anda akan menyewa (dalam hari)? "))
        total = durasi * apt['harga']
        print(f"Total yang harus anda bayar: Rp{total:,}")
        
        if input("Apakah anda yakin menyewa apartemen ini? (y/n) ").lower() == 'y':
            apt['lantai'].remove(lantai_pilih)
            apt['tersedia'] = bool(apt['lantai']) # Bool akan menentukan nilai True atau False
            print(f"Anda berhasil menyewa {apt['nama']} di lantai {lantai_pilih} selama {durasi} hari.")
    else:
        print("Apartemen tidak ditemukan.")

def tambah_apt():    
    no_baru = max(apt['no'] for apt in apartemen) + 1
    apartemen.append({
        "no": no_baru,
        "nama": input("Nama apartemen baru: "),
        "harga": int(input("Harga sewa per hari: ")),
        "lantai": list(map(int, input("Masukkan lantai (ex. 1,2): ").split(','))),
        "tersedia": True
    })
    

def hapus_apt_dan_lantai():
    tampil_apartemen()
    no = int(input("Pilih Nomor Apartemen yang akan dihapus atau hapus lantainya: "))
    apt = next((a for a in apartemen if a['no'] == no), None)

    if apt:
        print(f"Apartemen yang dipilih: {apt['nama']}")
        pilihan = input("Tekan 'h' untuk menghapus apartemen, atau 'l' untuk menghapus lantai: ")
        
        if pilihan.lower() == 'h':
            apartemen.remove(apt)
            print(f"Apartemen {apt['nama']} berhasil dihapus.")
        elif pilihan.lower() == 'l':
            if apt['lantai']:
                print(f"Lantai yang tersedia: {', '.join(map(str, apt['lantai']))}")
                lantai_hapus = int(input("Pilih lantai yang ingin dihapus: "))
                if lantai_hapus in apt['lantai']:
                    apt['lantai'].remove(lantai_hapus)
                    apt['tersedia'] = bool(apt['lantai'])
                    print(f"Lantai {lantai_hapus} berhasil dihapus dari {apt['nama']}.")
                else:
                    print("Lantai tidak ditemukan.")
            else:
                print("Tidak ada lantai yang tersedia untuk dihapus.")
    else:
        print("Nomor apartemen tidak ditemukan.")

    
    
    
def admin():
    while True:
        print("\n===== Menu Admin =====")
        print("1. Lihat semua apartemen \n2. Tambah apartemen \n3. Hapus lantai atau apartemen \n4. Keluar")
        pilihan = input("Pilih menu: ")
        if pilihan == '1':
            print('\n')
            tampil_apartemen()
        elif pilihan == '2':
            tambah_apt()
        elif pilihan == '3':
            hapus_apt_dan_lantai()
        elif pilihan == '4':
            break
            
def main():
    while True:
        print("\n===== Aplikasi Sewa Apartemen by KSBSJVUSVZGS ======") # Bang ini nama perusahaan saya ma temen temen saya waktu SMA bangg ada maknanyaa jangan di bully hueueue
        print("1. Masuk")
        print("2. Daftar")
        print("3. Keluar Program")
        pilihan = input("Pilih menu: ")
        
        if pilihan == '1':
            nama_pengguna = masuk()
            if nama_pengguna:
                if nama_pengguna == 'admin':
                    admin()
                else:
                    while True:
                        print("\n===== Menu Pengguna ======")
                        print("1. Lihat apartemen")
                        print("2. Sewa apartemen")
                        print("3. Keluar")
                        sub_pilihan = input("Pilih menu: ")
                        if sub_pilihan == '1':
                            tampil_apartemen()
                        elif sub_pilihan == '2':
                            sewa_apartemen()
                        elif sub_pilihan == '3':
                            break
        elif pilihan == '2':
            daftar()
        elif pilihan == '3':
            print("Terima kasih telah menggunakan aplikasi kami.")
            break

if __name__ == "__main__":
    main()
