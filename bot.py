import requests
from bs4 import BeautifulSoup
import csv
import time
import random
import re


class Dott:
    def __init__(self, jk, pendidikan, bagian):

        self.jk = jk
        self.pendidikan = pendidikan
        self.bagian = bagian

    def isi_form(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36',
        }

        url_form = "https://docs.google.com/forms/d/e/1FAIpQLSfERhEgNUKGx2qk7wIXztLcN21M2QMVS591YoGWigxSyH2RuA/viewform"
        ss = requests.session()

        # get form
        form = ss.get(url_form, headers=headers)
        fbzx = BeautifulSoup(form.content, 'lxml')
        kode_fbzx = fbzx.find(
            'input', attrs={'name': 'fbzx'})['value']

        # set kelamin
        if self.jk == "L":
            jk = "Pria"
        elif self.jk == "P":
            jk = "Wanita"

        rentang_umur = ["<30 Tahun", "31-40 Tahun",
                        "41 - 50 Tahun", ">51 Tahun"]
        lama_bekerja = ["< 1 Tahun", "2-10 Tahun", "11 - 20 Tahun"]
        pendidikan = ["SLTP", "SLTA", "Sarjana (S1)"]

        post_data = {
            "entry.1637583859": self.bagian,
            "entry.471594382": "Karyawan Pelaksana",
            "entry.72054100": "Kantor Kebun/Unit",
            "entry.923332375": jk,
            "entry.1989427240": random.choice(rentang_umur),
            "entry.88928586": random.choice(lama_bekerja),
            "entry.548470090":  random.choice(pendidikan),
            "entry.471594382_sentinel": None,
            "entry.72054100_sentinel": None,
            "entry.923332375_sentinel": None,
            "entry.1989427240_sentinel": None,
            "entry.88928586_sentinel": None,
            "entry.548470090_sentinel": None,
            "fvv": 1,
            "partialResponse": [None, None, kode_fbzx],
            "pageHistory": 0,
            "fbzx": kode_fbzx,
            "continue": 1,
        }
        # post data
        post_pertama = ss.post(url_form, data=post_data, headers=headers)
        print(post_pertama.status_code)


hitung = 0
total = 0

# mencari total data yang ada di dalam file csv
# total harus dikurangi dengan 1 karena header judul csv dihitung 1
with open("data.csv", "r") as file:
    # Create a CSV reader object
    reader = csv.reader(file)

    for data in reader:
        total += 1
    # print(total)


# Open the CSV file
with open("data.csv", "r") as file:
    # Create a CSV reader object
    reader = csv.reader(file)

    # Read the header row

    header = next(reader)

    # Print the header row
    # print(header)

    # Loop over the rest of the rows

    for row in reader:
        testoterone = Dott(row[2], row[3], row[4])
        print(testoterone.isi_form())
        # Print each row
        hitung += 1
        print(f"\033[96mTelah selesai {hitung} dari {total-1}\033[0m")
