from flask import Flask, render_template, request
import findLinks

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        print(url)
        links_in_url = findLinks.find_links_in_webpage(url)
        return render_template('result.html', links_in_url=links_in_url)
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run()

