import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Dashboard Data Mining Jantung", layout="wide")

st.title("📊 Dashboard Analisis Data Pasien Penyakit Jantung")
st.write("Aplikasi ini menampilkan ringkasan data hasil praktikum Data Mining.")

@st.cache_data
def load_data():
    return pd.read_csv('Data Pasien Penyakit Jantung.csv')

try:
    df = load_data()
    
    st.subheader("📋 5 Data Pertama")
    st.dataframe(df.head())
    
    st.subheader("ℹ️ Informasi Dataset")
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"**Total Baris:** {df.shape[0]}")
        st.write(f"**Total Kolom:** {df.shape[1]}")
    with col2:
        st.write(f"**Data Kosong:** {df.isnull().sum().sum()} kolom kosong")
        st.write(f"**Data Duplikat:** {df.duplicated().sum()} baris")

    st.subheader("🔥 Heatmap Korelasi Fitur")
    numeric_df = df.select_dtypes(include=['float64', 'int64'])
    if not numeric_df.empty:
        fig, ax = plt.subplots(figsize=(10, 8))
        sns.heatmap(numeric_df.corr(), annot=True, fmt=".2f", cmap='RdYlGn', ax=ax)
        st.pyplot(fig)
    else:
        st.write("Tidak ada kolom numerik untuk korelasi.")

except Exception as e:
    st.error(f"Gagal memuat dataset: {e}")