import DeepLab
import Model
import cv2
import FirebaseScript


FirebaseScript.initialize()

content_layer_ids = [4]
style_layer_ids = list(range(13))
#int_style = 1 ,2 ,3,
#url_content=
style_image = cv2.imread('style2.jpeg')
content_image=cv2.imread('Content1.jpeg')  


content_image = cv2.resize(content_image,(300,300))
content_image = cv2.cvtColor(content_image,cv2.COLOR_BGR2RGB)



style_image = cv2.cvtColor(style_image,cv2.COLOR_BGR2RGB)
style_image = cv2.resize(style_image,(300,300))

DeepLab.run_visualization("Content1")

image1 = cv2.imread('img.jpg')


gray = cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)


mask2_inv = cv2.bitwise_not(mask)

mask = cv2.cvtColor(mask,cv2.COLOR_GRAY2BGR)
mask = cv2.resize(mask,(300,300))
mask_inv = cv2.bitwise_not(mask)
input_image_content = cv2.bitwise_or(mask,content_image)
input_image_content_background = cv2.bitwise_or(mask_inv,content_image)


mixed_image = Model.style_transfer(content_image=input_image_content,
                     style_image=style_image,
                     content_layer_ids=content_layer_ids,
                     style_layer_ids=style_layer_ids,
                     weight_content=8.0,
                     weight_style=10.0,
                     weight_denoise=0.5,
                     num_iterations=30,
                     step_size=3.0)


mixed_image_background = Model.style_transfer(content_image=input_image_content_background,
                     style_image=style_image,
                     content_layer_ids=content_layer_ids,
                     style_layer_ids=style_layer_ids,
                     weight_content=1.5,
                     weight_style=10.0,
                     weight_denoise=0.5,
                     num_iterations=30,
                     step_size=3.0)



cv2.imwrite('saved.jpg',mixed_image)
imgs = cv2.imread('saved.jpg')

cv2.imwrite('saved2.jpg',mixed_image_background)
imgs_background = cv2.imread('saved2.jpg')

imgk = cv2.cvtColor(imgs,cv2.COLOR_RGB2BGR)
imgk_background = cv2.cvtColor(imgs_background,cv2.COLOR_RGB2BGR)

fore_ground = cv2.bitwise_or(mask,imgk)
back_ground = cv2.bitwise_or(content_image,mask_inv)

fore_ground_back = cv2.bitwise_or(mask_inv,imgk_background)
content_image = cv2.cvtColor(content_image,cv2.COLOR_RGB2BGR)
back_ground_back = cv2.bitwise_and(content_image,fore_ground_back)

final_image = cv2.bitwise_and(fore_ground,back_ground)
final_image_background = cv2.bitwise_and(fore_ground_back,back_ground_back)

#final_image = cv2.cvtColor(final_image,cv2.COLOR_BGR2RGB)
cv2.imwrite('FinalImage.jpg',final_image)
cv2.imwrite('FinalImage2.jpg',final_image_background)
content_image = cv2.cvtColor(content_image,cv2.COLOR_RGB2BGR)
cv2.imshow('Mixed Image',final_image)
cv2.imshow('Content Image',content_image)
cv2.imshow('Style Image',style_image)

content_image = cv2.cvtColor(content_image,cv2.COLOR_RGB2BGR)
cv2.imshow('Mixed Image',final_image_background)
cv2.imshow('Content Image',content_image	)
cv2.imshow('Style Image',style_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
