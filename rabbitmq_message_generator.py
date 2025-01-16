import pika
import time
import random
from faker import Faker

# RabbitMQ connection settings
RABBITMQ_HOST = 'localhost'
QUEUE_NAME = 'test_queue'

# Faker instance to generate random data
fake = Faker()

# Establish a connection to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
channel = connection.channel()

# Declare a queue
channel.queue_declare(queue=QUEUE_NAME)

print("Starting to publish messages to RabbitMQ... Press Ctrl+C to stop.")

try:
    while True:
        # Generate random message data
        message = {
            'name': fake.name(),
            'email': fake.email(),
            'address': fake.address(),
            'timestamp': fake.iso8601()
        }
        
        # Publish the message to the queue
        channel.basic_publish(exchange='', routing_key=QUEUE_NAME, body=str(message))
        print(f" [x] Sent: {message}")
        
        # Sleep for a random interval between 0.5 and 2 seconds
        time.sleep(random.uniform(0.5, 2.0))

except KeyboardInterrupt:
    print("\nStopped publishing messages.")
finally:
    # Close the connection
    connection.close()

