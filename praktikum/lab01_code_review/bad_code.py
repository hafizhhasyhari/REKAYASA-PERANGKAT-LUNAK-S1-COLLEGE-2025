# bad_code.py
# PERINGATAN: Kode ini SENGAJA ditulis dengan buruk untuk tujuan analisis.

import json

def process_order(data):
    # 1. Validasi data
    if "user_id" not in data or "items" not in data:
        print("ERROR: Data tidak lengkap")
        return

    user_id = data["user_id"]
    items = data["items"]

    # 2. Ambil data user dari "database" (file json)
    try:
        f = open("users.json", "r")
        users = json.load(f)
        f.close()
    except:
        print("ERROR: Database user tidak ditemukan")
        return

    current_user = None
    for u in users:
        if u["id"] == user_id:
            current_user = u
            break
    
    if current_user is None:
        print("ERROR: User tidak ditemukan")
        return

    print(f"Memproses pesanan untuk user: {current_user['name']}...")

    total_price = 0
    
    # 3. Ambil data produk dan hitung total
    try:
        f = open("products.json", "r")
        products = json.load(f)
        f.close()
    except:
        print("ERROR: Database produk tidak ditemukan")
        return

    item_details = []
    for item in items:
        prod_id = item["product_id"]
        quantity = item["quantity"]
        
        found_product = None
        for p in products:
            if p["id"] == prod_id:
                found_product = p
                break
        
        if found_product:
            price = found_product["price"] * quantity
            total_price += price
            item_details.append(f"{found_product['name']} (x{quantity})")
            print(f"  - Menambahkan {found_product['name']} (x{quantity}) - Harga: {price}")
        else:
            print(f"WARNING: Produk ID {prod_id} tidak ditemukan")

    print(f"Total harga pesanan: {total_price}")

    # 4. Simpan pesanan ke "database" (file json)
    order = {
        "user_id": user_id,
        "user_name": current_user["name"],
        "items": item_details,
        "total": total_price,
        "status": "processed"
    }

    try:
        # 5. Logika bonus: diskon jika > 100000
        if total_price > 100000:
            order["total_after_discount"] = total_price * 0.9
            print(f"Selamat! Anda dapat diskon 10%. Total baru: {order['total_after_discount']}")
            
            # 6. Kirim email notifikasi diskon
            # (Ini adalah pelanggaran Single Responsibility Principle)
            print(f"MENGIRIM EMAIL ke {current_user['email']}: Anda dapat diskon!")

        f = open("orders.json", "a")
        f.write(json.dumps(order) + "\n")
        f.close()
        print("Pesanan berhasil disimpan.")
    except:
        print("ERROR: Gagal menyimpan pesanan")

# Data dummy untuk pengujian
# users.json: [{"id": 1, "name": "Hafizh", "email": "hafizh@test.com"}]
# products.json: [{"id": 101, "name": "Laptop", "price": 150000}, {"id": 102, "name": "Mouse", "price": 15000}]

# Contoh pemanggilan
print("--- Skenario 1: Sukses ---")
order_1 = {
    "user_id": 1,
    "items": [
        {"product_id": 101, "quantity": 1},
        {"product_id": 102, "quantity": 2}
    ]
}
process_order(order_1)

print("\n--- Skenario 2: User tidak ada ---")
order_2 = {
    "user_id": 2,
    "items": [{"product_id": 101, "quantity": 1}]
}
process_order(order_2)

print("\n--- Skenario 3: Data tidak lengkap ---")
order_3 = {"user_id": 1}
process_order(order_3)
