from flask import Flask, render_template, request
from stories import stories
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "password"
debug = DebugToolbarExtension(app)

@app.route('/')
def choose_story():
    """lets user choose adlib prompt"""

    return render_template('prompt.html', stories = stories.values())
    

@app.route('/form')
def show_form():
    """shows form to input adlibs"""
    prompt_id = request.args["prompt"]
    story = stories[prompt_id]
    prompts = story.prompts

    return render_template('form.html', prompt_id = prompt_id, prompts = prompts, title = story.title)


@app.route('/story')
def show_story():
    """generates story for user"""
    prompt_id = request.args["prompt"]
    story = stories[prompt_id]

    adlib = story.generate(request.args)

    return render_template('story.html', adlib = adlib, title = story.title)