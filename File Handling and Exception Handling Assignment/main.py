def mergeFiles(*texts):
    finalDocument = input("What should be the fina document name?, ensure u add the file extension please!")
    for doc in texts:
        print(doc)
        with open (f'{doc}', "r") as text:
            textData = text.read()
            with open (f"{finalDocument}", "a") as final_text:
                final_text.write(textData + "\n\n" )
    final = open("./final_document.txt", "r")
    print(final.read())
    final.close()

def openFile ():
    fileName = input("Which file do you wish to open?")
    try:
        with open (f"{fileName}", "r") as file:
            print(file.read())
    except Exception as err:
        print("Error was encountered due to", err)
    finally:
        print("Have a great day!")

# mergeFiles("definition.txt", "types.txt", "examples.txt", "importance.txt")

openFile()
