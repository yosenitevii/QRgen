import qrcode
from PIL import Image, ImageDraw

# --- 1. QR Code Settings and Data ---
data = "https://www.linkedin.com/in/ulascolak/" # Insert your own LinkedIn profile link here!
# Or another link:
# data = "https://www.ulascolak.com"

# Use high error correction level (H) because a part of the logo will cover the QR code.
# This helps the QR code compensate for data loss in the area where the logo is located.
qr = qrcode.QRCode(
    version=None, # Let the library automatically choose the appropriate version
    error_correction=qrcode.constants.ERROR_CORRECT_H, # High error correction
    box_size=10,  # Size of each "box" (module) in pixels
    border=4,     # Border size (standard)
)
qr.add_data(data)
qr.make(fit=True)

# Create the QR code image
qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGBA")

# --- 2. Logo Loading and Resizing ---
logo_path = "icon.png" # File path for our logo
logo_img = Image.open(logo_path).convert("RGBA")

# Determine what percentage of the QR code the logo should cover (e.g., 20%)
# Be careful not to make it too large, as it may compromise the readability of the QR code.
logo_qr_ratio = 0.34 
qr_width, qr_height = qr_img.size
logo_size = int(qr_width * logo_qr_ratio)

# Resize the logo
logo_img = logo_img.resize((logo_size, logo_size), Image.LANCZOS) # Use Image.LANCZOS or Image.Resampling.LANCZOS instead of Image.ANTIALIAS

# --- 3. Placing the Logo in the Center of the QR Code ---
# Calculate the position of the top-left corner of the logo on the QR code
x_center = (qr_width - logo_size) // 2
y_center = (qr_height - logo_size) // 2

# Paste the logo onto the QR code
# mask=logo_img (if your logo has transparent parts, it keeps the background white)
qr_img.paste(logo_img, (x_center, y_center), logo_img)

# --- 4. Saving the QR Code ---
output_filename = "qrcode.png"
qr_img.save(output_filename)

print(f"QR code '{output_filename}' successfully saved.")