# OOP

Farklı küçük domain'ler üzerinden nesne yönelimli programlama pratiği

## Genel Bakış

`OOP`, nesne yönelimli programlama yaklaşımını farklı mini projeler üzerinden çalıştığım repo. Ağırlık Java tarafında olsa da, repo içinde Python ile hazırlanmış arayüzlü bir KNN örneği de bulunuyor.

Bu repo kapsamında odaklandığım başlıklar:

- sınıf tasarımı
- nesne sorumluluklarını ayırma
- domain modelleme
- veri ve davranışı aynı yapı içinde kurgulama
- küçük uygulama akışlarını sınıflar üzerinden kurma

## Alt Projeler

| Klasör | Alan | Teknik Odak |
| --- | --- | --- |
| `BankApp` | bankacılık | hesap durumu ve işlem mantığı |
| `CarRent` | araç kiralama | araç / kiralama ilişkisi |
| `Library` | kütüphane yönetimi | kitap koleksiyonu ve yönetim akışı |
| `SchoolManagement` | okul yapısı | öğrenci, öğretmen, okul ilişkisi |
| `KNN` | sınıflandırma arayüzü | Python GUI + algoritma denemesi |

## Proje Bazlı İnceleme

### `BankApp`

`BankAccount` sınıfı etrafında şekillenen basit bankacılık örneği. Amaç, bir nesnenin durumunu koruyan alanlar ile bu durumu değiştiren metotları birlikte düşünmekti. Para yatırma, para çekme ve bakiye yönetimi gibi temel işlemler sınıf sorumluluğu olarak ele alınmış durumda.

### `CarRent`

Araç kiralama domain'i üzerinden yazılmış çalışma. `Vehicle` ve `CarRental` sınıfları, gerçek hayattaki nesne rollerini koda dönüştürme pratiği sunuyor. Özellikle bir araç nesnesi ile kiralama sürecini ayrı yapılar halinde düşünme refleksi burada gelişiyor.

### `Library`

Kütüphane ve kitap yönetimi mantığını ele alan mini proje. Kitapların veri nesnesi olarak modellenmesi ve kütüphanenin bunları yöneten ana yapı olarak tasarlanması, koleksiyon mantığı ile nesne yönelimli yaklaşımın birleştiği bir örnek sunuyor.

### `SchoolManagement`

Okul, öğrenci ve öğretmen arasındaki ilişkiyi modelleyen çalışma. Bu proje, tek nesneli örneklerden daha zengin; çünkü birden fazla nesne tipinin aynı domain içinde nasıl konumlandığı burada daha net görülüyor.

### `KNN`

Repo içindeki en farklı parçalardan biri. Python ve Tkinter kullanılarak hazırlanmış bu bölüm, KNN algoritmasını arayüz üzerinden deneyimlenebilir hale getiriyor. Böylece nesne yönelimli düşünce ile algoritma ve kullanıcı arayüzü aynı repo içinde buluşuyor.

## Repo Yapısı

```text
OOP/
|-- BankApp/
|-- CarRent/
|-- KNN/
|-- Library/
|-- SchoolManagement/
`-- README.md
```

## Kullanılan Teknolojiler

- Java
- Python
- Tkinter
- nesne yönelimli programlama prensipleri
