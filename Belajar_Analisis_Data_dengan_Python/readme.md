# Dashboard Polusi Udara

Ini adalah sebuah aplikasi dashboard yang menunjukkan data polusi udara. Aplikasi ini menampilkan analisis polusi udara tahunan dan musiman, serta memungkinkan user untuk melihat korelasi antar kolom.

## Cara Menggunakan

1. **Instalasi Dependencies**
	Pastikan kamu memiliki Streamlit dan semua dependensi lainnya yang dibutuhkan. Kamu dapat menginstalnya dengan perintah berikut:
	```bash
   	pip install streamlit matplotlib seaborn pandas
	```
2. **Menjalankan Aplikasi**
	Jalankan aplikasi dengan menggunakan perintah berikut di terminal atau command prompt setelah membuka folder dimana dashboard.py berada:

    	streamlit run dashboard.py

3. **Penggunaan Dashboard**
        Setelah aplikasi berjalan, akan terlihat dashboard dengan beberapa pilihan.
        Pilih Kolom: Pilih salah satu atau banyak kolom polutan (PM2.5, PM10, SO2, NO2, CO, O3) yang ingin dianalisis dari menu multiselect.
        Polusi per-tahun:
        	untuk melihat data polusi dapat dipilih mode "normal" atau "persentase perubahan".
            	Mode normal menampilkan nilai polusi per tahun seperti biasa, sedangkan mode persentase perubahan menampilkan perubahan dari satu tahun ke tahun berikutnya.
        Polusi per-musim:
            	dapat dipilih antara mode "normal" atau "normalized" untuk melihat plot polusi per musim. Mode normal menunjukkan nilai polusi rata-rata per musim, sedangkan mode ternormalisasi menunjukkan data yang sudah dinormalisasi sehingga tidak lebih kecil dari 0 dan tidak lebih besar dari 1.
        Korelasi antar data:
            Lewat dashboard ini bisa menentukan nilai korelasi. Tabel akan menunjukkan korelasi antar variabel (polutan, suhu, tekanan, dll.) yang memiliki korelasi lebih besar atau sama dengan nilai threshold yang bisa ditentukan pada dashboard juga.

## Struktur Data

Aplikasi ini menggunakan beberapa dataset terkait polusi udara:

    data_clean.csv: Data utama yang berisi informasi polusi harian berdasarkan waktu dan stasiun.
    normalized_seasonal_avg_pollution.csv: Data rata-rata polusi musiman yang sudah dinormalisasi.
    seasonal_avg_pollution.csv: Data rata-rata polusi musiman.
    yearly_avg_pollution.csv: Data rata-rata polusi tahunan.
    yearly_avg_pollution_percentage_increase.csv: Data persentase peningkatan rata-rata polusi tahunan.

### Kolom yang Tersedia

Beberapa kolom dalam dataset termasuk:

    PM2.5, PM10, SO2, NO2, CO, O3: Berbagai jenis polutan.
    TEMP: Suhu udara (°C).
    PRES: Tekanan atmosfer (hPa).
    DEWP: Titik embun (°C).
    RAIN: Curah hujan (mm).
    WSPM: Kecepatan angin (m/s).

## Catatan

    Jika gagal load dengan data lokal, aplikasi akan mencoba download data dari GitHub.
    Sudah dicoba untuk dihost di streamlit cloud tapi program tidak bisa mengambil data baik dari lokal maupun dari GitHub
	
