#imports
import os
import subprocess
from read import Read
class Update:
    @staticmethod
    def uptodate(path:str)->bool:
        try:
            subprocess.run(
                    ["git", "pull", "--ff-only"],
                    cwd=path,
                    check=True,
                    capture_output=True,
                    text=True,
                )
            return True
        except Exception:
            return False
    #check for update
    # download will download the git clone
    # compare_files see if this file is good or outdated
    # apply updates for the app - update the json(if needed) replace the outdated files/code
    # clean the mess of the func that means that i will remove the clones that are not used anymore
