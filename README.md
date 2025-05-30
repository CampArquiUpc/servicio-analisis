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