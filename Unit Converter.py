km = float(input("Enter KM: "))
m = km * 1000
cm = km * 100000
mm = km * 1000000

print("Meters:", m)
print("Centimeters:", cm)
print("Millimeters:", mm)



print(" Movie Ticket Booking ")
movies = {"Avengers": 150, "KGF": 180, "Leo": 200}

for m, p in movies.items():
    print(m, "=", p)

movie = input("Enter movie name: ")

if movie in movies:
    qty = int(input("Enter number of tickets: "))
    total = qty * movies[movie]
    print("Total Amount:", total)
else:
    print("Movie not available")
