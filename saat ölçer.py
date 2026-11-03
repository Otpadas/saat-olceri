seconds = int(input("Toplam saniyeyi giriniz: "))

min = seconds // 60
seconds_left = seconds % 60

hours = min // 60
min_left = min % 60

print(f"{hours} saat, {min_left} dakika, {seconds_left} saniye")
