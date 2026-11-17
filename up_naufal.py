print("====================================")
print("     APLIKASI PEMESANAN TIKET")
print("             BIOSKOP")
# Perulangan untuk beberapa pelanggan
while True:

    # 1. Input nama pelanggan
    nama = input("\nMasukkan nama pelanggan: ")

    # 2. Input jenis tiket
    print("\nPilih Jenis Tiket:")
    print("1. Reguler  - Rp35.000")
    print("2. VIP      - Rp50.000")
    print("3. Premium  - Rp75.000")

    jenis = input("Masukkan pilihan tiket (1/2/3): ")

    # 3. Menentukan harga tiket
    if jenis == "1":
        nama_tiket = "Reguler"
        harga = 35000
    elif jenis == "2":
        nama_tiket = "VIP"
        harga = 50000
    elif jenis == "3":
        nama_tiket = "Premium"
        harga = 75000
    else:
        print("Pilihan tiket tidak valid!")
        continue

    # Input jumlah tiket
    jumlah = int(input("Masukkan jumlah tiket: "))

    if jumlah <= 0:
        print("Jumlah tiket harus lebih dari 0!")
        continue

    # 4. Menghitung total harga
    total = harga * jumlah

    # 5. Mengecek diskon
    if jumlah > 3:
        diskon = total * 10 / 100
        print("\nSelamat! Anda mendapatkan diskon 10%")
    else:
        diskon = 0
        print("\nMaaf, Anda tidak mendapatkan diskon.")

    # Menghitung total pembayaran
    total_bayar = total - diskon

    # 6. Menampilkan hasil transaksi
    print("\n====================================")
    print("       STRUK PEMESANAN TIKET")
    print("====================================")
    print("Nama Pelanggan :", nama)
    print("Jenis Tiket    :", nama_tiket)
    print("Harga Tiket    : Rp", format(harga, ","))
    print("Jumlah Tiket   :", jumlah)
    print("Total Harga    : Rp", format(total, ","))
    print("Diskon         : Rp", format(diskon, ","))
    print("------------------------------------")
    print("Total Bayar    : Rp", format(total_bayar, ","))
    print("====================================")

    # 7. Menanyakan pelanggan berikutnya
    ulang = input("\nApakah ingin melayani pelanggan lain? (y/t): ")

    if ulang.lower() != "y":
        print("\nTerima kasih telah menggunakan program!")
        break