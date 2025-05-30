from google.cloud import speech
from google.oauth2 import service_account
import tempfile

ruta_credenciales = "F:\\audios\\pontebarbon-a4bd39860683.json"
credentials = service_account.Credentials.from_service_account_file(ruta_credenciales)



def transcribe_audio(file_path):

    client = speech.SpeechClient(credentials=credentials)

    with open(file_path, "rb") as audio_file:
        content = audio_file.read()


    audio = speech.RecognitionAudio(content=content)

    config = speech.RecognitionConfig(
        encoding = speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=48000,
        language_code="es-PE",
    )

    response = client.recognize(config=config, audio=audio)

    for result in response.results:
        return result.alternatives[0].transcript


 
 