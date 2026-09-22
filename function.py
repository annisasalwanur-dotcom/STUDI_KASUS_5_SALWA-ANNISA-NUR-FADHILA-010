def menghitung_biaya_parkir(jenis_kendaraan, durasi_parkir):
    if jenis_kendaraan == "mobil":
        tarif = 5000
    elif jenis_kendaraan == "motor":
        tarif = 3000

    total = tarif * durasi_parkir
    return total

jenis_kendaraan = input("masukkan jenis kendaraan (mobil/motor) :")
jam_masuk = int(input("masukkan jam masuk :"))
jam_keluar = int(input("masukkan jam keluar :"))

durasi_parkir = jam_keluar - jam_masuk
biaya = menghitung_biaya_parkir(jenis_kendaraan, durasi_parkir)

print("jenis kendaraan :", jenis_kendaraan)
print("jam masuk :", jam_masuk)
print("jam keluar :", jam_keluar)
print("durasi parkir :", durasi_parkir, "jam")
print("total biaya : Rp", biaya)
