from flask import Flask, redirect, request, render_template, url_for
import random
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

if __name__ == '__main__':
    app.run(debug=True, port='5001')