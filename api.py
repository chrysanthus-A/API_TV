import flask, json, requests
from flask import request, jsonify


app = flask.Flask('siliconvalley')
app.config["DEBUG"] = True

#get the database from http get requests
response = requests.get('http://api.tvmaze.com/singlesearch/shows?q=silicon-valley&embed=episodes')
archive = response.json()                    # converting the response into JSON format
seasons = 6                                  #maximum number of season in silicon valley
max_ep={1:8, 2:10, 3:10, 4:10, 5:8, 6:7}        #maximum episodes per season

#breakpoint()

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)     #coverting json obj to text
    return (text)

def season_error():
    return f'<h3>Silicon valley has only {seasons} seasons </h3>'
def maxep_error(s):
    return f'<h3>Season {s} of silicon valley has only {max_ep[s]} episodes </h3>'
def display(res):
    if len(res) == 0:
        return '<h3>No results found</h3><p>make sure the required parameters are specified</p>'
    else:
        return jsonify(res)

#home page
@app.route('/', methods=['GET'])
def home():
    return '<h1>SILICON VALLEY</h1><p>This site is a prototype API for silicon valley episodes</p><p>refer README for more details.</p>'

# displaying the entire archive in str format
@app.route('/siliconvalley/all', methods=['GET'])
def silicon_valley():
    return(jprint(archive['_embedded']))


@app.route('/siliconvalley/episodes/title', methods=['GET'])
def title():
    results=[]
    #getting the arguments from the url
    s_no = request.args.get('s', None)
    ep_no  = request.args.get('e', None)
    title = request.args.get('name',None)
    #error handling
    if s_no is not None and (int(s_no)>6):
        return season_error()
    if ep_no is not None and s_no is not None and (int(s_no)<= 6) and (int(ep_no) > max_ep[int(s_no)]):
        return maxep_error(int(s_no))
    # argument handling
    else:
        if ep_no is not None and s_no is not None:
            for episode in archive['_embedded']['episodes']:
                if episode['season']==int(s_no) and episode['number']==int(ep_no):
                    results.append(episode)
    if title is not None :
        for episode in archive['_embedded']['episodes']:
            if episode['name']==title:
                results.append(episode)

    return display(results)


@app.route('/siliconvalley/episodes/count', methods=['GET'])
def count():
    ep_count = []
    #getting the arguments from the url
    s_no = request.args.get('s', None)
    if s_no is None:
        for episode in archive['_embedded']['episodes']:
            ep_count.append(episode['name'])
    else:
        #error handling
        if int(s_no) > 6:
            return season_error();

        else:
            #argument handling
            for episode in archive['_embedded']['episodes']:
                if(episode['season']== int(s_no)):
                    ep_count.append(episode['name'])

    return display(ep_count)

app.run()
