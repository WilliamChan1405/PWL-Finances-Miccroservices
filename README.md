# Migrasi Aplikasi Monolitik ke Arsitektur Microservices

Proyek ini mendemonstrasikan migrasi dari **Arsitektur Monolitik** ke **Arsitektur Microservices**. File ini menjelaskan perbedaan antara kedua pendekatan tersebut dan perubahan yang dilakukan pada struktur proyek, kode, dan deployment. Kami menggunakan Flask, Docker, dan Docker Compose untuk mengelola layanan microservices.

## Daftar Isi
1. [Tinjauan Arsitektur Monolitik](#tinjauan-arsitektur-monolitik)
2. [Tinjauan Arsitektur Microservices](#tinjauan-arsitektur-microservices)
3. [Proses Migrasi](#proses-migrasi)
4. [Struktur Proyek](#struktur-proyek)
5. [Struktur Database](#struktur-database)
6. [Menjalankan Aplikasi](#menjalankan-aplikasi)
7. [Kesimpulan](#kesimpulan)

## Tinjauan Arsitektur Monolitik

Pada **Arsitektur Monolitik** yang sebelumnya digunakan, seluruh aplikasi dibangun sebagai satu unit besar dan saling terhubung. Semua fitur (seperti manajemen pelanggan, manajemen saham, dan transaksi pembelian) digabungkan dalam satu basis kode. Komponen-komponen dalam monolit ini saling terintegrasi dengan erat, berbagi satu database, dan berkomunikasi secara internal.

### Fitur Utama:
- **Basis Kode Tunggal**: Semua komponen (Auth, Stock, Buy, Sell) adalah bagian dari satu proyek yang sama.
- **Database Bersama**: Satu database digunakan untuk semua layanan.
- **Deploy Tunggal**: Seluruh aplikasi di-deploy sebagai satu unit.
- **Tergantung Satu Sama Lain**: Semua komponen saling bergantung, membuatnya lebih sulit untuk melakukan skala, uji coba, dan pemeliharaan setiap layanan secara terpisah.

---

## Tinjauan Arsitektur Microservices

Pada **Arsitektur Microservices** yang baru, aplikasi dipecah menjadi beberapa layanan independen, masing-masing bertanggung jawab untuk domain bisnis tertentu:

- **Auth Service**: Mengelola data dan operasi terkait autentikasi pengguna.
- **Stock Service**: Menyediakan data harga saham dan informasi terkait.
- **Buy/Sell Service**: Mengelola transaksi pembelian dan penjualan saham.

Setiap layanan berdiri sendiri, memiliki database sendiri, dan dapat di-deploy, di-skala, dan dipelihara secara terpisah.

### Fitur Utama:
- **Layanan Independen**: Setiap microservice (Auth, Stock, Buy, Sell) adalah aplikasi terpisah dengan basis kode masing-masing.
- **Data Terdesentralisasi**: Setiap layanan memiliki database sendiri, memastikan isolasi data.
- **Keterkaitan Longgar**: Layanan-layanan berkomunikasi satu sama lain melalui API REST atau sistem pesan, sehingga lebih mudah untuk melakukan skala dan pemeliharaan secara terpisah.
- **Deploy Independen**: Setiap microservice dapat di-deploy secara independen, memungkinkan fleksibilitas lebih dalam skala dan pembaruan.

---

## Proses Migrasi

Proses migrasi melibatkan beberapa langkah:

1. **Memecah Monolit**: Aplikasi monolit yang besar dipecah menjadi layanan-layanan yang lebih kecil dan lebih spesifik.
2. **Pengisolasi Database**: Setiap microservice diberi database sendiri untuk menghindari keterkaitan data antar layanan.
3. **Komunikasi Antar Layanan**: API REST diperkenalkan untuk komunikasi antar layanan, memungkinkan mereka berinteraksi secara terpisah.
4. **Deployment Independen**: Docker dan Docker Compose digunakan untuk containerization dan orkestrasi layanan, memungkinkan deploy dan skala setiap layanan secara terpisah.
5. **Discovery Layanan dan API Gateway**: API Gateway digunakan untuk mengelola routing antara klien dan layanan mikro.

---

## Struktur Proyek

Struktur proyek telah diubah untuk mendukung arsitektur microservices. Berikut adalah gambaran umum struktur baru:

microservices-project
├── auth-service                      # Layanan Autentikasi
│   ├── src
│   ├── Dockerfile                    # Dockerfile untuk layanan Auth
│   ├── requirements.txt              # Dependensi Python untuk layanan Auth
│   └── auth_service.py               # Logika untuk layanan Auth
│
├── stock-service                     # Layanan Stock
│   ├── src
│   ├── Dockerfile                    # Dockerfile untuk layanan Stock
│   ├── requirements.txt              # Dependensi Python untuk layanan Stock
│   └── stock_services.py             # Logika untuk layanan Stock
│
├── api-gateway                       # API Gateway untuk mengelola komunikasi antar layanan
│   ├── src
│   ├── Dockerfile                    # Dockerfile untuk API Gateway
│   ├── requirements.txt              # Dependensi Python untuk API Gateway
│   └── api_gateway.py                # Logika untuk API Gateway
│
├── docker-compose.yml                # Konfigurasi Docker Compose untuk menjalankan semua layanan
└── README.md                         # Dokumentasi proyek


---

## Struktur Database

- **Database Monolitik**: Pada arsitektur monolitik, aplikasi menggunakan satu database besar untuk semua layanan.
- **Database Microservices**: Setelah migrasi, setiap layanan memiliki database terpisah, memastikan isolasi data antar layanan.

### Contoh Struktur Database:
- **Auth Service**: Menyimpan data pengguna (username, password).
- **Stock Service**: Menyimpan data harga dan informasi saham.
- **Buy/Sell Service**: Menyimpan data transaksi pembelian dan penjualan.

---

## Menjalankan Aplikasi

### Prasyarat:
- Docker dan Docker Compose sudah terinstal.
- File **`.env`** dengan `API_KEY` yang valid harus tersedia untuk Stock Service.

### Langkah-Langkah:

1. Clone Repositori:
    ```bash
    git clone https://github.com/username/microservices-project.git
    cd microservices-project
    ```

2. Build dan jalankan layanan dengan Docker Compose:
    ```bash
    docker-compose up --build
    ```

3. Akses Aplikasi:
    - **API Gateway** akan berjalan di `http://localhost:5000`.
    - Layanan-layanan lainnya (Auth, Stock, Buy/Sell) berjalan di port internal yang dikelola oleh Docker Compose.

4. Untuk menghentikan dan menghapus layanan:
    ```bash
    docker-compose down
    ```

---

## Kesimpulan

Dengan migrasi dari arsitektur monolitik ke microservices, berhasil membuat aplikasi lebih modular dan mudah untuk di-deploy dan di-maintain. Setiap layanan dapat diatur dan diskalakan secara independen, memungkinkan peningkatan kinerja dan ketahanan aplikasi secara keseluruhan. Selain itu, menggunakan Docker Compose untuk orkestrasi layanan memudahkan pengelolaan dan pengujian sistem secara menyeluruh.

