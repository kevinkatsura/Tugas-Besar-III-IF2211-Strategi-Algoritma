def boyer_moore_search(text, pattern):  # --> Fungsi untuk mengembalikan True jika ditemukan dan False jika tidak
    # Inspirasi dari: https://www.geeksforgeeks.org/boyer-moore-algorithm-for-pattern-searching/
    
    # Membuat Dictionary dengan:
    #   Key: seluruh char pada text
    #   Val: index pada pattern, -1 jika tidak ada
    char_index = {}

    for i in range(len(pattern)):
        char_index[pattern[i]] = i

    text_char_set = set()

    for char in text:
        text_char_set.update(char)

    for char in text_char_set:
        if (char_index.__contains__(char) == False):
            char_index[char] = -1

    pattern_ditemukan = False

    # Prose Pencarian
    # Inisialisasi
    shift = 0

    while (shift <= len(text) - len(pattern)):
        # Atur posisi karakter yang dibandingkan selalu di akhir (ketika terjadi perubahan shift)
        compare_pos = len(pattern) - 1

        # Jika karakter yang dibandingkan sama, lanjut membandingkan karakter di sebelah kirinya
        while (pattern[compare_pos] == text[shift + compare_pos] and compare_pos >= 0):
            compare_pos -= 1

        # Jika semua karakter yang dibandingkan sama
        if (compare_pos < 0):
            # Alternatif I:
            #print("Ditemukan pada shift {}".format(shift))
            
            # Geser sejauh panjang pattern atau disesuaikan agar tepat membandingkan karakter terakhir pada text
            if (shift == len(text) - len(pattern)):
                shift += 1
            else:
                if (shift + len(pattern) > len(text) - len(pattern)):
                    shift += (len(text) - len(pattern) - shift)
                else:
                    shift += len(pattern)

            # Alternatif II:
            pattern_ditemukan = True
            break
        # Jika ada karakter yang berbeda
        else:
            if (char_index[text[shift + compare_pos]] != -1):
                # Case 1 (index karakter yang dibandingkan belum terlewat)
                if (compare_pos >= char_index[text[shift + compare_pos]]):
                    shift += (compare_pos - char_index[text[shift + compare_pos]])
                # Case 2 (index karakter yang dibandingkan sudah terlewat)
                else:
                    shift += 1
            # Case 3 (index karakter yang dibandingkan = -1 / tidak ada)
            else:
                # Geser sejauh panjang pattern atau disesuaikan agar tepat membandingkan karakter terakhir pada text
                if (shift == len(text) - len(pattern)):
                    shift += 1
                else:
                    if (shift + len(pattern) > len(text) - len(pattern)):
                        shift += (len(text) - len(pattern) - shift)
                    else:
                        shift += len(pattern)

    return pattern_ditemukan

def boyer_moore_print_all(text, pattern): # --> Prosedur untuk menunjukkan seluruh posisi ditemukan
    char_index = {}

    for i in range(len(pattern)):
        char_index[pattern[i]] = i

    text_char_set = set()

    for char in text:
        text_char_set.update(char)

    for char in text_char_set:
        if (char_index.__contains__(char) == False):
            char_index[char] = -1

    shift = 0

    while (shift <= len(text) - len(pattern)):
        compare_pos = len(pattern) - 1

        while (pattern[compare_pos] == text[shift + compare_pos] and compare_pos >= 0):
            compare_pos -= 1

        if (compare_pos < 0):
            print("Ditemukan pada shift {}".format(shift))
            
            if (shift == len(text) - len(pattern)):
                shift += 1
            else:
                if (shift + len(pattern) > len(text) - len(pattern)):
                    shift += (len(text) - len(pattern) - shift)
                else:
                    shift += len(pattern)

        else:
            if (char_index[text[shift + compare_pos]] != -1):
                if (compare_pos >= char_index[text[shift + compare_pos]]):
                    shift += (compare_pos - char_index[text[shift + compare_pos]])
                else:
                    shift += 1
            else:
                if (shift == len(text) - len(pattern)):
                    shift += 1
                else:
                    if (shift + len(pattern) > len(text) - len(pattern)):
                        shift += (len(text) - len(pattern) - shift)
                    else:
                        shift += len(pattern)
