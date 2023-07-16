#!/bin/bash
# BETA
# Data f1nd3r Bash Version
# Authors Netr1d3r && Ebbaline 
# OSINT and Pen Testing Tool to Search files and directories faster for data..

Color_Off='\033[0m'
Red='\033[0;31m'          
Green='\033[0;32m'        
Yellow='\033[0;33m'       
Blue='\033[0;34m'         
Purple='\033[0;35m'       
Cyan='\033[0;36m'         
White='\033[0;37m'        

echo " "
banner()
{
	echo -e "${Red}[++++++++-----------------------------++++++++]"
	echo -e ${Cyan}
	figlet F1nd3r 1.0 
	echo -e "${Green}Bash Edition"
	echo " "
	echo -e "By Netr1d3r && ${Purple}Ebbaline "
	echo " "
	echo -e "${Red}[++++++++-----------------------------++++++++]"
	echo -e "${Color_Off}"
	echo " "
}


menu()
{
	PS3='Choose Scanning Options the Menu below: '
	opts=("Scan 2 Files one list and target list..."
		  "Use single file or list to scan a target directory..."
		  "Search a file or directory using single name, email etc.." 
		  "Quit...")
		  
	select usrch in "${opts[@]}"; do
		case $usrch in
			"Scan 2 Files one list and target list...")
				#echo "Coming Soon!"
				#exit
				opt1
				;;
			"Use single file or list to scan a target directory...")
				opt2
				;;
			"Search a file or directory using single name, email etc..")
				opt3
				;;
			"Quit...")
				echo "Exiting...."
				exit
				;;
			*) echo " "
			   echo -e "$REPLY is an Invalid Option!!! Enter 1-4..."
			   echo " "	 
			   menu	
				;;
				
		esac
	done
}			

opt1()
{
	echo " "
	echo -e "Enter full path if not in the same directory\nex. /home/${USER}/searchfile.txt..."
	echo " "
	
	read -p "Enter the file to search: " search_file
	
	if [ ! -f "$search_file" ]; then
		echo "File not found!"
		exit 1
	fi
	
	read -p "Enter the Target file to search for matches...: " target_file
	
	if [ ! -f "$target_file" ]; then
		echo "File not found!"
		exit 1
	fi
	
	COUNT=0
	
	while IFS= read -r line; do
		COUNT=$(( $COUNT + 1))
		if [[ -z "$line" || "$line" == \#* ]]; then
			continue
		fi
		
		matched_lines=$(grep -i -a "$line" "$target_file")
		if [[ -n "$matched_lines" ]]; then
			echo " "
			echo "Match found for: $line" 
			echo "Found in: $target_file"
			echo "On Line: $COUNT" 
			#echo "$matched_lines" 			
			echo "---------------------------------------" 
		fi
	done < "$search_file" > results.txt
	if [ -s "results.txt" ]; then
	  cat "results.txt"
	else
		echo "No matches found."
		rm results.txt
		exit
	fi
	echo "Done! Scan results saved as results.txt"
	echo " "
	exit 
}

opt2()
{

	echo " "
	echo -e "Enter full path if not in the same directory\nex. /home/${USER}/searchfile.txt..."
	echo " "

	read -p "Enter the Directory to search: " search_directory
	echo " "

	if [ ! -d "$search_directory" ]; then
		echo "Directory not found!"
		exit 1
	fi

	read -p "Enter the Target file to search the directory for...: " target_file

	if [ ! -f "$target_file" ]; then
		echo "File not found!"
		exit 1
	fi

	COUNT=0

	find "$search_directory" -type f -print0 | while IFS= read -r -d '' file; do
		while IFS= read -r line; do
			COUNT=$((COUNT + 1))
			
			if [[ -z "$line" || "$line" == \#* ]]; then
				continue
			fi
			
			matched_lines=$(grep -i -a -r "$line" "$file")
			
			if [[ -n "$matched_lines" ]]; then
				echo " "
				echo "Match found for: $line"
				echo "Found in: $file"
				echo "On Line: $COUNT"
				echo "$matched_lines"
				echo "---------------------------------------"
			fi
		done < "$target_file" 
		COUNT=0
	done > dir_results.txt
	if [ -s "dir_results.txt" ]; then
	cat "dir_results.txt"
	else
		echo "No matches found."
		rm dir_results.txt
		exit
	fi
	echo "Done! Scan results saved as dir_results.txt"
	echo " "
	exit
}

opt3()
{
	echo " "
	echo -e "Scan a file or directory/subdirectories for name, email, piece of data etc...."
	echo " "
	read -p "Enter the name to search ex. email@email.com : " target_name
	echo " " 
	read -p "Enter the file name for ex. /home/${USER}/searchfile.txt or directory ex. ${PWD} " search_var
	echo " " 

	COUNT=0
	matched_lines=$(grep -i -a -r -n $target_name "$search_var")
	if [[ -n "$matched_lines" ]]; then
		COUNT=$((COUNT + 1))
		#echo " "
		echo "Match found for: $target_name"
		echo "Found in: $search_var"
		#echo "On Line: $COUNT"
		echo "$matched_lines"
		echo "---------------------------------------"
	fi > single_namescan.txt
	if [ -s "single_namescan.txt" ]; then
	cat "single_namescan.txt"
	else
		echo "No matches found."
		rm single_namescan.txt
		exit
	fi
	echo "Done! Scan results saved as single_namescan.txt"
	echo " "
	exit
}

banner
menu

