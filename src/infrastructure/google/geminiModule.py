
from google import genai
from google.genai.types import HttpOptions


import json
import time

response_schema = {
    "type": "OBJECT",
        "properties": {
            "action": {"type": "STRING","enum": ["ADD", "REMOVE", "UPDATE"]},
            "description": {"type": "STRING"},
            "amount": {"type": "number"},
            "paymentMethod": {"type": "STRING","enum": ["YAPE", "INTERBANK", "BCP","PLIN", "CAJA", "BBVA","SCOTIABANK", "OTROS","EFECTIVO"]},
        }
}

def get_json_by_ia(text):

    prompt = f"""
     Analiza el siguiente texto y extrae los datos en formato JSON.

    Si se menciona un gasto nuevo, la acción debe ser "ADD".
    Si se menciona la eliminación de un gasto, la acción debe ser "REMOVE".
    Si se menciona un cambio, la acción debe ser "UPDATE".

    El método de pago debe ser uno de: YAPE, INTERBANK, BCP, PLIN, CAJA, BBVA, SCOTIABANK, EFECTIVO, OTROS.
    Si el método de pago no está en la lista, usa "OTROS".
    Si el monto es un texto transformalo a número.
    Si no se menciona el monto, usa 0.
    Cualquier texto que no pueda interpretarse devuelve el json vacio.
    Solo crea un gasto.
    Texto: {text}
    """

    client = genai.Client(http_options=HttpOptions(api_version="v1"),
                      project="pontebarbon",
                      location="us-central1",
                      vertexai=True)
    
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents= prompt,
        config= {
            "response_mime_type": "application/json",
            "response_schema": response_schema,
        },
    )

    json_data = json.loads(response.text)

    return json_data













