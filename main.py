from flask import Flask, render_template, url_for, request, jsonify
import os
import identifikasi as id
import connection as conn

app = Flask(__name__)
# input user container
connection = conn.Connection()


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/process', methods=['POST'])
def proccess():
    # USER MESSAGE
    message = request.form["message"]
    # NUMBER OF DATA RECORD
    sizeData = connection.db.child("LazyBotSize").get().val()

    # -----------------------------------------------------addTask-----------------------------------------------------
    addTask = id.cek_tambah_task(message) #SELESAI
    if (addTask[0]):
        # UPDATE NUMBER OF DATA RECORD IN DATABASE
        newSize = sizeData + 1
        connection.db.update({'LazyBotSize': newSize})

        # DATA TO POST TO DATABASE
        data = {'Id': newSize, 'Date': addTask[2][0], 'Course': addTask[1][0], 'Type': addTask[3][0],
                'Topic': addTask[4][0]}
        connection.db.child("LazyBot").push(data)

        # DATA RETURN TO USER
        result = "[TASK BERHASIL DICATAT]<br>" \
                 "(ID : " \
                 "" + str(newSize) + ") " + addTask[2][0] + " - " + addTask[1][0] + " - " + addTask[3][0] + " - " + \
                 addTask[4][0]
        return jsonify({'Ncase': 1,
                        'message': message,
                        'BOT': result})

    # ----------------------------------------------------checkTask----------------------------------------------------
    checkTask = id.cek_task(message)  # BELUM SELESAI
    if (checkTask[0]):
        # RETRIEVE DATA FROM DATABASE
        data = connection.db.child("LazyBot").get()

        bufferData = []
        for s_data in data.each():
            bufferData.append(s_data.val())
        # Urutkan berdasarkan Id

        result = "[DAFTAR DEADLINE]<br>"
        # ACCESS EVERY SINGLE DATA
        count = 1
        for s_data in (data.each()):
            valData = s_data.val()
            result = result + "" + count + ". (ID: " + valData["Id"] + ") " + valData["Date"] + " - " + valData[
                "Course"] + " - " + valData["Type"] + " - " + valData["Topic"] + "<br>"
            count += 1
        return jsonify({'Ncase': 2,
                        'message': message,
                        'BOT': result})

    # ----------------------------------------------------checkDeadline------------------------------------------------
    checkDeadline = id.cek_deadline(message)
    if (checkDeadline[0]):
        data = connection.db.child("LazyBot").get()
        for s_data in data.each():
            if str(checkDeadline[1][0]) == str(s_data.val()["Course"]):
                key = s_data.key()
                break
        if key:
            result = conn.Connection().db.child("LazyBot").child(key).get().val()["Date"]
        else:
            result = "Mata kuliah yang dimaksud tidak tersedia."
        return jsonify({'Ncase': 3,
                        'message': message,
                        'BOT': result})

    # ------------------------------------------------------checkUpdate------------------------------------------------
    checkUpdate = id.cek_perbaharui(message) #SELESAI
    if (checkUpdate[0]):
        # PENGKONDISIAN TASK YANG DIPILIH ADA TERSEDIA
        if (int(checkUpdate[1][0]) <= sizeData):
            # RETRIEVE DATA
            data = connection.db.child("LazyBot").get()
            # ACCESS TIAP DATA
            for s_data in data.each():
                if (s_data.val()['Id'] == int(checkUpdate[1][0])):
                    key = s_data.key()  # AMBIL KEY
                    break
            connection.db.child("LazyBot").child(key).update({'Date': checkUpdate[2][0]})
            result = "Task berhasil diperbaharui."
        else:
            result = "Task tidak dapat diperbaharui. Task tidak tersedia"

        # RETURN MESSAGE
        return jsonify({'Ncase': 4,
                        'message': message,
                        'BOT': result})

    # -----------------------------------------------------checkCompleted----------------------------------------------
    checkCompleted = id.cek_selesai(message) #SELESAI
    if (checkCompleted[0]):
        # PENGKONDISIAN TASK YANG DIPILIH ADA TERSEDIA
        if int(checkCompleted[1][0]) <= sizeData:
            # RETRIEVE DATA
            data = connection.db.child("LazyBot").get()
            # ACCESS TIAP DATA
            for s_data in data.each():
                if s_data.val()['Id'] == int(checkCompleted[1][0]):
                    key = s_data.key()  # AMBIL KEY
                    break
            connection.db.child("LazyBot").child(key).remove()
            connection.db.update({'LazyBotSize': sizeData - 1})

            # UPDATE ID DARI TIAP TASK
            data = connection.db.child("LazyBot").get()
            for s_data in data.each():
                if (s_data.val()['Id'] > int(checkCompleted[1][0])):
                    key = s_data.key()  # AMBIL KEY
                    oldId = s_data.val()['Id']
                    connection.db.child("LazyBot").child(key).update({'Id': oldId - 1})

            result = "Task berhasil ditandai selesai dan dihapus dari daftar."
        else:
            result = "Task tidak dapat ditandai selesai. Task tidak tersedia"
        return jsonify({'Ncase': 5,
                        'message': message,
                        'BOT': result})

    # --------------------------------------------------------checkHelp------------------------------------------------

    checkHelp = id.cek_help(message) #SELESAI
    if (checkHelp[0]):
        help = "[ FITUR ]<br>" \
               "1. Menambahkan task baru.<br>" \
               "2. Melihat daftar task.<br>" \
               "3. Menampilkan deadline task.<br>" \
               "4. Memperbaharui task.<br>" \
               "5. Menandai task selesai.<br>" \
               "6. Help.<br>" \
               "" \
               "<br>[ DAFTAR KATA PENTING ]<br>" \
               "1. Tubes<br>" \
               "2. Tucil<br>" \
               "3. Kuis<br>" \
               "4. Ujian<br>" \
               "5. Praktikum"

        return jsonify({'Ncase': 6,
                        'message': message,
                        'BOT': help})

    # -----------------------------------------------------------------------------------------------------------------

    return jsonify({'message': message, 'error': 'Pesan tidak dikenal!'})


@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)


def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)


if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'),
            port=int(os.getenv('PORT', 4444)))
