from PIL import Image
img = Image.new("RGB", (1376, 256))
pix = img.load()

for i in range(256):
    for y, j in enumerate(barcode):
        color = (255, 255, 255) if j == "w" else (0, 0, 0)
        pix[y,i] = color

img.save("barcode-analysis.png")
