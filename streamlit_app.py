import streamlit as st

# Judul aplikasi
st.title("🧮 Kalkulator Sederhana")
st.write("Aplikasi kalkulator menggunakan Python dan Streamlit")


# Nama pembuat
st.markdown("### 👨‍💻 Aplikasi dibuat oleh Agung")




# Input angka
angka1 = st.number_input("Masukkan angka pertama", value=0.0)
angka2 = st.number_input("Masukkan angka kedua", value=0.0)

# Pilihan operator
operator = st.selectbox(
    "Pilih operasi",
    ("Penjumlahan (+)", "Pengurangan (-)", "Perkalian (*)", "Pembagian (/)")
)

# Tombol hitung
if st.button("Hitung"):

    if operator == "Penjumlahan (+)":
        hasil = angka1 + angka2
        st.success(f"Hasil: {angka1} + {angka2} = {hasil}")

    elif operator == "Pengurangan (-)":
        hasil = angka1 - angka2
        st.success(f"Hasil: {angka1} - {angka2} = {hasil}")

    elif operator == "Perkalian (*)":
        hasil = angka1 * angka2
        st.success(f"Hasil: {angka1} × {angka2} = {hasil}")

    elif operator == "Pembagian (/)":
        if angka2 != 0:
            hasil = angka1 / angka2
            st.success(f"Hasil: {angka1} ÷ {angka2} = {hasil}")
        else:
            st.error("Error: Tidak bisa dibagi dengan nol!")



