###Usage

Run the script from your terminal:
```Bash
python generate_qr.py
```
⚙️ Customization

You can customize the output by editing the variables at the beginning of the script:
Variable	Description
data	The URL or text the QR code should target.
logo_path	The filename of your logo (Default: "icon.png").
logo_qr_ratio	The ratio of the logo's size to the QR code's width. (Recommended: 0.25 to 0.35)
output_filename	The desired name for the saved file (Default: "qrcode.png").

⚠️ Important Note

    Adjust the logo size (logo_qr_ratio) carefully. The high error correction (ERROR_CORRECT_H) tolerates ≈30% data loss.

    Always test the generated QR code with multiple scanners!
