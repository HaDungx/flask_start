from flask import Flask,request

app = Flask(__name__)

from txt_to_json import txt_to_json
import json

def format_string_to_json(json_string):
  json_string = json_string.replace('{ ' ,'{\n')
  json_string = json_string.replace('"' ,"'")
  json_string = json_string.replace(', ' ,',\n')
  return json_string

@app.route('/chat', methods = ['GET'])
def chat():
  if request.method == 'GET':
    txt_file = 'tudien.txt'				#Thay doi ten file .txt o day; e.g 'tudien.txt'.
    json_file = txt_to_json(txt_file)
    json_string = json.dumps(json_file, ensure_ascii=False, indent = 4)
    json_string = format_string_to_json(json_string)					#change from string format to json format
    json_string = '<pre>{}</pre>'.format(json_string)					#need to display format in html
  return json_string

if __name__ == '__main__':
    app.run(debug=True)