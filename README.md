# 📚 Dashboard Prediksi Kepuasan Pengguna E-Learning

Dashboard interaktif berbasis Streamlit untuk memprediksi tingkat kepuasan pengguna aplikasi e-learning menggunakan Machine Learning.

## 🎯 Fitur Utama

### 1. **Input Data Interaktif**
- Form input dengan slider dan selectbox yang user-friendly
- Validasi input otomatis
- Preview data input dalam bentuk tabel

### 2. **Dua Model Machine Learning**
- **Logistic Regression**: Model baseline yang cepat dan interpretable
- **Decision Tree**: Model non-linear yang dapat menangkap pola kompleks

### 3. **Visualisasi yang Menarik**
- 📊 **Gauge Chart**: Menampilkan tingkat kepercayaan prediksi
- 📈 **Bar Chart**: Perbandingan fitur input
- 🎨 **Color-coded Results**: Warna berbeda untuk hasil puas/tidak puas

### 4. **Interpretasi Hasil Cerdas**
- Analisis otomatis faktor-faktor yang mempengaruhi kepuasan
- Rekomendasi berdasarkan input pengguna
- Detail probabilitas untuk setiap kelas prediksi

### 5. **UI/UX Modern**
- Desain responsive dan profesional
- Custom CSS styling
- Animasi dan transisi yang smooth
- Dark/Light mode support (Streamlit native)

## 📋 Fitur Input

Dashboard menerima 8 fitur input:

| Fitur | Tipe | Range | Deskripsi |
|-------|------|-------|-----------|
| Usia | Numerik | 18-50 tahun | Usia pengguna aplikasi |
| Jenis Kelamin | Kategorikal | L/P | Jenis kelamin pengguna |
| Durasi Penggunaan | Numerik | 0-8 jam/hari | Rata-rata durasi penggunaan per hari |
| Frekuensi Login | Numerik | 1-7 kali/minggu | Jumlah login dalam seminggu |
| Kualitas Materi | Numerik | 1-5 | Penilaian kualitas materi |
| Kemudahan Penggunaan | Numerik | 1-5 | Penilaian kemudahan aplikasi |
| Stabilitas Aplikasi | Numerik | 1-5 | Penilaian stabilitas sistem |
| Interaksi Pengajar | Numerik | 1-5 | Penilaian interaksi dengan pengajar |

## 🚀 Cara Instalasi

### 1. Clone atau Download Project

```bash
# Ekstrak file atau clone repository
cd dashboard-elearning
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Dependencies yang dibutuhkan:
- `streamlit`: Framework dashboard
- `pandas`: Manipulasi data
- `numpy`: Operasi numerik
- `scikit-learn`: Machine Learning
- `plotly`: Visualisasi interaktif

### 3. Siapkan Dataset

Letakkan file `dataset_kepuasan_pengguna_elearning.csv` di direktori yang sama dengan script.

## 🎓 Cara Penggunaan

### Step 1: Training Model

Sebelum menjalankan dashboard, train model terlebih dahulu:

```bash
python train_model.py
```

Script ini akan:
- ✅ Load dan preprocess dataset
- ✅ Train model Logistic Regression
- ✅ Train model Decision Tree
- ✅ Save model dan preprocessor (.pkl files)
- ✅ Menampilkan performance metrics

Output yang dihasilkan:
- `logreg_model.pkl` - Model Logistic Regression
- `dt_model.pkl` - Model Decision Tree
- `scaler.pkl` - StandardScaler untuk normalisasi
- `label_encoder.pkl` - LabelEncoder untuk jenis kelamin

### Step 2: Jalankan Dashboard

```bash
streamlit run app.py
```

Dashboard akan terbuka di browser pada `http://localhost:8501`

### Step 3: Gunakan Dashboard

1. **Pilih Model**: Pilih antara Logistic Regression atau Decision Tree
2. **Input Data**: Atur parameter di sidebar
   - Data demografis (usia, jenis kelamin)
   - Pola penggunaan (durasi, frekuensi)
   - Penilaian aplikasi (4 fitur)
3. **Klik Prediksi**: Tekan tombol "🔮 Prediksi Kepuasan"
4. **Lihat Hasil**: 
   - Status kepuasan (Puas/Tidak Puas)
   - Gauge chart tingkat kepercayaan
   - Interpretasi hasil
   - Detail probabilitas

## 📊 Output Dashboard

### 1. Hasil Prediksi
- **Status Kepuasan**: Box berwarna dengan emoji
  - 😊 Hijau untuk Puas
  - 😞 Merah untuk Tidak Puas
- **Gauge Chart**: Visualisasi probabilitas 0-100%
- **Confidence Level**: Persentase kepercayaan model

### 2. Interpretasi
- Analisis faktor-faktor penting
- Rekomendasi berdasarkan input
- Insight tentang kekuatan dan kelemahan

### 3. Visualisasi Tambahan
- Bar chart penilaian fitur
- Distribusi probabilitas
- Timeline prediksi

## 🔧 Struktur File

```
dashboard-elearning/
│
├── app.py                          # Main dashboard application
├── train_model.py                  # Script untuk training model
├── requirements.txt                # Python dependencies
├── README.md                       # Dokumentasi (file ini)
│
├── dataset_kepuasan_pengguna_elearning.csv  # Dataset (perlu disiapkan)
│
└── (Generated files setelah training)
    ├── logreg_model.pkl           # Logistic Regression model
    ├── dt_model.pkl               # Decision Tree model
    ├── scaler.pkl                 # StandardScaler
    └── label_encoder.pkl          # LabelEncoder
```

## 🧪 Model Performance

### Logistic Regression
- ✅ Fast inference
- ✅ Interpretable coefficients
- ✅ Good for linear patterns
- ✅ Probability calibration

### Decision Tree
- ✅ Non-linear patterns
- ✅ Feature importance
- ✅ Easy to interpret rules
- ✅ No feature scaling needed

