import pandas as pd
from random import choice

def create():
	karakterler = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
	
	uzunluk = int(input("Şifre Uzunluğu : "))
	
	sebep = input("Şifre Sebebi Giriniz : ")
	
	sifre = ""
	
	for i in range(uzunluk):
		sifre += str(choice(karakterler))
	print("Şifreniz : "+sifre)
	
	file = open("data.txt", "a")
	file.write("\n Şifre: {} {}".format(sebep, sifre))
	
def list():
	dosya = open("data.txt", "a")
	pf = pd.read_table("data.txt", header=None,  names=["Sebep(ler)", "Şifre(ler)"])
	print(pf)

def cik():
	quit()
	
banner = """
1 )  Sifre Oluştur
2 )  Şifreleri Listele
3 )  Çıkış Yap

Bir Protokol Numarası Giriniz : 
"""
print(banner)
veri = int(input())
if veri == 1:
	create()
	
if veri == 2:
	list()

if veri == 3:
	cik()
