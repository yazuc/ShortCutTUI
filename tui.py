from prompt_toolkit import * 
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.shortcuts import choice
from prompt_toolkit.styles import Style
from prompt_toolkit.filters import is_done
from pathlib import Path
from prompt_toolkit.shortcuts import button_dialog
from prompt_toolkit.shortcuts import message_dialog
from prompt_toolkit.shortcuts import input_dialog
import os
import shutil

#kitty zsh -c "cd /mnt/Nvme/ShortCutTUI/ ; python3 tui.py"
#Importa o esqueleto de uma .desktop entry, baseado na archwiki
Skeleton = open("./example")
out = Skeleton.read()
if os.path.exists("temp"):
    os.remove("temp")

src = "/home/leozin/.local/share/applications"
Path = Path(src)
result = ""
clear = lambda: os.system('clear')
clear()
#TODO: Pess [Q] to quit
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
        enable_interrupt=True,
        show_frame=~is_done,
    )
    return result 


def Add():
    clear()
    name = input_dialog(
        title='Input a name for your shortcut',
        text='Please type your name:').run()

    comment = input_dialog(
        title='Input a comment for your shortcut',
        text='Please type your comment:').run()
    path = input_dialog(
        title='Input a path for your shortcut',
        text='Please type your path:').run()
    exec = input_dialog(
        title='Input the exec command for your shortcut',
        text='Please type your exec:').run()
    #icon = input_dialog(
    #    title='Input dialog example',
    #    text='Please type your name:').run()
    terminal = button_dialog(
        title='Does your shortcut use Terminal?',
        text='Does your shortcut use Terminal?',
        buttons=[
            ('Yes', "True"),
            ('No', "False")
        ],
    ).run()
    #categories = input_dialog(
    #    title='Input dialog example',
    #text='Please type your name:').run()
    eof = out
    eof = eof.replace("{Name}", name)
    eof = eof.replace("{Comment}", comment)
    eof = eof.replace("{Path}", path)
    eof = eof.replace("{Exec}", exec)
    #eof = eof.replace("{Icon}", icon)
    eof = eof.replace("{Terminal}", terminal) #true or false
    #eof = eof.replace("{Categories}", categories)
   

    result = button_dialog(
        title='Double check it',
        text=eof,
        buttons=[
            ('Yes', True),
            ('No', False)
        ],
    ).run()

    if result:
        #isso acontece após finalizada as alterações na string temp
        with open(src + "/" + name +".desktop", "x") as f:
            f.write(eof)

        message_dialog(
        title='Mensagem',
            text='O atalho foi salvo em ' + src).run()
    else:
      message_dialog(
        title='Mensagem',
        text='O atalho não foi salvo').run()


def Remove():
    clear()
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
        enable_interrupt=True,
        show_frame=~is_done,
    )

    result = button_dialog(
        title='Double check it',
        text="Do you really want to delete this entry?",
        buttons=[
            ('Yes', True),
            ('No', False)
        ],
    ).run()
    
    if result:        
        os.remove(delete_opt)
        clear()
        print("Deleted file:" + delete_opt)
    else:
        clear()
        print("File not deleted.")


while True:
    result = ChooseAct()

    if result == "Add":
        Add()
        clear()
        result = ChooseAct()
    if result == "Remove":
        Remove()
        result = ChooseAct()
    if result == "Exit":
        clear()
        os._exit(0)





