from PIL import Image, ImageDraw, ImageFont
import os
import sys

CHARSETS = {
    "standard": "@%#*+=-:. ",
    "simple": "@#=- ",
    "complex": "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. ",
    "blocks": "\u2588\u2593\u2592\u2591 ",
    "numeric": "0123456789 "
}

def image_to_ascii(image_path, output_width=100, charset="standard", invert=False):
    try:
        img = Image.open(image_path)
        img = img.convert("L")

        width, height = img.size
        ratio = height / width / 1.65
        new_height = int(output_width * ratio)

        img = img.resize((output_width, new_height))

        pixels = img.getdata()
        chars = CHARSETS.get(charset, CHARSETS["standard"])

        if invert:
            chars = chars[::-1]

        ascii_str = ""
        for i, pixel in enumerate(pixels):
            ascii_str += chars[int(pixel / 255 * (len(chars) - 1))]
            if (i + 1) % output_width == 0:
                ascii_str += "\n"

        return ascii_str

    except Exception as e:
        raise Exception(f"Error processing image: {e}")

def text_to_ascii(text, style="banner"):
    if style == "banner":
        return text_to_banner_ascii(text)
    elif style == "small":
        return text_to_small_ascii(text)
    else:
        return text_to_banner_ascii(text)

def text_to_banner_ascii(text):
    font_3x5 = {
        'A': [" ███ ", "█   █", "█████", "█   █", "█   █"],
        'B': ["████ ", "█   █", "████ ", "█   █", "████ "],
        'C': ["█████", "█    ", "█    ", "█    ", "█████"],
        'D': ["████ ", "█   █", "█   █", "█   █", "████ "],
        'E': ["█████", "█    ", "███  ", "█    ", "█████"],
        'F': ["█████", "█    ", "███  ", "█    ", "█    "],
        'G': ["█████", "█    ", "█ ███", "█   █", "█████"],
        'H': ["█   █", "█   █", "█████", "█   █", "█   █"],
        'I': ["█████", "  █  ", "  █  ", "  █  ", "█████"],
        'J': ["█████", "    █", "    █", "█   █", " ███ "],
        'K': ["█   █", "█  █ ", "███  ", "█  █ ", "█   █"],
        'L': ["█    ", "█    ", "█    ", "█    ", "█████"],
        'M': ["█   █", "██ ██", "█ █ █", "█   █", "█   █"],
        'N': ["█   █", "██  █", "█ █ █", "█  ██", "█   █"],
        'O': [" ███ ", "█   █", "█   █", "█   █", " ███ "],
        'P': ["████ ", "█   █", "████ ", "█    ", "█    "],
        'Q': [" ███ ", "█   █", "█ █ █", "█  █ ", " ██ █"],
        'R': ["████ ", "█   █", "████ ", "█  █ ", "█   █"],
        'S': ["█████", "█    ", " ███ ", "    █", "█████"],
        'T': ["█████", "  █  ", "  █  ", "  █  ", "  █  "],
        'U': ["█   █", "█   █", "█   █", "█   █", " ███ "],
        'V': ["█   █", "█   █", "█   █", " █ █ ", "  █  "],
        'W': ["█   █", "█   █", "█ █ █", "██ ██", "█   █"],
        'X': ["█   █", " █ █ ", "  █  ", " █ █ ", "█   █"],
        'Y': ["█   █", " █ █ ", "  █  ", "  █  ", "  █  "],
        'Z': ["█████", "   █ ", "  █  ", " █   ", "█████"],
        '0': [" ███ ", "█   █", "█ █ █", "█   █", " ███ "],
        '1': ["  █  ", " ██  ", "  █  ", "  █  ", "█████"],
        '2': [" ███ ", "█   █", "   █ ", "  █  ", "█████"],
        '3': ["████ ", "    █", " ███ ", "    █", "████ "],
        '4': ["█   █", "█   █", "█████", "    █", "    █"],
        '5': ["█████", "█    ", "████ ", "    █", "████ "],
        '6': [" ███ ", "█    ", "█████", "█   █", " ███ "],
        '7': ["█████", "    █", "   █ ", "  █  ", "  █  "],
        '8': [" ███ ", "█   █", " ███ ", "█   █", " ███ "],
        '9': [" ███ ", "█   █", " ████", "    █", " ███ "],
        '!': ["█", "█", "█", " ", "█"],
        '?': [" ███ ", "█   █", "  █  ", "     ", "  █  "],
        '.': [" ", " ", " ", " ", "█"],
        ',': [" ", " ", " ", "█", " "],
        '-': ["     ", "     ", "████ ", "     ", "     "],
        '+': ["     ", "  █  ", "████ ", "  █  ", "     "],
        '=': ["     ", "████ ", "     ", "████ ", "     "],
        ' ': ["     ", "     ", "     ", "     ", "     "],
    }

    result = []
    for line_idx in range(5):
        line = ""
        for char in text:
            upper_char = char.upper()
            if upper_char in font_3x5:
                line += font_3x5[upper_char][line_idx] + " "
            else:
                line += "????? "
        result.append(line)

    return "\n".join(result)

def text_to_small_ascii(text):
    font_small = {
        'A': ["█", "█", "██", "█", "█"],
        'B': ["██", "█", "██", "█", "██"],
        'C': ["██", "█", "█", "█", "██"],
        'D': ["██", "█", "█", "█", "██"],
        'E': ["██", "█", "██", "█", "██"],
        'F': ["██", "█", "██", "█", "█"],
        'G': ["██", "█", "██", "█", "██"],
        'H': ["█", "█", "██", "█", "█"],
        'I': ["██", "█", "█", "█", "██"],
        'J': ["██", " ", " ", "█", "██"],
        'K': ["█", "█", "██", "█", "█"],
        'L': ["█", "█", "█", "█", "██"],
        'M': ["█", "██", "█", "█", "█"],
        'N': ["█", "██", "█", "█", "█"],
        'O': ["██", "█", "█", "█", "██"],
        'P': ["██", "█", "██", "█", "█"],
        'Q': ["██", "█", "█", "█", " █"],
        'R': ["██", "█", "██", "█", "█"],
        'S': ["██", "█", "██", " ", "██"],
        'T': ["██", "█", "█", "█", "█"],
        'U': ["█", "█", "█", "█", "██"],
        'V': ["█", "█", "█", "█", "█"],
        'W': ["█", "█", "█", "█", "█"],
        'X': ["█", "█", " ", "█", "█"],
        'Y': ["█", "█", " ", "█", "█"],
        'Z': ["██", " ", "█", " ", "██"],
        '0': ["██", "█", "█", "█", "██"],
        '1': ["█", "█", "█", "█", "█"],
        '2': ["██", " ", "█", " ", "██"],
        '3': ["██", " ", "██", " ", "██"],
        '4': ["█", "█", "██", " ", " "],
        '5': ["██", "█", "██", " ", "██"],
        '6': ["██", "█", "██", "█", "██"],
        '7': ["██", " ", " ", " ", " "],
        '8': ["██", "█", "██", "█", "██"],
        '9': ["██", "█", "██", " ", " "],
        '!': ["█", "█", "█", " ", "█"],
        '?': ["██", " ", "█", " ", " "],
        '.': [" ", " ", " ", " ", "█"],
        '-': [" ", " ", "██", " ", " "],
    }

    result = []
    for line_idx in range(5):
        line = ""
        for char in text.upper():
            if char in font_small:
                line += font_small[char][line_idx]
            else:
                line += "?"
            line += " "
        result.append(line)
    return "\n".join(result)

def generate_sample_image():
    size = 200
    img = Image.new("RGB", (size, size), "white")
    draw = ImageDraw.Draw(img)

    draw.ellipse([20, 20, 180, 180], fill="blue")
    draw.ellipse([50, 50, 90, 90], fill="white")
    draw.ellipse([110, 50, 150, 90], fill="white")

    arc_y = 120
    draw.arc([40, arc_y-30, 160, arc_y+30], 0, 180, fill="black", width=3)

    return img

def save_ascii(ascii_text, filename="output.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(ascii_text)
    print(f"✓ Saved to: {os.path.abspath(filename)}")

def show_banner():
    banner = """
╔══════════════════════════════════════════╗
║                                          ║
║       ██████╗ ██╗   ██╗ █████╗           ║
║      ██╔════╝ ██║   ██║██╔══██╗          ║
║      ██║  ███╗██║   ██║███████║          ║
║      ██║   ██║██║   ██║██╔══██║          ║
║      ╚██████╔╝╚██████╔╝██║  ██║          ║
║       ╚═════╝  ╚═════╝ ╚═╝  ╚═╝          ║
║                                          ║
║           A R T   G E N E R A T O R      ║
║                                          ║
╚══════════════════════════════════════════╝
"""
    return banner

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(show_banner())
    print()

    while True:
        print("=" * 50)
        print("  OPTIONS:")
        print("=" * 50)
        print("  [1] Image to ASCII Art")
        print("  [2] Text to ASCII Banner")
        print("  [3] Generate Sample & Convert")
        print("  [4] Help & Info")
        print("  [0] Exit")
        print("=" * 50)
        print()

        choice = input("  Select option: ").strip()

        if choice == "1":
            print("\n--- Image to ASCII ---\n")
            path = input("  Enter image path: ").strip().strip('"')

            if not os.path.exists(path):
                print(f"\n  ✗ File not found: {path}")
                input("\n  Press Enter to continue...")
                continue

            try:
                width = int(input("  Output width (default 80): ") or "80")
                charset = input("  Charset [standard/simple/complex/blocks]: ").strip()
                if not charset:
                    charset = "standard"

                invert = input("  Invert colors? (y/n): ").lower() == "y"

                print("\n  Converting...")
                ascii_art = image_to_ascii(path, width, charset, invert)

                print("\n" + "-" * 60)
                print(ascii_art)
                print("-" * 60)

                save_opt = input("\n  Save to file? (y/n): ").lower()
                if save_opt == "y":
                    filename = input("  Filename (default output.txt): ") or "output.txt"
                    save_ascii(ascii_art, filename)

            except ValueError:
                print("\n  ✗ Invalid number!")
            except Exception as e:
                print(f"\n  ✗ Error: {e}")

            input("\n  Press Enter to continue...")

        elif choice == "2":
            print("\n--- Text to ASCII Banner ---\n")
            text = input("  Enter your text: ").strip()

            if not text:
                print("\n  ✗ No text entered!")
                input("\n  Press Enter to continue...")
                continue

            style = input("  Style [banner/small]: ").strip() or "banner"

            ascii_art = text_to_ascii(text, style)

            print("\n" + "=" * 60)
            print(ascii_art)
            print("=" * 60)

            save_opt = input("\n  Save to file? (y/n): ").lower()
            if save_opt == "y":
                filename = input("  Filename (default output.txt): ") or "output.txt"
                save_ascii(ascii_art, filename)

            input("\n  Press Enter to continue...")

        elif choice == "3":
            print("\n--- Generate Sample Image ---\n")
            print("  Creating a sample smiley face image...")

            img = generate_sample_image()
            sample_path = "sample.png"
            img.save(sample_path)
            print(f"  ✓ Sample saved: {sample_path}")

            print("\n  Converting to ASCII...")
            ascii_art = image_to_ascii(sample_path, 60, "standard")

            print("\n" + "-" * 60)
            print(ascii_art)
            print("-" * 60)

            save_opt = input("\n  Save ASCII art? (y/n): ").lower()
            if save_opt == "y":
                save_ascii(ascii_art, "sample_ascii.txt")

            del_opt = input("\n  Delete sample image? (y/n): ").lower()
            if del_opt == "y":
                os.remove(sample_path)
                print("  ✓ Sample image deleted.")

            input("\n  Press Enter to continue...")

        elif choice == "4":
            print("\n" + "=" * 50)
            print("  HELP & INFORMATION")
            print("=" * 50)
            print("""
  Supported formats: JPG, PNG, BMP, GIF, etc.

  Charsets explained:
    standard  - Good balance of detail (@%#*+=-:. )
    simple    - Minimal characters (@#=- )
    complex   - Maximum detail (70+ characters)
    blocks    - Unicode block characters (▓▒░ )
    numeric   - Numbers only (0123456789 )

  Tips:
    - Smaller width = faster but less detail
    - Use 'invert' for dark backgrounds
    - Try different charsets for unique looks!
""")
            input("\n  Press Enter to continue...")

        elif choice == "0":
            print("\n  Thanks for using ASCII Art Generator! 👋\n")
            break

        else:
            print("\n  ✗ Invalid option!")
            input("\n  Press Enter to continue...")

        os.system('cls' if os.name == 'nt' else 'clear')
        print(show_banner())

if __name__ == "__main__":
    main()
