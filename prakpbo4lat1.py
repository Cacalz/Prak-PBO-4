class DataMahasiswa:
    class Mahasiswa:
        def __init__(self, nama, nim, nilai):
            self.nama = nama
            self.nim = nim
            self.nilai = nilai

        #staticmethod
        def print_data_mahasiswa(mahasiswa):
            i = 1
            for mhs in mahasiswa:
                print("--- Data Mahasiswa", i, "---")
                print("Nama:", mhs.nama)
                print("NIM:", mhs.nim)
                print("Nilai:", mhs.nilai)
                print()
                i += 1

    def __init__(self):
        pass

    #staticmethod
    def main():
        mahasiswa = [
            DataMahasiswa.Mahasiswa("Calista Azzahra", "064002300008", 100),
            DataMahasiswa.Mahasiswa("Fairuz Maulidya", "064002030018", 99),
            DataMahasiswa.Mahasiswa("Zahwa Nur Azkia", "064002300038", 95),
            DataMahasiswa.Mahasiswa("Reyhan Arnas", "064002300002", 80)
        ]
        # Panggil metode print_data_mahasiswa menggunakan looping
        for mhs in mahasiswa:
            DataMahasiswa.Mahasiswa.print_data_mahasiswa([mhs])


DataMahasiswa.main()
