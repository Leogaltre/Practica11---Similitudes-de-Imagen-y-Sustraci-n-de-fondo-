import cv2

# Con BackgroundSubtractorMOG
# Algoritmo de segmentacion de fondo primer plano basado en una mezcla gaussiana
cap = cv2.VideoCapture('vtest.avi')

fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()

while True:
    ret, frame = cap.read()
    if ret == False: break

    # Obtencion de la mascará de primer plano
    # Obtenemos una imagen binaria en donde la seccion en blanco representaré el
    # primer plano u objetos en movimiento y en negro el fondo de la imagen que
    # es estatico
    fgmask = fgbg.apply(frame)

    cv2.imshow('fgmask', fgmask)
    cv2.imshow('frame', frame)

    if cv2.waitKey(30) & 0xFF == ord('n'):
        break
cap.release()
cv2.destroyAllWindows()

# Si se ubiera usado BackgroundSubtractorMOG2
# Ademas de detectar movimiento también detecta las sombras
# que los objetos en movimiento dejan
############################################

''' 
# Visualización del Video 
cap = cv2.VideoCapture('vtest.avi')

while True:
    ret, frame = cap.read()
    if ret == False: break
    cv2.imshow('frame', frame)
    k = cv2.waitKey(30) & 0xFF
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
'''