#!/bin/bash

echo -n "Type a, b, c or d for a suprise message:"

valid=0

while
[ $valid == 0 ]
do
	read ans
	case $ans in
	a|A         ) 	echo "Have a good day"
			valid=1
			;;

	b|B    	    )   echo "You're the best"
			valid=1
			;;

	c|C 	    )   echo "Hope you're doing good today"
                        valid=1
                        ;;

	d|D         )   echo "I ran out of things to say, sorry"
                        valid=1
                        ;;

	*	    )   echo Please enter a, b, c, or d ;;

	esac
done
