
""" This is QR code Generator made by the help of python
        

    library used:qrcode

    """
import qrcode  #library for qr code
a = input("Enter the file name with png: ") #enter the file name with an extension of png
b = input("Enter the url: ") #enter the url
features = qrcode.QRCode(version=1 , box_size=40 , border = 2) #qr code design
features.add_data(b) #adding datas of url to qr code
features.make(fit=True)  
generate_image = features.make_image(fill_color="black" , black_colour="white")  #to generate image with different colors
generate_image.save(a)  #saving the qr as png format
