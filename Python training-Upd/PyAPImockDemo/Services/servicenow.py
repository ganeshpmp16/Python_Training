# services/servicenow.py

import random
from config import MOCK_MODE

class ServiceNowService:

    def __init__(self):
        self.platform = "ServiceNow"

    def create_ticket(self, title, description, severity):
        payload = {
            "short_description": title,
            "description": description,
            "urgency": severity
        }

        print("\n[ServiceNow] Sending request...")
        print("Payload:", payload)

        if MOCK_MODE:
            ticket_id = f"SNOW-{random.randint(1000, 9999)}"
            print("Mock Mode: Ticket created")

            return {
                "platform": self.platform,
                "ticket_id": ticket_id,
                "status": "Created"
            }

        raise NotImplementedError("Real ServiceNow API not implemented")