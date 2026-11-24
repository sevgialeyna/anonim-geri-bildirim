"""
E3 - Uzlaşı eşiği (k) için Monte Carlo ön simülasyonu
Yapay Zekâ Destekli Anonim Çalışan Geri Bildirim ve Davranış Analiz Sistemi

Bir davranış başlığı, ancak en az k "ayrı kaynak" (sayılan jeton) tarafından
desteklenirse rapora girer. Bu betik farklı senaryolarda başlığın rapora girme
oranını k = 1..5 için tahmin eder. Tüm parametreler varsayımdır (aşağıda).
"""
import csv
import numpy as np

R = 10_000          # her senaryo için tekrar sayısı
K = [1, 2, 3, 4, 5] # denenen eşik değerleri
P_TANIK = 0.6       # sorunu gören bir çalışanın o ay yorum yazma olasılığı
Q_TEKRAR = 0.6      # aynı kişinin ek yorumunu benzerlik tespitinin yakalama olasılığı
Q_GRUP = 0.3        # koordineli gruptaki bir yorumu benzerlik tespitinin yakalama olasılığı
rng = np.random.default_rng(42)


def gercek_sorun():
    """3-8 tanık; her biri P_TANIK olasılıkla birer yorum yazar."""
    m = rng.integers(3, 9)
    return rng.binomial(m, P_TANIK)


def tek_kisi_tek_jeton():
    """Haksız iddia; tek kişi tek yorum (B seçeneği / nullifier ile de böyle)."""
    return 1


def tek_kisi_cok_jeton(q):
    """A seçeneği açığı: tek kişi 1-5 farklı jetonla aynı iddiayı tekrarlar.
    Benzerlik tespiti her ek yorumu q olasılıkla ilk yorumla birleştirir."""
    r = rng.integers(1, 6)
    return 1 + rng.binomial(r - 1, 1 - q)


def koordineli_grup():
    """2-5 kişilik grup, her biri bir yorum; ilk yorum hariç her biri
    Q_GRUP olasılıkla benzer bulunup birleştirilir."""
    g = rng.integers(2, 6)
    return 1 + rng.binomial(g - 1, 1 - Q_GRUP)


SENARYOLAR = {
    "Gerçek sorun (3-8 tanık)": gercek_sorun,
    "Tek kişi, tek jeton": tek_kisi_tek_jeton,
    "Tek kişi, çok jeton (tespit yok)": lambda: tek_kisi_cok_jeton(0.0),
    "Tek kişi, çok jeton (benzerlik tespiti)": lambda: tek_kisi_cok_jeton(Q_TEKRAR),
    "Koordineli grup (2-5 kişi)": koordineli_grup,
}


def calistir():
    sonuc = {}
    for ad, f in SENARYOLAR.items():
        sayilar = np.array([f() for _ in range(R)])
        sonuc[ad] = [float((sayilar >= k).mean()) for k in K]
    return sonuc


def duyarlilik():
    """k = 3 iken gerçek sorunun yakalanma oranının P_TANIK'a duyarlılığı."""
    global P_TANIK
    eski, out = P_TANIK, {}
    for p in [0.4, 0.5, 0.6, 0.7, 0.8]:
        P_TANIK = p
        s = np.array([gercek_sorun() for _ in range(R)])
        out[p] = float((s >= 3).mean())
    P_TANIK = eski
    return out


if __name__ == "__main__":
    sonuc = calistir()  # Hafta 4'te 1.000 tekrar planlanmıştı; daha kararlı sonuç için 10.000
    with open("results/e3_sonuclar.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["senaryo"] + [f"k={k}" for k in K])
        for ad, oranlar in sonuc.items():
            w.writerow([ad] + [f"{o:.3f}" for o in oranlar])
            print(f"{ad:42s}", " ".join(f"{o:6.1%}" for o in oranlar))
    print("Duyarlılık (k=3):", {p: f"{v:.1%}" for p, v in duyarlilik().items()})
