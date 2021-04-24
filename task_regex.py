import re

# Baca file berisi daftar kata penting untuk tipe task
file_kata_tipe = open("file_kata_tipe.txt", "r")
Lines = file_kata_tipe.readlines()
Lines = [line.strip('\n\r') for line in Lines]
regex_tipe = "|".join(line for line in Lines)

def regex_search(text):	# --> Funsgi untuk identifikasi apakah string adalah perintah tambah task
	matkul = re.findall("[A-Z]{2}[0-9]{4}", text, re.IGNORECASE)
	date = re.findall("[0-9]{2}.[/-].[0-9]{2}.[/-].[0-9]{4}|[0-9]{2}.\\w+.[0-9]{4}", text, re.IGNORECASE)
	tipe = re.findall(regex_tipe, text, re.IGNORECASE)
	topik = re.findall("[A-Z]{2}[0-9]{4}.(.*)", text, re.IGNORECASE)

	if (len(matkul) != 0 and len(date) != 0 and len(tipe) != 0 and len(topik) != 0):
		return (True, matkul, date, tipe, topik)
	else:
		return (False, matkul, date, tipe, topik)

def regex_print(text):	# --> Prosedur untuk print hasil yang dibaca dari regex
	matkul = re.findall("[A-Z]{2}[0-9]{4}", text, re.IGNORECASE)
	date = re.findall("[0-9]{2}.[/-].[0-9]{2}.[/-].[0-9]{4}|[0-9]{2}.\\w+.[0-9]{4}", text, re.IGNORECASE)
	tipe = re.findall(regex_tipe, text, re.IGNORECASE)
	topik = re.findall("[A-Z]{2}[0-9]{4}.(.*)", text, re.IGNORECASE)

	print("Matkul: {}".format(matkul))
	print("Date: {}".format(date))
	print("Tipe: {}".format(tipe))
	print("Topik: {}".format(topik))