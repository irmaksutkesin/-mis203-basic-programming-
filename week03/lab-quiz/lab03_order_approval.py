def main():
    # Girdilerin alınması
    order_amount = float(input("Sipariş tutarını girin (TRY): "))
    available_stock = int(input("Mevcut stok miktarını girin: "))
    requested_quantity = int(input("İstenen miktarı girin: "))
    is_member_input = input("Müşteri üye mi? (evet/hayır): ").strip().lower()

    is_member = is_member_input in ["evet", "e", "yes", "y"]

    # 1. Doğrulama ve Stok Kontrolü (Hata ve Geçersizlik Durumları)
    if requested_quantity <= 0 or order_amount <= 0:
        print("\n[REDDET] Geçersiz miktar veya sipariş tutarı.")
        return

    if requested_quantity > available_stock:
        print("\n[REDDET] Yetersiz stok.")
        return

    # 2. Onay ve İndirim Hesabı
    discount = 0.0
    # Mantıksal operatör (and) kullanımı
    if is_member and order_amount >= 500:
        discount = 0.10
        reason = "Sipariş onaylandı (%10 üyelik indirimi uygulandı)."
    else:
        reason = "Sipariş onaylandı (standart fiyat)."

    final_price = order_amount * (1 - discount)

    # 3. Sonuç Çıktısı (Onaylanan siparişler için)
    print(f"\n[ONAYLANDI] {reason}")
    print(f"Nihai Tutar: {final_price:.2f} TRY")


if __name__ == "__main__":
    main()
