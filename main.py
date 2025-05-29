
from google import genai
from google.genai.types import HttpOptions

from kafka import KafkaProducer
import json
import time

response_schema = {
    "type": "OBJECT",
        "properties": {
            "action": {"type": "STRING","enum": ["AÑADIR", "REMOVER", "ACTUALIZAR"]},
            "description": {"type": "STRING"},
            "mount": {"type": "number"},
            "Payment method": {"type": "STRING","enum": ["YAPE", "INTERBANK", "BCP","PLIN", "CAJA", "BBVA","SCOTIABANK", "OTROS","EFECTIVO"]},
        }
}

prompt = """
     Analiza el siguiente texto y extrae los datos en formato JSON.

    Si se menciona un gasto nuevo, la acción debe ser "AÑADIR".
    Si se menciona la eliminación de un gasto, la acción debe ser "REMOVER".
    Si se menciona un cambio, la acción debe ser "ACTUALIZAR".

    El método de pago debe ser uno de: YAPE, INTERBANK, BCP, PLIN, CAJA, BBVA, SCOTIABANK, EFECTIVO, OTROS.
    Si el método de pago no está en la lista, usa "OTROS".
    Si el monto es un texto transformalo a número.
    Si no se menciona el monto, usa 0.
    Texto: "el gasto de cine lo pague con transferencia monto un sol"
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


print(response.text)

