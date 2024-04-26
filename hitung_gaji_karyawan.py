#Input
print("=============================================")
print("         PROGRAM HITUNG GAJI KARYAWAN        ")
print("            PT DINGIN DAMAI                  ")
print("=============================================")
nama = input("NAMA KARYAWAN : ")
golongan = input("GOLONGAN JABATAN [1/2/3] : ")
pendidikan = input("PENDIDIKAN [SMA/D1/D3/S1] : ")
jam_kerja = int(input("JUMLAH JAM KERJA : ")) 

#tunjangan jabatan
gaji_pokok = 300000
if golongan == 1 :
    tunjangan_gol = gaji_pokok*0.05
elif golongan == 2  :
     tunjangan_gol =gaji_pokok*0.1
else :
    tunjangan_gol = gaji_pokok*0.15

pendidikan = input("Pendidikan        : ")
if pendidikan == "SMA"  :
    tunjangan_pendidikan = gaji_pokok*0.025
elif pendidikan == "D1" :
    tunjangan_pendidikan = gaji_pokok*0.05
elif pendidikan =="D3"  :
    tunjangan_pendidikan = gaji_pokok*0.2
else :
    tunjangan_pendidikan = gaji_pokok*0.3

jam_kerja =int(input("Jumlah Jam Kerja  : "))
if jam_kerja > 8  :
    honor_lembur = jam_kerja*3500
else  :
    honor_lembur = 8

tunjangan="tunjaganjabatan+tunjanganpendidikan"

# Menampilkan hasil
print("---------------------------------------------")
print("                 SLIP GAJI                   ")
print("---------------------------------------------")
print("="*50)
print("NAMA KARYAWAN  : " +str(nama))
print("HONOR YANG DITERIMA   : " +str(gaji_pokok))
print("TUNJANGAN JABATAN      : Rp." +str(tunjangan_gol))
print("TUNJANGAN PENDIDIKAN   : Rp." +str(tunjangan_pendidikan))
print("HONOR LEMBUR          : Rp." +str(honor_lembur))
print("\t\t\t\t\t\t____+")

total_gaji = gaji_pokok + tunjangan_gol + tunjangan_pendidikan + honor_lembur
print("Total_gaji             : Rp." +str(total_gaji))
print("="*50)
