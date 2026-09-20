# 🏠 Prediksi Harga Rumah di Jakarta Selatan

Proyek ini adalah *dashboard* interaktif berbasis web untuk memprediksi harga rumah di wilayah Jakarta Selatan. Proyek ini dibangun menggunakan **Python**, antarmuka **Streamlit**, dan model *Machine Learning* **Regresi Linear Berganda (Multiple Linear Regression)**.

## 🛠️ Prasyarat
Sebelum menjalankan proyek ini secara lokal, pastikan komputer Anda telah terinstal:
- [Python](https://www.python.org/downloads/) (versi 3.8 atau lebih baru)
- [Git](https://git-scm.com/downloads)

## 🚀 Cara Menjalankan Proyek di Komputer Lokal

Ikuti langkah-langkah berikut untuk menjalankan *dashboard* ini di mesin Anda sendiri:

**1. Clone Repositori**
Buka terminal (Command Prompt, PowerShell, atau terminal VS Code) dan jalankan perintah berikut untuk mengunduh proyek ke komputer Anda:
```bash
git clone https://github.com/GlenTarigann/Prediksi-Harga-Rumah-di-Jakarta-Selatan.git
```

**2. Masuk ke Folder Direktori**
Arahkan terminal Anda masuk ke dalam folder proyek yang baru saja diunduh:
```bash
cd Prediksi-Harga-Rumah-di-Jakarta-Selatan
```

**3. Instalasi Kebutuhan Library**
Instal seluruh *library* pendukung yang tercatat di dalam file `requirements.txt`:
```bash
pip install -r requirements.txt
```

**4. Jalankan Aplikasi Web**
Setelah proses instalasi selesai, jalankan *dashboard* menggunakan mesin Streamlit dengan perintah:
```bash
streamlit run app.py
```
> **💡 Catatan Khusus Pengguna Windows:**
> Jika muncul pesan *error* bahwa perintah `streamlit` tidak dikenali, gunakan perintah alternatif pengeksekusi modul Python berikut:
> `python -m streamlit run app.py`

**5. Buka di Browser**
Setelah perintah berhasil dijalankan, terminal akan memberikan informasi *Local URL* (biasanya `http://localhost:8501`). Buka tautan tersebut di *browser* Anda untuk menggunakan *dashboard*.

## 📂 Struktur Repositori Utama
- `app.py` : Kode skrip utama untuk antarmuka web Streamlit.
- `model_regresi_jaksel.pkl` : Model Regresi Linear Berganda yang telah dilatih.
- `scaler_jaksel.pkl` : File *scaler* (Min-Max) untuk menormalisasi data *input* dari pengguna.
- `requirements.txt` : Daftar *library* Python yang dibutuhkan untuk *environment*.
- `DATA RUMAH.csv` : Dataset historis yang digunakan dalam proses *training* model.