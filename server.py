from distutils.log import error
from lib2to3.pgen2.token import NEWLINE
from flask import Flask , render_template , url_for , request , redirect
import csv
app = Flask(__name__)

@app.route("/")
def my_home():
    return render_template("index.html")

@app.route('/<string:page_name>')
def html_pages(page_name):
    return render_template(page_name)
# print(hello_world())

def write_to_file(data):
    with open("database.txt",mode='a') as database:
        email=data['email']
        subject=data['subject']
        message=data['message']
        database.write(f"\n{email},{subject},{message}")

def write_to_csv(data):
    with open("database.csv",newline='',mode='a') as database2:
        email=data['email']
        subject=data['subject']
        message=data['message']
        csv_writer=csv.writer(database2,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])
# def api_response():
#     from flask import jsonify
#     if request.method == 'POST':
#         return jsonify(**request.json)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method=='POST':
        # try:
            data=request.form.to_dict()
            write_to_file(data)
            write_to_csv(data)
            return redirect('/thankyou.html')
        # except :
        #     return 'did not Save to Database'
    else:
        return error
    



if __name__ == '__main__':
    app.debug = True
    app.run()