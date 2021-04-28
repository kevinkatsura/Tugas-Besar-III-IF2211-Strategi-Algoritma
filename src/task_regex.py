import re

# Baca file berisi daftar kata penting untuk tipe task
file_kata_tipe = open("../test/file_kata_tipe.txt", "r")
Lines = file_kata_tipe.readlines()
Lines = [line.strip('\n\r') for line in Lines]
regex_tipe = "|".join(line for line in Lines)

def regex_search(text):	# --> Funsgi untuk identifikasi apakah string adalah perintah tambah task
	matkul = re.findall("[A-Z]{2}[0-9]{4}", text, re.IGNORECASE)
	date = re.findall("[0-9]{2}.[/-].[0-9]{2}.[/-].[0-9]{4}|[0-9]{2}.\\w+.[0-9]{4}", text, re.IGNORECASE)
	tipe = re.findall(regex_tipe, text, re.IGNORECASE)
	topik1 = re.findall("[A-Z]{2}[0-9]{4}.(.*).pada", text, re.IGNORECASE)
	topik2 = re.search("[A-Z]{2}[0-9]{4}.(.*).([0-9]{2}.[/-].[0-9]{2}.[/-].[0-9]{4}|[0-9]{2}.\\w+.[0-9]{4})", text, re.IGNORECASE)

	if (len(matkul) != 0 and len(date) != 0 and len(tipe) != 0):
		if (len(topik1) == 1):
			return (True, matkul, date, tipe, topik1)
		else:
			if (topik2):
				return (True, matkul, date, tipe, [topik2.group(1)])
			else:
				return (False, matkul, date, tipe, "error")
	else:
		return (False, matkul, date, tipe, "error")
