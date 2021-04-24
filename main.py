from flask import Flask,render_template,url_for,request, jsonify
import os


app = Flask(__name__)
# input user container
masukan = []

@app.route('/')
def index():
   # if(request.method == 'POST'):
   #    userInput = request.form.get("form")
   #    print(userInput)
   #    masukan.append(userInput)
   #    return render_template("index.html",masukan=masukan)
   return render_template("index.html")

@app.route('/proccess',methods=['POST'])
def proccess():
    message = request.form["message"]
    if ( message ):
        return jsonify({'message' : message})
    return jsonify({'error' : 'Pesan tidak dikenal!'})

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

