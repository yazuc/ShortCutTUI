from prompt_toolkit import * 
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.shortcuts import choice
from prompt_toolkit.styles import Style
from prompt_toolkit.filters import is_done
from pathlib import Path
import os

Path = Path("/home/leozin/.local/share/applications")
result = ""
def ChooseAct():
    style = Style.from_dict(
        {
            "input-selection": "fg:#ff0000",
            "number": "fg:#884444 bold",
            "selected-option": "underline",
        }
    )
    result = choice(
        message="Please choose an option:",
        options=[
            ("Add", "Add a shortcut"),
            ("Remove", "Remove a shortcut"),
            ("Exit", "Exit"),
        ],
        style=style,
        bottom_toolbar=HTML(
            " Press <b>[Up]</b>/<b>[Down]</b> to select, <b>[Enter]</b> to accept."
        ),
        show_frame=~is_done,
    )
    return result 



def Remove():
    print("We've entered the remove function, say hi to it !!")
    print("Remove action")
    style = Style.from_dict(
        {
            "input-selection": "fg:#ff0000",
            "number": "fg:#884444 bold",
            "selected-option": "underline",
        }
    )
    delete_opt = choice(
        message="Please choose an option:",
        options=tuple((str(p.resolve()), p.name) for p in Path.iterdir()),
        style=style,
        bottom_toolbar=HTML(
            " Press <b>[Up]</b>/<b>[Down]</b> to select, <b>[Enter]</b> to accept."
        ),
        show_frame=~is_done,
    )
    os.remove(delete_opt)
    print("Deleted file:" + delete_opt)


while True:
    result = ChooseAct()

    if result == "Add":
        print("Add action")
        ChooseAct()
    if result == "Remove":
        Remove()
        ChooseAct()
    if result == "Exit":
        print("Exit action")
        os._exit(0)





