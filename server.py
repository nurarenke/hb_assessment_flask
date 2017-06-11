from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined


app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"


# YOUR ROUTES GO HERE
@app.route('/')
def view_homepage():
    '''Display homepage.'''

    return render_template("index.html")

@app.route('/application-form')
def view_application_form():
    '''Display application-form for job application.'''

    return render_template("application-form.html", 
        jobs_list=["Software Engineer", "QA Engineer", "Product Manager"])

@app.route('/application-success', methods=["post"])
def process_form():
    '''Processes the form.'''

    first_name = request.form.get("first-name")
    last_name = request.form.get("last-name")
    salary = request.form.get("salary")
    user_job_choice = request.form.get("jobs_list")
    salary_text = "${:,.2f}".format(int(salary))
    return render_template("application-response.html",
                            first_name=first_name, 
                            last_name=last_name,
                            salary=salary_text,
                            user_choice=user_job_choice)

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
