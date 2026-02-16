class ArrayADT:
    def __init__(self, size):
        self.size = size
        self.data = [0] * size   # inisialisasi isi 0

    # operasi set (ubah nilai)
    def set(self, index, value):
        if 0 <= index < self.size:
            self.data[index] = value
        else:
            print("Index di luar batas!")

    # operasi get (ambil nilai)
    def get(self, index):
        if 0 <= index < self.size:
            return self.data[index]
        else:
            return "Index di luar batas!"

    # operasi tampilkan isi array
    def display(self):
        print(self.data)
      
