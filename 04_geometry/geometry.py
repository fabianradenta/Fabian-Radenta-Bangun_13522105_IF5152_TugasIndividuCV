# NAMA: FABIAN RADENTA BANGUN
# NIM: 13522105
#
# Deskripsi/Fitur:
# Script ini men-generate gambar papan catur sintetis,
# kemudian mendeteksi sudut-sudut internalnya, memvisualisasikannya,
# dan menyimpan koordinat sudut tersebut ke dalam file teks.

import cv2
import numpy as np
import os

# KONFIGURASI
OUTPUT_DIR = "04_geometry/geometry_results/"
# Kita akan buat papan catur dengan 9x6 kotak (ada 8x5 sudut internal)
PATTERN_SIZE = (8, 5) 
SQUARE_SIZE_PX = 50 # size setiap kotak dalam piksel


def generate_custom_checkerboard(pattern_size, square_size):
    """
    Membuat gambar papan catur sintetis dengan border putih yang cukup.
    Border ini sangat penting agar OpenCV mudah mendeteksi sudut terluar.
    """
    # Jumlah kotak = jumlah sudut+1
    board_width_squares = pattern_size[0] + 1
    board_height_squares = pattern_size[1] + 1
    
    # Tambahkan margin di sekeliling papan catur
    margin_px = square_size 
    
    img_width = board_width_squares * square_size + 2 * margin_px
    img_height = board_height_squares * square_size + 2 * margin_px
    
    # canvas putih
    checkerboard = np.full((img_height, img_width), 255, dtype=np.uint8)
    
    # Isi kotak-kotak hitam
    for y in range(board_height_squares):
        for x in range(board_width_squares):
            if (x + y) % 2 == 0:
                # Tentukan koordinat sudut kiri atas dan kanan bawah kotak
                start_x = x * square_size + margin_px
                start_y = y * square_size + margin_px
                end_x = start_x + square_size
                end_y = start_y + square_size
                # Isi hitam
                cv2.rectangle(checkerboard, (start_x, start_y), (end_x, end_y), 0, -1)
                
    return checkerboard


def find_and_draw_chessboard_corners(image, pattern_size):
    print(f"  -> Mencari sudut papan catur dengan pola {pattern_size}...")

    # OpenCV memerlukan gambar 8-bit grayscale untuk deteksi ini
    image_8bit = image 

    # temukan sudut-sudut
    ret, corners = cv2.findChessboardCorners(image_8bit, pattern_size, None)

    # Path untuk menyimpan hasil
    output_image_path = os.path.join(OUTPUT_DIR, "checkerboard_corners.png")
    output_matrix_path = os.path.join(OUTPUT_DIR, "checkerboard_matrix.txt")

    if ret:
        print("     - Pola papan catur berhasil ditemukan!")
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
        cv2.cornerSubPix(image_8bit, corners, (11, 11), (-1, -1), criteria)
        
        image_color_with_corners = cv2.cvtColor(image_8bit, cv2.COLOR_GRAY2BGR)
        cv2.drawChessboardCorners(image_color_with_corners, pattern_size, corners, ret)
        
        cv2.imwrite(output_image_path, image_color_with_corners)
        print(f"     - Gambar visualisasi disimpan di: {output_image_path}")
        
        corner_coordinates = corners.reshape(-1, 2)
        np.savetxt(output_matrix_path, corner_coordinates, fmt='%.4f', 
                   header=f"Koordinat Sudut (x, y) untuk pola {pattern_size}",
                   delimiter=',')
        print(f"     - Matriks koordinat disimpan di: {output_matrix_path}")
    else:
        print("     - !!! Gagal menemukan pola papan catur.")
        cv2.imwrite(output_image_path, image_8bit)


def main():
    print("--- Memulai Proses Geometri (Modul 4) ---")
    
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        print(f"Folder '{OUTPUT_DIR}' berhasil dibuat.")

    # Generate gambar papan catur
    print("  -> Men-generate gambar papan catur sintetis...")
    custom_checkerboard = generate_custom_checkerboard(PATTERN_SIZE, SQUARE_SIZE_PX)
    
    # menyimpan gambar papan catur yang digenerate
    cv2.imwrite(os.path.join(OUTPUT_DIR, "generated_checkerboard.png"), custom_checkerboard)

    # Jalankan fungsi deteksi pada gambar yang baru dibuat
    find_and_draw_chessboard_corners(custom_checkerboard, PATTERN_SIZE)

    print("\n--- Semua Proses Geometri Selesai ---")
if __name__ == "__main__":
    main()