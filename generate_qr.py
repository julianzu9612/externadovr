import qrcode

# URL del proyecto desplegado
url = "https://externadovr.vercel.app"

# Generar código QR
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Crear imagen
img = qr.make_image(fill_color="black", back_color="white")

# Guardar imagen
img.save("externadovr-qr.png")
print(f"QR generado exitosamente para {url}")
