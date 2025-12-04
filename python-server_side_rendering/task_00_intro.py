#!/usr/bin/python3
"""
A simple templating program that generates personalized invitation files.
This module provides functionality to create invitation files from a template
with placeholders and a list of attendee objects.
"""


def generate_invitations(template, attendees):
    """
    Generate personalized invitation files from a template and attendee list.
    
    Args:
        template (str): A string template with placeholders in {placeholder} format
        attendees (list): A list of dictionaries containing attendee information
    
    The function creates output files named output_1.txt, output_2.txt, etc.
    Missing values in attendee data are replaced with "N/A".
    
    Error Handling:
        - Invalid input types: Logs error and terminates
        - Empty template: Logs error and terminates
        - Empty attendees list: Logs message and terminates
        - Missing attendee data: Replaces with "N/A"
    """
    # Check if template is a string
    if not isinstance(template, str):
        print("Error: Template is not a string.")
        return
    
    # Check if attendees is a list
    if not isinstance(attendees, list):
        print("Error: Attendees is not a list.")
        return
    
    # Check if attendees is a list of dictionaries
    if attendees and not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: Attendees is not a list of dictionaries.")
        return
    
    # Check if template is empty
    if not template:
        print("Template is empty, no output files generated.")
        return
    
    # Check if attendees list is empty
    if not attendees:
        print("No data provided, no output files generated.")
        return
    
    # Process each attendee
    for index, attendee in enumerate(attendees, start=1):
        # Start with the original template
        invitation = template
        
        # Replace placeholders with actual values or "N/A"
        # Find all placeholders in the template
        import re
        placeholders = re.findall(r'\{(\w+)\}', template)
        
        # Replace each placeholder
        for placeholder in placeholders:
            value = attendee.get(placeholder)
            
            # If value is None or missing, use "N/A"
            if value is None or value == "":
                value = "N/A"
            
            # Replace the placeholder in the invitation
            invitation = invitation.replace(f"{{{placeholder}}}", str(value))
        
        # Generate output filename
        output_filename = f"output_{index}.txt"
        
        # Write the invitation to the file
        try:
            with open(output_filename, 'w') as output_file:
                output_file.write(invitation)
        except IOError as e:
            print(f"Error writing to file {output_filename}: {e}")


if __name__ == "__main__":
    # Example usage for testing
    
    # Read the template from a file
    try:
        with open('template.txt', 'r') as file:
            template_content = file.read()
    except FileNotFoundError:
        # If template file doesn't exist, use a simple template
        template_content = """Hello {name},

You are invited to the {event_title} on {event_date} at {event_location}.

We look forward to your presence.

Best regards,
Event Team"""
    
    # List of attendees
    attendees = [
        {"name": "Alice", "event_title": "Python Conference", 
         "event_date": "2023-07-15", "event_location": "New York"},
        {"name": "Bob", "event_title": "Data Science Workshop", 
         "event_date": "2023-08-20", "event_location": "San Francisco"},
        {"name": "Charlie", "event_title": "AI Summit", 
         "event_date": None, "event_location": "Boston"}
    ]
    
    # Call the function with the template and attendees list
    generate_invitations(template_content, attendees)
