#imports
import json
class Read:
    @staticmethod
    def get_from(father:str,son:str)->None|str:
        try:
            with open("config.json", encoding="utf-8") as file:
                config = json.load(file)
            return config[father][son]

        except Exception:
            return None
#load func
# save func
# i get an name of file that you want to inspect and u get it
# i get a nme and value and i change the thing with that name in the json file
# the first func this will be if it is your first download
