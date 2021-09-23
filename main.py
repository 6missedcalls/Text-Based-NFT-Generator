from PIL import Image, ImageDraw, ImageFont
import random
import os

i = 0
genNum = input("Enter the number of NFT's you'd like to generate: ")

path = './output'
if not os.path.exists(path):
    os.makedirs(path)
while (i < int(genNum)):
    weightedList = ['1 weight'] * 1 + ['25 weight'] * 25 + ['50 weight'] * 50 + ['24 weight'] * 24 
    r = random.choice(weightedList)
    img = Image.new('RGB', (250, 250), color = (235, 64, 52)) # rgb, size, color
    fnt = ImageFont.truetype('C:\Windows\Fonts\\Arial.ttf', 16)
    d = ImageDraw.Draw(img)
    # draw variables
    d.text((10,10), str(r), font=fnt, fill=(69, 69, 69))
    d.text((10,30), 'Made with <3', font=fnt, fill=(69, 69, 69))
    d.text((10,50), '0x0', font=fnt, fill=(69, 69, 69))

    i = i+1
    img.save('output\\'+str(i)+'.png')
    
else:
  print("NFT's Finished Randomly Generating!")