import os, random
# from crypto import AES
from PIL import ImageTk
import PIL.Image
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import sqlite3

rot = Tk()
rot.title('Encryption System')

# root.geometry("400x400")

connecting = sqlite3.connect('imagedb.db')
d = connecting.cursor()

# d.execute("""CREATE TABLE encimages (
#        imagenumber INT,
#        image VARCHAR,
#        imagename TEXT
#        )""")
# d.execute("""CREATE TABLE decimages (
#         imagenumber INT,
#         image BLOB
#         )""")
# d.execute("""CREATE TABLE registration (
#         name TEXT,
#        email TEXT,
#         contact INT,
#         location TEXT,
#         uname TEXT,
#         password VARCHAR
#         )""")
d.execute("""INSERT INTO registration (name, email, contact, location, uname, password)
            VALUES (Amittai, amittai, 12, ken, amittai, "rt")""")

def crypto():
    connector = sqlite3.connect('imagedb.db')
    f = connector.cursor()
    sets = f.execute("SELECT uname FROM registration WHERE uname=" + uname.get())
    if uname.get() == sets.fetchall():
        set1 = f.execute("SELECT password FROM registration WHERE password=" + password.get())
        if password.get() == set1.fetchall():
            root = Tk()
            root.title('Encrypt/Decrypt')
            conn = sqlite3.connect('imagedb.db')

            def encryptfunction():
                global rootfilename
                global finalenc
                if str(key.get()) == 'sonybravia':
                    root.filename = filedialog.askopenfile(initialdir="C:\\Users\\hp\\Desktop\\Images",
                                                           title="Select File",
                                                           filetypes=(("png files", "*.jpg"), ("all files", "*.*")))
                    rootfilename = ImageTk.PhotoImage(PIL.Image.open(root.filename))
                    # return rootfilename
                    chunk_size = 64 * 1024  # chunk_size is the size of the chunk which the function uses to read and encrypt the
                    # file and must be divisible by 16
                    out_image = root.filename.get() + ".enc"  # the name of the file is saved with the .enc as its extension
                    file_size = str(os.path.getsize(rootfilename), encoding="utf8").zfill(
                        16)  # get the size of the file and convert to string and store it in the file_size variable
                    iv = ''  # the initialization factor
                    for i in range(16):
                        iv += chr(random.randint(0, 0xFF))  # a 16 byte  initialization factor is randomly generated
                    encryptor = AES.new(AES.MODE_CBC, iv)  # create an AES encryptor Object
                    with open(rootfilename, 'rb') as inputfile:
                        with open(out_image, 'wb') as outf:
                            outf.write(file_size)
                            outf.write(iv)
                            while True:
                                chunk = inputfile.read(chunk_size)
                                if len(chunk) == 0:
                                    break
                                elif len(chunk) % 16 != 0:
                                    chunk += ' ' * (16 - len(chunk) % 16)
                                finalenc = outf.write(encryptor.encrypt(chunk))
                    connect = sqlite3.connect('imagedb.db')
                    e = connect.cursor()
                    e.execute("INSERT INTO encimages VALUES (:imagenumber, :imagename, :image)",
                              {
                                  'imagenumber': indexno.get(),
                                  'imagename': out_image,
                                  'image': finalenc,
                              })
                    connect.commit()
                    connect.close()
                else:
                    messagebox.showinfo("Security Alert!!!", "Wrong Key!!!")
                    root.destroy()

            def decrypt():
                if key.get() == 'sonybravia':
                    connect = sqlite3.connect('imagedb.db')
                    e = connect.cursor()
                    results = e.execute("SELECT image FROM encimages WHERE imagenumber = " + str(index.get()))
                    recordings = results.fetchall()
                    record = ''
                    for recording in recordings[1]:
                        record += recording
                    newrecord = record
                    chunk_size = 64 * 1024
                    output_file = newrecord[:-4]
                    with open(newrecord, 'rb') as inf:
                        filesize = long(inf.read(16))
                        iv = inf.read(16)
                        decryptor = AES.new(key, AES.MODE_CBC, iv)
                        with open(output_file, 'wb') as outf:
                            while True:
                                chunk = inf.read(chunk_size)
                                if len(chunk) == 0:
                                    break
                                outf.write(decryptor.decrypt(chunk))
                            outf.truncate(filesize)

                    connect.commit()
                    connect.close()
                else:
                    messagebox.showwarning("Security Alert!!!")  # style to show error message for 10 seconds
                    root.destroy()

            def openimage():
                test = Tk()
                test.title('Testing...')

                connec = sqlite3.connect('imagedb.db')
                g = connec.cursor()
                g.execute("SELECT image FROM encimages WHERE imagenumber = " + testnum)
                testers = g.fetchall()
                records = ''
                for tester in testers[1]:
                    records += tester
                testlabel = Label(test, text=records)
                testlabel.pack()
                connec.commit()
                connec.close()

                test.mainloop()

            label = Label(root, text='WELCOME TO CRYPTO', font="Verdana 11  bold")
            label1 = Label(root, text='Please Enter The Security Key')
            label4 = Label(root, text='Enter Chosen Index Number')
            label2 = Label(root, text='Decrypt')
            label3 = Label(root, text='Test')

            decryptbutton = Button(root, text='Decrypt', command=decrypt)
            encryptbutton = Button(root, text='Encrypt', command=encryptfunction)
            testbutton = Button(root, text='View Image', command=openimage)

            key = Entry(root)
            indexno = Entry(root)
            index = Entry(root)
            testnumber = Entry(root)

            label.grid(row=0, columnspan=3)
            label1.grid(row=1, column=0, padx=10, pady=10)
            key.grid(row=2, column=0, padx=10, pady=10)
            label4.grid(row=3, column=0, padx=10, pady=10)
            indexno.grid(row=4, column=0, padx=10, pady=10)
            encryptbutton.grid(row=5, column=0, padx=10, pady=10)
            label2.grid(row=6, column=0, padx=10, pady=10)
            index.grid(row=6, column=0, padx=10, pady=10, columnspan=2)
            decryptbutton.grid(row=7, column=0, padx=10, pady=10)
            label3.grid(row=8, column=0, padx=10, pady=10)
            testnumber.grid(row=9, column=0, padx=10, pady=10)
            testbutton.grid(row=10, column=0, padx=10, pady=10)

            testnum = testnumber.get()

            conn.commit()
            conn.close()

            root.mainloop()
        else:
            messagebox.showerror("Alert!!!", "Wrong Password")
    else:
        messagebox.showerror("Alert!!!", "Wrong Details....Try Again")


def register():
    reg = Tk()
    reg.title('Registration')

    connect = sqlite3.connect('imagedb.db')
    a = connect.cursor()

    def insert():
        if password01.get() == retype.get():
            # a.execute("""
            # CREATE TABLE registration('name', 'email', ':contact')""")
            a.execute("INSERT INTO registration VALUES(:name, :email, :contact, :location, :uname, :password)",
                      {
                          'name': name.get(),
                          'email': email.get(),
                          ':contact': contact.get(),
                          'location': location.get(),
                          'uname': username.get(),
                          'password': password01.get(),
                      })
            # messagebox.askquestion("Alert!!!", "Are You Sure With The Details?")
            name.delete(0, END)
            email.delete(0, END)
            contact.delete(0, END)
            location.delete(0, END)
            username.delete(0, END)
            password01.delete(0, END)
            retype.delete(0, END)
            reg.destroy()
        else:
            messagebox.showerror("Alert!!!", "The Retyped Password does not match")
            password01.delete(0, END)
            retype.delete(0, END)

    label01 = Label(reg, root='REGISTER', font="Verdana 11 bold")
    label11 = Label(reg, text='Name: ')
    label21 = Label(reg, text='Email Address: ')
    label31 = Label(reg, text='Contact: ')
    label41 = Label(reg, text='Location')
    label51 = Label(reg, text='Username: ')
    label61 = Label(reg, text='Password: ')
    label71 = Label(reg, text='Retype Password: ')

    button01 = Button(reg, text='DONE', font="bold", command=insert)

    name = Entry(reg)
    email = Entry(reg)
    contact = Entry(reg)
    location = Entry(reg)
    username = Entry(reg)
    password01 = Entry(reg)
    retype = Entry(reg)

    label01.grid(row=0, column=0, columnspan=3)
    label11.grid(row=1, column=0, padx=10, pady=10)
    label21.grid(row=3, column=0, padx=10, pady=10)
    label31.grid(row=5, column=0, padx=10, pady=10)
    label41.grid(row=7, column=0, padx=10, pady=10)
    label51.grid(row=9, column=0, padx=10, pady=10)
    label61.grid(row=11, column=0, padx=10, pady=10)
    label71.grid(row=13, column=0, padx=10, pady=10)

    button01.grid(row=15, column=0, columnspan=3)

    name.grid(row=2, column=0, padx=10, pady=10)
    email.grid(row=4, column=0, padx=10, pady=10)
    contact.grid(row=6, column=0, padx=10, pady=10)
    location.grid(row=8, column=0, padx=10, pady=10)
    username.grid(row=10, column=0, padx=10, pady=10)
    password01.grid(row=12, column=0, padx=10, pady=10)
    retype.grid(row=14, column=0, padx=10, pady=10)

    connect.commit()
    connect.close()

    reg.mainloop()


firstlabel = Label(rot, text='WELCOME TO CRYPTO', font="Verdana 11  bold")
secondlabel = Label(rot, text='LOGIN')
thirdlabel = Label(rot, text='Enter Username: ')
fourthlabel = Label(rot, text='Enter Password: ')
fifthlabel = Label(rot, text='Dont Have An Account?')

firstbutton = Button(rot, text='DONE', font="bold", command=crypto)
secondbutton = Button(rot, text='Click Here To Register', command=register)

uname = Entry(rot)
password = Entry(rot)

firstlabel.grid(row=0, column=0, columnspan=3)
secondlabel.grid(row=1, column=0, padx=10, pady=10)
thirdlabel.grid(row=2, column=0, padx=10, pady=10)
fourthlabel.grid(row=3, column=0, padx=10, pady=10)
fifthlabel.grid(row=5, column=0, padx=10, pady=10)

firstbutton.grid(row=4, column=0, padx=10, pady=10)
secondbutton.grid(row=6, column=0, padx=10, pady=10)

uname.grid(row=2, column=3, padx=10, pady=10)
password.grid(row=3, column=3, padx=10, pady=10)

connecting.commit()
connecting.close()

rot.mainloop()
