from kafka import KafkaProducer
import json

def sendToKafka(json_data,topic):

    producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

    producer.send(topic, value=json_data)

    print("Mensaje enviado a Kafka: "+ str(json_data))

    producer.flush()