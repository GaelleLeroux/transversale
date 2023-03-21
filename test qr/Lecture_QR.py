# le code de base est trouvable à l'adresse https://github.com/akpythonyt/AKpythoncodes
import cv2

def fin(data):
    nmb1 = ""
    nmb2 = ""
    a = True
    for i in range(len(data)):
        if data[i]!=" " and data[i]!="\n":
            if a:
                nmb1 = nmb1 + str(data[i])
        else :
            a = False

    nmb1 = int(nmb1)
    print(nmb1)

# initalize the cam
cap = cv2.VideoCapture(0)
# initialize the cv2 QRCode detector
detector = cv2.QRCodeDetector()
while True:
    _, img = cap.read()
    # detect and decode
    data, bbox, _ = detector.detectAndDecode(img)
    # check if there is a QRCode in the image
    if data:
        a=data
        fin(data)
        data=None
        #Si on veut qu'il ne le lise qu'une fois et ferme la caméra on met le break
        #break 
    # display the result
    cv2.imshow("QRCODEscanner", img)    
    if cv2.waitKey(1) == ord("q"):
        break



cap.release()
cv2.destroyAllWindows()