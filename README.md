# Analisis Sentimen Ulasan Aplikasi Shopee

Proyek ini bertujuan untuk melakukan analisis sentimen terhadap ulasan pengguna aplikasi Shopee di Google Play Store. Data diambil melalui teknik *web scraping* dan diklasifikasikan ke dalam tiga kategori sentimen: **Positif**, **Netral**, dan **Negatif** menggunakan berbagai pendekatan *Machine Learning* dan *Deep Learning*.

## 📌 Ringkasan Proyek
Alur kerja proyek ini meliputi:
1.  **Scraping Data**: Mengambil ulasan terbaru dari Google Play Store menggunakan pustaka `google-play-scraper`.
2.  **Preprocessing**: Meliputi pembersihan teks (*cleaning*), penyeragaman huruf (*case folding*), normalisasi kata gaul (*slangword*) menggunakan dataset eksternal, dan deteksi bahasa.
3.  **Labeling**: Pemberian label sentimen otomatis menggunakan model *pretrained* **IndoBERT** (`indonesian-roberta-base-sentiment-classifier`).
4.  **Feature Extraction**: Menggunakan teknik **TF-IDF** dan **Word2Vec**.
5.  **Modeling**: Implementasi model Naive Bayes, Random Forest, XGBoost, dan GRU (*Gated Recurrent Unit*).

## 📊 Hasil Metrik
Berdasarkan eksperimen pada dataset ulasan (pembagian data 80:20), berikut adalah hasil akurasi model yang diuji:

| Model | Ekstraksi Fitur | Akurasi |
| :--- | :--- | :--- |
| **XGBoost** | TF-IDF | **88.27%** |
| **Random Forest** | TF-IDF | 85.18% |
| **Multinomial Naive Bayes** | TF-IDF (+ SMOTE) | 84.58% |
| **Gaussian Naive Bayes** | Word2Vec | 69.06% |

*Catatan: Model XGBoost memberikan performa terbaik dalam mengklasifikasikan sentimen pengguna.*

## ⚙️ Instruksi Instalasi
Pastikan Anda telah menginstal Python 3.10 ke atas. Ikuti langkah berikut untuk menyiapkan lingkungan kerja:

1.  **Clone Repositori**:
    ```bash
    git clone https://github.com/username/analisis-sentimen-shopee.git
    cd analisis-sentimen-shopee
    ```

2.  **Instal Dependensi**:
    Gunakan file `requirements.txt` untuk menginstal semua pustaka yang diperlukan:
    ```bash
    pip install -r requirements.txt
    ```
    *Dependensi utama meliputi: `pandas`, `scikit-learn`, `torch`, `transformers`, `nltk`, `google-play-scraper`, dan `xgboost`*.

## 🚀 Cara Menjalankan Pipeline
Proyek ini terdiri dari beberapa tahap yang dapat dijalankan secara berurutan:

1.  **Scraping Data**:
    Jalankan skrip untuk mengambil data ulasan terbaru dari Play Store:
    ```bash
    python "kode scraping .py"
    ```
    Skrip ini akan menghasilkan file `scrapreview-ml.csv` berisi 10.020 ulasan.

2.  **Preprocessing & Pelatihan Model**:
    Gunakan Jupyter Notebook atau Google Colab untuk menjalankan seluruh alur dari pembersihan data hingga evaluasi model:
    * Buka file `pelatihan model.ipynb`.
    * Pastikan file `scrapreview-ml.csv` berada di direktori yang sama.
    * Jalankan sel secara berurutan untuk melihat proses EDA, *cleaning*, *labeling* dengan IndoBERT, hingga pelatihan berbagai model klasifikasi.

---
