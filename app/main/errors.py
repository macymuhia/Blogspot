from flask import render_template
from ..request import get_quote
from . import main


@main.app_errorhandler(404)
def four_Ow_four(error):
    """
    Function that defines the 404 error page
    """
    quote = get_quote()
    return render_template("fourOwfour.html", quote=quote), 404
