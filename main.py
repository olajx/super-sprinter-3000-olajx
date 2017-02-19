from models import Story
from flask import Flask, request, render_template, redirect, url_for
from connectdatabase import CreateDatabase

app = Flask(__name__, template_folder='templates')


@app.route('/', methods=['GET'])
@app.route('/list', methods=['GET'])
def display_stories():
    stories = Story.select().order_by(Story.id)
    return render_template('list.html', stories=stories)


@app.route('/story/', methods=['GET','POST'])
def add_story():
    new_story = Story.create(story_title=request.form['story_title'],
                             user_story=request.form['user_story'],
                             criteria=request.form['criteria'],
                             business_value=request.form['business_value'],
                             estimation=request.form['estimation'],
                             status=request.form['status'])
    new_story.save()
    return redirect(url_for('display_stories'))


@app.route('/story/<story_id>', methods=['POST'])
def update_story(story_id):
        update = Story.update(story_title=request.form["story_title"],
                              user_story=request.form["user_story"],
                              criteria=request.form["criteria"],
                              business_value=request.form["business_value"],
                              estimation=request.form["estimation"],
                              status=request.form["status"]).where(Story.id == story_id)
        update.execute()
        return redirect(url_for('display_stories'))


@app.route('/delete/<story_id>', methods=['POST'])
def delete_story(story_id):
    story = Story.select().where(Story.id == story_id).get()
    story.delete_instance()
    story.save()
    return redirect(url_for('display_stories'))


@app.route('/form', methods=['GET','POST'])
def create_new():
    story = []
    return render_template('form.html', story=story, header="Add new Story", button="Create")


@app.route("/story/<story_id>", methods=['GET'])
def edit(story_id):
    story = Story.get(Story.id == story_id)
    return render_template('form.html', story = story, header = "Edit", button="Update")

if __name__ == '__main__':
    CreateDatabase.create_db()
    app.run(debug=True)



