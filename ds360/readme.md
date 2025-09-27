# Iris Dataset DS360 Project

Bu proje, **Iris veri seti** üzerinde veri işleme ve makine öğrenimi sürecini kapsamlı bir şekilde gösterir. Proje üç ana aşamadan oluşur: veri indirme, veri ön işleme ve modelleme. Ayrıca DVC (Data Version Control) ile veri ve modellerin versiyonlanması planlanmaktadır.

---

## 📁 Proje Yapısı

iris_dataset_ds/
└─ ds360/
   ├─ data/
   │  ├─ raw_data/                  # Ham verilerin saklandığı klasör
   │  │  └─ iris.csv                # Ham dataset
   │  └─ preprocessed_data/         # İşlenmiş verilerin saklandığı klasör
   │     └─ iris_clean.csv          # Temizlenmiş dataset
   ├─ Include/                      # Include dosyaları
   ├─ Lib/                          # Kütüphane dosyaları
   ├─ Scripts/                      # Tüm Python scriptleri
   ├─ share/                        # Paylaşılan kaynaklar
   ├─ src/                          # Kaynak kod dosyaları
   ├─ pyvenv.cfg                    # Python virtual environment konfigürasyonu
   ├─ .gitignore                    # Git ignore dosyası
   ├─ dvc.yaml                      # DVC pipeline aşamalarını tutar
   ├─ requirements.txt              # Projede kullanılan paketler
   └─ README.md                     # Proje açıklamaları
---

## ⚙️ Kurulum

1. Python ortamı oluşturun ve aktif edin (opsiyonel ama önerilir):  


2. Gerekli paketleri yükleyin:  


**Gerekli paketler:**  
- pandas  
- numpy  
- scikit-learn  
- seaborn  
- matplotlib  

---

## 📝 Proje Aşamaları

### 1️⃣ Veri İndirme
- `download_iris_data.py` scripti, Seaborn kütüphanesinden Iris veri setini indirir.  
- Ham veri `ds360/data/raw_data/iris.csv` konumunda saklanır.  

### 2️⃣ Veri Ön İşleme
- `preprocess_iris_data.py` scripti:  
  - Eksik değerleri doldurur (gerektiğinde)  
  - Hedef değişkeni encode eder  
  - Özellikleri standardize eder  
- Temizlenmiş veri `ds360/data/preprocessed_data/iris_clean.csv` olarak kaydedilir.  

### 3️⃣ Modelleme
- `model_iris.py` scripti:  
  - Temizlenmiş veri ile RandomForest modeli eğitir  
  - Test setinde Accuracy, F1-score, Precision, Recall ve Confusion Matrix hesaplar  
  - Eğitilmiş modeli `ds360/models/iris_model.pkl` olarak kaydeder  

---

## 📊 Değerlendirme

- **Accuracy:** Modelin doğruluk oranı  
- **Classification Report:** Precision, Recall, F1-score  
- **Confusion Matrix:** Sınıflar arası tahmin hatalarını gösterir  
- **5-Fold Cross-Validation:** Modelin genel performansını ölçer  

---

## 🛠️ Gelecek Adımlar

- DVC pipeline entegrasyonu ile veri ve modellerin versiyonlanması  
- GitHub ile proje yönetimi ve paylaşımlı çalışma ortamı  

---

## 📌 Notlar

- Bu proje eğitim ve deneysel amaçlıdır.  
- Iris veri seti, küçük ve dengeli bir veri seti olduğu için model performansı genellikle çok yüksektir.
