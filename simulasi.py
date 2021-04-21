import identifikasi as id

str_input = ""

while (str_input != "exit"):
    str_input = input()

    N_test = 1
    decision = False

    while (decision == False and N_test < 7):
        result_cek_tambah_task = id.cek_tambah_task(str_input)
        decision = result_cek_tambah_task[0]
        N_test += 1
        if (decision == True):
            print("TAMBAH TASK")
            print(result_cek_tambah_task)
            break

        result_cek_task = id.cek_task(str_input)
        decision = result_cek_task[0]
        N_test += 1
        if (decision == True):
            print("TASK")
            print(result_cek_task)
            break

        result_cek_deadline = id.cek_deadline(str_input)
        decision = result_cek_deadline[0]
        N_test += 1
        if (decision == True):
            print("DEADLINE")
            print(result_cek_deadline)
            break

        result_cek_perbaharui = id.cek_perbaharui(str_input)
        decision = result_cek_perbaharui[0]
        N_test += 1
        if (decision == True):
            print("PERBAHARUI")
            print(result_cek_perbaharui)
            break

        result_cek_selesai = id.cek_selesai(str_input)
        decision = result_cek_selesai[0]
        N_test += 1
        if (decision == True):
            print("SELESAI")
            print(result_cek_selesai)
            break

        result_cek_help = id.cek_help(str_input)
        decision = result_cek_help[0]
        N_test += 1
        if (decision == True):
            print("HELP")
            print(result_cek_help)
            break

    if (decision == False):
        print("Masukan tidak dimengerti")
        