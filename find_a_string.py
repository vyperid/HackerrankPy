def count_substring(string, sub_string):
    
    count = 0
    
    string.replace(" ", "")
    
    stringLen=len(string) 
    subsLen=len(sub_string) 
    
    loop = stringLen - subsLen + 1
    
    for i in range(loop):
        if string[i:i+subsLen] == sub_string:
            count+=1
        
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
