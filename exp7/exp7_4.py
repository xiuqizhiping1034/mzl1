# import pickle
#
# def main:
#     str = "python123"
#
#     num = 12345.6789
#
#     list = [123, 'abc', [1, 2, 3]]
#
#
#     pickle.dump(pickle.load("C:\Users\Lenovo\Desktop\test\4-1.in"), "C:\Users\Lenovo\Desktop\test\4-1.in")
#     pickle.dump(pickle.load("C:\Users\Lenovo\Desktop\test\4-1.in"), "C:\Users\Lenovo\Desktop\test\4-1.in")
#     pickle.dump(pickle.load("C:\Users\Lenovo\Desktop\test\4-1.in"), "C:\Users\Lenovo\Desktop\test\4-1.in")
#     pickle.dump(str, "C:\Users\Lenovo\Desktop\test\4-1.in")
#     pickle.dump(num, "C:\Users\Lenovo\Desktop\test\4-1.in")
#     pickle.dump(list, "C:\Users\Lenovo\Desktop\test\4-1.in")
# main()


import pickle

def main():
    input = open(r"input.dat", "rb")
    output = open(r"output.dat", "wb")
    str = "python123"

    num = 12345.6789

    list = [123, 'abc', [1, 2, 3]]


    pickle.dump(pickle.load(input), output)
    pickle.dump(pickle.load(input), output)
    pickle.dump(pickle.load(input), output)
    pickle.dump(str, output)
    pickle.dump(num, output)
    pickle.dump(list, output)
    input.close()
    output.close()
main()