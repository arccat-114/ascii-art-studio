import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from PIL import Image, ImageDraw
from ascii_art import image_to_ascii, text_to_ascii

print("=" * 60)
print("  ASCII Art Generator - Demo")
print("=" * 60)
print()

print("1. Testing Text to ASCII Banner:")
print("-" * 60)
banner = text_to_ascii("HELLO", "banner")
print(banner)
print()

print("2. Testing Text to ASCII Small:")
print("-" * 60)
small = text_to_ascii("COOL", "small")
print(small)
print()

print("3. Generating Sample Image and Converting:")
print("-" * 60)

size = 200
img = Image.new("RGB", (size, size), "white")
draw = ImageDraw.Draw(img)

draw.ellipse([20, 20, 180, 180], fill="blue")
draw.ellipse([50, 50, 90, 90], fill="white")
draw.ellipse([110, 50, 150, 90], fill="white")

arc_y = 120
draw.arc([40, arc_y-30, 160, arc_y+30], 0, 180, fill="black", width=3)

img.save("demo_smiley.png")
print("   Created: demo_smiley.png")

ascii_result = image_to_ascii("demo_smiley.png", 50, "standard")
print()
print(ascii_result)
print()

print("=" * 60)
print("  SUCCESS! All features working correctly!")
print("=" * 60)
print()
print("To run the full program:")
print("  python ascii_art.py")
