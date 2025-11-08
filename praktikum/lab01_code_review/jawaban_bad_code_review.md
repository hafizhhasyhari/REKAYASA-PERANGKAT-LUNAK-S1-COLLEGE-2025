Analisis Kode: Mengapa bad_code.py adalah Mimpi Buruk Pemeliharaan?

Mata Kuliah: Rekayasa Perangkat Lunak
Minggu: 01
Topik: Analisis Kode & Prinsip Dasar RPL

Pendahuluan

Banyak developer pemula terjebak dalam pola pikir "yang penting jalan". Kode bad_code.py adalah contoh sempurna dari mentalitas ini. Sekilas, kode tersebut mungkin berfungsi: menerima pesanan, menghitung total, dan menyimpannya. Namun, dari kacamata Rekayasa Perangkat Lunak (RPL), kode ini adalah "bom waktu" yang siap meledak saat aplikasi perlu dikembangkan atau diperbaiki. Esai ini akan membedah lima masalah fundamental dalam kode tersebut dan menghubungkannya dengan prinsip-prinsip RPL yang dilanggar.

Analisis Masalah

1. Pelanggaran Single Responsibility Principle (SRP)

Masalah paling mencolok adalah fungsi process_order melakukan terlalu banyak hal. Dalam satu blok fungsi raksasa, ia melakukan: (1) Validasi input, (2) Pembacaan database user, (3) Pembacaan database produk, (4) Perhitungan logika bisnis (total harga, diskon), (5) Penulisan ke database order, dan bahkan (6) Simulasi pengiriman email.

Ini melanggar Single Responsibility Principle (SRP), yang menyatakan bahwa satu modul/fungsi harusnya hanya punya satu alasan untuk berubah. Jika kita ingin mengubah cara diskon dihitung, kita harus menyentuh fungsi ini. Jika kita ingin mengubah cara database disimpan (misal dari JSON ke SQL), kita juga harus menyentuh fungsi yang sama. Ini meningkatkan risiko bug secara eksponensial karena perubahan di satu bagian bisa merusak bagian lain yang tidak terkait.

2. Kode yang Tidak Dapat Diuji (Untestable Code)

Karena semua logika bercampur aduk, kode ini hampir mustahil untuk diuji secara otomatis (unit testing). Bagaimana kita bisa menguji logika "diskon 10%" tanpa harus benar-benar membaca file products.json atau menulis ke file orders.json?

Dalam RPL, Testability adalah atribut kualitas kunci. Kode yang baik harus modular sehingga tiap bagian (misal: logika diskon) bisa diuji secara terisolasi dengan mock data, tanpa bergantung pada sistem file eksternal atau koneksi jaringan yang nyata.

3. Pelanggaran Don't Repeat Yourself (DRY) & Hardcoding

Meskipun tidak terlihat eksplisit repetisinya di sini, pola pengambilan data sangat rentan terhadap duplikasi jika aplikasi berkembang. Selain itu, kode ini penuh dengan nilai hardcoded (nilai statis), seperti path file users.json, products.json, dan nilai ambang batas diskon 100000.

Jika file JSON dipindahkan ke folder lain, atau jika manajemen memutuskan batas diskon naik menjadi 200000, kita harus mencari dan mengubah nilai-nilai ini yang mungkin tersebar di banyak fungsi lain. RPL mengajarkan kita untuk menggunakan konfigurasi terpusat atau konstanta untuk nilai-nilai penting ini.

4. Penanganan Error yang Buruk (Poor Error Handling)

Kode menggunakan blok try...except yang terlalu umum (bare except:) dan hanya mencetak "ERROR" ke layar sebelum return. Ini adalah praktik buruk. Pertama, bare except akan menangkap semua jenis error, termasuk error yang mungkin tidak kita duga (seperti KeyboardInterrupt), menyembunyikan bug asli.

Kedua, hanya mencetak ke layar (console logging) tidak cukup untuk aplikasi produksi. RPL menekankan pentingnya proper logging (mencatat error ke file log atau sistem monitoring) dan graceful degradation (aplikasi tetap berjalan aman meski ada error), bukan sekadar berhenti mendadak.

5. Ketergantungan Kuat (Tight Coupling)

Fungsi process_order sangat terikat (tightly coupled) dengan implementasi penyimpanan data (file JSON). Ia tahu persis nama filenya dan format datanya. Jika suatu hari kita ingin mengganti JSON dengan database MySQL atau MongoDB, kita harus menulis ulang hampir seluruh fungsi ini.

Prinsip RPL menyarankan Dependency Inversion atau penggunaan abstraksi. Seharusnya, fungsi ini tidak perlu tahu dari mana data user berasal, ia hanya perlu memanggil antarmuka (misal: userRepository.getUser(id)), dan biarkan modul lain yang mengurus detail apakah itu dari JSON, SQL, atau API eksternal.

Kesimpulan

Kode bad_code.py mungkin menyelesaikan tugas hari ini, tapi ia menciptakan technical debt (hutang teknis) yang mahal untuk masa depan. Tanpa menerapkan prinsip SRP, Testability, dan abstraksi, kode seperti ini akan menjadi "spaghetti code" yang menakutkan bagi siapa pun yang harus memeliharanya. Inilah mengapa RPL bukan sekadar teori, melainkan fondasi untuk membangun perangkat lunak yang tahan lama dan adaptif.
