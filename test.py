def trepalce(olds,news,file_path,occ=0):
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


trepalce("us","hag","/home/kratos/Documents/streamhash/file.txt")