#!/bin/bash

# Script untuk menjalankan Dashboard E-Learning
# Author: AI Assistant
# Date: 2025

echo "=========================================="
echo "  Dashboard E-Learning - Setup & Run"
echo "=========================================="
echo ""

# Function untuk check apakah command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Check Python
if ! command_exists python3; then
    echo "❌ Error: Python3 tidak ditemukan!"
    echo "   Silakan install Python3 terlebih dahulu."
    exit 1
fi

echo "✓ Python3 found: $(python3 --version)"

# Check pip
if ! command_exists pip3; then
    echo "❌ Error: pip3 tidak ditemukan!"
    echo "   Silakan install pip3 terlebih dahulu."
    exit 1
fi

echo "✓ pip3 found"
echo ""

# Menu
echo "Pilih opsi:"
echo "1. Install dependencies"
echo "2. Generate dummy dataset"
echo "3. Train model"
echo "4. Run dashboard"
echo "5. Full setup (1+2+3+4)"
echo ""
read -p "Pilihan Anda (1-5): " choice

case $choice in
    1)
        echo ""
        echo "Installing dependencies..."
        pip3 install -r requirements.txt
        echo "✓ Dependencies installed!"
        ;;
    2)
        echo ""
        echo "Generating dummy dataset..."
        python3 generate_dummy_data.py
        echo "✓ Dataset generated!"
        ;;
    3)
        echo ""
        echo "Training models..."
        python3 train_model.py
        echo "✓ Models trained!"
        ;;
    4)
        echo ""
        echo "Starting dashboard..."
        echo "Dashboard akan terbuka di http://localhost:8501"
        echo "Tekan Ctrl+C untuk stop"
        echo ""
        streamlit run app.py
        ;;
    5)
        echo ""
        echo "=== FULL SETUP ==="
        echo ""
        
        echo "Step 1: Installing dependencies..."
        pip3 install -r requirements.txt
        echo "✓ Dependencies installed!"
        echo ""
        
        echo "Step 2: Checking dataset..."
        if [ -f "dataset_kepuasan_pengguna_elearning.csv" ]; then
            echo "✓ Dataset found!"
        else
            echo "⚠ Dataset not found. Generating dummy data..."
            python3 generate_dummy_data.py
            echo "✓ Dummy dataset generated!"
        fi
        echo ""
        
        echo "Step 3: Training models..."
        python3 train_model.py
        echo "✓ Models trained!"
        echo ""
        
        echo "Step 4: Starting dashboard..."
        echo "Dashboard akan terbuka di http://localhost:8501"
        echo "Tekan Ctrl+C untuk stop"
        echo ""
        streamlit run app.py
        ;;
    *)
        echo "❌ Pilihan tidak valid!"
        exit 1
        ;;
esac

echo ""
echo "=========================================="
echo "  Selesai!"
echo "=========================================="
