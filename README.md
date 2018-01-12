Question Maker GUI
==================
Thanks to this GUI application it is possible to create a proper database of
questions for the last game in [this](http://fare.polito.it/gioco/#section-3)
page.  It makes it easy to create and save the database file. The file
created, named `data.jj`, has to be moved to the folder where the game
executable is launched in order to be correctly read. 

HOW TO
======
* Download latest release from
  [here](https://github.com/Free-Polito/question-maker-gui/releases)
* Double click on ``questionmakergui`` file inside a folder with write
  permissions enabled.  

CREATE EXECUTABLE
==========
For developing purposes only:
* `pyinstaller -D -F -n questionmaker -c "main.py"`  
Tried only on Debian 8 

TODO
====
**v0.1-1**
* Check pylint and refactor code
* Use template for new python game
* Translate texts in English

AUTHOR
======
libremente 
<surf [AT] libremente [DOT] eu>

LICENSE
=======
GNU General Public License v3.0
