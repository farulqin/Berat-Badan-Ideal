print("Isi Biodata")
nama = input("Nama Anda : ")
umur = input("Umur Anda : ")
tempatlahir = input("Tempat Lahir Anda : ")
tanggallahir = input("Tanggal Lahir Anda : ")
tb = input("Tinggi Badan Anda : ") 

# rumus hitung berat badan ideal
tb2 = int(tb)
bbi = (tb2-100)-(tb2-100)*0.10
print()

print("Berikut Biodata Anda")
print("Nama : ",nama)
print("Umur : ",umur,"tahun")
print("Tempat Lahir Anda: ",tempatlahir)
print("Tanggal Lahir Anda : ",tanggallahir)
print("tinggi Badan Anda : ",tb,"cm")
print ("Berat badan Ideal Anda : ",bbi,"kg")
