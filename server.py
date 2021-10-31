# ///////////////////////////////////////////////////////////////////////////////
# Coding Dojo > Python Stack > Flask > Fundamentals: Dojo Survey
# By: Virgilio D. Cabading Jr   Created: Oct 31, 2021
# ///////////////////////////////////////////////////////////////////////////////

from flask import Flask, render_template, session, redirect, request

from werkzeug.datastructures import RequestCacheControl
from werkzeug.utils import redirect

app = Flask(__name__)
app.secret_key = "TiYSKDNRitA!"                                                     # This is Your Secret Key Do Not Reveal it to Anyone!

@app.route('/')                                                                     # Main Page
def index():
    return render_template("index.html")


# @app.route('/increment_by', methods=['POST'])                                     # route that receives a post
# def increment_by():

#     return redirect("/")

# **** Ensure that if the user types in any route other than the ones specified, 
#           they receive an error message saying "Sorry! No response. Try again ****
@app.errorhandler(404) 
def invalid_route(e): 
    return "Sorry! No response. Try again."

if __name__=="__main__":   
    app.run(debug=True)    