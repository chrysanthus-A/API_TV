import flask, json, requests
from flask import request, jsonify


app = flask.Flask(__name__)
app.config["DEBUG"] = True

response = requests.get('http://api.tvmaze.com/singlesearch/shows?q=silicon-valley&embed=episodes')
archive = response.json()

#breakpoint()
def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    #breakpoint()
    return (text)

@app.route('/', methods=['GET'])
def home():
    return "<h1>SILICON VALLEY</h1><p>This site is a prototype API for silicon valley episodes refer READ_ME for more details.</p>"



@app.route('/siliconvalley/episodes/all', methods=['GET'])
def silicon_valley():
    #return(jprint(archive['_embedded']))
    return (archive)

@app.route('/siliconvalley/episodes/title', methods=['GET'])
def title():
    results=[]
    if 'title' in request.args:
        title = str(request.args['title'])
        for episode in archive['_embedded']['episodes']:
            if episode['name']==title:
                results.append(episode)
    else:
        for episode in archive['_embedded']['episodes']:
            results.append(episode['name'])

    return jsonify(results)

    #breakpoint()





app.run()
