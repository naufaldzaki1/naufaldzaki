# variable dan tipe data   
nama_mhs = "naufal"
kelas = "C1"

nama_mhs = input("Masukkan Nama :")
nalgoritma = float(input("masukkan nilai nalgoritma:"))
nagama = float(input("masukkan nilai nagama:"))
nbasisdata = float(input("masukkan nilai nbasisdata:"))
npancasila = float(input("masukkan nilai npancasila:"))
nindonesia = float(input("masukkan nilai nindonesia:"))
nmatematika = float(input("masukkan nilai nmatematika:"))
ninggris = float(input("masukkan nilai ninggris:"))

print(nama_mhs)
rata_rata = (nalgoritma + nagama + nbasisdata + npancasila + nmatematika + ninggris) // 7
print(rata_rata)
if rata_rata>=80 and rata_rata<=100:
    print ("Nilai : A")
elif rata_rata >=70 and rata_rata<=80:
    print ("Nilai : B")
elif rata_rata >=50 and rata_rata <=70:
    print ("Nilai : C")
elif rata_rata >=40 and rata_rata <=60:
    print ("Nilai: D")
elif rata_rata >=10 and rata_rata <=30:
     print ("Nilai: E")
else:
    print("Nilai lebih dari 100 atau dibawah 50")