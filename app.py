from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    student_info = {
        "name": "Jordan Naegle",
        "student_id": "10778552",
        "university": "Utah Valley University",
        "course": "IT 3200 - Cloud Infrastructure & Deployment",
        "status": "Containerized & Running via Docker"
    }
    return render_template('index.html', student=student_info)

if __name__ == '__main__':
    # Listen on all interfaces on port 3000 to match assignment specs
    app.run(host='0.0.0.0', port=3000)
