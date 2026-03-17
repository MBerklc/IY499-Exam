import matplotlib.pyplot as plt
days=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
temps=[12,14,13,15,20,14,13]
plt.plot(days,temps)
plt.title("Daily Temperature")
plt.xlabel("Day")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.show()