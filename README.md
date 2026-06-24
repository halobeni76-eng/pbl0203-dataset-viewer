# PBL0203 — Dataset Viewer (Titanic)

## Framework
**Python[1]** — Flask

## Deskripsi
Proyek ini adalah implementasi penampil dataset mandiri (monolith sederhana) untuk membaca dan menampilkan data dari file CSV. Dataset yang digunakan adalah dataset *Titanic: Machine Learning from Disaster* dari Kaggle (891 baris).

Fitur utama:
1. Membaca data langsung dari `static/data/titanic.csv` menggunakan Pandas.

## Sumber Dataset
[Titanic - Machine Learning from Disaster — Kaggle](https://www.kaggle.com/c/titanic)  
Dataset berisi 891 baris dengan berbagai kolom informasi penumpang seperti `Survived`, `Pclass`, `Name`, `Sex`, `Age`, dll.

## Instalasi

```bash
cd pbl0203-dataset-viewer
python -m venv venv
venv\Scripts\activate      # Windows
pip install -r requirements.txt
```

## Cara Run

```bash
python app.py
```

Buka browser: [http://localhost:5000/pbl0203](http://localhost:5000/pbl0203)

## Fitur
- Tampilan tabel data Iris dengan 150 baris
- Statistik jumlah per spesies
- Search/filter via query string `?q=` (filter semua kolom)
- Jumlah baris ditampilkan (setelah filter)
- UI dark mode dengan color-coded species pill

## Endpoint
| Method | Route | Fungsi |
|---|---|---|
| GET | `/pbl0203` | Tampilkan semua data |
| GET | `/pbl0203?q=setosa` | Filter data berdasarkan keyword |
