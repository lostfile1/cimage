
import base64

filename = raw_input('Enter a filename: ')




with open(filename, "rb") as img_file:
    my_string = base64.b64encode(img_file.read())

print(my_string.decode('utf-8'))
print("encoding finished")

outtput = raw_input('output textfile name: ')
f= open(outtput,"w+")
f.write(my_string.decode('utf-8'))
f.close()

print("writing to file finished")
