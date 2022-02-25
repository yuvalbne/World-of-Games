from flask import Flask, render_template
from Score import get_score_from_file
from Utils import BAD_RETURN_CODE, GOOD_RETURN_CODE

app = Flask(__name__)


@app.route('/', methods=['Get', 'POST'])
def score_server():
    try:
        score = get_score_from_file()
    except:
        return render_template("/score_error.html", ERROR="Can't open file"), BAD_RETURN_CODE
    if score is None:
        return render_template("/score_error.html", ERROR="No Score"), BAD_RETURN_CODE
    else:
        return render_template("/score_success.html", SCORE=score), GOOD_RETURN_CODE


app.run('0.0.0.0', debug=True, port=8080)
