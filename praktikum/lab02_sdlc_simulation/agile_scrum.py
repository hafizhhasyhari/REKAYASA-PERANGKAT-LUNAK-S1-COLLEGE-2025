# agile_scrum.py
# Simulasi SDLC Agile (Scrum): Proses iteratif dan adaptif.
# Oleh : name : Hafizh Hilman Asyhari
# github : hafizhhasyhari  https://github.com/hafizhhasyhari 

import time

# Product Backlog: Daftar semua keinginan, bisa berubah
product_backlog = [
    "Fitur A (Login)", 
    "Fitur B (Payment)", 
    "Fitur C (Dashboard)",
    "Fitur E (Search)",
    "Perbaikan Bug X"
]

def run_sprint(sprint_number, backlog):
    print(f"\n--- MEMULAI SPRINT #{sprint_number} (Durasi 2 'Minggu') ---")
    
    # 1. Sprint Planning
    print("[Event] 📅 SPRINT PLANNING:")
    # Tim memilih apa yang akan dikerjakan
    if len(backlog) == 0:
        print("  -> Backlog kosong. Sprint dibatalkan.")
        return [], "Selesai"
        
    sprint_backlog = backlog[:2] # Ambil 2 item teratas
    backlog = backlog[2:]
    print(f"  -> Tim berkomitmen mengerjakan: {sprint_backlog}")

    # 2. Development "Sprint" (Implementasi & Testing terjadi bersamaan)
    print("[Proses] 💻 DEVELOPMENT & 🐞 TESTING:")
    time.sleep(2) # Simulasi 2 'minggu' kerja
    increment = [f"{feature} (v{sprint_number})" for feature in sprint_backlog]
    print(f"  -> Increment Selesai: {increment}")

    # 3. Sprint Review
    print("[Event] 🎤 SPRINT REVIEW:")
    print("  -> Menampilkan increment kepada Klien...")
    print("  -> Klien: 'Bagus! Tapi... saya ada ide baru.'")
    # Simulasi perubahan: Klien menambah/mengubah kebutuhan
    perubahan_dari_klien = "Fitur F (Social Media Share)"
    if perubahan_dari_klien:
        backlog.insert(0, perubahan_dari_klien) # Perubahan diterima dan diprioritaskan
        print(f"  -> FEEDBACK: Menambahkan '{perubahan_dari_klien}' ke Product Backlog.")

    # 4. Sprint Retrospective
    print("[Event] 🧘 SPRINT RETROSPECTIVE:")
    print("  -> Tim: 'Kita perlu meningkatkan kecepatan testing di sprint depan.'")
    
    return backlog, "Berlanjut"

# Menjalankan simulasi
status = "Berlanjut"
sprint_ke = 1
while status == "Berlanjut":
    product_backlog, status = run_sprint(sprint_ke, product_backlog)
    sprint_ke += 1

print("\n--- SIMULASI AGILE SELESAI ---")
print("Semua fitur telah selesai dikerjakan.")
