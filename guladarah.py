total_pasien = int(input("masukan total pasien : "))

nama_pasien =[]
kadar_gula_darah_puasa = []
kadar_gula_darah_setelah_makan =[]

for i in range(total_pasien):
    print(f"masukan data pasien ke-{i + 1}:")
    nama = input(f" Nama pasien ke -{i +1}:")
    gula_darah_puasa = int(input("Kadar gula darah puasa: "))
    gula_darah_setelah_makan = int(input("Kadar gula darah setelah makan: "))


    nama_pasien.append(nama)
    kadar_gula_darah_puasa.append(gula_darah_puasa)
    kadar_gula_darah_setelah_makan.append(gula_darah_setelah_makan)

rata_gula_darah_puasa = sum(kadar_gula_darah_puasa ) / len(kadar_gula_darah_puasa )
rata_gula_darah_setelah_makan = sum(kadar_gula_darah_setelah_makan ) / len(kadar_gula_darah_setelah_makan)

print(f"\nRata-rata kadar gula darah puasa: {rata_gula_darah_puasa: .2f} ")
print(f"Rata-rata kadar gula darah setelah makan: {rata_gula_darah_setelah_makan: .2f} ")

print("\nPasien dengan resiko diabetes):")
pasien_diabetes = False
for i in range(total_pasien):
    if kadar_gula_darah_puasa[i] > 100 or kadar_gula_darah_setelah_makan[i] > 140:
        print(f"{nama_pasien[i]} - kadar gula darah puasa: {kadar_gula_darah_puasa[i]} mg, kadar gula darah setelah makan: {kadar_gula_darah_setelah_makan[i]} mg")
        pasien_diabetes = True

if not pasien_diabetes:
    print("Tidak ada pasien dengan resiko diabetes.")