# Stock Management

## Proje Hakkında
Stock Management, depo/stok yönetimi için geliştirilmiş bir **Django** projesidir.  
Bu proje ile kullanıcılar ürün ekleyebilir, stokları takip edebilir ve hareketleri kaydedebilir.

---

## Özellikler
- Ürün ekleme, düzenleme ve silme
- Stok hareketlerini takip etme
- Sipariş yönetimi
- Kullanıcı yönetimi ve yetkilendirme
- Admin paneli ile kolay yönetim

---

## Kullanılan Teknolojiler
- Backend: Django, Django REST Framework
- Veri Tabanı: SQLite (default, istenirse PostgreSQL kullanılabilir)
- Frontend: Django Templates, HTML, CSS, Bootstrap

---

## Kurulum ve Çalıştırma

### 1. Projeyi klonlayın
```bash
git clone https://github.com/cakmaak/Stock-Management.git
cd Stock-Management/stokman
2. Virtual Environment’i aktifleştirin
Projede zaten myenv var, onu aktifleştirin:

Windows:

powershell
Kopyala
Düzenle
.\myenv\Scripts\activate
Mac/Linux:

bash
Kopyala
Düzenle
source myenv/bin/activate
3. Gerekli paketleri yükleyin
bash
Kopyala
Düzenle
pip install -r requirements.txt
4. Database migrasyonlarını uygulayın
bash
Kopyala
Düzenle
python manage.py makemigrations
python manage.py migrate
5. Superuser oluşturun
bash
Kopyala
Düzenle
python manage.py createsuperuser
Kullanıcı adı, e-posta ve şifre belirleyin.

Bu kullanıcı ile admin paneline giriş yapabilirsiniz.

6. Backend server’ı başlatın
bash
Kopyala
Düzenle
python manage.py runserver
Sunucu varsayılan olarak http://127.0.0.1:8000/ adresinde çalışır.

Kullanım
Admin paneline giriş: http://127.0.0.1:8000/admin/

Ürün ekleyebilir ve stokları takip edebilirsiniz.

Kullanıcılar ve hareketler admin panelinden yönetilebilir.

Katkıda Bulunanlar
Yusuf Ziya Çakmak
