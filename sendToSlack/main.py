import base64
import requests

def send_to_slack(event, context):
    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    url = 'webhookurl'
    mess = {"text":pubsub_message}
    request = requests.post (url, json=mess)
