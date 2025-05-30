import os
import tempfile
from flask import Flask, jsonify, render_template, request
from infrastructure.google.speechToTextModule import transcribe_audio
from infrastructure.google.geminiModule import get_json_by_ia
from infrastructure.kafka.kafkaModule import sendToKafka

app = Flask(__name__, template_folder='templates')

# Carpeta donde se guardarán los archivos subidos
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Extensiones permitidas (opcional)
ALLOWED_EXTENSIONS = {'wav'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/transcribe', methods=['POST'])
def transcribe():
    if 'audio' not in request.files:
        return jsonify({"error": "No se encontró el archivo de audio"}), 400

    audio_file = request.files['audio']

    # Guardar archivo temporalmente
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp:
        audio_file.save(temp.name)
        temp_path = temp.name

    try:
        texto = transcribe_audio(temp_path)
        
        jsonData = get_json_by_ia(texto)

        sendToKafka("expense-topic",jsonData)

        return jsonify({"transcription": jsonData}), 202

        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        os.remove(temp_path)  # Limpieza del archivo temporal

if __name__ == '__main__':
    app.run(debug=True)
