# F1nd3r BETA

This script takes the cmd line equation out for OSINT and Researchers. Very useful as well in Pen Testing to quickly search database dumps with lists of names or emails. So far initial tests with the python version work on csv files without the imported python module since we don't have an option to save in that format it still processes it like txt files. It will print each line if there is matches in both versions there are a few quirks to work out but pretty useful all around so far. 

Features include:

1.) Scan a file of names, emails, or any other data against another file or database.

2.) Scan a folder or directory and even the sub-directories of dumps or data.

3.) Is a 2 part scan of a single name or email for example to scan a single file
    or scan an entire folder/directory of files in your hunt.
# Install Instructions

For use on Linux distro's a Windows version will be released soon!

ps. Windows just sucks it won't even support some modules and color features as usual its worthless.
so we will make one in tkinter or something lol. 

```
git clone https://github.com/NiteR1d3r/F1nd3r.git
```
```
sudo pip install -r requirements.txt
```
Then run the file menu is super easy and interactive....
```
chmod +x f1nd3r1_0.py
python3 f1nd3r1_0.py

Bash Version:

chmod +x f1nd3r_beta.sh
./f1nd3r_beta.sh
```
# Example Use

Video and screenshot examples coming soon....

# TODO

1.) Add option to scan multiple files against multiple files.

2.) Fix threading in option3 still buggy or not sure if its even working completely yet :(

3.) Create GUI app for windows version.

4.) Release bash script version. [Done] fixing bugs

5.) Test on .sql files and other file formats so far bash version should work well not enough testing yet..


