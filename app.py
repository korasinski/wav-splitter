from flask import (
    Flask,
    request,
    render_template,
    send_from_directory,
    url_for,
    jsonify,
    make_response
)
from werkzeug import secure_filename
import os
import file

UPLOAD_FOLDER = '/upload/'



basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)


def dated_url_for(endpoint, **values):
    if endpoint == 'js_static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     'static/js', filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    elif endpoint == 'css_static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     'static/css', filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    elif endpoint == 'images_static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     'static/images', filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)


@app.route('/css/<path:filename>')
def css_static(filename):
    return send_from_directory(app.root_path + '/static/css/', filename)


@app.route('/js/<path:filename>')
def js_static(filename):
    return send_from_directory(app.root_path + '/static/js/', filename)

@app.route('/images/<path:filename>')
def images_static(filename):
    return send_from_directory(app.root_path + '/static/images/', filename)


@app.route('/upload/<path:filename>')
def upload_path(filename):
    return send_from_directory(app.root_path + '/upload/', filename)

@app.route('/<path:filename>')
def export_path(filename):
    return send_from_directory(app.root_path + '/',  filename)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/uploadajax', methods=['POST'])
def upldfile():
    if request.method == 'POST':
        files = request.files['file']
        if files:

            filename = secure_filename(files.filename)
            updir = os.path.join(basedir, 'upload/')
            file_path = os.path.join(updir,filename)
            files.save(file_path)

            #data
            #dane = [8,9]
            #chunkId = file.file_info(file_path, 1)
            totalSize = file.file_info(file_path, 2)
            #dataSize = file.file_info(file_path, 3)
            #format = file.file_info(file_path, 4)
            #subChunk1Id = file.file_info(file_path, 5)
            #subChunk1Size = file.file_info(file_path, 6)
            audioFormat = file.file_info(file_path, 7)
            numChannels = file.file_info(file_path, 8)
            sampleRate = file.file_info(file_path, 9)
            byteRate = file.file_info(file_path, 10)
            #blockAlign = file.file_info(file_path, 11)
            #bitsPerSample = file.file_info(file_path, 12)
            #subChunk2Id = file.file_info(file_path, 13)
            #subChunk2Size = file.file_info(file_path, 14)
            #S1 = file.file_info(file_path, 15)
            #S2 = file.file_info(file_path, 16)
            #S3 = file.file_info(file_path, 17)
            #S4 = file.file_info(file_path, 18)
            #S5 = file.file_info(file_path, 19)



            audio_path = os.path.join('/upload/', filename)

            file.multichannel(file_path, numChannels)

            information = file.file_info(file_path, 2)
            return jsonify(name = filename,
                           size = totalSize,
                           channel = numChannels,
                           sample = sampleRate,
                           byte = byteRate,
                           codec = audioFormat,
                           path=audio_path
                           )


if __name__ == '__main__':
    app.run(debug=True)



