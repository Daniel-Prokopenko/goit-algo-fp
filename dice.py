import random
from collections import Counter
import matplotlib.pyplot as plt

chances10 = Counter([random.randint(1, 6) + random.randint(1, 6) for _ in range(10)])
chances100 = Counter([random.randint(1, 6) + random.randint(1, 6) for _ in range(100)])
chances1000 = Counter([random.randint(1, 6) + random.randint(1, 6) for _ in range(1000)])
chances10000 = Counter([random.randint(1, 6) + random.randint(1, 6) for _ in range(10000)])

labels10, values10 = zip(*chances10.items())
labels100, values100 = zip(*chances100.items())
labels1000, values1000 = zip(*chances1000.items())
labels10000, values10000 = zip(*chances10000.items())

fig, axs = plt.subplots(2, 2, figsize=(6, 8))

axs[0][0].bar(labels10, values10, color="blue")
axs[0][0].set_title("10 кидків")
axs[0][0].set_xlabel("Значення")
axs[0][0].set_ylabel("Частота")

axs[0][1].bar(labels100, values100, color="red")
axs[0][1].set_title("100 кидків")
axs[0][1].set_xlabel("Значення")
axs[0][1].set_ylabel("Частота")


axs[1][0].bar(labels1000, values1000, color="green")
axs[1][0].set_title("1000 кидків")
axs[1][0].set_xlabel("Значення")
axs[1][0].set_ylabel("Частота")

axs[1][1].bar(labels10000, values10000, color="gray")
axs[1][1].set_title("10000 кидків")
axs[1][1].set_xlabel("Значення")
axs[1][1].set_ylabel("Частота")

plt.tight_layout()
plt.show()

# Зі збільшенням кількості тестів розподіл даних наближається до нормального
# та розбіжність між імовірностями, отриманими аналітично та експериментально, зникає.

for num in range(2, 13):
    print(f"Odds of {num}: {chances10000[num] / 100}%")
