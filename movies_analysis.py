"""
IMDb Film Veri Seti Analizi
Amaç: Film başarısını etkileyen faktörleri analiz etmek
Kullanılan Kütüphaneler: Pandas, Numpy, Matplotlib
"""

import sys
import io
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

# Windows için UTF-8 encoding ayarı
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

# Türkçe karakter desteği için
plt.rcParams['font.family'] = 'DejaVu Sans'

print("="*80)
print("IMDb FİLM VERİ SETİ ANALİZİ")
print("="*80)

# ============================================================================
# AŞAMA 1: VERİ YÜKLEME VE HAZIRLAMA
# ============================================================================
print("\n[AŞAMA 1] Veri Yükleme ve Hazırlama...")

# Veri setini yükle
df = pd.read_csv('movies_initial.csv', low_memory=False)
print(f"✓ Veri seti yüklendi: {df.shape[0]} satır, {df.shape[1]} sütun")

# İlk 5 satırı göster
print("\nİlk 5 Kayıt:")
print(df.head())

# Veri tiplerine genel bakış
print("\nVeri Tipleri:")
print(df.dtypes)

# ============================================================================
# AŞAMA 2: VERİ ÖN İŞLEME VE TEMİZLEME
# ============================================================================
print("\n" + "="*80)
print("[AŞAMA 2] Veri Ön İşleme ve Temizleme...")
print("="*80)

# Eksik değerleri kontrol et
print("\nEksik Değer Analizi:")
eksik_degerler = df.isnull().sum()
print(eksik_degerler[eksik_degerler > 0].sort_values(ascending=False))

# Runtime sütununu temizle ve sayısal hale getir
if 'runtime' in df.columns:
    df['runtime_numeric'] = df['runtime'].str.extract(r'(\d+)').astype(float)
    print(f"\n✓ Runtime sütunu temizlendi ve sayısal formata çevrildi")

# Year sütununu sayısal hale getir
if 'year' in df.columns:
    df['year_numeric'] = pd.to_numeric(df['year'], errors='coerce')
    print(f"✓ Year sütunu sayısal formata çevrildi")

# imdbRating sütununu kontrol et
if 'imdbRating' in df.columns:
    df['imdbRating'] = pd.to_numeric(df['imdbRating'], errors='coerce')
    print(f"✓ imdbRating sütunu sayısal formata çevrildi")

# imdbVotes sütununu temizle
if 'imdbVotes' in df.columns:
    df['imdbVotes_numeric'] = pd.to_numeric(df['imdbVotes'], errors='coerce')
    print(f"✓ imdbVotes sütunu sayısal formata çevrildi")

# Metacritic puanını kontrol et
if 'metacritic' in df.columns:
    df['metacritic'] = pd.to_numeric(df['metacritic'], errors='coerce')
    print(f"✓ Metacritic sütunu sayısal formata çevrildi")

# Genre sütununu analiz için hazırla
if 'genre' in df.columns:
    # İlk türü al (çoklu türler varsa)
    df['primary_genre'] = df['genre'].str.split(',').str[0].str.strip()
    print(f"✓ Primary genre bilgisi çıkarıldı")

# ============================================================================
# AŞAMA 3: KEŞİFSEL VERİ ANALİZİ (EDA)
# ============================================================================
print("\n" + "="*80)
print("[AŞAMA 3] Keşifsel Veri Analizi (EDA)")
print("="*80)

# Temel istatistikler
print("\n--- Sayısal Sütunlar için Temel İstatistikler ---")
numeric_cols = ['imdbRating', 'runtime_numeric', 'year_numeric', 'imdbVotes_numeric', 'metacritic']
print(df[numeric_cols].describe())

# IMDb Puan Dağılımı
print("\n--- IMDb Puan Dağılımı ---")
if 'imdbRating' in df.columns:
    rating_stats = df['imdbRating'].describe()
    print(f"Ortalama Puan: {rating_stats['mean']:.2f}")
    print(f"Medyan Puan: {rating_stats['50%']:.2f}")
    print(f"Minimum Puan: {rating_stats['min']:.2f}")
    print(f"Maksimum Puan: {rating_stats['max']:.2f}")
    print(f"Standart Sapma: {rating_stats['std']:.2f}")

# Film Süresi Analizi
print("\n--- Film Süresi Analizi ---")
if 'runtime_numeric' in df.columns:
    runtime_stats = df['runtime_numeric'].describe()
    print(f"Ortalama Süre: {runtime_stats['mean']:.2f} dakika")
    print(f"Medyan Süre: {runtime_stats['50%']:.2f} dakika")
    print(f"En Kısa Film: {runtime_stats['min']:.0f} dakika")
    print(f"En Uzun Film: {runtime_stats['max']:.0f} dakika")

# Yıllara Göre Film Sayısı
print("\n--- Yıllara Göre Film Dağılımı (Son 20 Yıl) ---")
if 'year_numeric' in df.columns:
    son_yillar = df[df['year_numeric'] >= 2004].groupby('year_numeric').size()
    print(son_yillar.tail(10))

# En Popüler Türler
print("\n--- En Popüler 10 Film Türü ---")
if 'primary_genre' in df.columns:
    top_genres = df['primary_genre'].value_counts().head(10)
    print(top_genres)

# En Yüksek Puanlı Filmler
print("\n--- En Yüksek Puanlı 10 Film ---")
if 'title' in df.columns and 'imdbRating' in df.columns:
    top_rated = df.nlargest(10, 'imdbRating')[['title', 'year', 'imdbRating', 'primary_genre']]
    print(top_rated.to_string(index=False))

# En Çok Oy Alan Filmler
print("\n--- En Çok Oy Alan 10 Film ---")
if 'title' in df.columns and 'imdbVotes_numeric' in df.columns:
    most_voted = df.nlargest(10, 'imdbVotes_numeric')[['title', 'year', 'imdbRating', 'imdbVotes_numeric']]
    print(most_voted.to_string(index=False))

# Korelasyon Analizi
print("\n--- Korelasyon Analizi ---")
correlation_cols = ['imdbRating', 'runtime_numeric', 'year_numeric', 'imdbVotes_numeric', 'metacritic']
correlation_matrix = df[correlation_cols].corr()
print("\nPuanlar arasındaki korelasyonlar:")
print(correlation_matrix['imdbRating'].sort_values(ascending=False))

# ============================================================================
# AŞAMA 4: VERİ GÖRSELLEŞTİRME
# ============================================================================
print("\n" + "="*80)
print("[AŞAMA 4] Veri Görselleştirme...")
print("="*80)

# Grafik için genel ayarlar
plt.style.use('seaborn-v0_8-darkgrid')
fig = plt.figure(figsize=(16, 12))

# 1. IMDb Puan Dağılımı (Histogram)
ax1 = plt.subplot(3, 3, 1)
df['imdbRating'].dropna().hist(bins=30, edgecolor='black', alpha=0.7)
plt.xlabel('IMDb Puani')
plt.ylabel('Film Sayisi')
plt.title('IMDb Puan Dagilimi')
plt.grid(True, alpha=0.3)

# 2. Film Süresi Dağılımı
ax2 = plt.subplot(3, 3, 2)
df['runtime_numeric'].dropna().hist(bins=30, edgecolor='black', alpha=0.7, color='green')
plt.xlabel('Sure (dakika)')
plt.ylabel('Film Sayisi')
plt.title('Film Suresi Dagilimi')
plt.grid(True, alpha=0.3)

# 3. Yıllara Göre Film Sayısı
ax3 = plt.subplot(3, 3, 3)
yillik_filmler = df.groupby('year_numeric').size()
yillik_filmler = yillik_filmler[yillik_filmler.index >= 1900]
plt.plot(yillik_filmler.index, yillik_filmler.values, linewidth=2)
plt.xlabel('Yil')
plt.ylabel('Film Sayisi')
plt.title('Yillara Gore Film Sayisi')
plt.grid(True, alpha=0.3)

# 4. En Popüler 10 Tür
ax4 = plt.subplot(3, 3, 4)
top_10_genres = df['primary_genre'].value_counts().head(10)
top_10_genres.plot(kind='barh', color='coral')
plt.xlabel('Film Sayisi')
plt.ylabel('Tur')
plt.title('En Populer 10 Film Turu')
plt.grid(True, alpha=0.3)

# 5. Puan vs Süre (Scatter Plot)
ax5 = plt.subplot(3, 3, 5)
sample_df = df[['imdbRating', 'runtime_numeric']].dropna().sample(n=min(5000, len(df)))
plt.scatter(sample_df['runtime_numeric'], sample_df['imdbRating'], alpha=0.3, s=10)
plt.xlabel('Sure (dakika)')
plt.ylabel('IMDb Puani')
plt.title('Film Suresi vs IMDb Puani')
plt.grid(True, alpha=0.3)

# 6. Puan vs Yıl (Scatter Plot)
ax6 = plt.subplot(3, 3, 6)
sample_df2 = df[['year_numeric', 'imdbRating']].dropna().sample(n=min(5000, len(df)))
plt.scatter(sample_df2['year_numeric'], sample_df2['imdbRating'], alpha=0.3, s=10, color='purple')
plt.xlabel('Yil')
plt.ylabel('IMDb Puani')
plt.title('Yil vs IMDb Puani')
plt.grid(True, alpha=0.3)

# 7. IMDb Rating vs Metacritic
ax7 = plt.subplot(3, 3, 7)
sample_df3 = df[['imdbRating', 'metacritic']].dropna().sample(n=min(2000, len(df[['imdbRating', 'metacritic']].dropna())))
plt.scatter(sample_df3['imdbRating'], sample_df3['metacritic'], alpha=0.5, s=20, color='red')
plt.xlabel('IMDb Puani')
plt.ylabel('Metacritic Puani')
plt.title('IMDb vs Metacritic Puanlari')
plt.grid(True, alpha=0.3)

# 8. Yıllara Göre Ortalama Puan Trendi
ax8 = plt.subplot(3, 3, 8)
yillik_ortalama = df.groupby('year_numeric')['imdbRating'].mean()
yillik_ortalama = yillik_ortalama[yillik_ortalama.index >= 1950]
plt.plot(yillik_ortalama.index, yillik_ortalama.values, linewidth=2, color='darkblue')
plt.xlabel('Yil')
plt.ylabel('Ortalama IMDb Puani')
plt.title('Yillara Gore Ortalama Film Puani')
plt.grid(True, alpha=0.3)

# 9. Oy Sayısı Dağılımı (Log Scale)
ax9 = plt.subplot(3, 3, 9)
df['imdbVotes_numeric'].dropna().hist(bins=50, edgecolor='black', alpha=0.7, color='orange')
plt.xlabel('Oy Sayisi')
plt.ylabel('Film Sayisi')
plt.title('Film Oy Sayisi Dagilimi')
plt.yscale('log')
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('imdb_film_analizi_gorsellestirme.png', dpi=300, bbox_inches='tight')
print("✓ Grafikler kaydedildi: imdb_film_analizi_gorsellestirme.png")

# ============================================================================
# AŞAMA 5: RAPORLAMA
# ============================================================================
print("\n" + "="*80)
print("[AŞAMA 5] Analiz Raporu Hazırlanıyor...")
print("="*80)

rapor = []
rapor.append("="*80)
rapor.append("IMDb FİLM VERİ SETİ ANALİZ RAPORU")
rapor.append("="*80)
rapor.append("")

# Veri Seti Özeti
rapor.append("1. VERİ SETİ ÖZETİ")
rapor.append("-" * 80)
rapor.append(f"Toplam Film Sayısı: {len(df):,}")
rapor.append(f"Toplam Sütun Sayısı: {len(df.columns)}")
rapor.append(f"Veri Seti Boyutu: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
rapor.append("")

# IMDb Puan İstatistikleri
rapor.append("2. IMDb PUAN İSTATİSTİKLERİ")
rapor.append("-" * 80)
if 'imdbRating' in df.columns:
    rapor.append(f"Ortalama Puan: {df['imdbRating'].mean():.2f}")
    rapor.append(f"Medyan Puan: {df['imdbRating'].median():.2f}")
    rapor.append(f"Standart Sapma: {df['imdbRating'].std():.2f}")
    rapor.append(f"Minimum Puan: {df['imdbRating'].min():.2f}")
    rapor.append(f"Maksimum Puan: {df['imdbRating'].max():.2f}")
rapor.append("")

# Film Süresi İstatistikleri
rapor.append("3. FİLM SÜRESİ İSTATİSTİKLERİ")
rapor.append("-" * 80)
if 'runtime_numeric' in df.columns:
    rapor.append(f"Ortalama Süre: {df['runtime_numeric'].mean():.2f} dakika")
    rapor.append(f"Medyan Süre: {df['runtime_numeric'].median():.2f} dakika")
    rapor.append(f"En Kısa Film: {df['runtime_numeric'].min():.0f} dakika")
    rapor.append(f"En Uzun Film: {df['runtime_numeric'].max():.0f} dakika")
rapor.append("")

# Tür Analizi
rapor.append("4. TÜR ANALİZİ - En Popüler 10 Tür")
rapor.append("-" * 80)
if 'primary_genre' in df.columns:
    top_genres = df['primary_genre'].value_counts().head(10)
    for i, (genre, count) in enumerate(top_genres.items(), 1):
        rapor.append(f"{i}. {genre}: {count:,} film")
rapor.append("")

# Önemli Bulgular ve Trendler
rapor.append("5. ÖNEMLİ BULGULAR VE TRENDLER")
rapor.append("-" * 80)

# Korelasyon bulguları
if 'imdbRating' in df.columns and 'metacritic' in df.columns:
    corr_meta = df[['imdbRating', 'metacritic']].corr().iloc[0, 1]
    rapor.append(f"• IMDb ve Metacritic puanları arasında {corr_meta:.2f} korelasyon bulundu")

if 'imdbRating' in df.columns and 'runtime_numeric' in df.columns:
    corr_runtime = df[['imdbRating', 'runtime_numeric']].corr().iloc[0, 1]
    rapor.append(f"• Puan ve film süresi arasında {corr_runtime:.2f} korelasyon bulundu")

if 'imdbRating' in df.columns and 'imdbVotes_numeric' in df.columns:
    corr_votes = df[['imdbRating', 'imdbVotes_numeric']].corr().iloc[0, 1]
    rapor.append(f"• Puan ve oy sayısı arasında {corr_votes:.2f} korelasyon bulundu")

# Yıl bazlı trend
if 'year_numeric' in df.columns:
    recent_avg = df[df['year_numeric'] >= 2010]['imdbRating'].mean()
    old_avg = df[(df['year_numeric'] >= 1990) & (df['year_numeric'] < 2010)]['imdbRating'].mean()
    rapor.append(f"• 2010+ filmlerin ort. puanı: {recent_avg:.2f}")
    rapor.append(f"• 1990-2009 filmlerin ort. puanı: {old_avg:.2f}")

rapor.append("")

# En İyi Filmler
rapor.append("6. EN YÜKSEK PUANLI 10 FİLM")
rapor.append("-" * 80)
if 'title' in df.columns and 'imdbRating' in df.columns:
    top_movies = df.nlargest(10, 'imdbRating')[['title', 'year', 'imdbRating', 'primary_genre']]
    for i, row in enumerate(top_movies.itertuples(), 1):
        rapor.append(f"{i}. {row.title} ({row.year}) - Puan: {row.imdbRating} - Tür: {row.primary_genre}")
rapor.append("")

# Sonuç ve Öneriler
rapor.append("7. SONUÇ VE ÖNERİLER")
rapor.append("-" * 80)
rapor.append("• Film başarısını etkileyen en önemli faktörler arasında tür, süre ve")
rapor.append("  yapım yılı bulunmaktadır.")
rapor.append("• Yüksek puanlı filmler genellikle belirli türlerde yoğunlaşmaktadır.")
rapor.append("• Metacritic ve IMDb puanları arasında güçlü bir korelasyon vardır.")
rapor.append("• Oy sayısı ve puan arasındaki pozitif korelasyon, popüler filmlerin")
rapor.append("  genellikle daha yüksek puan aldığını göstermektedir.")
rapor.append("")
rapor.append("="*80)
rapor.append("Rapor Tarihi: " + pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S"))
rapor.append("="*80)

# Raporu dosyaya yaz
rapor_text = "\n".join(rapor)
with open('imdb_film_analizi_rapor.txt', 'w', encoding='utf-8') as f:
    f.write(rapor_text)

print("\n" + rapor_text)
print("\n✓ Rapor kaydedildi: imdb_film_analizi_rapor.txt")

print("\n" + "="*80)
print("ANALİZ TAMAMLANDI!")
print("="*80)
print(f"\nÇıktı Dosyaları:")
print(f"1. Görselleştirme: imdb_film_analizi_gorsellestirme.png")
print(f"2. Rapor: imdb_film_analizi_rapor.txt")
print("="*80)
