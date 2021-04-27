def convertMonth(month):
    if (month.lower() == "januari" or month.lower() == "january"):
        return "01"
    elif (month.lower() == "februari" or month.lower() == "february"):
        return "02"
    elif (month.lower() == "maret" or month.lower() == "march"):
        return "03"
    elif (month.lower() == "april"):
        return "04"
    elif (month.lower() == "mei" or month.lower() == "may"):
        return "05"
    elif (month.lower() == "juni" or month.lower() == "june"):
        return "06"
    elif (month.lower() == "juli" or month.lower() == "july"):
        return "07"
    elif (month.lower() == "agustus" or month.lower() == "august"):
        return "08"
    elif (month.lower() == "september"):
        return "09"
    elif (month.lower() == "oktober" or month.lower() == "october"):
        return "10"
    elif (month.lower() == "november"):
        return "11"
    elif (month.lower() == "desember" or month.lower() == "december"):
        return "12"
    else:
        return 0

def formattingTime(waktu):
    # MENYERAGAMKAN FORMAT WAKTU
    theTime = waktu.split(" ")
    if (len(theTime) == 3):
        convTime = convertMonth(theTime[1])
        if (convTime != 0):
            resultDate = theTime[0] + "/" + convTime + "/" + theTime[2]
        else:
            resultDate = waktu
    else:
        resultDate = waktu
    return resultDate