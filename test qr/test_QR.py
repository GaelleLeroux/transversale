import cv2
import numpy as np
import sys
import time

def qr(filename):

    #inputImage = cv2.imread(filename)
    inputImage = filename

    # Display barcode and QR code location
    def display(im, bbox):
        n = len(bbox)
        for j in range(n-1):
            cv2.line(im, tuple(bbox[j][0]), tuple(bbox[ (j+1) % n][0]), (255,0,0), 3)
    
        # Display results
        


    qrDecoder = cv2.QRCodeDetector()
    Decte = False
    
    # Detect and decode the qrcode
    data,bbox,rectifiedImage = qrDecoder.detectAndDecode(inputImage)
    if len(data)>0:
        print("Decoded Data : {}".format(data))
        display(inputImage, bbox)
        rectifiedImage = np.uint8(rectifiedImage)
        cv2.imshow("Rectified QRCode", rectifiedImage)
        Detect = True
    else:
        cv2.imshow("Results", inputImage)

    if Decte :
        nmb1 = ""
        nmb2 = ""
        a = True
        for i in range(len(data)):
            if data[i]!=" " and data[i]!="\n":
                if a:
                    nmb1 = nmb1 + str(data[i])
                else :
                    nmb2 = nmb2 + str(data[i])
            else :
                a = False

        nmb1 = int(nmb1)
        nmb2 = int(nmb2)
        print(nmb1)
        print(nmb2)



cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 25.0, (640,480))

while( cap.isOpened() ):
    ret, frame = cap.read()
    if ret == True:
        frame = cv2.flip(frame,1)
        qr(frame)
        cv2.imshow('frame' , frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()





