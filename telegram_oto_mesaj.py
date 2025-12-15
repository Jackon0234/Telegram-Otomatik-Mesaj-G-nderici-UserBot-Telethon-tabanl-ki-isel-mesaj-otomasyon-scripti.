import asyncio
import random
import time
from typing import Final

try:
    from telethon.sync import TelegramClient
    from telethon.errors import FloodWaitError, UserIsBlockedError, PeerIdInvalidError
    from rich.console import Console
    from rich.panel import Panel
except ImportError:
    print("Gerekli kütüphaneler (telethon, rich) yüklü değil.")
    print("Lütfen 'pip install telethon rich' komutunu çalıştırarak yükleyin.")
    exit()


API_ID: Final[int] = 12345678  # BURAYA KENDİ API ID'Nİ GİR
API_HASH: Final[str] = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"  # BURAYA KENDİ API HASH'İNİ GİR
SESSION_NAME: Final[str] = "telegram_otomesaj"  # Oturum dosyasının adı değiştirmene gerek yok

# Göndermek istediğim mesajı yaz
MESAJ: Final[str] = """
Merhaba! Bu, Jackon tarafından geliştirilen otomatik bir mesajdır.
Nasılsın?
"""

# Zamanlama Ayarları (Saniye Cinsinden)
MIN_BEKLEME_SANIYESI: Final[int] = 45  # Her mesajdan sonra beklenecek en az saniye
MAX_BEKLEME_SANIYESI: Final[int] = 90  # Her mesajdan sonra beklenecek en fazla saniye
DONGU_BEKLEME_DAKIKASI: Final[int] = 45  # Tüm sohbetler bittikten sonra beklenecek dakika


console = Console()

def program_logosu_goster():
    """Program başlangıcında gösterilecek olan logoyu ve bilgiyi ekrana basar."""
    logo = Panel(
    """
    [bold blue]
╔═╗╔╦╗╔═╗   ╔╦╗╔═╗╔═╗╔═╗╔╗
║ ║ ║ ╠═╣   ║║║║╣ ╚═╗╠═╣╠╣
╚═╝ ╩ ╩ ╩   ╩ ╩╚═╝╚═╝╩ ╩╚╝
    OTO MESAJ GÖNDERİCİ 
    [/bold blue]
    [purple]@Jackon[/purple]
    """,
    title="[bold green]Telegram Otomasyon Aracı[/bold green]",
    border_style="bold blue",
    expand=False,
    padding=(1, 5)
)
    console.print(logo)
    console.print(Panel("[cyan]Tüm özel sohbetlere belirlediğiniz aralıklarla otomatik mesaj gönderir.[/cyan]", border_style="blue"))


async def mesajlari_gonder(client: TelegramClient):
    """
    Kullanıcının tüm diyaloglarını tarar ve özel sohbetlere mesaj gönderir.
    
    Args:
        client (TelegramClient): Aktif Telegram istemcisi.
    """
    gonderilen_sayisi = 0
    hatali_sayisi = 0
    console.print("\n[yellow]Mesaj gönderme döngüsü başlatılıyor...[/yellow]")
    time.sleep(2)

    try:
        async for dialog in client.iter_dialogs():
            if dialog.is_user and not dialog.entity.bot and not dialog.entity.is_self:
                kullanici = dialog.entity
                console.print(f"\n[cyan]» {kullanici.first_name} (@{kullanici.username}) adlı kullanıcıya mesaj gönderiliyor...[/cyan]")

                try:
                    await client.send_message(kullanici, MESAJ)
                    console.print(f"[green]  ✓ Mesaj başarıyla gönderildi.[/green]")
                    gonderilen_sayisi += 1

                    bekleme_suresi = random.uniform(MIN_BEKLEME_SANIYESI, MAX_BEKLEME_SANIYESI)
                    console.print(f"[dim]  Bekleniyor: {int(bekleme_suresi)} saniye...[/dim]")
                    await asyncio.sleep(bekleme_suresi)

                except FloodWaitError as e:
                    console.print(f"[bold red]  ! Flood hatası alındı. Telegram, {e.seconds} saniye beklememizi istiyor.[/bold red]")
                    await asyncio.sleep(e.seconds + 15)
                except (UserIsBlockedError, ValueError):
                    console.print(f"[yellow]  ! Kullanıcı sizi engellemiş veya sohbete mesaj gönderilemiyor. Atlanıyor.[/yellow]")
                    hatali_sayisi += 1
                except Exception as e:
                    console.print(f"[bold red]  ! Beklenmedik bir hata oluştu: {e}. Atlanıyor.[/bold red]")
                    hatali_sayisi += 1
    
    except Exception as e:
        console.print(f"[bold red]Diyaloglar alınırken kritik bir hata oluştu: {e}[/bold red]")

    console.print(Panel(f"[bold green]Döngü Tamamlandı![/bold green]\nBaşarılı: {gonderilen_sayisi}\nHatalı/Atlanan: {hatali_sayisi}", border_style="green"))


async def main():
    """
    Ana fonksiyon. Telegram istemcisini başlatır ve sonsuz bir döngü içinde
    mesaj gönderme işlemini periyodik olarak çalıştırır.
    """
    program_logosu_goster()
    
    console.print(Panel("[yellow]Telegram istemcisi başlatılıyor...[/yellow]", border_style="yellow"))
    
    async with TelegramClient(SESSION_NAME, API_ID, API_HASH) as client:
        console.print(Panel("[bold green]Başarıyla Telegram'a giriş yapıldı![/bold green]", border_style="green"))
        
        while True:
            await mesajlari_gonder(client)
            dongu_bekleme_saniyesi = DONGU_BEKLEME_DAKIKASI * 60
            console.print(f"\n[bold magenta]Tüm kullanıcılara mesaj gönderildi. Ana döngü {DONGU_BEKLEME_DAKIKASI} dakika bekleyecek.[/bold magenta]")
            await asyncio.sleep(dongu_bekleme_saniyesi)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (ValueError, TypeError):
         console.print(f"[bold red]HATA: Lütfen kodun başındaki 'API_ID' ve 'API_HASH' bilgilerini doğru girdiğinizden emin olun.[/bold red]")
    except KeyboardInterrupt:
        console.print("\n[bold yellow]Program kullanıcı tarafından sonlandırıldı. Hoşça kalın![/bold yellow]")