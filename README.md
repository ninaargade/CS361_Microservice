# CS361_Microservice

REQUEST data: Request data by writing the random number (data) to the randNum.txt file. A sample call can be seen in the UI.py file:
        randNum = e.get()
        numFile = open('randNum.txt', 'w')
        numFile.write(randNum)
        numFile.close()
        
RECEIVE data: Receive data by reading a link (data) from the URLname.txt file. A sample call:
    linkFile = open('URL_name.txt', 'r')
    link = linkFile.read()
    linkFile.close()
    
Include a list of 5 URLS in the URL_List.txt file. The links should be delimited by a " " character.

UML Diagram:
![Blank diagram](https://user-images.githubusercontent.com/71619173/198929853-3e55ac3d-2f4e-4bfc-b8f0-19808da9c3b6.png)
