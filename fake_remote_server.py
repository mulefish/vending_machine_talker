
from flask import Flask, redirect, url_for, request, render_template, send_file, render_template_string
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin, current_user
import json
from flask import jsonify





app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def no_path_given():
    print("test")
    tiny_html = '<html><body><h1>This is simple test harness to to mock test CURLs against the AVEND system</h1>'
    tiny_html += "<hr/>"
    tiny_html += "<table border='1'>"
        
    url = "http://localhost:9092/avend"
    
    possible_commands = {
        f"{url}?action=start":"Start a session to begin transaction. All other API calls will have no effect unless a session has started",
        f"{url}?action=dispense&code=v2":"Dispense selection v2 if cart is empty. Otherwise dispense the item(s) in cart",

        f"{url}?action=add&code=v2":"Add selection v2 to Cart.",
        f"{url}?action=dispense":"Dispense item(s) in Cart.",
        f"{url}?action=remove&code=v2":"Remove selection v2 from Cart.",
        f"{url}?action=clear":"Clear Cart"
    }
    for key, value in possible_commands.items():
        tiny_html += "<tr><td><a href={0}>{0}</a></td><td>{1}</td></tr>".format(key, value)

    tiny_html += "</table></body></html>"
    return render_template_string(tiny_html)

@app.route('/avend', methods=['GET', 'POST'])
def avend_command():
    x = request.args.get('action')
    
    print(x)
    if x == "dispense":
        c = request.args.get('code')

        return "{}   {}".format( x, c )
    elif x == "add":
        c = request.args.get('code')
        return "{}   {}".format( x, c )
    else: 
        return "{}".format(x)
    


if __name__ == '__main__':
    port = 9092
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.debug = True
    print("http://localhost:{}".format(port))

    from waitress import serve
    serve(app, host="0.0.0.0", port=port)
