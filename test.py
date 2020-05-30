def trepalce(olds: object, news: object, file_path: object, occ: object = 0) -> object:
    fin = open(file_path, "rt")
    #read file contents to string
    data = fin.read()
    #replace all occurrences of the required string
    if occ==0:
        data = data.replace(str(olds), str(news))
    else:
        data = data.replace(str(olds), str(news), occ)
    #close the input file
    fin.close()
    #open the input file in write mode
    fin = open(file_path, "wt")
    #overrite the input file with the resulting data
    fin.write(data)
    #close the file
    fin.close()


trepalce("max_execution_time = 30","max_execution_time = -1","/home/alpha/Desktop/stream hash/phptest.ini")
trepalce("max_input_time​= 60","max_input_time = -1","/home/alpha/Desktop/stream hash/phptest.ini")
trepalce("memory_limit = 128M","memory_limit​= -1","/home/alpha/Desktop/stream hash/phptest.ini")
trepalce("upload_max_filesize = 2M","upload_max_filesize = 5000M","/home/alpha/Desktop/stream hash/phptest.ini")
trepalce("post_max_size = 8M","post_max_size​ =3000M","/home/alpha/Desktop/stream hash/phptest.ini")
