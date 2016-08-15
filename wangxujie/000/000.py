from PIL import Image,ImageFont,ImageDraw

img = Image.open('test.jpg')
font = ImageFont.truetype('msyh.ttf',60)
d = ImageDraw.Draw(img)
d.text((100,0),'100',font=font,fill=(255,0,0,255))
img.save('target.jpg')