import time
import boto3
from datetime import datetime
from environment import AWS_REGION_NAME, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY

class Dynamodb:
    def __init__(self) -> None: 
        dynamo = boto3.resource(
            service_name = "dynamodb",
            region_name = AWS_REGION_NAME,
            aws_access_key_id = AWS_ACCESS_KEY_ID,
            aws_secret_access_key = AWS_SECRET_ACCESS_KEY
        )
        self.__weighings = dynamo.Table('weighings')
    
    def send(self, plant_id: int, weight: int) -> int:
        result = self.__weighings.put_item(
            Item = {
                "id": int(str(time.time()).replace(".","")),
                "content": {
                    "plant_id": plant_id,
                    "weight": weight,
                    "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
            }
        )
        return result['ResponseMetadata']['HTTPStatusCode']