# 🎬 IMDb Film Veri Seti Analizi

Geniş bir film veri setini (IMDb) analiz ederek film başarısını etkileyen faktörleri incelemek ve sinema dünyasındaki eğilimleri keşfetmek için geliştirilmiş kapsamlı bir veri analizi projesi.

## 📊 Proje Hakkında

Bu proje, 46,000+ filmi içeren bir IMDb veri setini kullanarak film endüstrisindeki önemli trendleri, başarı faktörlerini ve ilginç örüntüleri ortaya çıkarmayı amaçlamaktadır. Python'un güçlü veri analizi kütüphaneleri (Pandas, Numpy, Matplotlib) kullanılarak gerçekleştirilmiştir.

## ✨ Özellikler

- **Kapsamlı Veri Analizi**: 46,014 film üzerinde detaylı istatistiksel analiz
- **Çoklu Görselleştirme**: 9 farklı grafik ve görselleştirme
- **Trend Analizi**: Yıllara göre film trendlerini ve puan değişimlerini inceleme
- **Korelasyon Analizi**: Film başarısını etkileyen faktörlerin belirlenmesi
- **Otomatik Raporlama**: Detaylı analiz raporunun otomatik oluşturulması

## 🛠️ Kullanılan Teknolojiler

- **Python 3.x**
- **Pandas** - Veri manipülasyonu ve analizi
- **Numpy** - Sayısal hesaplamalar
- **Matplotlib** - Veri görselleştirme
- **Conda/Miniconda** - Paket yönetimi

## 📋 Gereksinimler

```bash
# Conda kullanılarak kurulum
conda install pandas numpy matplotlib

# veya pip kullanılarak
pip install pandas numpy matplotlib
```

## 🚀 Kurulum ve Kullanım

### 1. Projeyi Klonlayın

```bash
git clone https://github.com/HilmiTuncay/imdb.git
cd imdb
```

### 2. Veri Setini Yerleştirin

**Not**: Veri seti dosyası (`movies_initial.csv`) boyutu nedeniyle (40.8 MB) GitHub'a yüklenmemiştir.

Veri seti indirme linki:
https://www.kaggle.com/datasets/samruddhim/imdb-movies-analysis

Veri setinizi proje dizinine ekleyin:
- Dosya adı: `movies_initial.csv`
- Konum: Proje ana dizini
- IMDb veri seti formatında olmalıdır

### 3. Gerekli Kütüphaneleri Yükleyin

```bash
conda install pandas numpy matplotlib
```

### 4. Analizi Çalıştırın

```bash
python movies_analysis.py
```

### 5. Çıktıları İnceleyin

Analiz tamamlandığında şu dosyalar oluşturulacaktır:
- `imdb_film_analizi_gorsellestirme.png` - Görselleştirmeler
- `imdb_film_analizi_rapor.txt` - Detaylı analiz raporu

## 📁 Proje Yapısı

```
imdb/
│
├── movies_initial.csv                          # Veri seti (40.8 MB)
├── movies_analysis.py                          # Ana analiz scripti
├── imdb_film_analizi_gorsellestirme.png       # Görselleştirme çıktısı
├── imdb_film_analizi_rapor.txt                # Analiz raporu
└── README.md                                   # Proje dokümantasyonu
```

## 📈 Analiz Aşamaları

### Aşama 1: Veri Yükleme ve Hazırlama
- 46,014 film kaydının yüklenmesi
- Veri tiplerinin kontrolü ve düzenlenmesi
- Temel veri yapısının incelenmesi

### Aşama 2: Veri Ön İşleme ve Temizleme
- Eksik değerlerin tespiti ve analizi
- Runtime (süre) bilgisinin sayısal formata çevrilmesi
- Year (yıl) bilgisinin düzenlenmesi
- IMDb puanlarının ve oy sayılarının işlenmesi
- Genre (tür) bilgisinin kategorize edilmesi

### Aşama 3: Keşifsel Veri Analizi (EDA)
- Temel istatistiksel analizler
- Puan dağılımı analizi
- Film süresi analizi
- Yıllara göre film dağılımı
- Tür bazlı analizler
- En yüksek puanlı filmler
- Korelasyon analizleri

### Aşama 4: Veri Görselleştirme
9 farklı görselleştirme:
1. IMDb Puan Dağılımı (Histogram)
2. Film Süresi Dağılımı
3. Yıllara Göre Film Sayısı Trendi
4. En Popüler 10 Film Türü
5. Film Süresi vs IMDb Puanı (Scatter Plot)
6. Yıl vs IMDb Puanı
7. IMDb vs Metacritic Puanları Karşılaştırması
8. Yıllara Göre Ortalama Film Puanı Trendi
9. Film Oy Sayısı Dağılımı

### Aşama 5: Raporlama
- Detaylı analiz raporunun oluşturulması
- Önemli bulguların özetlenmesi
- Sonuç ve önerilerin sunulması

## 📊 Önemli Bulgular

### Genel İstatistikler
- **Toplam Film Sayısı**: 46,014
- **Ortalama IMDb Puanı**: 6.38/10
- **Medyan Puan**: 6.60/10
- **Ortalama Film Süresi**: 97 dakika
- **Puan Standart Sapması**: 1.18

### En Popüler Film Türleri
1. **Drama** - 11,381 film (24.7%)
2. **Comedy** - 10,963 film (23.8%)
3. **Action** - 5,284 film (11.5%)
4. **Documentary** - 4,187 film (9.1%)
5. **Crime** - 2,708 film (5.9%)

### Korelasyon Bulguları
- **IMDb vs Metacritic**: 0.71 (güçlü pozitif korelasyon)
- **Puan vs Film Süresi**: 0.13 (zayıf pozitif korelasyon)
- **Puan vs Oy Sayısı**: 0.15 (zayıf pozitif korelasyon)
- **Puan vs Yıl**: -0.13 (zayıf negatif korelasyon)

### Trend Analizleri
- 2000'li yıllardan sonra film üretimi katlanarak artmış
- 1950-2015 arasında ortalama film puanı düşüş eğiliminde
- 2010 sonrası filmlerin ortalama puanı: 6.26
- 1990-2009 arası filmlerin ortalama puanı: 6.30

### En Yüksek Puanlı Filmler
1. **Band of Brothers** (2001) - 9.6 ⭐
2. **Dances Sacred and Profane** (1985) - 9.5 ⭐
3. **The Chaos Class** (1975) - 9.5 ⭐
4. **Planet Earth** (2006) - 9.5 ⭐
5. **The Civil War** (1990) - 9.4 ⭐

### En Çok Oy Alan Filmler
1. **The Shawshank Redemption** (1994) - 1,521,105 oy
2. **The Dark Knight** (2008) - 1,495,351 oy
3. **Inception** (2010) - 1,294,646 oy
4. **Fight Club** (1999) - 1,191,784 oy
5. **Pulp Fiction** (1994) - 1,179,033 oy

## 🔍 Sonuç ve Öneriler

### Ana Bulgular
1. **Tür Etkisi**: Film başarısını etkileyen en önemli faktörlerden biri türdür. Drama ve Documentary türleri en yüksek puanlı filmler arasında öne çıkmaktadır.

2. **Kritik Konsensüsü**: IMDb ve Metacritic puanları arasında 0.71'lik güçlü korelasyon, eleştirmen ve seyirci görüşlerinin genellikle uyumlu olduğunu göstermektedir.

3. **Popülerlik ve Kalite**: Oy sayısı ile puan arasındaki pozitif korelasyon, popüler filmlerin genellikle daha yüksek puan aldığını göstermektedir.

4. **Süre Faktörü**: Film süresi ile puan arasında zayıf bir pozitif korelasyon bulunmaktadır, bu da uzun filmlerin mutlaka daha başarılı olmadığını gösterir.

5. **Zaman Trendi**: Yıllar ilerledikçe ortalama film puanlarında hafif bir düşüş gözlemlenmektedir, bu durum film üretiminin artması ve çeşitlenmesiyle açıklanabilir.

### Gelecek Geliştirmeler
- [ ] Yönetmen bazlı başarı analizi
- [ ] Oyuncu kadrosu etkisinin incelenmesi
- [ ] Bütçe ve hasılat verilerinin eklenmesi
- [ ] Makine öğrenmesi ile puan tahmini modeli
- [ ] İnteraktif dashboard oluşturulması

## 📸 Görselleştirme Örnekleri

Proje, 9 farklı görselleştirme içeren kapsamlı bir grafik dosyası oluşturur:

![IMDb Film Analizi Görselleştirmeleri](imdb_film_analizi_gorsellestirme.png)

## 📝 Veri Seti Hakkında

Veri seti (`movies_initial.csv`) aşağıdaki bilgileri içermektedir:

- **imdbID**: Film ID'si
- **title**: Film adı
- **year**: Yapım yılı
- **rating**: Yaş sınırı
- **runtime**: Film süresi
- **genre**: Film türü/türleri
- **director**: Yönetmen
- **writer**: Senarist
- **cast**: Oyuncu kadrosu
- **imdbRating**: IMDb puanı
- **imdbVotes**: Oy sayısı
- **metacritic**: Metacritic puanı
- **plot**: Kısa özet
- **language**: Dil
- **country**: Ülke
- **awards**: Ödüller

## 👤 Geliştirici

**Hilmi Tuncay**
- GitHub: [@HilmiTuncay](https://github.com/HilmiTuncay)

## 🤝 Katkıda Bulunma

Katkılarınızı bekliyoruz! Lütfen şu adımları izleyin:

1. Projeyi fork edin
2. Yeni bir branch oluşturun (`git checkout -b feature/yeniOzellik`)
3. Değişikliklerinizi commit edin (`git commit -m 'Yeni özellik eklendi'`)
4. Branch'inizi push edin (`git push origin feature/yeniOzellik`)
5. Pull Request oluşturun

## 📄 Lisans

Bu proje eğitim amaçlı geliştirilmiştir.

## 🙏 Teşekkürler

- IMDb veri setini sağlayan kaynaklara
- Python ve açık kaynak topluluğuna
- Veri bilimi topluluğuna

---

⭐ Bu projeyi beğendiyseniz yıldız vermeyi unutmayın!

**Son Güncelleme**: 2025-11-14
