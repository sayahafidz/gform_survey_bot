import sys
import time
import json
import random
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class Bot():
    def __init__(self, jk, pendidikan, bagian):
        self.jk = jk
        self.pendidikan = pendidikan
        self.bagian = bagian

    def bot_run(self):
        jk = ["i35", "i38"]
        rentang_umur = ["i45", "i48", "i51", "i54"]
        lama_bekerja = ["i61", "i64", "i67", "i70"]
        pendidikan = ["i80", "i83", "i86"]

        page2 = [5, 6, 7, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19,
                 21, 22, 23, 24, 26, 27, 28, 29, 30, 31, 33, 34, 35, 37, 38, 39, 41, 42, 43, 45, 46, 47, 49, 50, 51, 52, 53]

        page3 = [
            5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45, 46, 47
        ]

        page4 = [
            2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
        ]
        self.driver = webdriver.Chrome()

        self.driver.get(
            "https://docs.google.com/forms/d/e/1FAIpQLSfERhEgNUKGx2qk7wIXztLcN21M2QMVS591YoGWigxSyH2RuA/viewform")
        time.sleep(2)
        # self.driver.set_window_size(793, 818)
        self.driver.find_element(By.ID, "i14").click()
        self.driver.find_element(By.ID, "i24").click()
        self.driver.find_element(
            By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(self.bagian)
        time.sleep(1)
        self.driver.find_element(By.ID, random.choice(jk)).click()
        self.driver.find_element(By.ID, random.choice(rentang_umur)).click()
        self.driver.find_element(By.ID, random.choice(lama_bekerja)).click()
        self.driver.find_element(By.ID, random.choice(pendidikan)).click()
        self.driver.find_element(
            By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span').click()
        time.sleep(1)

        # page 2

        for data in page2:
            self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[' + str(
                data) + ']/div/div/div[2]/div/span/div/label[' + str(random.randint(4, 5)) + ']/div[2]/div/div/div[3]/div').click()

        self.driver.find_element(
            By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span').click()
        time.sleep(2)

        # page3

        for data in page3:
            self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[' + str(
                data) + ']/div/div/div[2]/div/span/div/label[' + str(random.randint(4, 5)) + ']/div[2]/div/div/div[3]/div').click()

        self.driver.find_element(
            By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span').click()
        time.sleep(1)

        # page 4
        for data in page4:
            self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[' + str(
                data) + ']/div/div/div[2]/div/span/div/label[' + str(random.randint(4, 5)) + ']/div[2]/div/div/div[3]/div').click()

        self.driver.find_element(
            By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span').click()  # kirim


hitung = 0
total = 0

# mencari total data yang ada di dalam file csv
# total harus dikurangi dengan 1 karena header judul csv dihitung 1
with open("data.csv", "r") as file:
    # Create a CSV reader object
    reader = csv.reader(file)

    for data in reader:
        total += 1

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
        testoterone = Bot(row[2], row[3], row[4])
        print(testoterone.bot_run())
        hitung += 1
        print(
            f"Nik : {row[0]}  \nNama : {row[1]}  \nJenis Kelamin: {row[2]} \nBagian : {row[4]}")
        print(f"\033[96mTelah selesai {hitung} dari {total-1}\033[0m")
