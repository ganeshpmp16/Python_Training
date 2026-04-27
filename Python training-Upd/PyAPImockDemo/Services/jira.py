# services/jira.py

import random # For generating mock ticket IDs.random is used to create unique ticket IDs in mock mode.
from config import MOCK_MODE

class JiraService:

    def __init__(self): # Initializes the JiraService class and sets the platform name.
        self.platform = "Jira"
    # self means the instance of the class. It allows us to access the attributes and methods of the class within its own methods. In this case, self.platform is set to "Jira", which can be used later to identify the source of the ticket when creating issues in Jira.
    def create_ticket(self, title, description, severity):
        payload = {
            "summary": title,
            "description": description,
            "priority": severity,
            "project": "ITOPS"
        }

        print("\n[JIRA] Sending request...")
        print("Payload:", payload)

        if MOCK_MODE:
            ticket_id = f"JIRA-{random.randint(100, 999)}"
            print("Mock Mode: Ticket created")

            return {
                "platform": self.platform,
                "ticket_id": ticket_id,
                "status": "Created"
            }

        # Real API logic will come later
        raise NotImplementedError("Real Jira API not implemented")





# #services jira.py
# import requests
# from config import JIRA_URL, JIRA_USERNAME, JIRA_API_TOKEN, MOCK_MODE
# def create_jira_issue(incident):
#     if MOCK_MODE:
#         print(f"Mock: Creating Jira issue for incident {incident['id']}")
#         return {"key": "MOCK-123", "url": f"{JIRA_URL}/MOCK-123"}
    
#     url = JIRA_URL
#     auth = (JIRA_USERNAME, JIRA_API_TOKEN)
#     headers = {"Content-Type": "application/json"}
#     data = {
#         "fields": {
#             "project": {"key": "INC"},
#             "summary": f"Incident {incident['id']}: {incident['short_description']}",
#             "description": incident['description'],
#             "issuetype": {"name": "Task"}
#         }
#     }
    
#     response = requests.post(url, json=data, auth=auth, headers=headers)
#     response.raise_for_status()
#     return response.json()
