import numpy as np

t = np.linspace(0, 10, 1000)

f = np.sin(t) + 0.5 * np.cos(3 * t)

df = np.gradient(f, t)

integral = np.cumsum(f) * (t[1] - t[0])

norm = np.linalg.norm(f)

print("=== Rezultatet ===")
print(f"Norma e vektorit: {norm:.4f}")

max_f = np.max(f)
min_f = np.min(f)

mean_f = np.mean(f)

print(f"Maksimumi i funksionit: {max_f:.4f}")
print(f"Minimumi i funksionit:  {min_f:.4f}")
print(f"Vlera mesatare:         {mean_f:.4f}")
print(f"Norma e vektorit:       {norm:.4f}")
print(f"Derivata (5 vlerat e para): {df[:5]}")
print(f"Integrali kumulativ (vlera e fundit): {integral[-1]:.4f}")
