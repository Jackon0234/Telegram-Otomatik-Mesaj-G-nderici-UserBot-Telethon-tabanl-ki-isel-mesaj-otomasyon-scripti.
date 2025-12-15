⚙️ Script Neler Yapabiliyor?

✅Otomatik Mesaj Gönderimi:
Belirlediğiniz bir mesajı kişi listenizdeki herkese otomatik olarak gönderir.

✅Spam Koruması:
Telegram’ın sizi spam olarak algılamaması için her mesaj arasında akıllı, rastgele bekleme süresi ekler.
(Hesabınızın güvenliği için çok önemli &#128274

✅Akıllı Hata Yönetimi:
Telegram’ın “Çok fazla istek gönderdin” (FloodWaitError) gibi uyarılarını algılar ve hata vermeden otomatik olarak bekleyip devam eder.

✅Kolay Ayarlar:
Tüm yapılandırmalar (API bilgileri, mesaj içeriği, bekleme süreleri vb.) dosyanın en üst kısmından kolayca düzenlenebilir.

✅Şık Görsel Arayüz:
rich kütüphanesi sayesinde terminalde renkli, anlaşılır ve estetik bir arayüz sunar. 🌈

---

🧩 Kurulum Adımları

1️⃣ Python Yükleyin
Bilgisayarınızda Python yoksa python.org adresine gidin ve en güncel sürümü indirin.
Kurulum sırasında "Add Python to PATH" kutusunu işaretlemeyi unutmayın.

2️⃣ Telegram API Bilgilerini Alın
1. https://my.telegram.org adresine gidin ve telefon numaranızla giriş yapın.
2. "API development tools" kısmına tıklayın.
3. Uygulama adı ve kısa adı girin (örnek: “OtoMesaj”, “mesajbot”).
4. Karşınıza çıkan api_id ve api_hash değerlerini bir kenara not alın.

3️⃣ Gerekli Kütüphaneleri Yükleyin
Komut satırına şu komutu yazın:
Kod
1
pip install telethon rich
4️⃣ Scripti Çalıştırın
Kaydettiğiniz dosyanın bulunduğu klasöre gidin ve terminalde:
Kod
1
python oto_mesaj.py
komutunu çalıştırın.

İlk çalıştırmada sizden telefon numaranızı, Telegram’a gelen kodu ve (varsa) iki adımlı doğrulama şifrenizi isteyecektir.
Bu bilgileri girdikten sonra program otomatik olarak çalışmaya başlar. ✅
