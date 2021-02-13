# API_TV

The API enables users to filter episodes of the hit TV show 'Silicon Valley' based on various categories.

*Pre-requisites
    * python 3.7+
    * requests
    * flask
    * Any http client(google chrome, fire fox, safari)

INSTALLATION :
* Windows

    Download the latest version of python from https://www.python.org/downloads/windows/
    after downloading the .exe file, run the installer, make sure you enable 'Add to path' check box.

    once the installation is complete you will have access to python and pip.
    rest of the pre-requisite packages can be installed easily via pip.

    example: pip install requests
             pip install flask

* Linux

    Ubuntu 20.04 and other versions of Debian Linux systems comes with python 3 pre installed.
    Make sure the latest version is installed by using 'sudo apt update'.

    to check the current available version type 'python -V' or 'python --version'
    Flask and Requests can be installed via pip using 'pip install [package_name]'.


USAGE:

    run the api.py python file provided with the project directory, using
    'python3 api.py'. you should see output similar to this in the terminal.

      * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

    copy the http address and paste it any web client that supports http. You
    should see a output that resembles the following.

      * SILICON VALLEY
        This site is a prototype API for silicon valley episodes
        refer README for more details.

    The base URL for the API is 'http://127.0.0.1:5000/siliconvalley/'
    all the other endpoints and parameters are built on this base URL.


    To view a entire list of episodes of Silicon Valley with other information
    like runtime, season and episode number, summary and many more, add 'all' to the
    base URL.

      *  http://127.0.0.1:5000/siliconvalley/all

    To view a list containing the title of all the episodes, add 'episodes/count' to the base URL.

      *  http://127.0.0.1:5000/siliconvalley/episodes/count

    To view the list of episodes in a particular season use the parameter 's' in the base URL.
    For example, to view just the episodes from season 4 add '/episodes/count?s=4' to the base
    URL.

      *  http://127.0.0.1:5000/siliconvalley/episodes/count?s=4

    to filter episodes based on title and episode number use the endpoint '/episodes/title'
    together with the base URL. Specify the season with the parameter 's' and episode with the
    parameter 'e'.
    for example, to view episode 6 from season 5 add '/episodes/title?s=5&e=6' to the base URL
    of the API.

      * http://127.0.0.1:5000/siliconvalley/episodes/title?s=5&e=6

    furthermore, you also have the option to filter episodes based on their title. You can do so
    using the 'name' parameter. for example if you want to see the details of the episode
    'Runaway Devaluation' add '/episodes/title?name=Runaway Devaluation' to the base URL.

      * http://127.0.0.1:5000/siliconvalley/episodes/title?name=Runaway%20Devaluation
