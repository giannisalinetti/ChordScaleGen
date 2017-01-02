#!/usr/bin/python

from __future__ import print_function

#    Chords and scales random generator. Version 0.1.
#    Giovan Battista Salinetti 2015/03/02
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

#    This program takes two arguments as raw_input() from the user: chord or scale progression and the number of elements
#    The 'chords' and the 'scales' lists can be expanded with new material without altering the rest of the code

#    TODO:
#    Export to file facilities (html, csv, xml, improve plain text)

import random
import textwrap

def tone_prog(n):
    tone_list = []
    tones = ["C", "C#/Db", "D", "D#/Eb", "E", "F", "F#/Gb", "G", "G#/Ab", "A", "A#/Bb", "B"]
    for t in range(0, n):
        tone_list.append(random.choice(tones))
    return tone_list

def chord_prog(n):
    chord_list = []
    chords = [ "Major", "Minor", "Diminished", "Augmented", "Maj7", "Min7", "Min/Maj7", "7", "7sus4", "Min7b5", "Dim7", "7alt", "7b9", "Maj7#5", "7#11", "7b5", "7sus4b2", "Maj6", "Min6", "7b9#9", "7#5" ]
    for c in range(0, int(prog_len)):
        chord_list.append(random.choice(chords))
    return chord_list

def scale_prog(n):
    scale_list = []
    scales = [ "Major", "Natural Minor", "Melodic Minor", "Harmonic Minor", "Harmonic Major", "Whole Tone", "Half-Whole"]
    for s in range(0, n):
        scale_list.append(random.choice(scales))
    return scale_list

def export_ptext(tn, spec, repeats):
    name = raw_input("Choose ouput file name, .txt will be appended: ")
    file_name = name + ".txt"
    out_file = open( file_name, "w")
    out_file.write("ChordScaleGen v0.3\n\n")
    for l in range(0, repeats):
        out_file.write(tn[l] + " " + spec[l] + "\n")
    out_file.close

<<<<<<< HEAD:src/ChordScaleGen.py
print
print "             ChordScaleGen              "
print "Chords and scales generator, Version 0.2"
print
=======
width = 72
dotted_line = '-' * width
print(dotted_line)
print("\033[1m" + "ChordScaleGen" + "\033[0m")
print("\033[1m" + "Chords and scales generator, Version 0.3" + "\033[0m")
msg = (
    "This tool helps musicians to create random sequences "
    "of chords and scale to practice on instruments. Choose "
    "between chord or scale generation and the lenght of "
    "iteration (how much long the sequence will be")
print(textwrap.fill(msg, width=width))
print(dotted_line)

>>>>>>> NewFeatures:src/ChordScaleGen.py
mode = raw_input("Generagete chords(c) or scales(s)? ")
prog_len = raw_input("Set number of iterations: ")

if mode == "c" or mode == "C":
    print("\033[1m" + "Printing chord chart..." + "\033[0m" + "\n")
    print(dotted_line)
    chord_out = chord_prog(int(prog_len))
    tone_out = tone_prog(int(prog_len))
    for i in range(0, int(prog_len)):
         print(tone_out[i], chord_out[i])
    print(dotted_line)
    txt_exp = raw_input("\n" + "Export sequence to text file? Yes(y)/No(n) ")
    if txt_exp == 'y' or txt_exp == 'Y':
         export_ptext(tone_out, chord_out, int(prog_len))

elif mode == "s" or mode == "S":
    print("\033[1m" + "Printing scale chart..." + "\033[0m" + "\n")
    print(dotted_line)
    scale_out = scale_prog(int(prog_len))
    tone_out = tone_prog(int(prog_len))
    for i in range(0, int(prog_len)):
         print(tone_out[i], scale_out[i])
    print(dotted_line)
    txt_exp = raw_input("\n" + "Export sequence to text file? Yes(y)/No(n) ")
    if txt_exp == 'y' or txt_exp == 'Y':
         export_ptext(tone_out, scale_out, int(prog_len))

else:
    print("Wrong choice. You must press \"c/C\" for chords or \"s/S\" for scales.")
print("Goodbye.")
