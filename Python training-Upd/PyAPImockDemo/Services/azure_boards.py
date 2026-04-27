# services/azure_boards.py

import random
from config import MOCK_MODE

class AzureBoardsService:

    def __init__(self):
        self.platform = "Azure Boards"

    def create_ticket(self, title, assigned_to, severity):
        payload = {
            "title": title,
            "assigned_to": assigned_to,
            "priority": severity
        }

        print("\n[Azure Boards] Sending request...")
        print("Payload:", payload)

        if MOCK_MODE:
            ticket_id = f"AZ-{random.randint(5000, 9999)}"
            print("Mock Mode: Ticket created")

            return {
                "platform": self.platform,
                "ticket_id": ticket_id,
                "status": "Created"
            }

        raise NotImplementedError("Real Azure API not implemented")