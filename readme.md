# Iris Dataset DS360 Project

Bu proje, **Iris veri seti** üzerinde veri işleme ve makine öğrenimi sürecini kapsamlı bir şekilde gösterir. Proje üç ana aşamadan oluşur: veri indirme, veri ön işleme ve modelleme. Ayrıca DVC (Data Version Control) ile veri ve modellerin versiyonlanması planlanmaktadır.

---

## 📁 Proje Yapısı

```
IRIS_DATASET_DS/  
├─ data/  
│  ├─ raw_data/                  # Ham verilerin saklandığı klasör  
│  │  └─ iris.csv                # ham veri seti
│  └─ preprocessed_data/         # Temizlenmiş/veri işlenmiş klasör  
│     └─ iris_clean.csv          # Önişleme sonrası veri  
├─ models/                       # Eğitilmiş modeller ve metrikler  
│  ├─ .gitignore                 # Git ile izlenmeyecek dosyalar  
│  ├─ features.json              # Kullanılan özellikler listesi  
│  ├─ metrics.json               # Modelin değerlendirme metrikleri  
│  └─ random_forest_iris_model.pkl # Eğitilmiş RandomForest modeli  
├─ src/                           # Python kodları  
│  ├─ download_iris.py            # iris datasetini indirme
│  ├─ data_processing.py          # veri ön işleme adımı
│  └─ modelling.py                # modelleme adımı
├─ .dvc/                          # DVC yapılandırması
├─ .dvcignore                     # DVC ignore dosyası
├─ dvc.lock                       # DVC lock dosyası
├─ dvc.yaml                       # DVC pipeline
├─ requirements.txt               # Projede kullanılan paketler  
└─ README.md                      # Proje dokümantasyonu

```

---

## ⚙️ Kurulum

1. Python ortamı oluşturun ve aktif edin (opsiyonel ama önerilir):  
```bash
python -m venv ds360
source ds360/bin/activate  # macOS/Linux
ds360\Scripts\activate     # Windows
```

2. Gerekli paketleri yükleyin:

```
pip install -r requirements.txt

```

**Gerekli paketler:**  
- pandas  
- numpy  
- scikit-learn  
- seaborn  
- matplotlib  

---

## 📝 Proje Aşamaları

### 1️⃣ Veri İndirme
- `download_iris.py` scripti, Seaborn kütüphanesinden Iris veri setini indirir.  
- Ham veri `data/raw_data/iris.csv` konumunda saklanır.  

### 2️⃣ Veri Ön İşleme
- `data_processing.py` scripti:  
  - Eksik değerleri doldurur (gerektiğinde)  
  - Hedef değişkeni encode eder  
  - Özellikleri standardize eder  
- Temizlenmiş veri `data/preprocessed_data/iris_clean.csv` olarak kaydedilir.  

### 3️⃣ Modelleme
- `modelling.py` scripti:  
  - Temizlenmiş veri ile RandomForest modeli eğitir  
  - Test setinde Accuracy, Cross-Validation ve Confusion Matrix hesaplar  
  - Eğitilmiş modeli `models/iris_model.pkl` olarak kaydeder  

### DVC ile Versiyonlama ve Pipeline

#### Modeli DVC ile eklemek

1. Eğitilmiş RandomForest modelini DVC ile ekleyin:  
   - `dvc add models/random_forest_iris_model.pkl`  
   - `git add models/random_forest_iris_model.pkl.dvc`  
   - `git commit -m "Add trained RandomForest model to DVC"`


#### DVC Pipeline Oluşturmak

Projeyi baştan sona çalıştırmak için DVC pipeline oluşturabilirsiniz:

1. **data_preparation**: Veri indirme ve temizleme  
2. **train_model**: Modeli eğit ve kaydet  

**Pipeline’ı çalıştırmak için:**  
```
dvc repro
```

**Değişiklikleri görmek için:**  
```
dvc status
```

**Remote’a göndermek için:**  
```
dvc push
```


---

## 📊 Değerlendirme

- **Accuracy:** Modelin doğruluk oranı  
- **Confusion Matrix:** Sınıflar arası tahmin hatalarını gösterir  
- **5-Fold Cross-Validation:** Modelin genel performansını ölçer  

---

🔄 Not: Bu proje, hem makine öğrenimi adımlarını hem de DVC ile veri ve model yönetimini öğrenmek için tasarlanmıştır. Ödevde DVC kullanarak veriyi ve modeli versionlamak temel amaçtır.