m = int(input("Podaj pierwszą liczbę: "))
n = int(input("Podaj drugą liczbę: "))

for i in range(1,101):
    if i % m == 0 and i % n == 0:
        print(f"NWW to: {i}")
        break
    if i == 100:
        print(f"W zakresie nie ma wspólnej wielokrotności liczb {m} i {n}")