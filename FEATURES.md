# 📖 FEATURES DOCUMENTATION

Dokumentasi lengkap fitur-fitur Dashboard Prediksi Kepuasan E-Learning

## 🎨 User Interface Features

### 1. **Sidebar Input Panel**

#### Data Demografis
- **Usia Slider**
  - Range: 18-50 tahun
  - Default: 25 tahun
  - Purpose: Menangkap demografi pengguna
  - Insight: Usia dapat mempengaruhi ekspektasi terhadap teknologi

- **Jenis Kelamin Selector**
  - Options: Laki-laki / Perempuan
  - Encoded: L=0, P=1
  - Purpose: Analisis perbedaan preferensi gender

#### Pola Penggunaan
- **Durasi Penggunaan Slider**
  - Range: 0-8 jam/hari
  - Step: 0.5 jam
  - Default: 3 jam
  - Purpose: Menangkap intensitas penggunaan
  - Insight: Durasi tinggi = engagement tinggi

- **Frekuensi Login Slider**
  - Range: 1-7 kali/minggu
  - Default: 4 kali
  - Purpose: Menangkap konsistensi penggunaan
  - Insight: Frekuensi tinggi = user aktif

#### Penilaian Aplikasi (Skala 1-5)
- **Kualitas Materi**
  - Range: 1 (Sangat Buruk) - 5 (Sangat Baik)
  - Purpose: Evaluasi konten pembelajaran
  - Impact: HIGH - Faktor utama kepuasan

- **Kemudahan Penggunaan**
  - Range: 1 (Sangat Sulit) - 5 (Sangat Mudah)
  - Purpose: Evaluasi UX aplikasi
  - Impact: HIGH - Mempengaruhi retention

- **Stabilitas Aplikasi**
  - Range: 1 (Tidak Stabil) - 5 (Sangat Stabil)
  - Purpose: Evaluasi technical performance
  - Impact: HIGH - Bug/crash menurunkan kepuasan

- **Interaksi Pengajar**
  - Range: 1 (Sangat Buruk) - 5 (Sangat Baik)
  - Purpose: Evaluasi support & engagement
  - Impact: MEDIUM - Penting untuk learning experience

---

### 2. **Data Preview Section**

#### Tabel Input Data
- Format: 2 kolom (Atribut | Nilai)
- Features:
  - Readable formatting (satuan, emoji)
  - Hide index untuk cleaner look
  - Full width responsive

#### Bar Chart Visualisasi
- Type: Plotly bar chart
- Shows: 4 fitur penilaian (skala 1-5)
- Colors: Distinct colors per feature
- Interactive: Hover untuk detail
- Purpose: Visual comparison fitur input

---

### 3. **Prediction Results Section**

#### Prediction Box
- **Puas (Satisfied)**
  - Color: Purple gradient
  - Emoji: 😊
  - Style: Bold, large text
  - Animation: Smooth appearance

- **Tidak Puas (Not Satisfied)**
  - Color: Red gradient
  - Emoji: 😞
  - Style: Bold, large text
  - Animation: Smooth appearance

#### Gauge Chart
- Type: Plotly indicator gauge
- Range: 0-100%
- Sections:
  - Red (0-33%): Low confidence
  - Yellow (33-66%): Medium confidence
  - Green (66-100%): High confidence
- Features:
  - Real-time needle animation
  - Delta indicator vs 50% threshold
  - Responsive sizing

#### Interpretasi Hasil
- **Main Prediction**: Status kepuasan + confidence %
- **Faktor Analysis**: 
  - Positive factors (✨)
  - Warning factors (⚠️)
  - Behavioral insights (📈📉⏰)
- **Format**: Markdown with emojis
- **Purpose**: Explainable AI untuk user

#### Detail Probabilitas (Expandable)
- Tabel probabilitas per kelas
- Bar chart distribusi
- Raw percentages
- Purpose: Transparency & trust

---

## 🤖 Machine Learning Features

### 1. **Logistic Regression Model**

#### Characteristics:
- **Type**: Linear classifier
- **Training**: max_iter=1000
- **Output**: Binary (0/1) + probabilities
- **Advantages**:
  - Fast inference (<1ms)
  - Interpretable coefficients
  - Good for linear patterns
  - Probability calibration

#### Use Cases:
- Production deployment (speed)
- Baseline comparison
- When interpretability is crucial

#### Performance Metrics:
- Accuracy
- Precision, Recall, F1
- ROC-AUC curve
- Confusion Matrix

---

### 2. **Decision Tree Model**

#### Characteristics:
- **Type**: Non-linear classifier
- **Hyperparameters**:
  - max_depth=5
  - min_samples_leaf=10
  - random_state=42
- **Output**: Binary (0/1) + probabilities
- **Advantages**:
  - Captures non-linear patterns
  - Feature importance analysis
  - Rule-based interpretation
  - No feature scaling needed

#### Use Cases:
- Complex pattern recognition
- Feature importance analysis
- When non-linearity suspected

#### Performance Metrics:
- Same as Logistic Regression
- Plus: Feature importance scores

---

### 3. **Preprocessing Pipeline**

#### Feature Engineering:
```
Input → Encoding → Scaling → Model → Prediction
```

#### Steps:
1. **Label Encoding** (jenis_kelamin)
   - L → 0
   - P → 1

2. **Standard Scaling** (all numeric features)
   - Mean = 0
   - Std = 1
   - Formula: (x - μ) / σ

3. **Model Input**
   - Shape: (1, 8)
   - Features: 8 columns
   - Dtype: float64

---

## 📊 Visualization Features

### 1. **Gauge Chart**
```python
create_gauge_chart(probability, title)
```
- Library: Plotly
- Type: Indicator gauge
- Customization:
  - Color steps
  - Threshold line
  - Delta reference
  - Title & labels

### 2. **Bar Chart (Input)**
```python
create_feature_comparison(data)
```
- Shows: 4 rating features
- Colors: Multi-color palette
- Labels: Readable names
- Values: Displayed on bars

### 3. **Probability Distribution**
- Type: Bar chart
- Shows: P(Not Satisfied) vs P(Satisfied)
- Colors: Gradient (red vs purple)
- Interactive: Hover details

---

## 🎯 Advanced Features

### 1. **Session State Management**
```python
st.session_state.model
st.session_state.last_prediction
st.session_state.history
```
- Persistent data across reruns
- Model caching
- History tracking
- User preferences

### 2. **Caching System**
```python
@st.cache_resource
def load_model():
    # Cached for entire session
    pass

@st.cache_data
def load_data():
    # Cached with TTL
    pass
```
- Resource caching: Models
- Data caching: Preprocessing
- TTL: Configurable
- Invalidation: Automatic

### 3. **Error Handling**
- Try-catch blocks
- User-friendly messages
- Fallback mechanisms
- Logging (optional)

### 4. **Responsive Design**
- Mobile-friendly
- Column layout adaptation
- Font size scaling
- Touch-friendly controls

---

## 🔍 Interactive Elements

### 1. **Sliders**
- Real-time updates
- Value display
- Step controls
- Help tooltips

### 2. **Selectbox**
- Dropdown options
- Custom formatting
- Default values
- Clear labels

### 3. **Buttons**
- Primary button (Prediksi)
- Styled with type="primary"
- Full-width option
- Click feedback

### 4. **Expanders**
- Collapsible sections
- Clean interface
- Additional info
- Optional details

---

## 📈 Metrics & KPIs

### Displayed Metrics:
1. **Accuracy**: Overall correctness
2. **Precision**: Positive prediction accuracy
3. **Recall**: True positive detection rate
4. **F1-Score**: Harmonic mean
5. **Confidence**: Probability percentage
6. **Model Name**: Algorithm used
7. **Timestamp**: Prediction time

### Calculated Internally:
- Confusion Matrix (TP, FP, TN, FN)
- ROC-AUC score
- Feature importances
- Prediction probabilities

---

## 🎨 Styling & Theming

### Custom CSS:
- Gradient backgrounds
- Card-based layouts
- Shadow effects
- Border radius
- Color palette:
  - Primary: #1f77b4 (blue)
  - Secondary: #ff7f0e (orange)
  - Success: Purple gradient
  - Warning: Red gradient

### Typography:
- Main header: 2.5rem, bold
- Sub headers: 1.5rem
- Body text: Default
- Metrics: Large, bold

---

## 🔧 Configuration Options

### Streamlit Config:
```toml
[theme]
primaryColor = "#1f77b4"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"

[server]
port = 8501
headless = false
```

### Model Config:
- Threshold: 0.5 (adjustable)
- Probability output: 2 decimals
- Confidence display: 1 decimal

---

## 📱 Mobile Features

- Responsive columns
- Touch-friendly sliders
- Readable font sizes
- Collapsible sidebar
- Optimized images
- Fast loading

---

## 🆕 Future Features (Roadmap)

### Planned:
- [ ] Batch prediction (CSV upload)
- [ ] Export results to PDF/Excel
- [ ] Historical predictions tracking
- [ ] Model comparison side-by-side
- [ ] A/B testing capability
- [ ] Real-time retraining
- [ ] Multi-language support
- [ ] Dark mode toggle
- [ ] User authentication
- [ ] API endpoint

### Under Consideration:
- [ ] Feedback mechanism
- [ ] Model explainability (SHAP)
- [ ] Confidence intervals
- [ ] Ensemble predictions
- [ ] Time series analysis
- [ ] Recommendation system

---

## 📞 Feature Requests

To request new features:
1. Check existing roadmap
2. Verify feasibility
3. Describe use case
4. Provide mockups (if UI)
5. Submit request

---

**Dashboard Features v1.0**

Last updated: January 2025
