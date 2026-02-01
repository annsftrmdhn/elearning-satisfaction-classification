import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import pickle
import warnings
warnings.filterwarnings('ignore')

print("="*60)
print("TRAINING MODEL PREDIKSI KEPUASAN E-LEARNING")
print("="*60)

# 1. Load Dataset
print("\n1. Loading dataset...")
try:
    df = pd.read_csv('dataset_kepuasan_pengguna_elearning.csv')
    print(f"   ✓ Dataset loaded: {df.shape[0]} rows, {df.shape[1]} columns")
except FileNotFoundError:
    print("   ✗ Error: File dataset_kepuasan_pengguna_elearning.csv tidak ditemukan!")
    print("   Silakan letakkan file dataset di direktori yang sama dengan script ini.")
    exit(1)

# 2. Data Preprocessing
print("\n2. Data Preprocessing...")

# Hapus kolom ID
if 'id_responden' in df.columns:
    df = df.drop(columns=['id_responden'])
    print("   ✓ Kolom 'id_responden' dihapus")

# Cek missing values
print(f"   - Missing values sebelum handling:")
missing_before = df.isnull().sum()
for col in missing_before[missing_before > 0].index:
    print(f"     • {col}: {missing_before[col]} ({missing_before[col]/len(df)*100:.1f}%)")

# Handle missing values dengan median untuk kolom numerik
numeric_cols = ['durasi_penggunaan', 'kualitas_materi', 'stabilitas_aplikasi']
for col in numeric_cols:
    if df[col].isnull().sum() > 0:
        median_val = df[col].median()
        df[col].fillna(median_val, inplace=True)
        print(f"   ✓ Missing values di '{col}' diisi dengan median: {median_val:.2f}")

# Hapus duplikasi
duplicates = df.duplicated().sum()
if duplicates > 0:
    df = df.drop_duplicates()
    print(f"   ✓ {duplicates} baris duplikat dihapus")

print(f"   ✓ Dataset final: {df.shape[0]} rows, {df.shape[1]} columns")

# 3. Encode Categorical Variables
print("\n3. Encoding categorical variables...")
label_encoder = LabelEncoder()
df['jenis_kelamin'] = label_encoder.fit_transform(df['jenis_kelamin'])
print(f"   ✓ Jenis kelamin encoded: {dict(zip(label_encoder.classes_, label_encoder.transform(label_encoder.classes_)))}")

# 4. Split Features and Target
print("\n4. Splitting features and target...")
X = df.drop(columns=['kepuasan_pengguna'])
y = df['kepuasan_pengguna']

# Pastikan urutan kolom konsisten
expected_cols = ['usia', 'jenis_kelamin', 'durasi_penggunaan', 'frekuensi_login', 
                 'kualitas_materi', 'kemudahan_penggunaan', 'stabilitas_aplikasi', 
                 'interaksi_pengajar']
X = X[expected_cols]

print(f"   ✓ Features (X): {X.shape}")
print(f"   ✓ Target (y): {y.shape}")
print(f"   ✓ Feature order: {list(X.columns)}")
print(f"   ✓ Distribusi target:")
print(f"     • Tidak Puas (0): {(y==0).sum()} ({(y==0).sum()/len(y)*100:.1f}%)")
print(f"     • Puas (1): {(y==1).sum()} ({(y==1).sum()/len(y)*100:.1f}%)")

# 5. Train-Test Split
print("\n5. Splitting train-test data...")
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
print(f"   ✓ Training set: {X_train.shape[0]} samples")
print(f"   ✓ Testing set: {X_test.shape[0]} samples")

# 6. Feature Scaling
print("\n6. Feature scaling...")
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
print("   ✓ Features scaled menggunakan StandardScaler")

# 7. Training Models
print("\n7. Training models...")
print("   " + "="*55)

# 7a. Logistic Regression
print("   A. LOGISTIC REGRESSION")
print("   " + "-"*55)
logreg = LogisticRegression(max_iter=1000, random_state=42)
logreg.fit(X_train_scaled, y_train)

y_pred_logreg = logreg.predict(X_test_scaled)
y_prob_logreg = logreg.predict_proba(X_test_scaled)

acc_logreg = accuracy_score(y_test, y_pred_logreg)
print(f"   ✓ Model trained")
print(f"   ✓ Accuracy: {acc_logreg*100:.2f}%")

print("\n   Classification Report:")
report_logreg = classification_report(y_test, y_pred_logreg, 
                                      target_names=['Tidak Puas', 'Puas'],
                                      output_dict=True)
print(f"     • Precision (Puas): {report_logreg['Puas']['precision']:.3f}")
print(f"     • Recall (Puas): {report_logreg['Puas']['recall']:.3f}")
print(f"     • F1-Score (Puas): {report_logreg['Puas']['f1-score']:.3f}")

# 7b. Decision Tree
print("\n   B. DECISION TREE")
print("   " + "-"*55)
dt = DecisionTreeClassifier(
    max_depth=5,
    min_samples_leaf=10,
    random_state=42
)
dt.fit(X_train_scaled, y_train)

y_pred_dt = dt.predict(X_test_scaled)
y_prob_dt = dt.predict_proba(X_test_scaled)

acc_dt = accuracy_score(y_test, y_pred_dt)
print(f"   ✓ Model trained")
print(f"   ✓ Accuracy: {acc_dt*100:.2f}%")

print("\n   Classification Report:")
report_dt = classification_report(y_test, y_pred_dt, 
                                  target_names=['Tidak Puas', 'Puas'],
                                  output_dict=True)
print(f"     • Precision (Puas): {report_dt['Puas']['precision']:.3f}")
print(f"     • Recall (Puas): {report_dt['Puas']['recall']:.3f}")
print(f"     • F1-Score (Puas): {report_dt['Puas']['f1-score']:.3f}")

print("\n   " + "="*55)

# 8. Confusion Matrix
print("\n8. Confusion Matrix:")
cm_logreg = confusion_matrix(y_test, y_pred_logreg)
cm_dt = confusion_matrix(y_test, y_pred_dt)

print("\n   Logistic Regression:")
print("   " + "-"*30)
print(f"   TN: {cm_logreg[0,0]:3d}  |  FP: {cm_logreg[0,1]:3d}")
print(f"   FN: {cm_logreg[1,0]:3d}  |  TP: {cm_logreg[1,1]:3d}")

print("\n   Decision Tree:")
print("   " + "-"*30)
print(f"   TN: {cm_dt[0,0]:3d}  |  FP: {cm_dt[0,1]:3d}")
print(f"   FN: {cm_dt[1,0]:3d}  |  TP: {cm_dt[1,1]:3d}")

# 9. Feature Importance (Decision Tree)
print("\n9. Feature Importance (Decision Tree):")
feature_importance = pd.DataFrame({
    'Feature': X.columns,
    'Importance': dt.feature_importances_
}).sort_values('Importance', ascending=False)

print("   " + "-"*40)
for idx, row in feature_importance.iterrows():
    print(f"   {row['Feature']:25s}: {row['Importance']:.4f}")

# 10. Save Models
print("\n10. Saving models...")
try:
    # Save models
    with open('logreg_model.pkl', 'wb') as file:
        pickle.dump(logreg, file)
    print("   ✓ logreg_model.pkl saved")
    
    with open('dt_model.pkl', 'wb') as file:
        pickle.dump(dt, file)
    print("   ✓ dt_model.pkl saved")
    
    # Save preprocessors
    with open('scaler.pkl', 'wb') as file:
        pickle.dump(scaler, file)
    print("   ✓ scaler.pkl saved")
    
    with open('label_encoder.pkl', 'wb') as file:
        pickle.dump(label_encoder, file)
    print("   ✓ label_encoder.pkl saved")
    
    print("\n   ✓ Semua model dan preprocessor berhasil disimpan!")
    
except Exception as e:
    print(f"\n   ✗ Error saat menyimpan model: {str(e)}")

# Summary
print("\n" + "="*60)
print("TRAINING SUMMARY")
print("="*60)
print(f"Dataset: {df.shape[0]} samples, {df.shape[1]} features")
print(f"Train/Test Split: {X_train.shape[0]}/{X_test.shape[0]}")
print(f"\nModel Performance:")
print(f"  • Logistic Regression - Accuracy: {acc_logreg*100:.2f}%")
print(f"  • Decision Tree       - Accuracy: {acc_dt*100:.2f}%")

if acc_logreg > acc_dt:
    print(f"\n✓ Logistic Regression memiliki performa terbaik!")
else:
    print(f"\n✓ Decision Tree memiliki performa terbaik!")

print("\n✓ Model siap digunakan untuk deployment!")
print("✓ Jalankan dashboard dengan: streamlit run app.py")
print("="*60)
