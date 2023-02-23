import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")
print("KEY:",openai.api_key)

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        animal = request.form["animal"]
        response = openai.Completion.create(
            model="davinci",
            prompt=generate_prompt(animal),
            temperature=0,
        )
        print("RESPONSE:" , response)
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(animal):
    return """Extract address from the Text

Text: in your headed to was the the Fort Lauderdale Hollywood Airport correct
Address: Fort Lauderdale Hollywood Airport
Text: 7800 Southwest 104th Street Delta Target there at the corner
Address: 7800 Southwest 104th Street Delta Target
Text: That would be 411, 98th street, No, I think it's 5th street
Address: 411,5th street
Text: {}
Address:""".format(
        animal.capitalize()
    )
