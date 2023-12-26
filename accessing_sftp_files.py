import pysftp

host = "test.rebex.net"
username = "demo"
password = "password"

with pysftp.Connection(host=host,username=username,password=password) as sftp:
    print("connection successfully established")
    
    #switch to the remote directory
    sftp.cwd("pub/example")
    print("switched to the current working directory")
    
    #check the directory structure ...we assign it to a variable directory_structure
    #we can give it any name whatasoever
    directory_structure = sftp.listdir_attr()
    
    #print all the data there in using the for loop
    for attr in directory_structure:
        print(attr.filename,attr)
    
    #lets download the data,for this case its a readme.txt file
    sftp.get("readme.txt","readme.txt")
    print("already downloaded the readme.txt")
    
    sftp.close()
    