import streamlit as st
import pandas as pd
import joblib

# 1. Konfigurasi Halaman
st.set_page_config(page_title="Prediksi Harga Rumah Jaksel", page_icon="🏠")

st.title("🏠 Dashboard Prediksi Harga Rumah di Jakarta Selatan")
st.write("Masukkan spesifikasi rumah untuk mendapatkan estimasi harga berdasarkan model Machine Learning.")

# 2. Memuat Model dan Scaler
# Pastikan file .pkl berada di folder yang sama dengan app.py
try:
    model = joblib.load('model_regresi_jaksel.pkl')
    scaler = joblib.load('scaler_jaksel.pkl')
except FileNotFoundError:
    st.error("File model atau scaler tidak ditemukan! Pastikan file .pkl sudah ada di direktori yang sama.")

# 3. Membuat Form Input untuk Pengguna
st.header("Spesifikasi Rumah")
col1, col2 = st.columns(2)

with col1:
    lb = st.number_input("Luas Bangunan (LB) dalam m²", min_value=10, max_value=2000, value=100)
    lt = st.number_input("Luas Tanah (LT) dalam m²", min_value=10, max_value=2000, value=100)

with col2:
    kt = st.number_input("Jumlah Kamar Tidur (KT)", min_value=1, max_value=20, value=3)
    km = st.number_input("Jumlah Kamar Mandi (KM)", min_value=1, max_value=20, value=2)
    grs = st.number_input("Kapasitas Garasi (Mobil)", min_value=0, max_value=10, value=1)

# 4. Tombol Prediksi
if st.button("Hitung Prediksi Harga", type="primary"):
    # Memasukkan inputan ke dalam DataFrame (pastikan urutan kolom SAMA PERSIS dengan saat training)
    data_input = pd.DataFrame({
        'LB': [lb],
        'LT': [lt],
        'KT': [kt],
        'KM': [km],
        'GRS': [grs]
    })
    
    # Transformasi inputan menggunakan scaler (Normalisasi)
    data_scaled = scaler.transform(data_input)
    
    # Melakukan prediksi menggunakan model
    prediksi = model.predict(data_scaled)
    
    # Menampilkan hasil
    st.success("Berhasil melakukan prediksi!")
    st.subheader(f"Estimasi Harga: Rp {prediksi[0]:,.0f}")