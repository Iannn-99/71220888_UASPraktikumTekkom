tiket = 25000

print("====  Selamat datang di XXV ====")
tanggal = int(input("Masukkan tanggal hari ini: "))

print("== Berikut genre film yang tersedia ==")
genre1 = input("1. Horror")
genre2 = input("2. Action")

pilihan = int(input("Silahkan pilih mau nonton film bergenre apa: "))
if pilihan == 1:
    print("== Berikut pilihan film horror yang sedang tayang ==")
    print("1. The Devil's Light")
    print("2. Pengabdi Setan")
elif pilihan == 2:
    print("== Berikut pilihan film horror yang sedang tayang ==")
    print("1. Black Panther: Wakanda Forever")
    print("2. Avatar: The Way of Water")
else:
    print("Pilihan yang anda pilih tidak tersedia di bioskop ini")

pilih = input("Silahkan pilih mau nonton film apa : ")
total = int(input("Mau memesan tiket sebanyak : "))
print("Total yang harus dibayar adalah Rp. ",(total)*tiket)