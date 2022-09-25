# 今天开始 new life new begin
"""
python 文件操作

"""
# f= open(r'C:\Users\Lenovo\Desktop\test.txt','r',encoding='utf-8')
# print(f.read())
# f.close()
#
# b= open('C:\\Users\\Lenovo\\Desktop\\test.txt','r',encoding='utf-8')
# print(b.read())
# b.close()
# read = open('input.txt','r')


    # # Open file for input
    # infile = open("/test.txt", "r")
    # print("(1) Using read(): ")
    # print(infile.read())
    # infile.close() # Close the input file
    #
    # # Open file for input
    # infile = open('/input.txt', "r",encoding="utf-8")
    # print("\n(2) Using read(number): ")
    # s1 = infile.read(4)
    # print(s1)
    # s2 = infile.read(10)
    # print(repr(s2))

    # s3 = infile.read(15)
    # numbers = [eval(x) for x in repr(s3).split()]
    # print(numbers)

    # infile.close() # Close the input file

    # Open file for reading data
    # infile = open("/input.txt", "r",encoding="utf-8")
    # infile = open(r"input.txt", "r",encoding="utf-8")
def main():
    infile = open(r'/input.txt', "r")
    s = infile.read()

    print(len(s),"characters")

    s = s.lower()
    count = 0
    for string in s.split():
        count+=1
    print(count, "words")

    count = 0
    for string in s.split('\n'):
        count += 1
    print(count, "lines")
    infile.close()  # Close the file
main()  # Call the main function






    # numbers = [eval(x) for x in s.split()]
    # for number in numbers:
    #     print(number, end=" ")
    # count = 0
    # for string in s:
    #     count+=1

    #
    # # Open file for input
    # infile = open('/input.txt', "r",encoding="utf-8")
    # print("\n(3) Using readline(): ")
    # line1 = infile.readline()
    # line2 = infile.readline()
    # line3 = infile.readline()
    # line4 = infile.readline()
    # print(repr(line1))
    # print(repr(line2))
    # print(repr(line3))
    # print(repr(line4))
    # infile.close() # Close the input file
    #
    # # Open file for input
    # infile = open('/input.txt', "r",encoding="utf-8")
    # print("\n(4) Using readlines(): ")
    # print(infile.readlines())
    # infile.close() # Close the input file




