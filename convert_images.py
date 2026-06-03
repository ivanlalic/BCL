import os
import sys
import subprocess

# Step 1: Ensure Pillow is installed
try:
    from PIL import Image
except ImportError:
    print("Pillow library not found. Installing now...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pillow"])
        from PIL import Image
        print("Pillow installed successfully!")
    except Exception as e:
        print(f"Failed to install Pillow: {e}")
        print("Please run: pip install pillow")
        sys.exit(1)

def convert_to_webp(quality=85, delete_original=False):
    # Scan current folder
    current_dir = os.path.dirname(os.path.abspath(__file__))
    files = os.listdir(current_dir)
    image_extensions = ('.png', '.jpg', '.jpeg', '.bmp', '.tiff')
    
    converted_count = 0
    
    print(f"\nScanning folder: {current_dir}")
    print(f"Converting images to WebP (Quality: {quality}%)...")
    
    for filename in files:
        if filename.lower().endswith(image_extensions):
            source_path = os.path.join(current_dir, filename)
            # Create webp name
            base_name = os.path.splitext(filename)[0]
            target_filename = f"{base_name}.webp"
            target_path = os.path.join(current_dir, target_filename)
            
            # Skip if already a webp with that name exists to avoid overwriting or redundant work
            # unless the user wants to force it.
            try:
                img = Image.open(source_path)
                # Convert RGBA to RGB if saving as JPEG, but WebP supports RGBA! So we can save directly.
                img.save(target_path, 'WEBP', quality=quality)
                
                original_size = os.path.getsize(source_path) / 1024
                webp_size = os.path.getsize(target_path) / 1024
                saving = original_size - webp_size
                saving_pct = (saving / original_size) * 100 if original_size > 0 else 0
                
                print(f"[OK] Converted: {filename} ({original_size:.1f} KB) -> {target_filename} ({webp_size:.1f} KB) | Saved: {saving:.1f} KB ({saving_pct:.1f}%)")
                converted_count += 1
                
                if delete_original:
                    os.remove(source_path)
                    print(f"  Deleted original: {filename}")
                    
            except Exception as e:
                print(f"[ERROR] Failed to convert {filename}: {e}")
                
    print(f"\nDone! Successfully converted {converted_count} images.")

if __name__ == "__main__":
    print("=" * 60)
    print("      IMAGE TO WEBP CONVERTER (OPTIMIZED FOR WEB/CRO)")
    print("=" * 60)
    
    # Prompt for options
    ans = input("Do you want to delete original images after conversion? (y/n) [default: n]: ").strip().lower()
    delete_orig = ans == 'y'
    
    q_ans = input("Set WebP quality (1-100) [default: 85]: ").strip()
    quality = 85
    if q_ans.isdigit():
        quality = int(q_ans)
        
    convert_to_webp(quality=quality, delete_original=delete_orig)
    input("\nPress Enter to exit...")
