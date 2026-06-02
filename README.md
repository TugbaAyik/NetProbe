# NetProbe
UDP Tabanlı Güvenilir Dosya Aktarımı, Trafik İzleme ve Ağ Performans Analiz Platformu
Proje Hakkında

Bu proje, Bursa Teknik Üniversitesi Bilgisayar Mühendisliği Bölümü Bilgisayar Ağları dersi kapsamında geliştirilmiştir.

NetProbe, UDP protokolü üzerinde çalışan güvenilir bir dosya aktarım sistemi geliştirmeyi amaçlamaktadır. UDP'nin doğasında bulunmayan güvenilirlik mekanizmaları uygulama katmanında tasarlanmış ve gerçekleştirilmiştir.

Proje kapsamında yalnızca dosya aktarımı değil, aynı zamanda ağ trafiğinin izlenmesi, performans verilerinin toplanması ve analiz edilmesi de sağlanmıştır.

Projenin Amacı

Bu projenin temel amacı:

UDP ve TCP arasındaki farkları uygulamalı olarak incelemek
UDP üzerinde güvenilir veri aktarımı sağlamak
Ağ performans metriklerini ölçmek
Ağ davranışlarını farklı senaryolar altında analiz etmek
Trafik kayıtları oluşturarak sistem performansını değerlendirmektir
Özellikler
UDP İstemci-Sunucu Mimarisi
Güvenilir Dosya Aktarımı
Sequence Number Kullanımı
ACK Mekanizması
Timeout Kontrolü
Retransmission (Yeniden Gönderim)
Duplicate Paket Kontrolü
MD5 Hash ile Dosya Bütünlüğü Doğrulama
Trafik Loglama Sistemi
Throughput Hesaplama
Goodput Hesaplama
Packet Loss Rate Hesaplama
RTT (Round Trip Time) Ölçümü
Performans Grafikleri Oluşturma
Proje Yapısı
NetProbe/
│
├── client/
│   └── client.py
│
├── server/
│   └── server.py
│
├── analysis/
│   └── analysis.py
│
├── logs/
│   └── client_log.csv
│
├── test.txt
│
└── README.md
Kullanılan Teknolojiler
Python 3.x
socket
hashlib
csv
pandas
matplotlib
Kurulum

Gerekli kütüphaneleri yüklemek için:

pip install pandas matplotlib
Çalıştırma Adımları
1. Sunucuyu Başlatma
cd server
python server.py
2. İstemciyi Çalıştırma

Yeni bir terminal açarak:

cd client
python client.py
3. Performans Analizi

Aktarım tamamlandıktan sonra:

cd analysis
python analysis.py

komutu ile performans grafikleri oluşturulabilir.

Güvenilirlik Mekanizmaları

Projede UDP'nin eksik bıraktığı güvenilirlik özellikleri uygulama katmanında gerçekleştirilmiştir:

Sequence Number
ACK Mesajları
Timeout Yönetimi
Yeniden Gönderim (Retransmission)
Duplicate Paket Kontrolü
Dosya Bütünlüğü Kontrolü (MD5 Hash)
Ölçülen Performans Metrikleri

Sistem aşağıdaki performans ölçümlerini gerçekleştirmektedir:

Throughput
Goodput
Packet Loss Rate
Completion Time
Retransmission Rate
Ortalama RTT

Elde edilen sonuçlar CSV dosyalarına kaydedilmekte ve grafiklerle görselleştirilmektedir.

Deney Senaryoları

Proje kapsamında aşağıdaki senaryolar test edilmiştir:

Senaryo 1: Paket Boyutunun Etkisi

Farklı paket boyutlarının throughput ve tamamlanma süresi üzerindeki etkisi incelenmiştir.

Senaryo 2: Timeout Değerinin Etkisi

Farklı timeout değerlerinin retransmission sayısı ve gecikme üzerindeki etkileri analiz edilmiştir.

Senaryo 3: Paket Kayıp Oranının Etkisi

Yapay paket kaybı oluşturularak sistem performansı değerlendirilmiştir.

Senaryo 4: Dosya Boyutunun Etkisi

Küçük, orta ve büyük boyutlu dosyalar ile aktarım performansı karşılaştırılmıştır.

Gelecekte Yapılabilecek Geliştirmeler
Sliding Window Mekanizması
Selective Repeat Protokolü
Çoklu İstemci Desteği
TCP ile Karşılaştırmalı Testler
Gerçek Zamanlı Görselleştirme Paneli
Gelişmiş Ağ Simülasyonları
