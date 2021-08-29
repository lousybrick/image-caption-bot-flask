from flask import Flask, render_template, redirect
from flask.globals import request
import caption_bot

#__name__ == __main__
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/', methods = ['POST'])
def caption_img_bot():
    if request.method == 'POST':
        f = request.files['userfile']
        path = "./static/{}".format(f.filename) #./statis/images.jpg
        f.save(path)
        caption = caption_bot.caption_this_image(path)
        #print(caption)

        result_dict = {
            'image' : path,
            'caption' : caption
        }
    
    return render_template("index.html", img_result = result_dict)

if __name__ == '__main__':
    #app.debug = True
    app.run(debug = True)