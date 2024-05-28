class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
        self.krs = []

    def tambah_matkul(self, mata_kuliah):
        self.krs.append(mata_kuliah)
        print(f"{self.nama} telah menambahkan mata kuliah {mata_kuliah} ke dalam KRS.")
    def tampilkan_krs(self):
        print(f"KRS {self.nama} ({self.nim}): {', '.join(self.krs)}")

class Dosen:
    def __init__(self, nama, nip):
        self.nama = nama
        self.nip = nip
        self.mahasiswa_bimbingan = []

    def bimbing_mahasiswa(self, mahasiswa):
        self.mahasiswa_bimbingan.append(mahasiswa)
        print(f"{self.nama} telah memvalidasi krs {mahasiswa.nama}.")

    def tampilkan_mahasiswa_bimbingan(self):
        print(f"Daftar mahasiswa bimbingan {self.nama} ({self.nip}):")
        for mahasiswa in self.mahasiswa_bimbingan:
            print(f"- {mahasiswa.nama} ({mahasiswa.nim})")

mahasiswa1 = Mahasiswa("Aila", "123456")
mahasiswa2 = Mahasiswa("Cikaro", "234567")
dosen1 = Dosen("Pak Deny Budiyanto", "987654")

mahasiswa1.tambah_matkul("Kecerdasan Buatan")
mahasiswa1.tambah_matkul("Technopreneurship")
mahasiswa2.tambah_matkul("Pengolahan Citra")

mahasiswa1.tampilkan_krs()
mahasiswa2.tampilkan_krs()

dosen1.bimbing_mahasiswa(mahasiswa1)
dosen1.bimbing_mahasiswa(mahasiswa2)

dosen1.tampilkan_mahasiswa_bimbingan()
