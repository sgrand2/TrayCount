import cv2
gray = cv2.imread("pp148.jpg",0)

## set threshold
tup, specimen = cv2.threshold(gray, 100, 255,cv2.THRESH_BINARY_INV|cv2.THRESH_OTSU)

## output batch view post threshold
cv2.imwrite("blah.png",specimen)

## getcontours
tot_spec = cv2.findContours(specimen, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[-2]


## filter area
s1= 15 
s2 = 20

ftot_spec = []

## Count by Area
for counts in tot_spec:
    if s1<cv2.contourArea(counts) <s2:
        ftot_spec.append(counts)

print("Alive number: {}".format(len(ftot_spec)))
print("Potential Size: {}".format(len(tot_spec)))

