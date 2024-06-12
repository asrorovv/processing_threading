

import threading
import multiprocessing
import time

def func1(file_name: str):
    enter = input(f"""
                1. Read file
                2. Create file >>> """)
    if enter == '1':
        try:
            with open(file_name, 'r') as file:
                data = file.read()
                if file_name is isEmpty():
                    x = input(""" THIS FILE IS EMPTY
                      Do you want to add something
                      1. Yes
                      2. No >>> """)
                    if x == '1':
                        time.sleep(1)
                        ent = input("Write something: ")
                        with open(file_name, 'w') as f:
                            exm = f.write(ent)
                    elif x == '2':
                        time.sleep(3)
                        breakpoint()
                    else:
                        return f"Error!"
                time.sleep(1)
                print(f"Data read from {file_name}: {data}")
        except Exception as error:
            print(f"Error! {error}")
    elif enter == '2':
        # Fayl nomini foydalanuvchidan so'raymiz
        file_name = input("Enter the name of file: ")

    # Matnni foydalanuvchidan qabul qilish
        data = input("Enter the information you want to write to the file: ")

    # Faylni yaratish va ma'lumotni yozish
        with open(file_name, 'w') as file:
            time.sleep(2)
            file.write(data)
        time.sleep(2)
        print(f"{file_name} was created successfully and written data")
    else:
        return func1



def isEmpty(file_name: str):
    #fayl bo'shligini tekshirish
    return len(file_name) == 0

def main():
    file_name1 = 'text.txt'
    file_name2 = 'text1.txt'
    data1 = 'Muhammadxon Asrorov Pyhton Django'
    data2 = 'Hasanjon Nazarov Node js '

    thread1 = threading.Thread(target=func1, args=(file_name1))
    thread2 = threading.Thread(target=func1, args=(file_name2))
    process1 = multiprocessing.Process(target=func1, args=(file_name1, data1))
    process2 = multiprocessing.Process(target=func1, args=(file_name2, data2))

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

if __name__ == '__main__':
    main()

