#imports
import os
import subprocess
from read import Read
class Update:
    @staticmethod
    def uptodate(path:str)->bool:
        try:
            subprocess.run(
                ["git", "-C", path, "pull", "--ff-only", "origin", "main"],
                check=True
            )
            return True
        except Exception:
            return False




    @staticmethod
    def runpa(path: str) -> bool:
          try:
              subprocess.run(["sh", path], check=True)
              return True
          except (subprocess.CalledProcessError, OSError):
              return False
    #check for update
    # download will download the git clone
    # compare_files see if this file is good or outdated
    # apply updates for the app - update the json(if needed) replace the outdated files/code
    # clean the mess of the func that means that i will remove the clones that are not used anymore
