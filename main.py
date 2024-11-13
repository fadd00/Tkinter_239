import tkinter as tk

def hasil_prediksi():
    # Logika prediksi sederhana: selalu mengembalikan "Teknologi Informasi"
    hasil_label.config(text="Hasil Prediksi: Teknologi Informasi")

# Membuat jendela utama
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")

# Label judul
judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 16))
judul_label.grid(row=0, column=0, columnspan=2, pady=10)

# Membuat input untuk 10 mata pelajarans
input_labels = []
input_entries = []
for i in range(10):
    label = tk.Label(root, text=f"Nilai Mata Pelajaran {i+1}:")
    label.grid(row=i+1, column=0, padx=10, pady=5, sticky="e")
    entry = tk.Entry(root)
    entry.grid(row=i+1, column=1, padx=10, pady=5)
    
    input_labels.append(label)
    input_entries.append(entry)

# Tombol untuk hasil prediksi
prediksi_button = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi)
prediksi_button.grid(row=11, column=0, columnspan=2, pady=10)

# Label untuk menampilkan hasil prediksi
hasil_label = tk.Label(root, text="Hasil Prediksi: ")
hasil_label.grid(row=12, column=0, columnspan=2, pady=10)

# Menjalankan aplikasi
root.mainloop()