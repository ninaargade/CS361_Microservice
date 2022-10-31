# CS361_Microservice

REQUEST data: Request data by writing the random number (data) to the randNum.txt file. A sample call can be seen in the UI.py file:
        randNum = e.get()
        numFile = open('randNum.txt', 'w')
        numFile.write(randNum)
        numFile.close()
        
RECEIVE data: Receive data by reading a link (data) from the URLname.txt file. A sample call:
    linkFile = open('URL_list.txt', 'r+')
    links = linkFile.read()
    linkFile.close()
    
Include a list of 5 URLS in the URL_List.txt file. The links should be delimited by a " " character.

UML Diagram:
