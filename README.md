# Java + Python OOP Projects

Bu proje dizini, Nesne Yönelimli Programlama (OOP) prensiplerini uygulamak için geliştirilmiş örnek projeler içerir. Her klasör bağımsız bir uygulamadır ve farklı alanlarda OOP kavramlarını pratik etmeyi amaçlar.

## Projeler

---

### OOP/BankApp

**Dosyalar:**
- `Main.java`
- `BankAccount.java`

**Açıklama:**  
Basit bir banka uygulamasıdır. `BankAccount` sınıfı üzerinden para yatırma, çekme gibi işlemler yapılabilir. Kullanıcı etkileşimi `Main` sınıfı üzerinden sağlanır.

---

### OOP/CarRent

**Dosyalar:**
- `Main.java`
- `CarRental.java`
- `Vehicle.java`

**Açıklama:**  
Araç kiralama sistemidir. `Vehicle` sınıfı kalıtım için temel sınıftır. `CarRental` sınıfı kiralama işlemlerini yürütür. `Main` sınıfı, bu yapıyı kullanarak uygulamayı çalıştırır.

---

### OOP/KNN

**Dosya:**
- `knn.py`

**Açıklama:**  
Python ile yazılmış basit bir K-En Yakın Komşu (KNN) sınıflandırma algoritması örneği. Makine öğrenmesi konularına giriş niteliği taşır.

---

### OOP/SchoolManagement

**Dosyalar:**
- `Main.java`
- `School.java`
- `Student.java`
- `Teacher.java`

**Açıklama:**  
Okul yönetim sistemi örneğidir. Öğrenci ve öğretmen nesneleri, `School` sınıfı altında yönetilir. Nesne ilişkileri, kalıtım ve bileşenlik (composition) gibi OOP ilkelerini uygular.

---

### OOP/library

**Dosyalar:**
- `Main.java`
- `Book.java`
- `Library.java`

**Açıklama:**  
Kütüphane yönetim sistemidir. Kitaplar `Book` sınıfı ile tanımlanır ve `Library` sınıfı altında saklanır. `Main` sınıfı, kullanıcı arayüzünü oluşturur.

---

## Gereksinimler

- Java JDK 11+ (Java projeleri için)
- Python 3.x (KNN için)

## Derleme ve Çalıştırma

### Java Projeleri
```bash
cd OOP/BankApp
javac *.java
java Main
