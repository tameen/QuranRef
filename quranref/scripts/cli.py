
import os
import sys
from typing import Optional 
import typer
#from database_conn import *
from pyramid.paster import get_appsettings, setup_logging
from quranref.scripts.surah_info_import import *
from quranref.scripts.text_import import *
from quranref.scripts.populate import *

app = typer.Typer()
quranref_app = typer.Typer() 
app.add_typer(quranref_app, name="quranref")

@quranref_app.command("quranref_populate")
def quranref_populate(val:str):
    populate_main("quranref_populate development.ini")
    print("quranref_populate development.ini")

@quranref_app.command("quranref_import_surah_info")
def quranref_scripts_surah_info_import(val:str):
    surah_info_import("quranref_import_surah_info development.ini")
    print("quranref_import_surah_info development.ini") 

@quranref_app.command("quranref_import_text")
def quranref_import_text(val:str):
    text_import_main("quranref_import_text development.ini "+ val)
    print("quranref_import_text development.ini")   
       

if __name__=="__main__":
    app()
