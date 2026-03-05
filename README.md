<p align="center">
  <img src="https://capsule-render.vercel.app/render?type=waving&color=0088cc&height=200&section=header&text=Telegram%20Bulk%20Messenger&fontSize=50&animation=fadeIn" />
</p>

<div align="center">

# 📩 Telegram Auto-Message & Marketing Suite
**Güvenli, Akıllı ve Hızlı Toplu Mesaj Gönderim Çözümü**

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Telethon](https://img.shields.io/badge/Library-Telethon-blue.svg?style=for-the-badge)](https://docs.telethon.dev/)
[![Safety](https://img.shields.io/badge/Security-Anti--Spam_Ready-brightgreen.svg?style=for-the-badge)]()
[![UI](https://img.shields.io/badge/UI-Rich_Terminal-ff69b4.svg?style=for-the-badge)]()

</div>

---

## ⚡ Temel Yetenekler

Bu script, sıradan bir mesaj göndericiden ziyade, Telegram limitlerini akıllıca yöneten bir **otomasyon motorudur**.

- **🤖 Tam Otomasyon:** Rehberinizdeki veya kişi listenizdeki herkese belirlediğiniz mesajı iletir.
- **🛡️ Gelişmiş Anti-Spam:** Telegram algoritmalarına yakalanmamak için **"Smart Random Delay"** (Akıllı Rastgele Bekleme) kullanır.
- **🚦 FloodWait Yönetimi:** "Çok fazla istek" uyarısı aldığında durmaz; süreyi hesaplar, bekler ve otomatik devam eder.
- **🌈 Rich Terminal UI:** İşlem süreçlerini, hataları ve başarıları renkli, estetik tablolarla anlık takip edin.
- **⚙️ Kolay Konfigürasyon:** Teknik bilgi gerekmeden `config` üzerinden saniyeler içinde ayarlanabilir.

---

## 📸 Arayüz Önizlemesi

---

## 🛠️ Kurulum Rehberi

### 1️⃣ Hazırlık
Sisteminizde Python yüklü olduğundan emin olun. Ardından gerekli kütüphaneleri tek komutla kurun:
pip install telethon rich
2️⃣ Telegram API Anahtarlarını Alma
my.telegram.org adresine gidin ve giriş yapın.

API development tools bölümünden yeni bir uygulama oluşturun.

Size verilen api_id ve api_hash değerlerini script içerisindeki ilgili alanlara yapıştırın.

3️⃣ Çalıştırma
Klasör içinde terminali açın ve botu ateşleyin:

python oto_mesaj.py
[!TIP]
İlk girişte telefon numaranıza gelen doğrulama kodunu terminale girmeniz yeterlidir. Oturumunuz güvenli bir şekilde .session dosyasında saklanacaktır.

📂 Dosya Yapısı
Plaintext
├── 📄 oto_mesaj.py      # Ana çalışma motoru ve UI
├── 🔑 telegram.session  # (İlk girişten sonra oluşur) Oturum dosyası
└── 📄 README.md         # Kullanım kılavuzu
