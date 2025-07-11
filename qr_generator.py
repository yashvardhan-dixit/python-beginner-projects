import qrcode

def create_qr(data, filename="qr_code.png"):
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill="black", back_color="white")
    img.save(filename)
    print(f"✅ QR Code saved as {filename}")

if __name__ == "__main__":
    print("📷 QR Code Generator")
    data = input("🔤 Enter text or URL to convert into QR: ")
    filename = input("💾 Enter file name to save (with .png): ") or "qr_code.png"
    create_qr(data, filename)
