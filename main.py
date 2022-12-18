from flask import *
from utils.analyze_attendance import *
from utils.teams_fetch_attendance import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get', methods=['GET'])
def get():
      link = request.args.get('url')
      try:
         attendance = get_attendance_by_json(teams_fetch_attendance_by_link(link))
      except Exception as e:
         return render_template('error.html', error=e)
      return render_template('result.html', result=attendance)

if __name__ == '__main__':
   app.run()