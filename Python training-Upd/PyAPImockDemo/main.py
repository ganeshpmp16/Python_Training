# main.py

from Services.jira import JiraService
from Services.servicenow import ServiceNowService
from Services.azure_boards import AzureBoardsService

def main():

    # Sample incident
    title = "Database timeout in payment service"
    description = "Users unable to process payments due to DB timeout"
    severity = "High"
    assigned_team = "Database Team"

    # Initialize services
    jira = JiraService()
    snow = ServiceNowService()
    azure = AzureBoardsService()

    # Call services
    jira_result = jira.create_ticket(title, description, severity)
    snow_result = snow.create_ticket(title, description, severity)
    azure_result = azure.create_ticket(title, assigned_team, severity)

    print("\n--- Final Results ---")
    print(jira_result)
    print(snow_result)
    print(azure_result)


if __name__ == "__main__": # This line checks if the script is being run directly (as the main program) rather than imported as a module. If this condition is true, it calls the main() function to execute the program.
    main()