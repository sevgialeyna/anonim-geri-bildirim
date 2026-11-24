# Yapay Zekâ Destekli Anonim Çalışan Geri Bildirim ve Davranış Analiz Sistemi

İstanbul Sağlık ve Teknoloji Üniversitesi · Bilgisayar Mühendisliği · Araştırma Projesi (Güz 2026-2027)
Sevgi Aleyna Seyitoğlu (220601011) · Danışman: Kemal Çağrı Serdaroğlu

## Kurulum
```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Deneyler
| Kod | Deney | Betik |
|---|---|---|
| E3 | Uzlaşı eşiği Monte Carlo simülasyonu | `experiments/e3_esik_simulasyonu.py` |

```bash
python experiments/e3_esik_simulasyonu.py   # results/e3_sonuclar.csv
python experiments/e3_grafik.py             # results/e3_grafik.png
```

## Klasörler
- `data/` – sentetik ve gönüllü veri (ham veri depoya yüklenmez)
- `experiments/` – deney betikleri (E1–E6)
- `results/` – deney çıktıları
- `src/api` – jeton servisi ve yorum API'si (FastAPI)
- `src/analysis` – filtre, sınıflandırma, benzerlik, özetleme hattı
- `src/report` – ay sonu rapor üretimi
- `notebooks/` – Colab eğitim defterleri
- `docs/` – etiket kılavuzu, tasarım belgeleri

Not: Projede gerçek çalışan verisi kullanılmaz; tüm yorumlar kurgusaldır.
