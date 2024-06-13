import os
import threading
import multiprocessing
import time



def isEmpty():
    return os.stat(os.getcwd()).st_size == 0
def isExist():
    return os.path.exists(os.getcwd()) and os.stat(os.getcwd()).st_size != 0
def main():
    enter = input("""
            1. Create file
            2. Read file >>> """)
    if enter == '1':
        file_name = input("Enter file name: ")
        if not isExist():
            print("File exist")
            return main()
        type_file = input("Enter file type: ")
        while type_file == 'csv' and 'txt' and 'py' and 'xml' and ('yaml' or 'yml') and ('xls' or 'xlsx'):
            type_file = input("Enter file type: ")
        data = input("""
                Do you want to add something
                1. yes
                2. no
        """)
        if data == '1':
            data_file = input("Enter data: ")
            with open(f"{file_name}.{type_file}", "w") as f:
                f.write(data_file)
                time.sleep(2)
                print("The file has been saved successfully")
        elif data == '2':
            with open(f"{file_name}.{type_file}", "w") as fayl:
                fayl.write('')
                time.sleep(2)
                print("The file has been saved successfully")
        else:
            print("Invalid input")
            return main()
        process1 = multiprocessing.Process(target=main(), args=(file_name, type_file))
        process1.start()
        process1.join()
        file_name1 = 'text.txt'
        file_name2 = 'text2.txt'

        thread1 = threading.Thread(target=read_file, args=(file_name1,))
        thread2 = threading.Thread(target=read_file, args=(file_name2,))

        thread1.start()
        thread2.start()
        thread1.join()
        thread2.join()


    elif enter == '2':
        return read_file
def read_file(file_name: str):
    try:
        with open(file_name, 'r') as file:
            data = file.read()
        print(f"The file has been read from {file_name}: {data}")
    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    print(main())