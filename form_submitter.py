import requests
import time

def get_user_input(prompt, default):
    user_input = input(prompt).strip()
    return user_input if user_input else default

def submit_form():
    default_url = "https://docs.google.com/forms/d/e/1FAIpQLSdRbjMqJ8uBtjuGzogXGj2R7GpGtM5NnVt_NP6kQhMGV_uY3A/formResponse"
    url = get_user_input("Enter the form URL or press enter to use the default: ", default_url)
    if not url.endswith('/formResponse'):
        url += '/formResponse'

    form_data = {}
    print("Enter the form data fields. Type 'done' when finished:")
    while True:
        field = get_user_input("Entry name (e.g., entry.123456): ", "done")
        if field == "done":
            break
        value = input("Value for the field: ")
        form_data[field] = value

    if not form_data: 
        form_data = {
            'entry.1492262284': 'Team 1',
            'entry.161041764': '5',
            'entry.1472206529': '5',
            'entry.628601682': '5',
            'entry.1128061035': '5',
        }

    n = int(input("Enter the number of submissions (default is 1): ") or 1)

    for i in range(n):
        try:
            response = requests.post(url, data=form_data)
            if response.status_code == 200:
                print(f"Form submitted successfully! Count: {i+1}")
            else:
                print(f"Failed to submit form: {response.status_code} Response: {response.text}")
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
        time.sleep(1)

if __name__ == "__main__":
    submit_form()
