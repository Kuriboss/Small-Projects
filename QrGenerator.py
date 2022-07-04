import qrcode,qrtools,pyqrcode

choice=int(input('Which QRcode do you want to generate? Enter 1 for websiteQR or 2 for imageQR: '))
if(choice==1):
# This code will generate a .png file with the QR Code of the website entered
    site = input("Enter web address for QR code generation: ")
    imname = input("Enter name for QR code image: ")
    image = qrcode.make(site)
    image.save(f'{site}.png', 'png')
elif(choice==2):
    textz = input("Enter text to be put in QR code image: ")
    imname = input("Enter name for QR code image: ")
    qr = qrcode.QRCode()
    qr.add_data(textz)
    qr.make()
    img = qr.make_image()
    img.save(f'{imname}.png', 'png')
    



qr=qrtools.QR()
qr.decode(imname)
print(qr.data)
