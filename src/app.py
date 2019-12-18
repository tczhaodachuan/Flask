from flask import Flask, redirect, request, render_template, url_for, make_response
import random
import os
app = Flask(__name__, template_folder='views')

@app.route("/")
def hello():
    return render_template('index.html')

@app.route('/upload/', methods=['POST'])
def upload():
    if request.method == "POST":
        report_id = random.randint(1,100)
        return redirect(url_for('get_report', report_id=report_id))
    return render_template('index.html')

@app.route('/report/<int:report_id>', methods=['POST', 'GET'])
def get_report(report_id):
    report_id2=  report_id + 10
    return render_template('report.html', report_id=report_id, report_id2=report_id2)

def generate_image(folder_name):
    import shutil
    random_int = int(folder_name)
    image_name = 'google.png'
    if random_int % 2 == 0:
        image_name = 'sample.png'
    directory = os.path.join('static', str(random_int))
    if not os.path.exists(directory):
        os.mkdir(directory)
    shutil.copy(os.path.join('static', image_name), directory)
    return os.path.join(directory, image_name)

@app.route('/images')
def get_image():
    folder_name = request.args.get('filename')
    full_path = generate_image(folder_name)
    resp = make_response(open(full_path).read())
    resp.content_type = "image/jpeg"
    return resp

if __name__ == '__main__':
    app.run(debug=True)