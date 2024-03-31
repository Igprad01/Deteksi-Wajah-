import cv2 

ref = cv2.CascadeClassifier('ref.xml')
cam = cv2.VideoCapture(0)


def settingCamera(kamera):
    bnw = cv2.cvtColor(kamera, cv2.COLOR_BGR2GRAY)
    wajah = ref.detectMultiScale(bnw, 1.3,5)   
    return wajah


def box(kamera):
    for x,y,w,h in settingCamera(kamera):
        cv2.rectangle(kamera ,(x,y),(x+w,y+h),(255,255,0),2)
        

            
def main():
    while True:
        _, kamera = cam.read()
        box(kamera)
        cv2.imshow("box camera", kamera)
        
        key = cv2.waitKey(1) & 0xFF
        if key == 27 :
            break
        
        
        cam.release()
        cv2.destroyAllWindows()
        

result = main()