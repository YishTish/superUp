import os
from flask import Flask, send_from_directory, request, Response
from google.cloud import translate

translate_client = translate.Client()


public_dir = os.path.join(os.getcwd(), "public/")
print("serving public files from: %s" % public_dir)
app = Flask(__name__, static_url_path=public_dir)


@app.route('/', methods=['GET'])
def main():
    print(public_dir)
    return send_from_directory("%s/html" % public_dir, "index.html")


@app.route('/js/<path:path>', methods=['GET'])
def send_js(path):
    return send_from_directory("%s/js" % public_dir, path)


@app.route('/css/<path:path>', methods=['GET'])
def send_css(path):
    return send_from_directory("%s/css" % public_dir, path)


@app.route("/getColor", methods=['GET'])
def getColor():
    color = request.args.get('color')
    language = request.args.get('lang')
    if color is None or language is None:
        return Response("color and language were not sent", status=400)
    if language == 'en':
        return Response(color, status=200)
    else:
        translation = translate_client.translate(color, target_language='en', source_language=language)
        return Response(format(translation['translatedText']), 200)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)

