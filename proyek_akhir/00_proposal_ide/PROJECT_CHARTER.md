# 🏛️ Project Charter: [Isi Judul Proyek Anda, cth: "Sistem Manajemen Klinik Sehat"]

| **Proyek:** | [Isi Judul Proyek Anda] | **Tanggal:** | 09 November 2025 |
| :--- | :--- | :--- | :--- |
| **Manajer Proyek:** | [Isi Nama PM Tim Anda] | **Sponsor Proyek:** | [Isi Nama Dosen/Profesor Anda] |
| **Anggota Tim:** | 1. [Nama Anggota 1]<br>2. [Nama Anggota 2]<br>3. [Nama Anggota 3]<br>4. [Nama Anggota 4] | | |

---

## 1. Latar Belakang Masalah (Problem Statement)

> *Jelaskan masalah yang ingin diselesaikan (1-2 paragraf). Mengapa proyek ini perlu ada?*
> 
> **(Contoh untuk 'Sistem Manajemen Klinik')**
> "Klinik Sehat saat ini mengelola pendaftaran pasien dan rekam medis secara manual menggunakan buku besar. Proses ini lambat, rentan terhadap *human error* (salah tulis), dan menyulitkan pencarian riwayat pasien. Pasien harus menelepon untuk *booking* dan sering terjadi tumpang tindih jadwal. Di era digital, metode ini tidak efisien, tidak *scalable*, dan berisiko tinggi terhadap kehilangan data (kebakaran, banjir, dll)."

## 2. Tujuan Proyek (Goals & Objectives)

> *Apa yang ingin dicapai oleh proyek ini? Buatlah spesifik dan terukur (jika bisa) menggunakan SMART (Specific, Measurable, Achievable, Relevant, Time-bound).*
> 
> * **Tujuan 1 (Specific):** Mendigitalisasi proses pendaftaran pasien dan manajemen rekam medis.
> * **Tujuan 2 (Measurable):** Mengurangi waktu tunggu pendaftaran pasien di *front-desk* sebesar 70%.
> * **Tujuan 3 (Achievable):** Menyediakan sistem *booking* mandiri berbasis web yang dapat diakses 24/7 oleh pasien.
> * **Tujuan 4 (Relevant):** Meningkatkan akurasi data rekam medis dan mempermudah audit.
> * **Tujuan 5 (Time-bound):** Perancangan (SRS, SDD, ADD) selesai dalam 16 minggu ke depan.

## 3. Ruang Lingkup (Scope)

### 3.1. Di Dalam Ruang Lingkup (In-Scope)

> *Fitur-fitur utama yang **AKAN** dirancang:*
> 
> * **Modul Autentikasi:** Login/Register/Logout untuk 3 peran (Pasien, Dokter, Admin).
> * **Modul Manajemen Pasien (Admin):** CRUD data pasien.
> * **Modul Manajemen Dokter (Admin):** CRUD data dan jadwal dokter.
> * **Modul Booking Pasien (Pasien):** Pasien dapat melihat jadwal dokter dan membuat janji temu.
> * **Modul Rekam Medis (Dokter):** Dokter dapat melihat riwayat dan menambahkan rekam medis baru untuk pasien.
> * **Modul Antrian (Admin):** Mengelola antrian pasien yang datang.

### 3.2. Di Luar Ruang Lingkup (Out-of-Scope)

> *Fitur-fitur yang **TIDAK AKAN** dirancang untuk proyek ini (penting untuk membatasi pekerjaan):*
> 
> * Modul Pembayaran, Billing, dan Kasir.
> * Integrasi dengan sistem asuransi (BPJS).
> * Modul Manajemen Inventori Obat (Farmasi).
> * Fitur Konsultasi Jarak Jauh (*Telemedicine*).
> * Aplikasi *mobile native* (kita fokus pada perancangan sistem web).

## 4. Stakeholder Utama

| Stakeholder | Peran / Kepentingan |
| :--- | :--- |
| **Pasien** | Pengguna utama, menginginkan kemudahan *booking* dan akses riwayat. |
| **Dokter** | Pengguna utama, membutuhkan akses cepat & akurat ke rekam medis. |
| **Admin Klinik** | Pengguna utama, mengelola jadwal dokter dan data pasien. |
| **Pemilik Klinik** | Sponsor, menginginkan efisiensi operasional dan laporan. |
| **Dosen (Prof.)** | Klien/Sponsor (dalam konteks kuliah), mengevaluasi kualitas perancangan. |

## 5. Asumsi dan Risiko Awal

### 5.1. Asumsi

> *Hal-hal yang kita anggap benar agar proyek ini bisa berjalan.*
> 
> 1. Asumsi bahwa dokter dan admin bersedia dan mampu belajar menggunakan sistem baru.
> 2. Asumsi bahwa koneksi internet di klinik stabil untuk operasional sistem web.
> 3. Asumsi bahwa kebutuhan yang didefinisikan di awal tidak akan berubah secara drastis (karena kita tidak *full-Agile* dalam perancangan ini).

### 5.2. Risiko Awal

> *Hal-hal yang berpotensi menggagalkan proyek.*
> 
> 1. **Risiko (User):** Pasien (terutama yang senior) menolak menggunakan sistem *booking online* dan tetap menelepon.
>    * **Mitigasi:** Admin tetap bisa mendaftarkan pasien via telepon melalui *dashboard* Admin.
> 2. **Risiko (Teknis):** Tim kekurangan pemahaman tentang aturan keamanan data rekam medis (cth: standar HIPAA atau Kemenkes).
>    * **Mitigasi:** Melakukan riset spesifik (komponen **Penelitian**) tentang regulasi data medis di Minggu 02-03.
> 3. **Risiko (Proyek):** *Scope Creep* (Klien tiba-tiba meminta fitur Farmasi).
>    * **Mitigasi:** Menggunakan Project Charter ini (khususnya bagian *Out-of-Scope*) sebagai acuan tegas.

## 6. Persetujuan (Sign-off)

| Peran | Nama |
| :--- | :--- |
| **Sponsor Proyek (Dosen)** | [Nama Dosen Anda] |
| **Manajer Proyek (Tim)** | [Nama PM Anda] |
