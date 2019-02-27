from PIL import Image,ImageDraw,ImageSequence

source = 'test.gif'

def get_char(pix):
    char_list = 'slkjfeijskjafnvkajfe{}><():;|\/+-*'
    char_len = len(char_list)
    index = int(pix/255)*(char_len-1)
    return (char_list[index])

'''图片根据像素转化为字符'''
def img2char(img):
    img = img.convert('L')
    img = img.resize((int(img.height),int(img.width)),Image.NEAREST)
    txt = ''
    for h in range(img.height):
        for w in range(img.width):
            txt += get_char(img.getpixel((w,h)))
        txt += '\n'
    return txt

def txt2img(txtstring):
    img = Image.new('RGB',(1100,1900),(255,255,255))
    draw = ImageDraw.Draw(img)
    draw.text((0,0),txtstring,fill='black')
    return img


def img2gif(frames):
    frames[0].save('newresult.gif',save_all=True,append_images=frames[1:])

'''动态图转化为许多张静态图'''
def gif2char():
    new_frames = []
    with Image.open(source) as im:
        frames = [f.copy() for f in ImageSequence.Iterator(im)]
        for i,frame in enumerate(frames):
            # frame.save('%d.png'%i)
            res = img2char(frame)
            # with open('%d.txt'%i,'w') as f:
            #     f.write(res)
            # txt2img(res).save('%d.png'%i)
            new_frames.append(txt2img(res))
    img2gif(new_frames)

gif2char()