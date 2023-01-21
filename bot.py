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

        # data_post = {
        #     "entry.2011322744": random.randint(4, 5),
        #     "entry.470933383": random.randint(4, 5),
        #     "entry.150869826": random.randint(4, 5),
        #     "entry.1363487349": random.randint(4, 5),
        #     "entry.1450659233": random.randint(4, 5),
        #     "entry.638459393": random.randint(4, 5),
        #     "entry.571162281": random.randint(4, 5),
        #     "entry.1674697811": random.randint(4, 5),
        #     "entry.1423370286": random.randint(4, 5),
        #     "entry.1227889361": random.randint(4, 5),
        #     "entry.679533346": random.randint(4, 5),
        #     "entry.2045667905": random.randint(4, 5),
        #     "entry.517152619": random.randint(4, 5),
        #     "entry.1590359108": random.randint(4, 5),
        #     "entry.4063816": random.randint(4, 5),
        #     "entry.917045382": random.randint(4, 5),
        #     "entry.1797749411": random.randint(4, 5),
        #     "entry.670537173": random.randint(4, 5),
        #     "entry.891870252": random.randint(4, 5),
        #     "entry.2011322744_sentinel": None,
        #     "entry.470933383_sentinel": None,
        #     "entry.150869826_sentinel": None,
        #     "entry.1363487349_sentinel": None,
        #     "entry.1450659233_sentinel": None,
        #     "entry.638459393_sentinel": None,
        #     "entry.571162281_sentinel": None,
        #     "entry.1674697811_sentinel": None,
        #     "entry.1423370286_sentinel": None,
        #     "entry.1227889361_sentinel": None,
        #     "entry.679533346_sentinel": None,
        #     "entry.2045667905_sentinel": None,
        #     'entry.517152619_sentinel': None,
        #     "entry.1590359108_sentinel": None,
        #     "entry.4063816_sentinel": None,
        #     "entry.917045382_sentinel": None,
        #     "entry.1797749411_sentinel": None,
        #     "entry.670537173_sentinel": None,
        #     "entry.891870252_sentinel": None,
        #     "fvv": 1,
        #     "partialResponse": [[[None, 471594382, ["Karyawan Pelaksana"], 0], [None, 72054100, ["Kantor Kebun/Unit"], 0], [None, 1637583859, [self.bagian], 0], [None, 923332375, [jk], 0], [None, 1989427240, [random.choice(rentang_umur)], 0], [None, 88928586, [random.choice(lama_bekerja)], 0], [None, 548470090, [random.choice(pendidikan)], 0], [None, 1087158034, [random.randint(4, 5)], 0], [None, 1691039459, [random.randint(4, 5)], 0], [None, 36473046, [random.randint(4, 5)], 0], [None, 1753017366, [random.randint(4, 5)], 0], [None, 1473048860, [random.randint(4, 5)], 0], [None, 104955151, [random.randint(4, 5)], 0], [None, 1147898399, [random.randint(4, 5)], 0], [None, 657279955, [random.randint(4, 5)], 0], [None, 1932247558, [random.randint(4, 5)], 0], [None, 314356000, [random.randint(4, 5)], 0], [None, 950844370, [random.randint(4, 5)], 0], [None, 1427314292, [random.randint(4, 5)], 0], [None, 382077540, [random.randint(4, 5)], 0], [None, 1571337487, [random.randint(4, 5)], 0], [None, 282773223, [random.randint(4, 5)], 0], [None, 2007341158, [random.randint(4, 5)], 0], [None, 1254559791, [random.randint(4, 5)], 0], [None, 468296381, [random.randint(4, 5)], 0], [None, 253909439, [random.randint(4, 5)], 0], [None, 73213463, [random.randint(4, 5)], 0], [None, 1485393260, [random.randint(4, 5)], 0], [None, 994354195, [random.randint(4, 5)], 0], [None, 777158224, [random.randint(4, 5)], 0], [None, 1537704125, [random.randint(4, 5)], 0], [None, 439425146, [random.randint(4, 5)], 0], [None, 1679917278, [random.randint(4, 5)], 0], [None, 1643342118, [random.randint(4, 5)], 0], [None, 1392033369, [random.randint(4, 5)], 0], [None, 382336754, [random.randint(4, 5)], 0], [None, 729018029, [random.randint(4, 5)], 0], [None, 1106110690, [random.randint(4, 5)], 0], [None, 1999663633, [random.randint(4, 5)], 0], [None, 1734901334, [random.randint(4, 5)], 0], [None, 1962763702, [random.randint(4, 5)], 0], [None, 1086389430, [random.randint(4, 5)], 0], [None, 1821388039, [random.randint(4, 5)], 0], [None, 1087038450, [random.randint(4, 5)], 0], [None, 1064673931, [random.randint(4, 5)], 0], [None, 367487777, [random.randint(4, 5)], 0], [None, 1630911137, [random.randint(4, 5)], 0], [None, 849550115, [random.randint(4, 5)], 0], [None, 580013811, [random.randint(4, 5)], 0], [None, 182508495, [random.randint(4, 5)], 0], [None, 1732408543, [random.randint(4, 5)], 0], [None, 1222419873, [random.randint(4, 5)], 0], [None, 1503232389, [random.randint(4, 5)], 0], [None, 108818387, [random.randint(4, 5)], 0], [None, 2037052632, [random.randint(4, 5)], 0], [None, 1320178625, [random.randint(4, 5)], 0], [None, 1104651274, [random.randint(4, 5)], 0], [None, 1021578083, [random.randint(4, 5)], 0], [None, 46428979, [random.randint(4, 5)], 0], [None, 1564497236, [random.randint(4, 5)], 0], [None, 641980537, [random.randint(4, 5)], 0], [None, 1811420375, [random.randint(4, 5)], 0], [None, 2088732108, [random.randint(4, 5)], 0], [None, 1637666813, [random.randint(4, 5)], 0], [None, 1008495816, [random.randint(4, 5)], 0], [None, 1120780285, [random.randint(4, 5)], 0], [None, 499962831, [random.randint(4, 5)], 0], [None, 1421278781, [random.randint(4, 5)], 0], [None, 429867905, [random.randint(4, 5)], 0], [None, 1431546373, [random.randint(4, 5)], 0], [None, 515149872, [random.randint(4, 5)], 0], [None, 1089174334, [random.randint(4, 5)], 0], [None, 85291541, [random.randint(4, 5)], 0], [None, 1574146990, [random.randint(4, 5)], 0], [None, 1796161026, [random.randint(4, 5)], 0], [None, 1680668878, [random.randint(4, 5)], 0], [None, 578136623, [random.randint(4, 5)], 0], [None, 295026411, [random.randint(4, 5)], 0], [None, 468775908, [random.randint(4, 5)], 0], [None, 688987482, [random.randint(4, 5)], 0], [None, 1647400981, [random.randint(4, 5)], 0], [None, 31204951, [random.randint(4, 5)], 0], [None, 1623987663, [random.randint(4, 5)], 0], [None, 2115436821, [random.randint(4, 5)], 0], [None, 743758118, [random.randint(4, 5)], 0], [None, 1829955532, [random.randint(4, 5)], 0]], None, kode_fbzx],
        #     "pageHistory": "0,1,2,3",
        #     "fbzx": kode_fbzx,
        # }
        # post data
        post_pertama = ss.post(url_form, data=post_data, headers=headers)
        # print(post_pertama.text)
        print(post_pertama.status_code)
        # print(post_pertama.content)

        # print(data_post)


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
        # print(row[0])
        hitung += 1
        # time.sleep(2)
        # print(
        # f"Jenis Kelamin: {row[2]} \nPendidikan : {row[3]}  \nBagian : {row[4]}")
        print(f"\033[96mTelah selesai {hitung} dari {total-1}\033[0m")


# testing = Dott()
# testing.isi_form()
