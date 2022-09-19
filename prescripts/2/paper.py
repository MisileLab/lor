from os import remove
from requests import get
from simple_term_menu import TerminalMenu
from os.path import isfile

def main():
    versions = get("https://api.papermc.io/v2/projects/paper").json()["versions"]
    menu = TerminalMenu(versions)
    menu.show()
    version = menu.chosen_menu_entry
    if version is None:
        return
    bversion = max(get(f"https://api.papermc.io/v2/projects/paper/versions/{version}").json()["builds"])
    with get(f"https://api.papermc.io/v2/projects/paper/versions/{version}/builds/{bversion}/downloads/paper-{version}-{bversion}.jar") as r:
        if isfile("paper.jar"):
            remove("paper.jar")
        with open("paper.jar", "wb") as f:
            f.write(r.content)
    print("done")

if __name__ == "__main__":
    main()
    
