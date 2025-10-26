# NAMA: FABIAN RADENTA BANGUN
# NIM: 13522105
# 
# Deskripsi/Fitur:
# Script ini menerapkan dua metode edge detection Sobel dan Canny pada 
# gambar standar (cameraman, coins, dan checkerboard) dan satu gambar bebas.
# Hasilnya disimpan dalam format .png di folder 'edge_results'.

import cv2
import numpy as np
from skimage import data
import os

# KONFIGURASI
OUTPUT_DIR = "02_edge/edge_results/"
CUSTOM_IMAGE_DIR = "02_edge/custom_dataset/"
CUSTOM_IMAGE_FILENAME = "free_image.png"


def run_edge_detection_on_image(image, base_name):
    print(f"  -> Memproses '{base_name}'...")
    # Metode 1: Sobel Operator
    # Menghitung gradien pada sumbu X dan Y.
    # Menggunakan cv2.CV_64F untuk presisi agar tidak ada nilai yang terpotong.
    sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)
    sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)
    
    # Menghitung magnitudo gradien
    sobel_magnitude = np.sqrt(sobel_x**2 + sobel_y**2)
    
    # Normalisasi hasil ke rentang 0-255 agar dapat disimpan sebagai gambar
    sobel_result = cv2.normalize(sobel_magnitude, None,0,255, cv2.NORM_MINMAX).astype(np.uint8)
    
    # Simpan hasil Sobel
    output_path_sobel = os.path.join(OUTPUT_DIR, f"{base_name}_sobel.png")
    cv2.imwrite(output_path_sobel, sobel_result)
    print(f"     - Hasil Sobel disimpan di: {output_path_sobel}")

    # Metode 2: Canny Edge Detector
    # Threshold bawah (100): Tepi dengan gradien di bawah ini akan diabaikan.
    # Threshold atas (200): Tepi dengan gradien di atas ini pasti dianggap tepi.
    # Tepi di antara keduanya akan dianggap tepi jika terhubung dengan tepi yang kuat.
    canny_result = cv2.Canny(image, 100, 200)
    
    # Simpan hasil Canny
    output_path_canny = os.path.join(OUTPUT_DIR, f"{base_name}_canny.png")
    cv2.imwrite(output_path_canny, canny_result)
    print(f"     - Hasil Canny disimpan di: {output_path_canny}")


def main():
    print("--- Memulai Proses Deteksi Tepi (Modul 2) ---")
    
    # Pastikan folder output ada
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        print(f"Folder '{OUTPUT_DIR}' berhasil dibuat.")

    # Proses gambar-gambar standar
    print("\n[1] Memproses gambar standar dari scikit-image...")
    img_cameraman = data.camera()
    run_edge_detection_on_image(img_cameraman, "cameraman")
    
    img_coins = data.coins()
    run_edge_detection_on_image(img_coins, "coins")

    img_checkerboard = data.checkerboard()
    run_edge_detection_on_image(img_checkerboard, "checkerboard")

    # Proses gambar custom
    print("\n[2] Memproses gambar pribadi...")
    custom_image_path = os.path.join(CUSTOM_IMAGE_DIR, CUSTOM_IMAGE_FILENAME)
    
    if not os.path.exists(custom_image_path):
        print(f"!!! ERROR: Gambar pribadi tidak ditemukan di '{custom_image_path}'")
        print("--- Proses Selesai dengan Error ---")
        return

    img_pribadi_color = cv2.imread(custom_image_path)
    # Convert ke grayscale
    img_pribadi_gray = cv2.cvtColor(img_pribadi_color, cv2.COLOR_BGR2GRAY)
    run_edge_detection_on_image(img_pribadi_gray, "free_image")
    
    print("\n--- Semua Proses Deteksi Tepi Selesai ---")

if __name__ == "__main__":
    main()