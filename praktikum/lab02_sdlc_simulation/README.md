## 🔬 Refleksi dari Simulasi SDLC (Minggu 01)

Setelah menjalankan kedua skrip simulasi (`waterfall.py` dan `agile_scrum.py`), perbedaan fundamental antara kedua filosofi SDLC menjadi sangat jelas dan nyata. Ini bukan lagi sekadar teori, tapi sesuatu yang bisa diamati dari *output* terminal.

Berikut adalah hasil analisis detail saya:

### 1. Simulasi `waterfall.py`: Kaku dan Rapuh

Simulasi ini secara sempurna menunjukkan alur yang **100% linear dan kaku**.

* **Proses yang Diamati:** Setiap fase (Requirements, Design, Implementation) berjalan secara berurutan. Satu fase harus selesai 100% dan "dibekukan" (`freezed`) sebelum fase berikutnya bisa dimulai. Waktu terus berjalan (disimulasikan dengan `time.sleep()`) tanpa ada *output* yang bisa digunakan oleh klien.
* **Titik Kegagalan:** "Bencana" terjadi di Fase 4 (Testing). Setelah *semua* upaya pengembangan selesai, "Klien" tiba-tiba meminta perubahan (`Fitur D` sebagai ganti `Fitur C`).
* **Hasil Akhir:** Reaksi sistem adalah **kegagalan total** (`Status = Gagal`). Tim "berteriak" (`TIDAAAK!`) karena mereka tahu bahwa model ini tidak memiliki mekanisme untuk menangani perubahan. Untuk mengakomodasi perubahan itu, mereka harus membuang hasil kerja Fase 2, 3, dan 4, lalu kembali ke Fase 1.
* **Analisis:** Simulasi ini membuktikan betapa **rapuh** dan **berisiko tinggi** model Waterfall di dunia nyata, di mana perubahan kebutuhan adalah hal yang *pasti* terjadi. Model ini mengasumsikan kita tahu segalanya di awal, yang hampir tidak pernah benar.

### 2. Simulasi `agile_scrum.py`: Adaptif dan Inkremental

Simulasi ini menunjukkan alur yang **siklikal (berulang), adaptif, dan berfokus pada *value***.

* **Proses yang Diamati:** Proses dibagi menjadi "Sprint". Alih-alih merencanakan semuanya, tim hanya merencanakan pekerjaan untuk satu Sprint (`Sprint Planning`).
* **Pengiriman Nilai (Value Delivery):** Di akhir Sprint 1, sistem berhasil memproduksi *Increment* (potongan software yang berfungsi), yaitu `[Fitur A (v1), Fitur B (v1)]`. Ini adalah sesuatu yang nyata dan bisa didemokan ke klien.
* **Penanganan Perubahan:** "Bencana" yang sama terjadi di `Sprint Review`. "Klien" meminta fitur baru (`Fitur F`). Namun, reaksinya sangat berbeda:
    1.  Proses **tidak gagal**.
    2.  Sprint 1 tetap dianggap **sukses** karena menghasilkan *increment*.
    3.  Perubahan (`Fitur F`) diterima sebagai hal yang wajar dan **dimasukkan ke dalam `Product Backlog`**.
    4.  Pada `Sprint Planning` Sprint 2, fitur baru tersebut langsung diprioritaskan dan dikerjakan.
* **Analisis:** Simulasi ini membuktikan nilai inti Agile: **"Menanggapi Perubahan lebih penting daripada Mengikuti Rencana."** Agile tidak menganggap perubahan sebagai kegagalan, tapi sebagai *feedback* normal. Sistem ini *adaptif* dan *resilien* (tangguh), memastikan bahwa produk yang dikembangkan di setiap siklus adalah yang paling relevan dengan kebutuhan klien saat itu juga.

### Kesimpulan Analisis

Simulasi ini secara praktis menunjukkan mengapa industri beralih ke Agile. **Waterfall** membuang-buang waktu dan sumber daya jika terjadi satu perubahan, sedangkan **Agile** menyambut perubahan tersebut untuk menyempurnakan produk secara iteratif.
