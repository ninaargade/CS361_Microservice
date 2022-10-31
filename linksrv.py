import time

while True:
    time.sleep(1.0)
    linksFile = open('URL_list.txt', 'r+')
    links_list = linksFile.read()
    linksFile.close()
    li = list(links_list.split(" "))

    numFile = open('randNum.txt', 'r+')
    line = numFile.read()
    numFile.close()

    if line.isnumeric():
        # Use Mod operator to mod number with number of images
        remainder = int(line) % 5
        URL_name = li[remainder]
        URLFile = open('URLName.txt', 'w')
        URLFile.write(URL_name)
        URLFile.close()
      
