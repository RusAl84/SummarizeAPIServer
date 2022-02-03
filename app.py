from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

# https://docs-python.ru/packages/veb-frejmvork-flask-python/registratsija-marshrutov-url-adresov-flask/
# https://stackoverflow.com/questions/10434599/get-the-data-received-in-a-flask-request
@app.route('/')
def root():  # put application's code here
    return "Автоматическая суммаризация текстов"

@app.route('/sum', methods=['POST'])
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
    mas2=[]
    for item in mas:
        if len(item)>30:
            mas2.append(item) 
    opti = {}
    title= {}
    title['text']= ""
    title['left']= "center"
    opti['title']=title
    tooltip = {}
    tooltip['trigger']= "item"
    tooltip['formatter'] =  r"{a} <br/>{b} : {c} ({d}%)"
    opti['tooltip']=tooltip
    legend={}
    legend['orient']="vertical"
    legend['left']= "left"
    datal=[]
    for i1 in mas2:
        datal.append(i1)
    legend['data']= datal
    opti['legend']=legend
    series=[]
    serI={}
    serI['name']= ""
    serI['type']= "pie"
    serI['radius']= "55%"
    serI['center']=  ["50%", "60%"]
    dataS=[]
    for i1 in mas2:
        item={}
        item['value']=random.randrange(1, 10)
        item['name']=i1
        dataS.append(item)
    serI['data']=dataS
    emphasisD={}
    itemStyle={}
    itemStyle['shadowBlur'] = 10
    itemStyle['shadowOffsetX'] = 0
    itemStyle['shadowColor'] = "rgba(0, 0, 0, 0.5)",   
    emphasisD['itemStyle']=itemStyle
    serI['emphasis']=emphasisD
    series.append(serI)
    opti['series']=series

    return jsonify(opti), 200, {'Content-Type': 'application/json'}

if __name__ == '__main__':
    app.run(host='0.0.0.0')
app.run(host='0.0.0.0')


# {
#       title: {
#         text: "Traffic Sources",
#         left: "center",
#       },
#       tooltip: {
#         trigger: "item",
#         formatter: "{a} <br/>{b} : {c} ({d}%)",
#       },
#       legend: {
#         orient: "vertical",
#         left: "left",
#         data: ["Direct", "Email", "Ad Networks", "Video Ads", "Search Engines"],
#       },
#       series: [
#         {
#           name: "",
#           type: "pie",
#           radius: "55%",
#           center: ["50%", "60%"],
#           data: [
#             { value: 335, name: "Direct" },
#             { value: 310, name: "Email" },
#             { value: 234, name: "Ad Networks" },
#             { value: 135, name: "Video Ads" },
#             { value: 1548, name: "Search Engines" },
#           ],
#           emphasis: {
#             itemStyle: {
#               shadowBlur: 10,
#               shadowOffsetX: 0,
#               shadowColor: "rgba(0, 0, 0, 0.5)",
#             },
#           },
#         },
#       ],
#     }