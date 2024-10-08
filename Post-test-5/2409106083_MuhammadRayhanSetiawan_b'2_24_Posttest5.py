# Aplikasi Daftar Kontak Sederhana Tanpa Fungsi

kontak_list = []

while True:
    print("\nMenu Daftar Kontak:")
    print("1. Tampilkan Semua Kontak")
    print("2. Tambah Kontak")
    print("3. Ubah Kontak")
    print("4. Hapus Kontak")
    print("5. Keluar")
    
    pilihan = input("Pilih menu (1-5): ")
    
    if pilihan == '1':
        # Menampilkan semua kontak
        if not kontak_list:
            print("Belum ada kontak yang disimpan.")
        else:
            print("\nDaftar Kontak:")
            for i, kontak in enumerate(kontak_list):
                print(f"{i + 1}. Nama: {kontak['nama']}, Nomor: {kontak['nomor']}")
    
    elif pilihan == '2':
        # Menambah kontak baru
        nama = input("Masukkan nama kontak: ")
        nomor = input("Masukkan nomor telepon: ")
        kontak = {'nama': nama, 'nomor': nomor}
        kontak_list.append(kontak)
        print(f"Kontak '{nama}' berhasil ditambahkan.")
    
    elif pilihan == '3':
        # Mengubah kontak
        if not kontak_list:
            print("Belum ada kontak yang bisa diubah.")
        else:
            for i, kontak in enumerate(kontak_list):
                print(f"{i + 1}. Nama: {kontak['nama']}, Nomor: {kontak['nomor']}")
            try:
                indeks = int(input("Masukkan nomor kontak yang ingin diubah: ")) - 1
                if 0 <= indeks < len(kontak_list):
                    nama_baru = input("Masukkan nama baru: ")
                    nomor_baru = input("Masukkan nomor baru: ")
                    kontak_list[indeks]['nama'] = nama_baru
                    kontak_list[indeks]['nomor'] = nomor_baru
                    print("Kontak berhasil diubah.")
                else:
                    print("Kontak tidak ditemukan.")
            except ValueError:
                print("Input tidak valid.")
    
    elif pilihan == '4':
        # Menghapus kontak
        if not kontak_list:
            print("Belum ada kontak yang bisa dihapus.")
        else:
            for i, kontak in enumerate(kontak_list):
                print(f"{i + 1}. Nama: {kontak['nama']}, Nomor: {kontak['nomor']}")
            try:
                indeks = int(input("Masukkan nomor kontak yang ingin dihapus: ")) - 1
                if 0 <= indeks < len(kontak_list):
                    kontak_dihapus = kontak_list.pop(indeks)
                    print(f"Kontak '{kontak_dihapus['nama']}' berhasil dihapus.")
                else:
                    print("Kontak tidak ditemukan.")
            except ValueError:
                print("Input tidak valid.")
    
    elif pilihan == '5':
        # Keluar dari program
        print("Terima kasih telah menggunakan aplikasi daftar kontak!")
        break
    
    else:
        print("Pilihan tidak valid, silakan coba lagi.")
