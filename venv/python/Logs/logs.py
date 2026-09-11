import logging
import os.path
import requests
import json

# Set up basic logging with level=logging.DEBUG and a format string including timestamp and level.
# Log one message at each of the 5 levels.
# Set up logging to write to a file instead of the screen,
# run your script, then open the log file and confirm the messages were written correctly.
dirname = os.path.dirname(os.path.abspath(__file__))
print((dirname))
project_root_path = os.path.join(dirname, "..", "..", "..", "Test_Data")
print(project_root_path)
logging.basicConfig(filename=f'{project_root_path}//writing_logs.txt', level=logging.INFO, format="%(asctime)s - %(levelname)s -%(message)s")

logging.debug("This is DEBUG")
logging.info("This is INFO")
logging.warning("This is WARNING")
logging.error("This is ERROR")
logging.critical("This is CRITICAL")

# Wrap a risky operation (like int() conversion, or a division) in try/except,
# and use logging.error() (or logging.exception()) to log the failure instead of just printing it.
def intConversion(string):
    try:
        return int(string)
    except ValueError:
        logging.error("Type conversion error")
        return string
    except Exception as e:
        logging.exception(f'An exception occured in intConversion function {e}')
        return string
intConversion("sdfe234")

class API:
    user_details = None
    def __init__(self, url="https://jsonplaceholder.typicode.com/"):
        self.url = url

    def getting_user_details(self, user_id):
        try:
            logging.info("Test starts")
            response = requests.get(f'{self.url}users/{user_id}')
            response.raise_for_status()
            print(f'Response status code: {response.status_code}')
            global user_details
            user_details = response.json()
            print(json.dumps(user_details, indent=4))
        except requests.exceptions.HTTPError:
            logging.error(f'user_id={user_id} failed with status {response.status_code}')

    def getting_user_city(self):
        global user_details
        return user_details.get("address").get("city")

url = "https://jsonplaceholder.typicode.com/"
api = API(url)
user_ids = [1,1,3]
user_city_list = []
for user_id in user_ids:
    api.getting_user_details(user_id)
    print(api.getting_user_city())
    if api.getting_user_city() not in user_city_list:
        user_city_list.append(api.getting_user_city())
print(user_city_list)