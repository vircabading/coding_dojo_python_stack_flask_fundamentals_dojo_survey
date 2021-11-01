# ///////////////////////////////////////////////////////////////////////////////
# Coding Dojo > Python Stack > Flask > Fundamentals: Dojo Survey
# By: Virgilio D. Cabading Jr   Created: Oct 31, 2021


from flask import Flask, render_template, session, redirect, request

from werkzeug.datastructures import RequestCacheControl
from werkzeug.utils import redirect

app = Flask(__name__)
app.secret_key = "TiYSKDNRitA!"                                                     # This is Your Secret Key Do Not Reveal it to Anyone!

@app.route('/')                                                                     # Main Page
def index():
    return render_template("index.html")


@app.route('/get_survey', methods=['POST'])                                     # route that receives a post
def increment_by():
    print("::: FORM RECEIVED :::")
    # print(request.form)
    session['f-name'] = request.form['f-name']
    session['l-name'] = request.form['l-name']
    session['location'] = request.form['location']
    session['fav-language'] = request.form['fav-language']
    session['comment'] = request.form['comment']
    print(f"::: Name: {session['f-name']} {session['l-name']} :: location: {session['location']} :::")
    print(f"::: Favorite Language: {session['fav-language']} :: Comment: {session['comment']} :::")
    return redirect("/")

# **** Ensure that if the user types in any route other than the ones specified, 
#           they receive an error message saying "Sorry! No response. Try again ****
@app.errorhandler(404) 
def invalid_route(e): 
    return "Sorry! No response. Try again."

if __name__=="__main__":   
    app.run(debug=True)    