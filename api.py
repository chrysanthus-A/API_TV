import flask, json, requests
from flask import request, jsonify


app = flask.Flask(__name__)
app.config["DEBUG"] = True

response = requests.get('http://api.tvmaze.com/singlesearch/shows?q=silicon-valley&embed=episodes')
archive = response.json()
seasons = 6
max_ep={1:8, 2:10, 3:10, 4:10, 5:8, 6:7} #maximum episodes per season
#breakpoint()
def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    #breakpoint()
    return (text)

#def season_error():
#    return f'<h3>Silicon valley has only {seasons} seasons </h3>'

@app.route('/', methods=['GET'])
def home():
    return '<h1>SILICON VALLEY</h1><p>This site is a prototype API for silicon valley episodes refer READ_ME for more details.</p>'


@app.route('/siliconvalley/all', methods=['GET'])
def silicon_valley():
    #return(jprint(archive['_embedded']))
    return (archive)

@app.route('/siliconvalley/episodes/title', methods=['GET'])
def title():
    results=[]
    s_no = request.args.get('s', None)
    ep_no  = request.args.get('e', None)
    title = request.args.get('name',None)
    if ep_no is not None and s_no is not None and (s_no < 6) and (ep_no > max_ep[s_no]):
        return f'<h3>Season {s_no} of silicon valley has only {max_ep[s_no]} episodes </h3>'
    if title is not None :
    #if 'name' in request.args:
        for episode in archive['_embedded']['episodes']:
            if episode['name']==title:
                results.append(episode)


    return jsonify(results)

    #breakpoint()

@app.route('/siliconvalley/episodes/count', methods=['GET'])
def count():
    ep_count = []
    s_no = request.args.get('s', None)
    if s_no is None:
        for episode in archive['_embedded']['episodes']:
            ep_count.append(episode['name'])
    else:
        if int(s_no) > 6:
            return f'<h3>Silicon valley has only {seasons} seasons </h3>'
        else:
            for episode in archive['_embedded']['episodes']:
                if(episode['season']== int(s_no)):
                    ep_count.append(episode['name'])
    #breakpoint()
    return jsonify(ep_count)
app.run()
