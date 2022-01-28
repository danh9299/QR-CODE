#We need to import the qrcode in order to use all the pre-set features
import qrcode

#set myURL as the link, to which our QR code will navigate
myURL ="https://www.facebook.com/nguyen.duyanh.12345/"

#Edit our QR CODE
qr = qrcode.QRCode(
    #Size of our QR
    version = 1,
    #Number of pixels in a square
    box_size=10,
    #Set the weight of our border
    border=5)
#embed the link into the QR
qr.add_data(myURL)

#You will need the fit = True to allow the QR code to spread
qr.make(fit=True)

#Edit the appearance of the QR code
img = qr.make_image(fill='black', back_color='white')

#The QR code will be save into an image after we run this program
img.save('QR_MyProfile.png')
