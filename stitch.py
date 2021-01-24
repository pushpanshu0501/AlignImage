from panorama import Panaroma
import imutils
import cv2

print("Enter the number of images you want to concantenate:")
no_of_images = int(input())
print("Enter the image name in order of left to right in way of concantenation:")
filename = []

for i in range(no_of_images):
    print("Enter the %d image:" %(i+1))
    filename.append(input())

images = []


for i in range(no_of_images):
    images.append(cv2.imread(filename[i]))

for i in range(no_of_images):
    images[i] = imutils.resize(images[i], width=400)
for i in range(no_of_images):
    images[i] = imutils.resize(images[i], height=400)


panaroma = Panaroma()
if no_of_images==2:
    (result, matched_points) = panaroma.image_stitch([images[0], images[1]], match_status=True)
else:
    (result, matched_points) = panaroma.image_stitch([images[no_of_images-2], images[no_of_images-1]], match_status=True)
    for i in range(no_of_images - 2):
        (result, matched_points) = panaroma.image_stitch([images[no_of_images-i-3],result], match_status=True)


#cv2.imshow("Keypoint Matches", matched_points)
cv2.imshow("StitchedImmage", result)
cv2.imwrite("Result.jpg",result)


cv2.waitKey(0)
cv2.destroyAllWindows()
