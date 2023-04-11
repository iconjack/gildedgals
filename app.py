import openai
import os
from flask import Flask, redirect, render_template, request, url_for

# https://github.com/openai/openai-quickstart-python


app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        animal = request.form["animal"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(animal),
            temperature=0.6,
        )
        print(response)
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(animal):
    return """Suggest a description of a so-called intellectual Examples:"

Name: Scott Alexander
Description: Psychiatrist and San Francisco rationalist with unusual love life who constantly pours his heart out to the world.

Name: Matt Yglesias
Description: Guy who’s willing to challenge his own side with a kind of detached irony and do funny things to operationalize his utilitarian reasoning like calling the cops on car owners with tinted license plates. 

Name: Nassim Nicholas Taleb
Description: Deadlifting Med bro with a short fuse who lets people know they are IMBECILES.

Name: Andrew Sullivan
Description: Gay, Catholic, and conservative, and somehow reconciling all of that while talking about it every step of the way.

Name: Curtis Yarvin
Description: Monarchist and anti-egalitarian allegedly whispering into the ears of powerful and important figures telling them to abolish democracy.

Name: Noah Smith: 
Description: Anime fan asexual economist who likes rabbits and dunking on people on Twitter. 

Name: {}
Description:"""

