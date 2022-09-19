from os import remove
from requests import get
from simple_term_menu import TerminalMenu
from os.path import isfile

def main():
    versions = get("https://api.purpurmc.org/v2/purpur").json()["versions"]
    menu = TerminalMenu(versions)
    menu.show()
    version = menu.chosen_menu_entry
    if version is None:
        return
    with get(f"https://api.purpurmc.org/v2/purpur/{version}/latest/download") as r:
        if isfile("purpur.jar"):
            remove("purpur.jar")
        with open("purpur.jar", "wb") as f:
            f.write(r.content)
    print("done")

if __name__ == "__main__":
    main()
    
