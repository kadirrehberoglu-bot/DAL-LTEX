# DAL-LTEX: Tekstil Mühendisliği Profesyonel Hesaplama Sistemi

## 📋 Genel Bilgi

**DAL-LTEX**, tekstil mühendisliği üretim süreçlerinde kullanılan teknik hesaplamaları otomatik olarak yapan profesyonel bir masaüstü uygulamasıdır.

## 🎯 Özellikler

### Hesaplama Modülleri

✅ **Çekim Hesabı (Draft Calculation)**
- Nm tabanlı çekim: `Çekim = (Nm_çıkış × Dublaj) / Nm_giriş`
- ktex tabanlı çekim: `Çekim = (ktex_giriş × Dublaj) / ktex_çıkış`

✅ **Tarama Hesabı (Comber Calculation)**
- Formül: `Tarama = [Çıkış ktex × (100 − Telef%) × Dublaj] / (100 × Giriş ktex)`

✅ **Büküm Hesabı (Twist Calculation)**
- Formül: `T/m = αm × √Nm`

✅ **Nm ↔ ktex Dönüşümü**
- Nm → ktex: `ktex = 1000 / Nm`
- ktex → Nm: `Nm = 1000 / ktex`

✅ **İplik Teslim Hızı (Delivery Speed)**
- Formül: `L = ni / (T/m)`

✅ **Günlük Üretim Hesabı**
- Formül: `Günlük Üretim = (m/dk × 60 × 24 × verim × iğ sayısı) / (1000 × Nm)`

✅ **Pasaj Çekim Hesapları**
- 1., 2. ve 3. pasaj hesaplamaları

### Diğer Özellikler

- 📊 Hesaplama geçmişi (SQLite veritabanı)
- 📈 Profesyonel arayüz (PySide6 / Qt)
- 🎨 Koyu tema desteği
- 🔤 Türkçe dil desteği
- ⚠️ Kapsamlı hata kontrolleri
- 💾 Veritabanı entegrasyonu

## 🛠️ Teknik Bilgiler

### Gereksinimler

- Python 3.10 veya üzeri
- PySide6
- numpy
- pandas
- matplotlib
- openpyxl

### Kurulum

```bash
# Repository'i klonla
git clone https://github.com/kadirrehberoglu-bot/DAL-LTEX.git
cd DAL-LTEX

# Bağımlılıkları yükle
pip install -r requirements.txt

# Uygulamayı çalıştır
python main.py
```

## 📁 Proje Yapısı

```
DAL-LTEX/
├── main.py                 # Ana giriş noktası
├── requirements.txt        # Python bağımlılıkları
│
├── ui/                     # Kullanıcı Arayüzü
│   ├── main_window.py     # Ana pencere
│   ├── tabs/              # Sekme modülleri
│   │   ├── draft_tab.py
│   │   ├── comber_tab.py
│   │   ├── twist_tab.py
│   │   ├── delivery_tab.py
│   │   ├── production_tab.py
│   │   ├── passage_tab.py
│   │   ├── conversion_tab.py
│   │   └── history_tab.py
│   └── widgets/           # Özel widget'lar
│       └── result_display.py
│
├── services/              # İş Mantığı Servisleri
│   └── textile_calculations.py
│
├── database/              # Veritabanı Modülü
│   └── db_manager.py
│
├── models/                # Veri Modelleri
│   └── textile_data.py
│
├── utils/                 # Yardımcı Fonksiyonlar
│   ├── validators.py
│   └── formatters.py
│
└── README.md
```

## 📖 Kullanım Örneği

### Çekim Hesabı

1. "Çekim Hesabı" sekmesine tıklayın
2. Aşağıdaki verileri girin:
   - Giriş Nm: 20
   - Çıkış Nm: 40
   - Dublaj Sayısı: 1
3. "Hesapla" butonuna tıklayın
4. Sonuç: Çekim = (40 × 1) / 20 = 2.0

### Günlük Üretim Hesabı

1. "Günlük Üretim" sekmesine tıklayın
2. Aşağıdaki verileri girin:
   - Makine Hızı: 100 m/dk
   - Verim: 90%
   - İğ Sayısı: 1000
   - Nm: 32
3. "Hesapla" butonuna tıklayın
4. Sonuç hesaplanır ve gösterilir

## 🔒 Hata Kontrolü

Program aşağıdaki hataları otomatik olarak kontrol eder:

- ❌ Sıfıra bölme hatası
- ❌ Negatif değer girişi
- ❌ Boş veri girişi
- ❌ Sayısal olmayan veri girişi
- ❌ Geçersiz Nm/ktex değerleri
- ❌ Telef yüzdesinin 0-100 dışında olması

## 🎨 Arayüz Özellikleri

- Modern ve profesyonel tasarım
- Sekmeli yapı (8 sekme)
- Renkli butonlar kategorilere göre
- Sonuçları HTML tablo formatında gösterim
- Hesaplama geçmişi tablosu
- Temizle ve dışa aktarma seçenekleri

## 📝 Lisans

MIT Lisansı - Detaylar için LICENSE dosyasına bakın.

## 👨‍💻 Geliştirici

Kadir Rehberoglu Bot

## 🚀 Gelecek Sürümler

- [ ] PDF rapor oluşturma
- [ ] Excel dışa aktarma
- [ ] CSV dışa aktarma
- [ ] İngilizce dil desteği
- [ ] Grafik gösterimi
- [ ] İleri hesaplama modülleri

---

**Sürüm:** 1.0.0  
**Son Güncelleme:** 2026
