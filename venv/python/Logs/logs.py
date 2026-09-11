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
logging.basicConfig(filename=f'{project_root_path}//writing_logs.txt', level=logging.INFO, format="%(asctime)s - %(levelname)s -%(message)s", filemode="w")

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

    def __init__(self, url="https://jsonplaceholder.typicode.com/" ):
        self.url = url
        self.user_details = None

    def getting_user_details(self, user_id):
        try:
            logging.info("Test starts")
            response = requests.get(f'{self.url}users/{user_id}')
            response.raise_for_status()
            assert response.status_code == 200, "Getting response status code error"
            print(f'Response status code: {response.status_code}')
            self.user_details = response.json()
            json.dumps(self.user_details, indent=4)
        except requests.exceptions.HTTPError:
            logging.error(f'user_id={user_id} failed with status {response.status_code}')

    def getting_user_city(self):
        return self.user_details.get("address").get("city")

    def getting_user_detail_custom(self, key):
        return self.user_details.get(key)

url = "https://jsonplaceholder.typicode.com/"
user_id_list = [1, 1, 3]
user_name_list = ["Leanne Graham", "Clementine Bauch"]
user_city_list = []
user_name = None
api = API(url)

def tes():
    for user_id in user_id_list:
        api.getting_user_details(user_id)
        global user_name
        user_name = api.getting_user_detail_custom("name")

        if user_name in user_name_list:
            logging.info(f'{user_name} exist in user_names variable')
        else:
            logging.warning(f'{user_name} not in user_names variable')

        if api.getting_user_city() not in user_city_list:
            user_city_list.append(api.getting_user_city())

tes()
print(user_city_list)
print(f'String contains user name: {user_name}')