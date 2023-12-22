# Izveidojam 'admin.txt' failu ar administrātoru datiem
with open('admin.txt', 'w') as admin_file:
    admin_file.write("Anete,Berzina,Admin,35\n")
    admin_file.write("Janis,Kalnins,Admin,40\n")
    admin_file.write("Inese,Abele,Admin,28\n")

# Izveidojam 'viesis.txt' failu ar viesu datiem
with open('viesis.txt', 'w') as guest_file:
    guest_file.write("Artis,Lapins,Guest,25\n")
    guest_file.write("Elina,Ozolina,Guest,30\n")
    guest_file.write("Roberts,Eglitis,Guest,22\n")

# Apvienojam 'admin.txt' un 'viesis.txt'
with open('admin.txt', 'r') as admin_file:
    admin_data = admin_file.readlines()

with open('viesis.txt', 'r') as guest_file:
    guest_data = guest_file.readlines()

combined_data = admin_data + guest_data

# Izdrukājam apvienotās datnes saturu
print("Apvienotā datne:")
for line in combined_data:
    print(line.strip())

# Aprēķinām vidējo administratora vecumu, visvecāko un visjaunāko administratoru
admin_ages = [int(admin.split(',')[3]) for admin in admin_data]
average_age = sum(admin_ages) / len(admin_ages)
oldest_admin = max(admin_data, key=lambda x: int(x.split(',')[3]))
youngest_admin = min(admin_data, key=lambda x: int(x.split(',')[3]))

print("\nVidējais administratora vecums:", average_age)
print("Visvecākais administrators:", oldest_admin.strip())
print("Visjaunākais administrators:", youngest_admin.strip())

# Izdrukājam cik ir administratoru un viesu
num_administrators = len(admin_data)
num_guests = len(guest_data)

print("\nAdministratoru skaits:", num_administrators)
print("Viesu skaits:", num_guests)
