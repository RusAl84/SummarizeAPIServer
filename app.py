from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# toDOlist = []
# toDoItem = {}
# toDoItem['name'] = "Flask"
# toDoItem['priority'] = 3
# toDOlist.append(toDoItem)
# toDOlist.append(toDoItem)
# toDOlist.append(toDoItem)


@app.route('/')
def get_status():  # put application's code here
    status = ""
    for item in toDOlist:
        status += f"name: {item['name']}   &nbsp; &nbsp; " \
                  f" priority: {item['priority']}  </br> "
    return status

# https://docs-python.ru/packages/veb-frejmvork-flask-python/registratsija-marshrutov-url-adresov-flask/
# https://stackoverflow.com/questions/10434599/get-the-data-received-in-a-flask-request
@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/get/<id>')
def getToDO(id):
    # if 0 <= int(id) < len(toDOlist):
    #     item=toDOlist[int(id)]
    #     # return f"name: {item['name']}   &nbsp; &nbsp; " \
    #     #           f" priority: {item['priority']}  </br> "
    #     return jsonify(item)
    # else:
    #     return jsonify(toDOlist)
    return "Not Found"

@app.route('/api/set', methods=['POST'])
def foo():
    text = request.json
    text = text['text']
    print(text)
    # return jsonify(data)
    import nltk
    nltk.download('stopwords')
    nltk.download('punkt')
    from rake_nltk import Metric, Rake
    r = Rake(language="russian")
    r.extract_keywords_from_text(text)
    mas = r.get_ranked_phrases()
    set2 = set()
    for item in mas:
        if not "nan" in str(item).replace(" nan ", " "):
            set2.add(str(item).replace(" nan ", " "))
    mas = list(set2)
    print("Исходный текст:")
    print(text)
    print("Результат работы Rake:")

    print(str(mas))
    print(mas[0])
    return jsonify(mas), 200, {'Content-Type': 'application/json'}
if __name__ == '__main__':
    app.run(host='0.0.0.0')
app.run(host='0.0.0.0')