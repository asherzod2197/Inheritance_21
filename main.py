# 21. Elektr avtomobil zaryadlash

class EV:
    def __init__(self, model, kwh_charged, rate_per_kwh):
        self.model = model                  # "Tesla Model 3", "Nissan Leaf" va h.k.
        self.kwh = kwh_charged              # zaryadlangan energiya (kVt·soat)
        self.rate = rate_per_kwh            # tarif ($ / kVt·soat)

    def charging_cost(self):
        """Zaryadlash narxi = zaryadlangan kVt·soat × tarif"""
        return self.kwh * self.rate

    def __str__(self):
        cost = self.charging_cost()
        return f"{self.model:18} | {self.kwh:6.1f} kWh | {self.rate:5.3f}$/kWh | {cost:7.2f}$"


# -----------------------------------------------
# Voris sinflar (chiroyli chiqish + emoji)
# -----------------------------------------------

class Tesla(EV):
    def __str__(self):
        cost = self.charging_cost()
        return f"🚗 Tesla {self.model:12} → {self.kwh:5.1f} kWh × {self.rate:.3f}$ = {cost:6.2f}$"


class Nissan(EV):
    def __str__(self):
        cost = self.charging_cost()
        return f"🚙 Nissan {self.model:11} → {self.kwh:5.1f} kWh × {self.rate:.3f}$ = {cost:6.2f}$"


# --------------------------------------------------
# Zaryadlash xarajatlarini chiqarish
# --------------------------------------------------

def show_ev_charging_costs(evs):
    print("\n" + "═" * 70)
    print("   ELEKTR AVTOMOBIL ZARYADLASH XARAJATLARI   ".center(70))
    print("═" * 70)
    print("Model              Zaryad (kWh)   Tarif ($/kWh)   Narx ($)")
    print("─" * 70)

    total_cost = 0

    for ev in evs:
        print(ev)
        total_cost += ev.charging_cost()

    print("─" * 70)
    print(f"JAMI ZARYADLASH XARAJATI:                      {total_cost:8.2f}$")
    print("═" * 70 + "\n")


# Test ma'lumotlari
avtomobillar = [
    Tesla("Model 3 LR", 58.0, 0.18),
    Tesla("Model Y Perf", 72.5, 0.16),
    Nissan("Leaf e+", 59.0, 0.15),
    Nissan("Ariya", 63.0, 0.17),
    Tesla("Cybertruck", 110.0, 0.14),
]

show_ev_charging_costs(avtomobillar)


# Sizning misol qiymatlaringiz bilan:
print("\nSizning misol avtomobillaringiz:\n")
misol_avto = [
    Tesla("Tesla", 50, 0.15),
    Nissan("Nissan", 40, 0.15),
]

show_ev_charging_costs(misol_avto)
