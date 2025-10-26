# Simple Integrated Application
> *Source Code* ini dibuat untuk memenuhi Tugas Individu 1 Mata kuliah IF5152 Visi Komputer yaitu "Aplikasi Sederhana Integratif: Materi Minggu 3-6".

## Deskripsi Singkat Program
Program ini merupakan kumpulan skrip Python yang mengimplementasikan empat teknik fundamental dalam Computer Vision:
1. **Image Filtering**: Menerapkan dua jenis filter, yaitu **Gaussian Blur** untuk menghaluskan gambar dan **Median Blur** untuk menghilangkan noise.
2. **Edge Detection**: Menerapkan dua metode *edge detection*, yaitu **Operator Sobel** untuk menghitung gradien dan **Algoritma Canny** untuk deteksi tepi yang presisi.
3. **Feature Point Detection**: Menggunakan algoritma **SIFT (Scale-Invariant Feature Transform)** untuk mendeteksi titik-titik fitur (keypoints) pada gambar.
4. **Camera Geometry**: Mendemonstrasikan deteksi pola geometris dengan **menemukan sudut-sudut internal pada papan catur**.

Program ini disusun dalam empat modul terpisah, di mana setiap modul bertanggung jawab untuk satu tugas spesifik. Setiap modul memproses serangkaian gambar input standar (`cameraman`, `coins`, `checkerboard`) dan satu gambar *custom*, kemudian menghasilkan output berupa gambar yang telah diproses serta file data pendukung (`.csv` atau `.txt`) untuk analisis lebih lanjut.

## Prasyarat
- Python 3.8+
- pip

## Cara Menjalankan Program
1. **Clone Repository**
   ```bash
   git clone https://github.com/fabianradenta/Fabian-Radenta-Bangun_13522105_IF5152_TugasIndividuCV.git
   cd Fabian-Radenta-Bangun_13522105_IF5152_TugasIndividuCV
   ```
2.  **Buat Virtual Environment**<br>
    Buka terminal di direktori utama proyek dan jalankan perintah berikut untuk membuat dan mengaktifkan virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate # MacOS/Linux
    .\venv\Scripts\activate  # Windows
    ```

3.  ***Install* Dependensi**<br>
    *Install* semua library yang tercantum dalam file `requirements.txt`.
    ```bash
    pip install -r requirements.txt
    ```

## Author
Nama : Fabian Radenta Bangun<br>
NIM : 13522105<br>
Program Studi : Teknik Informatika<br>