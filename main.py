from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

KEY = 'f3b7a805121fdabe5028f0016c2cca27'
SEARCH_URL = 'https://api.themoviedb.org/3/search/movie'
app = Flask(__name__)
app.config['SECRET_KEY'] = '123A678'
Bootstrap(app)


class SearchForm(FlaskForm):
    title = StringField('Find Movie by Title', validators=[DataRequired()])
    submit = SubmitField('Search')


@app.route('/', methods=['GET', 'POST'])
def home():
    form = SearchForm()
    if form.validate_on_submit():
        params = {'api_key': KEY,
                  'query': form.title.data,
                  'page': 1
                  }
        response = requests.get(SEARCH_URL, params=params)
        response = response.json()
        results = response['results']
        return render_template('results.html', results=results)
    return render_template('search.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
