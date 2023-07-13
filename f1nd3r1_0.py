from pyfiglet import Figlet
import os
from termcolor import colored
import threading
from queue import Queue
from matrix3 import matrix
#import time

# Data Hunter   
# By: NetR1d3r & Ebbaline

def banner():
    print('\n')
    f = Figlet(font='computer')
    print(colored("0101010100101010101010101010101010101010101010100101010101010010001010001", color="blue"))
    print('\n')
    print(colored(f.renderText('Th4 F1nd3r 1.0'), 'green'))
    print(colored("0101010100101010101010101010101010101010101010100101010101010010010001111", color="blue"))
    print('\n')
    print(colored("By: ", color="green" ), colored("N", color="red"), colored("e", color="blue"), colored("t", color="white"), colored("R", color="green"), colored("1", color="red"), colored("d", color="blue"), colored("3", color="red"), colored("r", color="green"), colored("& Ebbaline", color="magenta"))
    print('\n')
    print(colored("For OSINT Data Gathering and Hunting Through Dumps etc...", color="green"))
    
    

def menu():

    print('\n')
    print("1. Scan a Single File of Names or Data against another Single File")
    print("2. Scan a Directory with a Single File")
    print("3. Scan a Single Name or Data point with a File or Directory") 
    print(colored("4. Exit", color="red"))
    print('\n')
    choice = input("Enter your Choice 1-4: ")
    print('\n')

    if choice == '1':
        opt1()
    elif choice == '2':
        opt2()
    elif choice == '3':
        opt3()
    elif choice == '4':
        print("Ok Then Bye Bye Now...")
        matrix(3)
        exit()
    else:
        print(colored("Invalid choice Options are 1-4 press 4 to Exit", color="red"))
        print('\n')
        menu()

def opt1():
    # Option 1
    fileline_count = 0
    print(colored("Scan a Single File of Names or Data against another Single File", color="blue"))
    print('\n')

    def search_lines(key_words, all_lines, start_line, end_line, result_queue):
        for lin_no, line in enumerate(all_lines[start_line:end_line]):
            if any(word in line for word in key_words):
                result_queue.put((start_line + lin_no, line))

    file1 = input("Enter the Hunted file name: ")
    print('\n')
    if not os.path.exists(file1):
        print (colored("File does not exist", color="red"))
        print('\n')
        opt1()
    file2 = input("Enter the Second file name: ")
    print('\n')
    if not os.path.exists(file2):
        print (colored("File does not exist", color="red"))
        print('\n')
        opt1()

    with open(file1) as f:
        key_words = f.read().casefold().strip().splitlines()

    with open(file2) as f2:
        all_lines = f2.read().casefold().strip().splitlines()

    # Threading
    num_threads = 4  # Number of threads to use
    lines_per_thread = len(all_lines) // num_threads
    remaining_lines = len(all_lines) % num_threads

    result_queue = Queue()

    threads = []
    for i in range(num_threads):
        start_line = i * lines_per_thread
        end_line = (i + 1) * lines_per_thread

        if i == num_threads - 1:
            end_line += remaining_lines

        thread = threading.Thread(target=search_lines, args=(key_words, all_lines, start_line, end_line, result_queue))
        thread.start()
        threads.append(thread)
        for line in all_lines:
            fileline_count += 1
            print(f"\rScanning {fileline_count} lines ", end='', flush=True)    
    # Display file line count
    print('\n')
    # Wait for all threads to finish
    for thread in threads:
        thread.join()
    # Collect results from the queue
    results = []
    while not result_queue.empty():
        results.append(result_queue.get())

    if len(results) == 0:
        print(colored("No results found.", color="red"))
        print('\n')
        print("Do you want to scan another file? ")
        print('\n')
        print ("Enter 1 for Yes")
        print ("Enter 2 for No and to Exit")
        print('\n')
        anwser = input("Enter your choice: ")
        if anwser == '1':
            opt1()
        elif anwser == '2':
            print(colored("Exiting...", color="red"))
            matrix(3)
            exit()
        else:
            print(colored("Invalid choice Options are 1-2", color="red"))
            print('\n')
            print(colored("Returning to Options...", color="red"))
            print('\n')
            opt1()
    else:
        print("Data found:")
        print()
        for lin_no, line in results:
            print(colored("Line Number:", color="red"), lin_no)
            print(colored("Found: ", color="green", attrs=['bold']), line.strip())
            print()
    # Save results to a file

    while True:
        print("Save Scan results to a File? ")
        print('\n')
        print("Enter 1 for Yes")
        print("Enter 2 for No and to Exit")
        print('\n')
        choice = input("Enter your choice: ")
        print('\n')
        if choice == '1':
            print("Saving results to a file...")
            print('\n')
            save_file = input("Enter the name of the file to save results to: ")
            print('\n')
            with open(save_file, 'w') as f:
                for lin_no, line in results:
                    f.write(f"Line Number: {lin_no}\n")
                    f.write(f"{line.strip()}\n\n")
            print(f.name, " Has been saved to the following location: ", os.path.dirname(os.path.abspath(f.name)))
            print('\n')
            print("Press 1 to go back to the Main Menu.")
            print("Press 2 to scan another File.")
            print("Press 3 to Exit.")
            print('\n')
            choice = input("Enter your choice: ")
            print('\n')
            if choice == '1':
                menu()
                #exit()
            elif choice == '2':
                opt1()
            elif choice == '3':
                print(colored("Exiting...", color="red"))
                matrix(3)
                exit()
        elif choice == '2':
            print(colored("Exiting...", color="red"))
            matrix(3)
            exit()
        else:
            print(colored("Invalid choice Options are 1-3", color="red"))
            print('\n')
            continue
      
def opt2():
    
    # Option 2
    def search_lines(file, key_words, result_queue):
        with open(file, errors='ignore') as f:
            all_lines = f.read().casefold().strip().splitlines()
            for lin_no, line in enumerate(all_lines):
                if any(word in line for word in key_words):
                    result_queue.put((file, lin_no, line))

    print(colored("Scan a Folder/Directory of Files....", color="blue"))
    print('\n')
    file1 = input("Enter the Hunted File Name: ")
    print('\n')
    if not os.path.exists(file1):
        print(colored("Invalid File Name, Please enter a valid File Name", color="red"))
        print('\n')
        opt2()
        
    path = input("Enter the Folder/Directory Path: ")
    print('\n')
    if not os.path.exists(path):
        print(colored("Invalid Path, Please enter a valid Path", color="red"))
        print('\n')
        opt2()

    current_path = os.getcwd()
    print(current_path)
    print('\n')
    print("Files in the Folder/Directory are: ")
    print('\n')
    for root, dirs, files in os.walk(path):
        for file in files:
            print(os.path.join(root, file))
        for dir in dirs:
            print(os.path.join(root, dir))    

    with open(file1, errors='ignore') as f1:
        key_words = f1.read().casefold().strip().splitlines()
        print('\n')
        #print(colored("Data found : ", color="green"))
        print('\n')
        found_results = False
        files_in_dir = []
        for root, dirs, files in os.walk(path):
            for file in files:
                files_in_dir.append(os.path.join(root, file))

        result_queue = Queue()

        threads = []
        for file in files_in_dir:
            fileline_count = 0
            thread = threading.Thread(target=search_lines, args=(file, key_words, result_queue))
            thread.start()
            threads.append(thread)
            for line in file:
                fileline_count += 1
                print(f"\rScanning {fileline_count} lines ", end='', flush=True)
            
        # Wait for all threads to finish
        for thread in threads:
            thread.join()

        results = []
        while not result_queue.empty():
            results.append(result_queue.get())
        
        for file, lin_no, line in results:
            found_results = True
            print('\n')
            print(colored("File Name: ", color="green") + colored(file, color="blue"))
            print(colored("Line Number:", color="red"), lin_no)
            print(colored("Found: ", color="green", attrs=['bold']), line.strip())
            #print('\n')
            
        if not found_results:
            print(colored("No results found.", color="red"))
            print('\n')
            print("Do you want to scan another file? ")
            print('\n')
            print("Enter 1 for Yes")
            print("Enter 2 for No and to Exit")
            print('\n')
            answer = input("Enter your choice: ")
            if answer == '1':
                opt2()
            elif answer == '2':
                print(colored("Exiting...", color="red"))
                matrix(3)
                exit()
            else:
                print(colored("Invalid choice Options are 1-2", color="red"))
                print('\n')
                print(colored("Returning to Options...", color="red"))
                print('\n')
                opt2()
    
    while True:

        print("Save Scan results to a File? ")
        print('\n')
        print("Enter 1 for Yes")
        print("Enter 2 for No and to Exit")
        print('\n')
        choice = input("Enter your choice: ")
        print('\n')
        if choice == '1':
            with open(file1, errors='ignore') as f1:
                key_words = f1.read().casefold().strip().splitlines()
                files_in_dir = []
                for root, dirs, files in os.walk(path):
                    for file in files:
                        files_in_dir.append(os.path.join(root, file))
                save_file = input("Enter the File Name to save the results: ")

                result_queue = Queue()

                threads = []
                for file in files_in_dir:
                    thread = threading.Thread(target=search_lines, args=(file, key_words, result_queue))
                    thread.start()
                    threads.append(thread)

                # Wait for all threads to finish
                for thread in threads:
                    thread.join()

                with open(save_file, 'a', errors='ignore') as f2:
                    while not result_queue.empty():
                        file, lin_no, line = result_queue.get()
                        f2.write("File Name: " + str(file) + '\n')
                        f2.write("Line Number: " + str(lin_no) + '\n')
                        f2.write(line + '\n')
                        f2.write('\n')

            print('\n')
            print(f2.name, " Has been saved to the following location: ", os.path.dirname(os.path.abspath(f2.name)))
            print('\n')
            print("Press 1 to go back to the Main Menu.")
            print("Press 2 to scan another File.")
            print("Press 3 to Exit.")
            print('\n')
            choice = input("Enter your choice: ")
            print('\n')
            if choice == '1':
                menu()
                #exit()
            elif choice == '2':
                opt2()
            elif choice == '3':
                print("Exiting...")
                matrix(3)
                exit()
        elif choice == '2':
            print("Exiting...")
            matrix(3)
            exit()
        else:
            print("Invalid Choice press 1 or 2...")
            print('\n')
            continue

def opt3():

    # Option 3
    print("Press 1 Scan a Name or Data ex. an Email Address with a Single File")
    print("Press 2 and Scan a Directory or Folder of Files")
    print('\n')
    choice = input("Enter your Choice 1-2: ")
    print('\n')

    if choice == '1':
        name_Data = input("Enter the Name or Data: ")
        print('\n')
        file1 = input("Enter the File Name: ")
        print('\n')
        if not os.path.exists(file1):
            print(colored("File does not exist"))
            print('\n')
            opt3()

        
        with open(file1) as f1:
            fileline_count = 0
            words = f1.read().casefold().strip().splitlines()
            name_Data = name_Data.casefold()
            found_results = False
            print("Data found : ")
            print('\n')
            for lin_no, line in enumerate(words):
                fileline_count += 1
                print(f"\rScanning {fileline_count} lines ", end='', flush=True)
                if name_Data in line:
                    print('\n')
                    found_results = True
                    print(colored("Line Number:", color="red"), lin_no)
                    print(colored("Found: ", color="green", attrs=['bold']), line.strip())
                    print('\n')
            if not found_results:
                print('\n')
                print(colored("No Results Found...", color="red"))
                print('\n')
                print("Do you want to scan again? ")
                print('\n')
                print("Enter 1 for Yes")
                print("Enter 2 for No and to Exit")
                print('\n')
                answer = input("Enter your choice: ")
                if answer == '1':
                    print('\n')
                    opt3()
                elif answer == '2':
                    print(colored("Exiting...", color="red"))
                    matrix(3)
                    exit()

    
        while True:
            print('\n')
            print("Save Scan results to a File? ")
            print('\n')
            print("Enter 1 for Yes")
            print("Enter 2 for No and to Exit")
            print('\n')
            choice = input("Enter your choice: ")
            print('\n')
            if choice == '1':
                with open(file1) as f1:
                    words = f1.read().casefold().strip().splitlines()
                    name_Data = name_Data.casefold()
                    save_file = input("Enter the File Name to save the results: ")
                    print('\n')
                    with open(save_file, "w") as f2:
                        f2.write("Data found in File : " + file1)
                        f2.write('\n')
                        for lin_no, line in enumerate(words):
                            if name_Data in line:
                                f2.write("Line Number:")
                                f2.write(str(lin_no))
                                f2.write('\n')
                                f2.write(line.strip())
                                f2.write('\n')
                print(f2.name, " Has been saved to the following location: ", os.path.dirname(os.path.abspath(f2.name)))
                f2.close()
                print('\n')
                print("Press 1 to go back to the Main Menu.")
                print("Press 2 to scan another name or email etc...")
                print("Press 3 to Exit.")
                print('\n')
                choice = input("Enter your choice: ")
                print('\n')
                if choice == '1':
                    menu()
                elif choice == '2':
                    opt3()
                elif choice == '3':
                    print(colored("Exiting...", color="red"))
                    print('\n')
                    matrix(3)
                    exit()
            elif choice == '2':
                print(colored("Exiting...", color="red"))
                print('\n')
                matrix(3)
                exit()
            else:
                print(colored("Invalid Choice", color="red"))
                print('\n')
                continue

            thread1 = threading.Thread(args=name_Data, line=words)
            thread1.start()

            thread2 = threading.Thread(args=name_Data, line=words)
            thread2.start()

            thread1.join()
            thread2.join()

    elif choice == '2':
        found_results = False
        print('\n')
        name_Data = input("Enter the Name or Data: ")
        print('\n')
        path = input("Enter the Directory path: ")
        print('\n')
        if not os.path.isdir(path):
            print ("The path specified does not exist")
            print('\n')
            opt3()
        current_path = os.getcwd()
        print(current_path)
        print('\n')
        print("Files in the directory are: ")
        print('\n')
        for root, dirs, files in os.walk(path):
            for file in files:
                print(os.path.join(root, file))
            for dir in dirs:
                print(os.path.join(root, dir))
        print('\n')
        files_in_dir = []
        for root, dirs, files in os.walk(path):
            for file in files:
                files_in_dir.append(os.path.join(root, file))
        for file in files_in_dir:
            with open(file, errors='ignore') as f:
                fileline_count = 0
                name_Data = name_Data.casefold()
                all_lines = f.read().casefold().strip().splitlines()
                for lin_no, line in enumerate(all_lines):
                    fileline_count += 1
                    print(f"\rScanning {fileline_count} lines ", end='', flush=True)
                    if name_Data in line:
                        found_results = True
                        print('\n')
                        print(colored("Data found in: ", color="green"), file)
                        print(colored("Line Number: ", color="green"), lin_no)
                        print(colored("Line: ", color="green"), line)
                        print('\n')
        if not found_results:
            print('\n')
            print("No Results Found...")
            print('\n')
            print("Do you want to scan another directory? ")
            print('\n')
            print ("Enter 1 for Yes")
            print ("Enter 2 for No and to Exit")
            print('\n')
            choice = input("Enter your choice: ")
            print('\n')
            if choice == '1':
                opt3()
            elif choice == '2':
                print(colored("Exiting...", color="red"))
                print('\n')
                matrix(3)
                exit()
            else:
                print("Invalid Choice")
                print('\n')
                opt3()

        while True:
            print('\n')
            print("Save Scan results to a File? ")
            print('\n')
            print("Enter 1 for Yes")
            print("Enter 2 for No and to Exit")
            print('\n')
            choice = input("Enter your choice: ")
            print('\n')
            if choice == '1':
                files_in_dir = []
                for root, dirs, files in os.walk(path):
                    for file in files:
                        files_in_dir.append(os.path.join(root, file))
                save_file = input("Enter the File Name to save the results: ")
                print('\n')
                for files in files_in_dir:
                    with open(files, errors='ignore') as f:
                        name_Data = name_Data.casefold()
                        all_lines = f.read().casefold().strip().splitlines()
                        for lin_no,line in enumerate(all_lines):
                            if name_Data in line:
                                with open(save_file, 'a', errors='ignore') as f2:
                                    f2.write("File Name: " + str(files) + '\n')
                                    f2.write("Line Number: " + str(lin_no) + '\n')
                                    f2.write(line.strip() + '\n')
                                    f2.write('\n')
                                    f2.close()
                print('\n')
                print(f2.name, " Has been saved to the following location: ", os.path.dirname(os.path.abspath(f2.name)))
                print('\n')
                print("Press 1 to go back to the Main Menu.")
                print("Press 2 to scan another File.")
                print("Press 3 to Exit.")
                print('\n')
                choice = input("Enter your choice: ")
                print('\n')
                if choice == '1':
                    menu()
                elif choice == '2':
                    opt3()
                elif choice == '3':
                    print(colored("Exiting...", color="red"))
                    print('\n')
                    matrix(3)
                    exit()
            elif choice == '2':
                print(colored("Exiting...", color="red"))
                print('\n')
                matrix(3)
                exit()
            else:
                print("Invalid Choice")
                print('\n')
                continue
            
            thread1 = threading.Thread(args=name_Data, line=all_lines)
            thread1.start()

            thread2 = threading.Thread(args=name_Data, line=all_lines)
            thread2.start()

            thread1.join()
            thread2.join()
    else:
        print(colored("Invalid choice Options are 1-2", color="red"))
        print('\n')
        opt3()

def main():
    print('\n')
    

if __name__ == '__main__':
    banner()
    menu()
