import cv2
import sys
import pytesseract
import numpy as np

 
if __name__ == '__main__':
  print(__name__)
  if len(sys.argv) < 2:
    print('Usage: python ocr_simple.py image.jpg')
    sys.exit(1)
   
  # Read image path from command line
  imPath = sys.argv[1]
     
  # Uncomment the line below to provide path to tesseract manually
  # pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'
 
  # Define config parameters.
  # '-l eng'  for using the English language
  # '--oem 1' for using LSTM OCR Engine
  config = ('-l pubg --oem 1 --psm 3')
 
  # Read image from disk
  img = cv2.imread(imPath, cv2.IMREAD_COLOR)
  img = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)

  # Convert to gray
  img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

  # Apply dilation and erosion to remove some noise
  # kernel = np.ones((1, 1), np.uint8)
  # img = cv2.dilate(img, kernel, iterations=1)
  # img = cv2.erode(img, kernel, iterations=1)

  # img = cv2.GaussianBlur(img, (5, 5), 0)

  # Apply threshold to get image with only b&w (binarization)
  # img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

  # Print image
  cv2.imshow('image',img)
  cv2.waitKey(0)

  # Run tesseract OCR on image
  text = pytesseract.image_to_string(img, config=config)
 
  # Print recognized text
  # print(text)







