Question Maker GUI
==================
This package is meant for creating a proper database of questions for the
[game](http://fare.polito.it/gioco). It has a GUI interface in order to easily
create and save the database file. The file created has to be moved to the
folder where the game executable is launched. 

HOW TO
======
* Download latest release from
  [here](https://github.com/Free-Polito/question-maker-gui/releases)
* Double click on ``questionmakergui`` file inside a folder with write
  permissions enabled.  

CREATE EXECUTABLE
==========
For developing purposes only:
* pyinstaller -D -F -n questionmaker -c "main.py"
-> Tried only on Debian 8 

TODO
====
* Use template for new python game
* Translate texts in English

FIXED BUGS
==========
* [1] FIXED ~~Does not work with this numbering, change to 1 to 3 (instead of 0 to 2)~~ 

KNOWN BUGS
==========
None

AUTHOR
======
libremente <surf [AT] libremente [DOT] eu>

LICENSE
=======
GNU General Public License v3.0
