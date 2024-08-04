wordleTI
A port of Wordle to TI-BASIC

v0.1 (alpha)

wordleTI is currently still in development, and is incomplete. If you encounter errors or problems, please post an issue on GitHub so they can be fixed!

This readme last updated on 3 Aug 2024.

Included files:

wordleTI/
|- readme.txt
|- calc-files/
|  |- Str1.8xs
|  |- Str2.8xs
|  |- Str3.8xs
|  |- Str4.8xs
|  |- Str5.8xs
|  |- Str6.8xs
|  |- Str7.8xs
|  |- WORDLE.8xg
|- generator-scripts/
|  |- answers-formatted.txt
|  |- answers.txt
|  |- makestrs.py
|  |- validwords-formatted.txt
|  |- validwords.txt

HOW TO USE:

First, send all the files in the folder calc-files/ to archive memory on your calculator, and ungroup WORDLE.8xg using the menu at [2nd][+][8]. 

Then, run prgmWORDLE! Enter letters using the normal buttons (you don't need to press [Alpha]), and use the [Del] key to delete letters. Once you have typed in your word, press [Enter].

If the word you entered is deleted, that means that it was not recognized as a valid word, so enter something else and try again.

A ^ under a letter means that that letter is both correct and in the right location, while a - under a letter means that the letter is somewhere in the word but is in an incorrect location.

For example:

M A T H S
  ^ -   ^

This would mean that the A and S are in the correct spot, and the T is somewhere in the word, but not in that spot.

KNOWN BUGS/ISSUES:

This project will break on Jun 28 2027 due to an issue with how SourceCoder 3 handles characters; specifically due to SourceCoder misinterprets the characters "PV" as a single "PV" token. I am working on a fix for this.

Acknowledgements:

- SourceCoder 3 (converting .txt files to TI's string format)
URL: cemetech.net/sc

- dracos (list of allowed words)
URL: gist.github.com/dracos/dd0668f281e685bad51479e5acaadb93

- Owen Yin (list of answers)
URL: medium.com/@owenyin/here-lies-wordle-2021-2027-full-answer-list-52017ee99e86

- Josh Wardle (creator of Wordle)
URL: powerlanguage.co.uk

