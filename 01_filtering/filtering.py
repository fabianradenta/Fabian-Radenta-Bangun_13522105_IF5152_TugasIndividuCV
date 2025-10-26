# NAMA: FABIAN RADENTA BANGUN
# NIM: 13522105
#
# Deskripsi/Fitur:
# Menerapkan dua jenis filter, yaitu Gaussian Blur dan Median Blur pada 
# gambar standar (cameraman, coins) dan satu gambar bebas.
# Hasilnya disimpan dalam format .png di folder 'filtering_results'.

import cv2
import numpy as np
from skimage import data
import os

# KONFIGURASI
OUTPUT_DIR = "01_filtering/filtering_results/"
CUSTOM_IMAGE_DIR = "01_filtering/custom_image_dataset/" 
CUSTOM_IMAGE_FILENAME = "free_image.png"


def apply_filters_on_image(image, base_name):
    print(f"  -> Menerapkan filter pada '{base_name}'...")

    # Filter 1: Gaussian Blur
    # Parameter: (sumber_gambar, ukuran_kernel, sigmaX)
    # Ukuran harus ganjil. semakin besar, semakin blur
    gaussian_result = cv2.GaussianBlur(image, (5, 5), 0)
    
    # Simpan hasil
    output_path_gaussian = os.path.join(OUTPUT_DIR, f"{base_name}_gaussian.png")
    cv2.imwrite(output_path_gaussian, gaussian_result)
    print(f"     - Hasil Gaussian Blur disimpan di: {output_path_gaussian}")

    # Filter 2: Median Blur
    # Parameter: (sumber_gambar, ukuran_kernel)
    # Ukuran kernel (misal: 5) harus bilangan bulat ganjil.
    median_result = cv2.medianBlur(image, 5)
    
    # Simpan hasil Median Blur
    output_path_median = os.path.join(OUTPUT_DIR, f"{base_name}_median.png")
    cv2.imwrite(output_path_median, median_result)
    print(f"     - Hasil Median Blur disimpan di: {output_path_median}")


def main():
    """
    Fungsi utama untuk menjalankan seluruh proses filtering.
    """
    print("--- Memulai Proses Filtering (Modul 1) ---")
    
    # Pastikan folder output ada
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        print(f"Folder '{OUTPUT_DIR}' berhasil dibuat.")

    # Proses gambar-gambar standar
    print("\n[1] Memproses gambar standar dari scikit-image...")
    img_cameraman = data.camera()
    apply_filters_on_image(img_cameraman, "cameraman")
    
    img_coins = data.coins()
    apply_filters_on_image(img_coins, "coins")

    # Proses gambar pribadi
    print("\n[2] Memproses gambar pribadi...")
    custom_image_path = os.path.join(CUSTOM_IMAGE_DIR, CUSTOM_IMAGE_FILENAME)
    
    if not os.path.exists(custom_image_path):
        print(f"!!! ERROR: Gambar pribadi tidak ditemukan di '{custom_image_path}'")
        print("--- Proses Selesai dengan Error ---")
        return

    img_pribadi_color = cv2.imread(custom_image_path)
    img_pribadi_gray = cv2.cvtColor(img_pribadi_color, cv2.COLOR_BGR2GRAY)
    apply_filters_on_image(img_pribadi_gray, "free_image")
    
    print("\n--- Semua Proses Filtering Selesai ---")

if __name__ == "__main__":
    main()