from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask import send_file

from logic import route_logic


def register(app: Flask) -> None:
    @app.route('/', methods=['GET'])
    def go_home():
        return redirect("/home", code=302)

    @app.route('/home', methods=['GET'])
    def get_homepage():
        return render_template('homepage.html', **route_logic.homepage())

    @app.route('/download', methods=['GET'])
    def get_productpage():
        product_id = request.args.get('id')  # ?id=some-value
        try:
            return send_file('web/content/{}.pdf'.format(product_id),
                             attachment_filename='{}.pdf'.format(product_id))
        except Exception as err:
            raise
