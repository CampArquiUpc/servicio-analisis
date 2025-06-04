# Ejecutar Docker
docker compose up

python -m venv venv

# Activar entorno virtual linux
source venv/bin/activate

# Activar entorno virtual windows
venv\Scripts\activate

# Desactivar entorno virtual
deactivate

# Instalar librerias
pip install --upgrade google-genai
pip install google-cloud-speech
pip install kafka-python
pip install flask



# Ejecutar Flask 
flask --app main run

# Configuracion de Google Cloud

1) Crear proyecto en google cloud

2) Habilitar API Speech to Text

3) Crear cuenta de servicio
	3.1) Habilitar el api Access Management (IAM) API.
	3.2) usertest   usertest@pontebarbon.iam.gserviceaccount.com
	3.3) Rol: Editor
	3.4) Crear clave en Json presionando en la cuenta de servicio creada

4) set GOOGLE_APPLICATION_CREDENTIALS=F:\audios\pontebarbon-7a8ae86045da.json "Ejecuta esto para un variable de entorno temporal"

