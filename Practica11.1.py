import cv2

# Similitudes de una Imagen con otra
imagen1 = cv2.imread("Luis.png", cv2.IMREAD_GRAYSCALE) #COLOR_BGR2GRAY
img1 = cv2.resize(imagen1, (500, 778))
img2 = cv2.imread("Luis2.png", cv2.IMREAD_GRAYSCALE)

n= int(input("Cuantas coincidencias te gustaría ver: "))

# Detector ORB
orb = cv2.ORB_create()
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

# Coincidencia de fuerza bruta
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(des1, des2)
matches = sorted(matches, key=lambda x:x.distance)

# Coincidencias
matching_result = cv2.drawMatches(img1, kp1, img2, kp2, matches[:n], None)
# print(len(matches)) pueden ser solo cierta n cantidad matches[:20]

for m in matches:
    print(m.distance)

cv2.imshow('Libro de Luis', img1)
cv2.imshow('Libro de Luis cargado por Luis', img2)
cv2.imshow('Resultado Coincidente', matching_result)
cv2.waitKey(0)
cv2.destroyAllWindows()