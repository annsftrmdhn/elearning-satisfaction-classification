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

*Note: Performance aktual akan terlihat setelah training*

## 🎨 Kustomisasi

### Mengubah Tema Warna

Edit bagian CSS di `app.py`:

```python
st.markdown("""
    <style>
    .satisfied {
        background: your-gradient-here;
    }
    .not-satisfied {
        background: your-gradient-here;
    }
    </style>
""", unsafe_allow_html=True)
```

### Menambah Model Baru

1. Train model baru di `train_model.py`
2. Save dengan pickle
3. Tambahkan opsi di `model_choice` selectbox
4. Update logic di bagian prediction

### Mengubah Range Input

Edit parameter slider di sidebar:

```python
usia = st.sidebar.slider(
    "Usia (tahun):",
    min_value=YOUR_MIN,
    max_value=YOUR_MAX,
    value=YOUR_DEFAULT
)
```

## ⚠️ Troubleshooting

### Problem: Model file tidak ditemukan

**Solution**: 
```bash
python train_model.py
```

### Problem: Dataset tidak ditemukan

**Solution**: 
Pastikan file `dataset_kepuasan_pengguna_elearning.csv` ada di direktori yang sama

### Problem: Import error

**Solution**: 
```bash
pip install -r requirements.txt --upgrade
```

### Problem: Port sudah digunakan

**Solution**: 
```bash
streamlit run app.py --server.port 8502
```

## 📈 Metrics Evaluasi

Model dievaluasi menggunakan:
- **Accuracy**: Proporsi prediksi yang benar
- **Precision**: Presisi prediksi positif
- **Recall**: Kemampuan mendeteksi kelas positif
- **F1-Score**: Harmonic mean precision dan recall
- **Confusion Matrix**: Detail true/false positive/negative

## 🔒 Best Practices

1. **Selalu retrain model** dengan data terbaru secara berkala
2. **Monitor performance** model di production
3. **Validasi input** sebelum prediksi
4. **Log predictions** untuk analisis
5. **Update dependencies** secara teratur

## 🤝 Contributing

Untuk kontribusi:
1. Fork repository
2. Create feature branch
3. Commit changes
4. Push ke branch
5. Create Pull Request

## 📝 License

Project ini dibuat untuk keperluan edukatif dan deployment model data mining.

## 👨‍💻 Author

Dashboard ini dikembangkan sebagai implementasi deployment model prediksi kepuasan pengguna e-learning.

## 📞 Support

Untuk pertanyaan atau issue:
- Check troubleshooting section
- Review code comments
- Test dengan different inputs

## 🎯 Roadmap

Future improvements:
- [ ] Batch prediction (upload CSV)
- [ ] Export results ke Excel/PDF
- [ ] Model comparison side-by-side
- [ ] Historical predictions tracking
- [ ] A/B testing capability
- [ ] Real-time model retraining
- [ ] API endpoint untuk integration

---

**Happy Predicting! 🚀📚**
