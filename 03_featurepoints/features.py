# NAMA: FABIAN RADENTA BANGUN
# NIM: 13522105
#
# Deskripsi/Fitur:
# Script ini menggunakan algoritma SIFT (Scale-Invariant Feature Transform) 
# untuk mendeteksi keypoints (titik fitur) pada gambar standar dan gambar bebas.
# Hasilnya divisualisasikan dalam bentuk gambar yang ditandai.

import cv2
import numpy as np
from skimage import data
import os
import csv

# KONFIGURASI
OUTPUT_DIR = "03_featurepoints/featurepoints_results/"
CUSTOM_IMAGE_DIR = "03_featurepoints/custom_dataset/"
CUSTOM_IMAGE_FILENAME = "free_image.png"


def detect_and_draw_features(image, base_name):
    print(f"  -> Mendeteksi fitur SIFT pada '{base_name}'...")

    # Init SIFT detector
    sift = cv2.SIFT_create()

    # Deteksi keypoints dan hitung descriptors
    # Keypoints adalah lokasi fitur, descriptors adalah vektor yang mendeskripsikan fitur tsb
    keypoints, descriptors = sift.detectAndCompute(image, None)

    # Gambar keypoints pada gambar asli
    # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS akan menggambar lingkaran dengan ukuran
    # dan orientasi yang sesuai dengan fitur yang terdeteksi.
    image_with_features = cv2.drawKeypoints(image, keypoints, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    # Simpan gambar hasil visualisasi
    output_path = os.path.join(OUTPUT_DIR, f"{base_name}_sift.png")
    cv2.imwrite(output_path, image_with_features)
    print(f"     - Visualisasi fitur disimpan di: {output_path}")
    
    # Siapkan data statistik untuk dikembalikan
    stats = {
        "image_name": base_name,
        "method": "SIFT",
        "feature_count": len(keypoints)
    }
    return stats


def main():
    print("--- Memulai Proses Deteksi Fitur (Modul 3) ---")

    # Pastikan folder output ada
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        print(f"Folder '{OUTPUT_DIR}' berhasil dibuat.")

    all_statistics = [] # Untuk menyimpan statistik semua gambar

    # Proses gambar-gambar standar
    print("\n[1] Memproses gambar standar dari scikit-image...")
    
    img_cameraman = data.camera()
    stats_cameraman = detect_and_draw_features(img_cameraman, "cameraman")
    all_statistics.append(stats_cameraman)
    
    img_coins = data.coins()
    stats_coins = detect_and_draw_features(img_coins, "coins")
    all_statistics.append(stats_coins)

    img_checkerboard = data.checkerboard()
    stats_checkerboard = detect_and_draw_features(img_checkerboard, "checkerboard")
    all_statistics.append(stats_checkerboard)

    # Proses gambar pribadi
    print("\n[2] Memproses gambar pribadi...")
    custom_image_path = os.path.join(CUSTOM_IMAGE_DIR, CUSTOM_IMAGE_FILENAME)
    
    if not os.path.exists(custom_image_path):
        print(f"!!! ERROR: Gambar pribadi tidak ditemukan di '{custom_image_path}'")
        print("--- Proses Selesai dengan Error ---")
        return

    img_pribadi_color = cv2.imread(custom_image_path)
    img_pribadi_gray = cv2.cvtColor(img_pribadi_color, cv2.COLOR_BGR2GRAY)
    stats_pribadi = detect_and_draw_features(img_pribadi_gray, "free_image")
    all_statistics.append(stats_pribadi)

    # Tulis semua statistik ke dalam satu file CSV
    stats_file_path = os.path.join(OUTPUT_DIR, "feature_statistics.csv")
    try:
        with open(stats_file_path, 'w', newline='') as csvfile:
            # header untuk file CSV
            fieldnames = ["image_name", "method", "feature_count"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(all_statistics)
        print(f"\n[3] File statistik berhasil disimpan di: {stats_file_path}")
    except IOError:
        print("!!! ERROR: Gagal menulis file statistik.")

    print("\n--- Semua Proses Deteksi Fitur Selesai ---")


if __name__ == "__main__":
    main()