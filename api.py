import flask, json, requests
from flask import request, jsonify


app = flask.Flask('siliconvalley')
app.config["DEBUG"] = True


response = requests.get('http://api.tvmaze.com/singlesearch/shows?q=silicon-valley&embed=episodes')
archive = response.json()
seasons = 6
max_ep={1:8, 2:10, 3:10, 4:10, 5:8, 6:7} #maximum episodes per season
#breakpoint()

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    return (text)
def season_error():
    return f'<h3>Silicon valley has only {seasons} seasons </h3>'
def maxep_error(s):
    return f'<h3>Season {int(s)} of silicon valley has only {max_ep[int(s)]} episodes </h3>'
def display(res):
    if len(res) == 0:
        return '<h3>No results found</h3>'
    else:
        return jsonify(res)


@app.route('/', methods=['GET'])
def home():
    return '<h1>SILICON VALLEY</h1><p>This site is a prototype API for silicon valley episodes refer READ_ME for more details.</p>'


@app.route('/siliconvalley/all', methods=['GET'])
def silicon_valley():
    return(jprint(archive['_embedded']))


@app.route('/siliconvalley/episodes/title', methods=['GET'])
def title():
    results=[]
    s_no = request.args.get('s', None)
    ep_no  = request.args.get('e', None)
    title = request.args.get('name',None)
    #breakpoint()
    if s_no is not None and (int(s_no)>6):
        return season_error()
    if ep_no is not None and s_no is not None and (int(s_no)<= 6) and (int(ep_no) > max_ep[int(s_no)]):
        return maxep_error(s_no)
    else:
        if ep_no is not None and s_no is not None:
            for episode in archive['_embedded']['episodes']:
                if episode['season']==int(s_no) and episode['number']==int(ep_no):
                    results.append(episode)
    if title is not None :
        for episode in archive['_embedded']['episodes']:
            if episode['name']==title:
                results.append(episode)

    #breakpoint()
    return display(results)


@app.route('/siliconvalley/episodes/count', methods=['GET'])
def count():
    ep_count = []
    s_no = request.args.get('s', None)
    if s_no is None:
        for episode in archive['_embedded']['episodes']:
            ep_count.append(episode['name'])
    else:
        if int(s_no) > 6:
            return season_error();

        else:
            for episode in archive['_embedded']['episodes']:
                if(episode['season']== int(s_no)):
                    ep_count.append(episode['name'])
    #breakpoint()
    return display(ep_count)

app.run()
