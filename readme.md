Server/Client side Google Calendar Python Quickstart
=========================

This repo contains a server-side(built with python and fastapi) google calender api and a client-side(built with raw html and css) version in html-js-version directory

server-side set up
=========================

1. Download oath2.0 client ID json file from google developer console
2. insert in app directory and rename file to `credentials.json`
3. create env
```
    $ python3 -m venv /path/to/new/virtual/environment
```
4. activate env
```
    $ source {/path/to/new/virtual/environment}/bin/activate
```
5. install app requirements:
```
    $ python3 -m pip install -r requirements.txt
```
6. run app with command:
```
    $ uvicorn main:app --reload
```

client-side set up
=========================
1. retrieve oath2.0 client ID and API key from google developer console
2. change directory to `html-js-version/`
3. replace `<YOUR_CLIENT_ID>` and `<YOUR_API_KEY>` with `client ID` and `API key` in index.html file respectively
4. run app with command:
```
    $ python3 -m http.server 8000
```
5. open app with url: `http://localhost:8000`


Useful link
=========================

#### * [official documentation](https://developers.google.com/calendar/api?hl=en_US)
#### * [documentation guides](https://developers.google.com/calendar/api/guides/overview?hl=en_US)
#### * [python reference](https://developers.google.com/calendar/api/quickstart/python)
#### * [javaScript reference](https://developers.google.com/calendar/api/quickstart/python)
#### * [video tutorial playlist](https://www.youtube.com/playlist?list=PL3JVwFmb_BnTO_sppfTh3VkPhfDWRY5on)
#### * [Google OAuth2: How the fix redirect_uri_mismatch error(video)](https://www.youtube.com/watch?v=QHz1Rs6lZHQ)
