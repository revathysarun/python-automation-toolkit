import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import qrcode

font = ImageFont.load_default()

# Load participant data (force all columns as text)
df = pd.read_excel("participants.xlsx", dtype=str)

# Load certificate template
template = Image.open("certificate_template.png")

# Font settings
font = ImageFont.load_default()

# Loop through participants
for index, row in df.iterrows():
    name = str(row["Name"]).strip()
    cert_id = str(row["Certificate ID"]).strip()

    # Create a copy of the template
    cert = template.copy()
    draw = ImageDraw.Draw(cert)

    # Add name to certificate
    draw.text((900, 750), name, fill="black", font=font)

    # Generate and place QR code
    qr_data = f"Certificate ID: {cert_id} | Name: {name}"
    qr = qrcode.make(qr_data)
    qr = qr.resize((100, 100))
    cert.paste(qr, (cert.width - 120, cert.height - 120))

    # Save the certificate
    filename = f"{name}_certificate.png"
    cert.save(filename)
    print(f"Certificate generated: {filename}")

print("All certificates generated successfully!")
