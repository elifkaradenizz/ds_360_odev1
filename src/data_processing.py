import pandas as pd
import os
from sklearn.preprocessing import LabelEncoder, StandardScaler

def clean_iris_data():
    input_path = r"data\raw_data\iris.csv"
    output_path = r"data\preprocessed_data\iris_clean.csv"

    # 1️⃣ Dosyanın varlığını kontrol et
    if not os.path.exists(input_path):
        print("❌ HATA: Input dosya bulunamadı:", input_path)
        return

    print("✅ Input dosya bulundu:", input_path)

    # 2️⃣ Veriyi yükle
    df = pd.read_csv(input_path)
    print("✅ Veri yüklendi. Boyut:", df.shape)

    # 3️⃣ Temizleme işlemleri
    df_clean = df.copy()

    # Eksik değer
    if df_clean.isnull().sum().sum() > 0:
        df_clean = df_clean.fillna(df_clean.mean())
        print("Eksik değerler dolduruldu")
    else:
        print("Eksik değer yok")

    # Hedef değişken encode
    df_clean['species_encoded'] = LabelEncoder().fit_transform(df_clean['species'])

    # Özellikleri scale
    feature_cols = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
    df_clean[feature_cols] = StandardScaler().fit_transform(df_clean[feature_cols])

    # 4️⃣ Çıktı klasörünü oluştur
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    print("✅ Çıktı klasörü hazır:", os.path.dirname(output_path))

    # 5️⃣ Dosyayı kaydet
    df_clean.to_csv(output_path, index=False)

    # 6️⃣ Kaydedilip kaydedilmediğini kontrol et
    if os.path.exists(output_path):
        print("✅ Dosya başarıyla kaydedildi:", output_path)
    else:
        print("❌ Dosya kaydedilemedi:", output_path)

    return df_clean

if __name__ == "__main__":
    clean_iris_data()

