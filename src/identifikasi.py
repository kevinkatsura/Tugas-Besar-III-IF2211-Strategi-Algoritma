import boyer_moore as bm
import task_regex as tre
import re

def cek_tambah_task(text):
    return tre.regex_search(text)

def cek_task(text):
    # Case a
    # Kata penting: deadline
    result_deadline = bm.boyer_moore_search(text.lower(), "deadline")

    # Case b.i
    # Kata penting: deadline, tgl1, tgl2
    date = re.findall("[0-9]{2}.[/-].[0-9]{2}.[/-].[0-9]{4}|[0-9]{2}.\\w+.[0-9]{4}", text, re.IGNORECASE)

    # Case b.ii
    # Kata penting: deadline, N, minggu
    result_minggu = bm.boyer_moore_search(text.lower(), "minggu")
    N_minggu = re.findall("(\\d+).minggu", text, re.IGNORECASE)

    # Case b.iii
    # Kata penting: deadline, N, hari
    N_hari = re.findall("(\\d+).hari", text, re.IGNORECASE)
    result_hari = bm.boyer_moore_search(text.lower(), "hari")

    # Case b.iv
    # Kata penting: deadline, hari ini
    result_hari_ini = bm.boyer_moore_search(text.lower(), "hari ini")

    # Case c
    # Kata penting: kata_penting_tipe, N, minggu/hari
    tipe = re.findall(tre.regex_tipe, text, re.IGNORECASE)

    if (result_deadline == False):
        if(len(tipe) == 0):
            return (False, "error")
        else:
            if ( len(N_minggu) > 0  and result_minggu == True):
                return (True, "case_c",tipe,N_minggu,"minggu")
            if ( len (N_hari) > 0 and result_hari == True ):
                return (True, "case_c",tipe,N_hari,"hari")
            return (False, "error")
    else:
        if (len(date) == 0):
            if (result_hari_ini == True):
                return (True, "case_biv")
            elif (result_minggu == True and len(N_minggu) != 0):
                if (len(tipe) == 0):
                    return (True, "case_bii",N_minggu)
                elif (len(tipe) != 0):
                    return (True, "case_c",tipe,N_minggu,"minggu")
                else:
                    return (True, "case_a")
            elif (result_hari == True and len(N_hari) != 0):
                if (len(tipe) == 0):
                    return (True, "case_biii",N_hari)
                elif (len(tipe) != 0):
                    return (True, "case_c",tipe,N_hari,"hari")
                else:
                    return (True, "case_a")
            else:
                return (True, "case_a")
        elif (len(date) == 2):
            return (True, "case_bi",date[0],date[1])
        else:
            return (False, "error")

def cek_deadline(text):
    # Kata penting: deadline, matkul
    result_deadline = bm.boyer_moore_search(text.lower(), "deadline")
    matkul = re.findall("[A-Z]{2}[0-9]{4}", text, re.IGNORECASE)
    
    if (result_deadline == True and len(matkul) != 0):
        return (True, matkul)
    else:
        return (False, matkul)

def cek_perbaharui(text):
    # Kata penting: task, IDTask, tgl
    result_task = bm.boyer_moore_search(text.lower(), "task")
    N_task = re.findall("task.(\\d)", text, re.IGNORECASE)
    date = re.findall("[0-9]{2}.[/-].[0-9]{2}.[/-].[0-9]{4}|[0-9]{2}.\\w+.[0-9]{4}", text, re.IGNORECASE)

    if (result_task == True and len(N_task) != 0 and len(date) == 1):
        return (True, N_task, date)
    else:
        return (False, N_task, date)    

def cek_selesai(text):
    # Kata penting: task, IDTask
    result_task = bm.boyer_moore_search(text.lower(), "task")
    N_task = re.findall("task.(\\d)", text, re.IGNORECASE)

    if (result_task == True and len(N_task) != 0):
        return (True, N_task)
    else:
        return (False, N_task)

def cek_help(text):
    # Kata penting: bisa, help, petunjuk, dll.
    kata_kunci = re.findall("\\bbisa\\b|\\bhelp\\b|\\bpetunjuk\\b", text, re.IGNORECASE)

    if (len(kata_kunci) != 0):
        return (True, "true")
    else:
        return (False, "false")

    