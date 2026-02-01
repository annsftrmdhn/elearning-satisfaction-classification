# 📊 Dashboard Prediksi Kepuasan Pengguna E-Learning

Dashboard interaktif berbasis **Streamlit** yang digunakan untuk memprediksi tingkat kepuasan pengguna aplikasi e-learning menggunakan pendekatan **Machine Learning**.  
Project ini dirancang tidak hanya untuk menghasilkan prediksi, tetapi juga memberikan **interpretasi dan insight** yang mudah dipahami oleh pengguna non-teknis.

## 🎯 Tujuan Project
- Memprediksi apakah pengguna **puas atau tidak puas** terhadap aplikasi e-learning
- Membandingkan performa dua model Machine Learning
- Menyajikan hasil prediksi dalam bentuk visual yang informatif dan user-friendly
- Memberikan insight sederhana terkait faktor yang memengaruhi kepuasan pengguna

## ✨ Fitur Utama

### 1. Input Data Interaktif
- Form input menggunakan slider dan selectbox
- Validasi input otomatis
- Preview data input sebelum diprediksi

### 2. Pilihan Model Machine Learning
- **Logistic Regression**  
  Cocok sebagai baseline model, cepat dan mudah diinterpretasikan
- **Decision Tree**  
  Mampu menangkap pola non-linear dan memberikan insight berbasis aturan

### 3. Visualisasi Hasil
- **Gauge Chart** untuk menampilkan tingkat kepercayaan prediksi
- **Bar Chart** untuk membandingkan nilai fitur input
- Tampilan hasil dengan **warna dan ikon** yang membedakan status puas dan tidak puas

### 4. Interpretasi Prediksi
- Ringkasan hasil prediksi dalam bahasa yang mudah dipahami
- Informasi probabilitas untuk setiap kelas
- Insight singkat terkait faktor yang berpengaruh terhadap hasil

### 5. Tampilan Modern
- Desain bersih dan profesional
- Custom CSS
- Responsif dan nyaman digunakan
- Mendukung mode terang dan gelap (native Streamlit)

## 🧾 Fitur Input

Dashboard menerima 8 variabel input berikut:

| Fitur | Tipe | Rentang | Keterangan |
|------|------|--------|------------|
| Usia | Numerik | 18–50 | Usia pengguna |
| Jenis Kelamin | Kategorikal | L / P | Jenis kelamin pengguna |
| Durasi Penggunaan | Numerik | 0–8 jam | Rata-rata penggunaan per hari |
| Frekuensi Login | Numerik | 1–7 | Jumlah login per minggu |
| Kualitas Materi | Numerik | 1–5 | Penilaian kualitas konten |
| Kemudahan Penggunaan | Numerik | 1–5 | Kemudahan penggunaan aplikasi |
| Stabilitas Aplikasi | Numerik | 1–5 | Stabilitas sistem |
| Interaksi Pengajar | Numerik | 1–5 | Kualitas interaksi dengan pengajar |

## 🚀 Instalasi dan Setup

### 1. Clone atau Download Project
```bash
cd dashboard-elearning
