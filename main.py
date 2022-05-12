from flask import Flask, render_template, request, url_for, redirect
import csv

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', mode='a') as base:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        print(email, message, subject)
        base.write(str(f'\n {email},{subject},{message}'))
        base.close()


def write_to_csv(data):
    with open('database.csv', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        print(email, message, subject)
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', lineterminator ='\n', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])
        database2.close()


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        write_to_csv(data)
        return redirect('thanks.html')

    else:
        return 'something went wrong'
