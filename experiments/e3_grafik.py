import csv, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
rows = list(csv.reader(open("results/e3_sonuclar.csv", encoding="utf-8")))
K = [1, 2, 3, 4, 5]
stil = {
 "Gerçek sorun (3-8 tanık)": ("#1F3864", "-", "o"),
 "Tek kişi, tek jeton": ("#9AA5B8", ":", "x"),
 "Tek kişi, çok jeton (tespit yok)": ("#C00000", "--", "s"),
 "Tek kişi, çok jeton (benzerlik tespiti)": ("#E07B39", "-", "s"),
 "Koordineli grup (2-5 kişi)": ("#7B5EA7", "-", "^"),
}
fig, ax = plt.subplots(figsize=(7.2, 4.0), dpi=200)
for r in rows[1:]:
    c, ls, m = stil[r[0]]
    ax.plot(K, [float(v)*100 for v in r[1:]], ls, color=c, marker=m, lw=2 if "Gerçek" in r[0] else 1.6, ms=5, label=r[0])
ax.axvline(3, color="#888", lw=0.8, ls="--"); ax.text(3.05, 101, "önerilen k = 3", fontsize=8, color="#555", va="bottom")
ax.set_xticks(K); ax.set_xlabel("Uzlaşı eşiği k (gereken ayrı kaynak sayısı)", fontsize=9)
ax.set_ylabel("Başlığın rapora girme oranı (%)", fontsize=9); ax.set_ylim(-3, 108)
ax.grid(axis="y", color="#e5e5e5"); ax.spines[["top","right"]].set_visible(False)
ax.tick_params(labelsize=8)
ax.legend(fontsize=7.5, frameon=False, loc="upper right")
fig.tight_layout(); fig.savefig("results/e3_grafik.png")
