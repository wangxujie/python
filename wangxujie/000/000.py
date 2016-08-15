from PIL import Image,ImageFont,ImageDraw

#img = Image.open('test.jpg')
#font = ImageFont.truetype('msyh.ttf',60)
#d = ImageDraw.Draw(img)
#d.text((100,0),'100',font=font,fill=(255,0,0,255))
#img.save('target.jpg')


def generateImg(num = 1):
	img  = Image.open('test.jpg')
	w,h = img.size
	print w, h
	font = ImageFont.truetype('msyh.ttf',40)
	d = ImageDraw.Draw(img)
	d.text((w - 50,10),str(num),font=font,fill='red')
	img.save('test2.jpg')
	
if __name__== '__main__':
	generateImg(65)