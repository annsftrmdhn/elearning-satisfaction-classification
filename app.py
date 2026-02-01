import streamlit as st
import pandas as pd
import numpy as np
import pickle
from datetime import datetime
import plotly.graph_objects as go
import plotly.express as px

# Konfigurasi halaman
st.set_page_config(
    page_title="E-Learning Satisfaction Analytics",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS untuk styling profesional
st.markdown("""
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Global Styles */
    * {
        font-family: 'Inter', sans-serif;
    }
    
    /* Navigation Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 2rem;
        background-color: #f5f5f5;
        padding: 1rem 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        padding: 0 2rem;
        background-color: transparent;
        border-radius: 8px;
        font-weight: 500;
        font-size: 1rem;
        color: #666;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: #2c3e50;
        color: white;
    }
    
    /* Main Header */
    .main-header {
        font-size: 2.2rem;
        font-weight: 600;
        color: #1a1a1a;
        text-align: center;
        padding: 2rem 0 1rem 0;
        letter-spacing: -0.5px;
        border-bottom: 2px solid #e0e0e0;
        margin-bottom: 2rem;
    }
    
    /* Sub Header */
    .sub-header {
        font-size: 1.3rem;
        font-weight: 500;
        color: #2c3e50;
        margin-top: 2rem;
        margin-bottom: 1rem;
        padding-bottom: 0.5rem;
        border-bottom: 1px solid #e0e0e0;
    }
    
    /* Dashboard Stats Card */
    .stat-card {
        background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%);
        color: white;
        padding: 2rem;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        text-align: center;
        transition: transform 0.3s ease;
            
        height: 180px;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    
    .stat-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 6px 12px rgba(0,0,0,0.15);
    }
    
    .stat-number {
        font-size: 2.5rem;
        font-weight: 700;
        margin: 0.5rem 0;
    }
    
    .stat-label {
        font-size: 0.9rem;
        opacity: 0.9;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    /* Insight Card */
    .insight-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #2c3e50;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        margin: 1rem 0;
    }
    
    .insight-title {
        font-weight: 600;
        color: #2c3e50;
        margin-bottom: 0.5rem;
    }
    
    .insight-text {
        color: #666;
        line-height: 1.6;
    }
    
    /* Prediction Box */
    .prediction-box {
        padding: 2.5rem;
        border-radius: 12px;
        text-align: center;
        font-size: 1.8rem;
        font-weight: 600;
        margin: 2rem 0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.07);
        letter-spacing: -0.3px;
    }
    
    .satisfied {
        background: #2c3e50;
        color: white;
        border-left: 5px solid #1a252f;
    }
    
    .not-satisfied {
        background: #95a5a6;
        color: white;
        border-left: 5px solid #7f8c8d;
    }
    
    /* Info Box */
    .info-box {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 8px;
        border-left: 4px solid #2c3e50;
        margin: 1.5rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    
    .info-box strong {
        color: #2c3e50;
        font-weight: 600;
    }
    
    /* Section Divider */
    .section-divider {
        height: 2px;
        background: #e0e0e0;
        margin: 2rem 0;
        border-radius: 2px;
    }
    
    /* Button Styling */
    .stButton>button {
        background: #2c3e50;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.7rem 2rem;
        font-weight: 500;
        letter-spacing: 0.3px;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    .stButton>button:hover {
        background: #34495e;
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(0,0,0,0.15);
    }
    
    /* Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# Fungsi untuk memuat model
@st.cache_resource
def load_model(model_name):
    """Memuat model yang sudah dilatih"""
    try:
        with open(f'{model_name}.pkl', 'rb') as file:
            model = pickle.load(file)
        return model
    except FileNotFoundError:
        st.error(f"Model {model_name} tidak ditemukan. Silakan jalankan train_model.py terlebih dahulu.")
        return None

# Fungsi untuk memuat scaler dan encoder
@st.cache_resource
def load_preprocessors():
    """Memuat scaler dan encoder"""
    try:
        with open('scaler.pkl', 'rb') as file:
            scaler = pickle.load(file)
        with open('label_encoder.pkl', 'rb') as file:
            label_encoder = pickle.load(file)
        return scaler, label_encoder
    except FileNotFoundError:
        st.warning("File preprocessor tidak ditemukan. Menggunakan preprocessing default.")
        return None, None

# Fungsi untuk preprocessing input
def preprocess_input(data, scaler=None, label_encoder=None):
    """Preprocessing data input sebelum prediksi"""
    df = pd.DataFrame([data])
    
    # Encode jenis kelamin SEBELUM scaling
    if label_encoder:
        df['jenis_kelamin'] = label_encoder.transform(df['jenis_kelamin'])
    else:
        df['jenis_kelamin'] = df['jenis_kelamin'].map({'L': 0, 'P': 1})
    
    # Pastikan urutan kolom sesuai dengan training
    # Urutan: usia, jenis_kelamin, durasi_penggunaan, frekuensi_login, 
    #         kualitas_materi, kemudahan_penggunaan, stabilitas_aplikasi, interaksi_pengajar
    expected_cols = ['usia', 'jenis_kelamin', 'durasi_penggunaan', 'frekuensi_login', 
                     'kualitas_materi', 'kemudahan_penggunaan', 'stabilitas_aplikasi', 
                     'interaksi_pengajar']
    
    df = df[expected_cols]
    
    # Scale semua fitur jika scaler tersedia
    if scaler:
        df_scaled = pd.DataFrame(
            scaler.transform(df),
            columns=expected_cols
        )
        return df_scaled
    
    return df

# Fungsi untuk membuat gauge chart
def create_gauge_chart(probability, title="Tingkat Kepercayaan"):
    """Membuat gauge chart untuk menampilkan probabilitas"""
    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=probability * 100,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': title, 'font': {'size': 24}},
        delta={'reference': 50, 'increasing': {'color': "green"}},
        gauge={
            'axis': {'range': [None, 100], 'tickwidth': 1, 'tickcolor': "darkblue"},
            'bar': {'color': "darkblue"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [0, 33], 'color': '#ffebee'},
                {'range': [33, 66], 'color': '#fff9c4'},
                {'range': [66, 100], 'color': '#e8f5e9'}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': 50
            }
        }
    ))
    
    fig.update_layout(
        height=300,
        margin=dict(l=20, r=20, t=50, b=20)
    )
    
    return fig

# Fungsi untuk membuat bar chart perbandingan fitur
def create_feature_comparison(data):
    """Membuat bar chart untuk perbandingan fitur input"""
    features = ['kualitas_materi', 'kemudahan_penggunaan', 
                'stabilitas_aplikasi', 'interaksi_pengajar']
    values = [data[f] for f in features]
    labels = ['Kualitas Materi', 'Kemudahan Penggunaan', 
              'Stabilitas Aplikasi', 'Interaksi Pengajar']
    
    fig = go.Figure(data=[
        go.Bar(
            x=labels,
            y=values,
            marker_color=['#2c3e50', '#34495e', '#7f8c8d', '#95a5a6'],
            text=values,
            textposition='auto',
        )
    ])
    
    fig.update_layout(
        title="Penilaian Platform (Skala 1-5)",
        xaxis_title="Kategori Penilaian",
        yaxis_title="Rating",
        yaxis=dict(range=[0, 5.5]),
        height=350,
        showlegend=False,
        font=dict(family="Inter, sans-serif")
    )
    
    return fig

# Fungsi interpretasi hasil
def interpret_prediction(prediction, probability, data):
    """Memberikan interpretasi hasil prediksi"""
    interpretation = []
    
    if prediction == 1:
        interpretation.append("**Prediksi: PENGGUNA PUAS**")
        interpretation.append(f"Tingkat keyakinan: **{probability*100:.1f}%**")
    else:
        interpretation.append("**Prediksi: PENGGUNA TIDAK PUAS**")
        interpretation.append(f"Tingkat keyakinan: **{(1-probability)*100:.1f}%**")
    
    # Analisis faktor
    interpretation.append("\n**Faktor-faktor Penting:**")
    
    if data['kualitas_materi'] >= 4:
        interpretation.append("- Kualitas materi dinilai baik oleh pengguna")
    elif data['kualitas_materi'] <= 2:
        interpretation.append("- Kualitas materi perlu ditingkatkan")
    
    if data['kemudahan_penggunaan'] >= 4:
        interpretation.append("- Platform mudah digunakan")
    elif data['kemudahan_penggunaan'] <= 2:
        interpretation.append("- Kemudahan penggunaan masih kurang optimal")
    
    if data['stabilitas_aplikasi'] >= 4:
        interpretation.append("- Stabilitas sistem berjalan dengan baik")
    elif data['stabilitas_aplikasi'] <= 2:
        interpretation.append("- Ditemukan masalah pada stabilitas sistem")
    
    if data['interaksi_pengajar'] >= 4:
        interpretation.append("- Interaksi dengan pengajar berlangsung baik")
    elif data['interaksi_pengajar'] <= 2:
        interpretation.append("- Perlu peningkatan dalam interaksi pengajar")
    
    if data['frekuensi_login'] >= 5:
        interpretation.append("- Pengguna aktif dengan frekuensi login tinggi")
    elif data['frekuensi_login'] <= 2:
        interpretation.append("- Frekuensi login relatif rendah")
    
    if data['durasi_penggunaan'] >= 4:
        interpretation.append("- Durasi penggunaan harian cukup tinggi")
    elif data['durasi_penggunaan'] <= 2:
        interpretation.append("- Durasi penggunaan masih terbatas")
    
    return "\n".join(interpretation)

# Header
st.markdown('<div class="main-header">Sistem Analisis Kepuasan Pengguna E-Learning</div>', 
            unsafe_allow_html=True)

# Navigation Tabs
tab1, tab2 = st.tabs(["Beranda", "Prediksi"])

# ==================== HOME DASHBOARD ====================
with tab1:
    st.markdown("## Ringkasan Kinerja Platform")
    
    # Top metrics row
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="stat-card">
            <div class="stat-label">Total Pengguna</div>
            <div class="stat-number">2.547</div>
            <div style="font-size: 0.85rem; margin-top: 0.5rem;">Naik 12% dari bulan lalu</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="stat-card">
            <div class="stat-label">Tingkat Kepuasan</div>
            <div class="stat-number">73%</div>
            <div style="font-size: 0.85rem; margin-top: 0.5rem;">Meningkat 5%</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="stat-card">
            <div class="stat-label">Rata-rata Penggunaan</div>
            <div class="stat-number">3,2 jam</div>
            <div style="font-size: 0.85rem; margin-top: 0.5rem;">Per hari</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="stat-card">
            <div class="stat-label">Sesi Aktif</div>
            <div class="stat-number">1.893</div>
            <div style="font-size: 0.85rem; margin-top: 0.5rem;">Saat ini online</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Main insights section
    col_left, col_right = st.columns([6, 4])
    
    with col_left:
        st.markdown("### Tren Kepuasan Pengguna")
        
        # Create trend chart
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun']
        satisfied = [65, 68, 71, 69, 72, 73]
        unsatisfied = [35, 32, 29, 31, 28, 27]
        
        fig_trend = go.Figure()
        fig_trend.add_trace(go.Scatter(
            x=months, y=satisfied,
            mode='lines+markers',
            name='Puas',
            line=dict(color='#2c3e50', width=3),
            marker=dict(size=8)
        ))
        fig_trend.add_trace(go.Scatter(
            x=months, y=unsatisfied,
            mode='lines+markers',
            name='Tidak Puas',
            line=dict(color='#95a5a6', width=3),
            marker=dict(size=8)
        ))
        
        fig_trend.update_layout(
            height=300,
            margin=dict(l=20, r=20, t=20, b=20),
            hovermode='x unified',
            showlegend=True,
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
            yaxis=dict(title="Persentase", range=[0, 100])
        )
        
        st.plotly_chart(fig_trend, use_container_width=True)
        
        # Platform ratings
        st.markdown("### Penilaian Platform")
        
        categories = ['Kualitas Materi', 'Kemudahan Penggunaan', 'Stabilitas Sistem', 'Dukungan Pengajar']
        ratings = [4.2, 4.0, 3.8, 4.1]
        
        fig_ratings = go.Figure(go.Bar(
            x=categories,
            y=ratings,
            marker_color=['#2c3e50', '#34495e', '#7f8c8d', '#95a5a6'],
            text=[f"{r}/5" for r in ratings],
            textposition='auto',
        ))
        
        fig_ratings.update_layout(
            height=300,
            margin=dict(l=20, r=20, t=20, b=20),
            yaxis=dict(range=[0, 5], title="Rating Rata-rata"),
            showlegend=False
        )
        
        st.plotly_chart(fig_ratings, use_container_width=True)
    
    with col_right:
        st.markdown("### Temuan Penting")
        
        st.markdown("""
        <div class="insight-card">
            <div class="insight-title">Tren Positif</div>
            <div class="insight-text">
                Tingkat kepuasan pengguna mengalami kenaikan sebesar 5% dalam tiga bulan terakhir. 
                Hal ini menunjukkan bahwa perbaikan yang dilakukan platform mulai memberikan dampak positif 
                pada pengalaman pengguna secara keseluruhan.
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="insight-card">
            <div class="insight-title">Area yang Perlu Perhatian</div>
            <div class="insight-text">
                Stabilitas sistem mendapat penilaian 3,8 dari 5, sedikit lebih rendah dibanding aspek lainnya. 
                Perlu dilakukan investigasi lebih lanjut terkait masalah teknis yang mungkin mempengaruhi 
                kenyamanan pengguna saat mengakses platform.
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="insight-card">
            <div class="insight-title">Tingkat Engagement</div>
            <div class="insight-text">
                Rata-rata penggunaan harian mencapai 3,2 jam, menandakan keterlibatan yang cukup baik. 
                Data menunjukkan bahwa pengguna yang menghabiskan waktu 4 jam atau lebih per hari 
                cenderung memiliki tingkat kepuasan hingga 90%.
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Bottom section - Distribution
    st.markdown("### Analisis Distribusi Pengguna")
    
    col_dist1, col_dist2 = st.columns(2)
    
    with col_dist1:
        # Age distribution
        age_groups = ['18-24', '25-29', '30-34', '35+']
        age_counts = [35, 42, 18, 5]
        
        fig_age = go.Figure(data=[go.Pie(
            labels=age_groups,
            values=age_counts,
            hole=.4,
            marker_colors=['#2c3e50', '#34495e', '#7f8c8d', '#95a5a6']
        )])
        
        fig_age.update_layout(
            title="Pengguna Berdasarkan Usia",
            height=300,
            margin=dict(l=20, r=20, t=40, b=20),
            showlegend=True
        )
        
        st.plotly_chart(fig_age, use_container_width=True)
    
    with col_dist2:
        # Usage frequency
        freq_labels = ['Setiap hari', '4-6x/minggu', '2-3x/minggu', '< 2x/minggu']
        freq_counts = [45, 30, 18, 7]
        
        fig_freq = go.Figure(data=[go.Pie(
            labels=freq_labels,
            values=freq_counts,
            hole=.4,
            marker_colors=['#2c3e50', '#34495e', '#7f8c8d', '#95a5a6']
        )])
        
        fig_freq.update_layout(
            title="Distribusi Frekuensi Login",
            height=300,
            margin=dict(l=20, r=20, t=40, b=20),
            showlegend=True
        )
        
        st.plotly_chart(fig_freq, use_container_width=True)
    
    # Summary box
    st.markdown("""
    <div class="info-box">
        <strong>Ringkasan:</strong> Platform menunjukkan pertumbuhan yang sehat dengan 2.547 pengguna aktif 
        dan tingkat kepuasan 73%. Kualitas materi dan dukungan pengajar mendapat penilaian baik, 
        sementara stabilitas sistem masih perlu ditingkatkan. Sebagian besar pengguna (75%) mengakses 
        platform minimal 4 kali per minggu, menunjukkan tingkat retensi yang kuat.
    </div>
    """, unsafe_allow_html=True)

# ==================== PREDICTION TOOL ====================
with tab2:
    
    # Sidebar untuk input
    st.sidebar.markdown("### Parameter Input")
    
    # Pilihan model
    model_choice = st.sidebar.selectbox(
        "Model:",
        ["Logistic Regression", "Decision Tree"]
    )
    
    st.sidebar.markdown("---")
    
    # Input demografis
    usia = st.sidebar.slider("Usia:", 18, 50, 25)
    jenis_kelamin = st.sidebar.selectbox(
        "Jenis Kelamin:",
        ["L", "P"],
        format_func=lambda x: "Laki-laki" if x == "L" else "Perempuan"
    )
    
    # Pola penggunaan
    durasi_penggunaan = st.sidebar.slider("Penggunaan Harian (jam):", 0.0, 8.0, 3.0, 0.5)
    frekuensi_login = st.sidebar.slider("Login per Minggu:", 1, 7, 4)
    
    # Penilaian
    kualitas_materi = st.sidebar.slider("Kualitas Materi:", 1, 5, 3)
    kemudahan_penggunaan = st.sidebar.slider("Kemudahan Penggunaan:", 1, 5, 3)
    stabilitas_aplikasi = st.sidebar.slider("Stabilitas Aplikasi:", 1, 5, 3)
    interaksi_pengajar = st.sidebar.slider("Interaksi Pengajar:", 1, 5, 3)
    
    # Tombol prediksi
    predict_button = st.sidebar.button("Prediksi", type="primary", use_container_width=True)
    
    # Main content
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### Ringkasan Input")
        
        input_data = {
            'usia': usia,
            'jenis_kelamin': jenis_kelamin,
            'durasi_penggunaan': durasi_penggunaan,
            'frekuensi_login': frekuensi_login,
            'kualitas_materi': kualitas_materi,
            'kemudahan_penggunaan': kemudahan_penggunaan,
            'stabilitas_aplikasi': stabilitas_aplikasi,
            'interaksi_pengajar': interaksi_pengajar
        }
        
        display_data = {
            'Parameter': [
                'Usia', 'Jenis Kelamin', 'Penggunaan Harian', 'Frekuensi Login',
                'Kualitas Materi', 'Kemudahan Penggunaan', 'Stabilitas', 'Interaksi Pengajar'
            ],
            'Nilai': [
                f"{usia} tahun",
                "Laki-laki" if jenis_kelamin == "L" else "Perempuan",
                f"{durasi_penggunaan} jam/hari",
                f"{frekuensi_login}x/minggu",
                f"{kualitas_materi}/5",
                f"{kemudahan_penggunaan}/5",
                f"{stabilitas_aplikasi}/5",
                f"{interaksi_pengajar}/5"
            ]
        }
        
        st.dataframe(
            pd.DataFrame(display_data),
            hide_index=True,
            use_container_width=True
        )
        
        # Visualisasi fitur penilaian
        st.plotly_chart(create_feature_comparison(input_data), use_container_width=True)
    
    with col2:
        st.markdown("### Hasil Prediksi")
        
        if predict_button:
            model_file = 'logreg_model' if model_choice == "Logistic Regression" else 'dt_model'
            model = load_model(model_file)
            scaler, label_encoder = load_preprocessors()
            
            if model is not None:
                X = preprocess_input(input_data, scaler, label_encoder)
                
                try:
                    prediction = model.predict(X)[0]
                    probability = model.predict_proba(X)[0]
                    
                    # Result box
                    if prediction == 1:
                        st.markdown(
                            '<div class="prediction-box satisfied">PUAS</div>',
                            unsafe_allow_html=True
                        )
                    else:
                        st.markdown(
                            '<div class="prediction-box not-satisfied">TIDAK PUAS</div>',
                            unsafe_allow_html=True
                        )
                    
                    # Gauge chart
                    prob_satisfied = probability[1]
                    st.plotly_chart(
                        create_gauge_chart(prob_satisfied, "Tingkat Keyakinan"),
                        use_container_width=True
                    )
                    
                    # Analysis
                    st.markdown("**Analisis Faktor:**")
                    interpretation = interpret_prediction(prediction, prob_satisfied, input_data)
                    st.markdown(interpretation)
                    
                    # Metrics
                    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
                    col_a, col_b = st.columns(2)
                    with col_a:
                        st.metric("Model", model_choice.split()[0])
                    with col_b:
                        st.metric("Waktu", datetime.now().strftime("%H:%M"))
                    
                    # Details
                    with st.expander("Detail Probabilitas"):
                        prob_df = pd.DataFrame({
                            'Kategori': ['Tidak Puas', 'Puas'],
                            'Probabilitas': [f"{probability[0]*100:.1f}%", f"{probability[1]*100:.1f}%"]
                        })
                        st.dataframe(prob_df, hide_index=True, use_container_width=True)
                    
                except Exception as e:
                    st.error(f"Terjadi kesalahan: {str(e)}")
            else:
                st.warning("Model belum tersedia. Jalankan train_model.py terlebih dahulu.")
        else:
            st.info("Atur parameter di sidebar lalu klik tombol Prediksi.")
            st.image("https://via.placeholder.com/500x300/2c3e50/ffffff?text=Hasil+Prediksi", 
                    use_container_width=True)

# Footer
st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
st.markdown("""
<div style='text-align: center; color: #7f8c8d; padding: 1.5rem;'>
    <p style='margin: 0; font-size: 0.85rem;'>Sistem Analisis Kepuasan Pengguna E-Learning</p>
</div>
""", unsafe_allow_html=True)