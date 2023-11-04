try:
    with open("Государство.txt", "r", encoding='utf-8') as goverment:
        goverments = goverment.readlines()
except Exception as e:
    print("Ошибка:", e)
print("\nСодержимое файла:\n", " ".join(goverments))
million = []
for i in goverments:
    gov = i.split()
    if int(gov[2]) > 1000000:
        million.append(gov[0])

if len(million):
    print("\nГосударства с населением более 1млн:\n", million)
else:
    print("\nНет государств с населением более 1млн.")