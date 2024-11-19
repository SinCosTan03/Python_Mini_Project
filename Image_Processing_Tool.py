from PIL import Image, ImageFilter, ImageOps

class ImageProcessor:
    def __init__(self):
        self.image = None  # Stores the loaded image

    def load_image(self, file_path):
        """Loads an image from the specified file path."""
        try:
            self.image = Image.open(file_path)
            print("✅ Image loaded successfully!")
        except Exception as e:
            print(f"❌ Error loading image: {e}")

    def save_image(self, output_path):
        """Saves the processed image to the specified file path."""
        if self.image:
            try:
                self.image.save(output_path)
                print(f"✅ Image saved at: {output_path}")
            except Exception as e:
                print(f"❌ Error saving image: {e}")
        else:
            print("❌ No image to save! Please load an image first.")

    def apply_grayscale(self):
        """Converts the image to grayscale."""
        if self.image:
            self.image = ImageOps.grayscale(self.image)
            print("✅ Grayscale filter applied!")
        else:
            print("❌ No image loaded!")

    def apply_sepia(self):
        """Applies a sepia filter to the image."""
        if self.image:
            sepia = self.image.convert("RGB")
            width, height = sepia.size
            pixels = sepia.load()

            for py in range(height):
                for px in range(width):
                    r, g, b = pixels[px, py]

                    # Sepia transformation
                    tr = int(0.393 * r + 0.769 * g + 0.189 * b)
                    tg = int(0.349 * r + 0.686 * g + 0.168 * b)
                    tb = int(0.272 * r + 0.534 * g + 0.131 * b)

                    pixels[px, py] = (min(255, tr), min(255, tg), min(255, tb))

            self.image = sepia
            print("✅ Sepia filter applied!")
        else:
            print("❌ No image loaded!")

    def apply_blur(self):
        """Applies a blur filter to the image."""
        if self.image:
            self.image = self.image.filter(ImageFilter.BLUR)
            print("✅ Blur filter applied!")
        else:
            print("❌ No image loaded!")

    def resize_image(self, width, height):
        """Resizes the image to the specified width and height."""
        if self.image:
            self.image = self.image.resize((width, height))
            print(f"✅ Image resized to {width}x{height}!")
        else:
            print("❌ No image loaded!")

    def rotate_image(self, angle):
        """Rotates the image by the specified angle."""
        if self.image:
            self.image = self.image.rotate(angle)
            print(f"✅ Image rotated by {angle} degrees!")
        else:
            print("❌ No image loaded!")

    def show_image(self):
        """Displays the current image."""
        if self.image:
            self.image.show()
        else:
            print("❌ No image loaded!")


# Main program
if __name__ == "__main__":
    processor = ImageProcessor()

    while True:
        print("\n--- Image Processing Tool ---")
        print("1. Load Image")
        print("2. Show Image")
        print("3. Apply Grayscale")
        print("4. Apply Sepia")
        print("5. Apply Blur")
        print("6. Resize Image")
        print("7. Rotate Image")
        print("8. Save Image")
        print("9. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            file_path = input("Enter the path of the image: ")
            processor.load_image(file_path)
        elif choice == "2":
            processor.show_image()
        elif choice == "3":
            processor.apply_grayscale()
        elif choice == "4":
            processor.apply_sepia()
        elif choice == "5":
            processor.apply_blur()
        elif choice == "6":
            try:
                width = int(input("Enter new width: "))
                height = int(input("Enter new height: "))
                processor.resize_image(width, height)
            except ValueError:
                print("❌ Please enter valid dimensions.")
        elif choice == "7":
            try:
                angle = int(input("Enter rotation angle (in degrees): "))
                processor.rotate_image(angle)
            except ValueError:
                print("❌ Please enter a valid angle.")
        elif choice == "8":
            output_path = input("Enter the output file path (e.g., output.jpg): ")
            processor.save_image(output_path)
        elif choice == "9":
            print("👋 Exiting the tool. Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please try again.")
