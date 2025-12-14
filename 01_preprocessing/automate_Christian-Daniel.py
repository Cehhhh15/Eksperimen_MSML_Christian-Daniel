import pandas as pd
from sklearn.preprocessing import LabelEncoder
import os

def load_data(path):
    # Membaca data dari path yang diberikan
    if not os.path.exists(path):
        raise FileNotFoundError(f"File tidak ditemukan di: {path}")
    df = pd.read_csv(path)
    print(f"Data berhasil dimuat. Shape: {df.shape}")
    return df

def preprocessing_data(df):
    # Handle Missing Values
    if 'Sleep Disorder' in df.columns:
        df['Sleep Disorder'] = df['Sleep Disorder'].fillna('None')
    
    # Feature Engineering
    if 'Blood Pressure' in df.columns:
        print("   [INFO] Memecah kolom Blood Pressure...")
        df[['BP_Systolic', 'BP_Diastolic']] = df['Blood Pressure'].str.split('/', expand=True).astype(int)
        df = df.drop('Blood Pressure', axis=1)

    # Drop kolom tidak digunakan
    if 'Person ID' in df.columns:
        df = df.drop('Person ID', axis=1)

    # Encoding
    le = LabelEncoder()
    categorical_cols = ['Gender', 'Occupation', 'BMI Category', 'Sleep Disorder']
    
    for col in categorical_cols:
        if col in df.columns:
            df[col] = le.fit_transform(df[col])
            print(f"   [INFO] Kolom '{col}' berhasil di-encode.")
            
    return df

def save_data(df, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Data bersih berhasil disimpan di: {output_path}")

if __name__ == "__main__":
    input_path = "data_raw/Sleep_health_and_lifestyle_dataset.csv" 
    output_path = "01_preprocessing/data_clean/Sleep_health_clean.csv"
    
    if not os.path.exists(input_path):
        input_path = "../data_raw/Sleep_health_and_lifestyle_dataset.csv"
    
    print("Memulai Otomatisasi Preprocessing...")
    
    try:
        data = load_data(input_path)
        clean_data = preprocessing_data(data)
        save_data(clean_data, output_path)
        print("Selesai!")
    except Exception as e:
        print(f"Terjadi Error: {e}")