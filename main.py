#imports
from logging import exception

from read import Read
from update import Update
#main block

def main()->None:
    try:
        path = Read.get_from("storage","downloadPath")
        if path == None:
            raise Exception("sorry didn't work")
        res = Update.uptodate(path)
        print(f"ok no errors but did it work? -> {res}")
    except Exception:
        print("sorry didn't work")
main()
# crate a spot in the pc that we will save and do evry thing there
# clone the new thing and replace it with the new thing
