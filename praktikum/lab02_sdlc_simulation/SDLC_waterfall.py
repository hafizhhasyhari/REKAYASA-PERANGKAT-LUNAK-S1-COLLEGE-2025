# waterfall.py
# Simulasi SDLC Waterfall: Proses linear dan kaku.
# oleh : Hafizh Hilman Asyhari

import time

def phase_requirements():
    print("[Fase 1] 📋 REQUIREMENTS: Mengumpulkan SEMUA kebutuhan di awal...")
    # Asumsikan butuh waktu 2 'minggu' (detik)
    time.sleep(2)
    print("  -> Selesai. Dokumen SRS (Software Requirements Specification) dibekukan.")
    # Kebutuhan 'dibekukan' (tidak bisa diubah)
    return ["Fitur A", "Fitur B", "Fitur C"]

def phase_design(requirements):
    print("\n[Fase 2] 🏛️ DESIGN: Merancang SEMUA arsitektur sistem...")
    print(f"  -> Berdasarkan {len(requirements)} kebutuhan.")
    time.sleep(2)
    print("  -> Selesai. Dokumen Desain (SDD) dibekukan.")
    return "Arsitektur 3-Tier yang Kaku"

def phase_implementation(design, requirements):
    print("\n[Fase 3] 💻 IMPLEMENTATION: Mengkode SEMUA fitur...")
    print(f"  -> Menggunakan desain: {design}")
    for feature in requirements:
        print(f"    -> Mengkode {feature}...")
        time.sleep(1)
    print("  -> Selesai. Seluruh kode dibekukan.")
    return "Aplikasi v1.0 (Banyak Bug)"

def phase_testing(application):
    print("\n[Fase 4] 🐞 TESTING: Menguji SEMUA aplikasi...")
    print(f"  -> Menguji {application}")
    time.sleep(2)
    print("  -> Selesai. Menemukan 50 bug kritis.")
    # Simulasi perubahan besar
    print("\n  !!! PERUBAHAN DARI KLIEN: 'Kami tidak mau Fitur C, kami mau Fitur D!'")
    print("  -> Tim: 'TIDAAAK! Kita harus kembali ke Fase 1!'")
    return "Gagal (Perlu revisi besar)"

def phase_deployment(status):
    print(f"\n[Fase 5] 🚀 DEPLOYMENT: Status = {status}")
    if status != "Gagal":
        print("  -> Meluncurkan produk ke user.")
    else:
        print("  -> Peluncuran ditunda. Proyek kembali ke Fase 1.")

# Menjalankan simulasi
print("--- MEMULAI SIMULASI WATERFALL ---")
kebutuhan = phase_requirements()
desain = phase_design(kebutuhan)
aplikasi = phase_implementation(desain, kebutuhan)
status_final = phase_testing(aplikasi)
phase_deployment(status_final)
print("--- SIMULASI WATERFALL SELESAI ---")
