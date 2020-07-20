#-----------------------#
#   Prints out even 	#
#	numberbed lines		#
#	in directory		#
#-----------------------#
#	Luis Valdivia		#
#		CSE 150			#
#-----------------------#

#!/bin/bash

for i in *; 	#This line is a wildcard

do
	Script=LuisValdivia-Script.sh	#Uses the script that I created
	if [ $i != $Script ]; then		#Checks any other file besides my .sh file
		awk 'NR % 2 == 0 {print" '"$i"'" ":" $0}' "$i"  #Prints out the even lines in a text file
	fi #I use 'awk' because it analyzes text files in particular data files that are organized
	   #by rows and columns
done





