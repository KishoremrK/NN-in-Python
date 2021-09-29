#For Circle
for i in range(0,401 ):
    
    canvas = np.zeros((16, 16, 3), dtype="uint8")
    white = (255, 255, 255)

    radius = np.random.randint(2, high=6)

    pt = np.random.randint(2, high=14, size=(2,))

    cv2.circle(canvas, tuple(pt), radius, white, -1)

    cv2.imshow("Canvas", canvas)
  
    cv2.waitKey(0)

#for Square
for i in range(0,400 ):
    
    canvas = np.zeros((16, 16, 3), dtype="uint8")
    white = (255,255,255)

    

    pt = np.random.randint(10, high=14, size=(2,))

    cv2.rectangle(canvas,(10,10),(5,5), white, -1)

    cv2.imshow("Canvas", canvas)

   
    
    cv2.waitKey(0)