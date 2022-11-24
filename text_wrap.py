import textwrap

def wrap(string, max_width):
       
    return '\n'.join(textwrap.wrap(string,width=max_width)
                     
    # return textwrap.fill(string,max_width) can be done as well! 

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
