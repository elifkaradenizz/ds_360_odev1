import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
import joblib
import json
import os

def train_iris_model(model_type='random_forest',
                     input_path=r'C:\Users\karad\Desktop\iris_dataset_ds\ds360\data\preprocessed_data\iris_clean.csv',
                     output_dir=r'C:\Users\karad\Desktop\iris_dataset_ds\ds360\models'):
    """Iris veri seti üzerinde model eğit, kaydet ve metrikleri JSON olarak sakla"""
    
    # Veri yükleme
    if not os.path.exists(input_path):
        print("❌ HATA: Veri bulunamadı:", input_path)
        return
    df = pd.read_csv(input_path)
    print("✅ Veri yüklendi. Boyut:", df.shape)
    
    # Feature ve target
    feature_cols = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
    X = df[feature_cols]
    y = df['species_encoded']
    
    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    # Model seçimi
    if model_type == 'random_forest':
        model = RandomForestClassifier(n_estimators=100, random_state=42)
    else:
        raise ValueError("Şu an sadece 'random_forest' destekleniyor.")
    
    # Modeli eğit
    model.fit(X_train, y_train)
    
    # Tahminler
    y_pred = model.predict(X_test)
    
    # Accuracy
    accuracy = accuracy_score(y_test, y_pred)
    
    # Cross-validation
    cv_scores = cross_val_score(model, X, y, cv=5)
    
    # Confusion matrix
    cm = confusion_matrix(y_test, y_pred)
    
    # Confusion matrix görselleştirme
    plt.figure(figsize=(6,5))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
                xticklabels=df['species'].unique(),
                yticklabels=df['species'].unique())
    plt.xlabel("Tahmin Edilen")
    plt.ylabel("Gerçek")
    plt.title("Confusion Matrix")
    plt.show()
    
    # Klasör oluştur ve modeli kaydet
    os.makedirs(output_dir, exist_ok=True)
    model_path = os.path.join(output_dir, f"{model_type}_iris_model.pkl")
    joblib.dump(model, model_path)
    
    # Metrikleri kaydet
    metrics = {
        'model_type': model_type,
        'accuracy': float(accuracy),
        'cv_mean': float(cv_scores.mean()),
        'cv_std': float(cv_scores.std()),
        'n_features': len(feature_cols),
        'n_train_samples': len(X_train),
        'n_test_samples': len(X_test)
    }
    
    with open(os.path.join(output_dir, 'metrics.json'), 'w') as f:
        json.dump(metrics, f, indent=2)
    
    # Özellik listesini kaydet
    with open(os.path.join(output_dir, 'features.json'), 'w') as f:
        json.dump(feature_cols, f, indent=2)
    
    print(f"✅ Model eğitildi: {model_type}")
    print(f"📊 Test Accuracy: {accuracy:.4f}")
    print(f"📊 5-Fold CV Accuracy: {cv_scores.mean():.4f} ± {cv_scores.std():.4f}")
    print(f"💾 Model kaydedildi: {model_path}")
    
    return model, metrics

if __name__ == "__main__":
    model, metrics = train_iris_model()
    print("\n🎯 Model eğitildi ve kaydedildi!")
