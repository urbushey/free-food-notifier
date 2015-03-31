from flask import Flask, request, render_template, jsonify
from slack_talker import send_to_channel

ERROR_CODE = 422  # "UNPROCESSABLE ENTITY"
SUCCESS_CODE = 200  # SUCCESS

app = Flask(__name__, static_folder="static")


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/_post_slack', methods=['POST'])
def post_slack():
    channel = request.form["channel"]
    location = request.form["radioLocation"]
    username = request.form["username"]
    if send_to_channel(channel, location, username):
        response = construct_success_response("Notified!")
    else:
        response = construct_error_response("Could not post your message")
    return response


def construct_error_response(error_msg):
    response = jsonify({"status":   ERROR_CODE,
                        "error":    error_msg})
    response.status_code = ERROR_CODE
    return response


def construct_success_response(success_msg):
    response = jsonify({"status":     SUCCESS_CODE,
                        "message":    success_msg})
    response.status_code = SUCCESS_CODE
    return response

if __name__ == '__main__':
    app.run(debug=True)
