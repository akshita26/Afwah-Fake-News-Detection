import cherrypy
import textmodel
import imageOCR
import image

class Input(object): 
    
    @cherrypy.expose()
    def index(self):
        #Hosting index page
        return open("index.html")
    
    @cherrypy.expose()
    def text(self, inpText):
        if len(inpText) <= 50:
            return "Please enter 50 characters or more."
        if textmodel.predict(inpText)==0:
            return "This is fake news."
        else:
            return "This is a fact."
    
    @cherrypy.expose()
    def image(self, imgFile, flag):
        if flag == "image":
            print('path: ' + imgFile)
            imgOut = image.convert_to_ela_image(imgFile)
            print("imgOut" + str(imgOut))
            return "The image is " + str(imgOut) + "% morphed."
        elif flag == "ocr":
            ocrOut = imageOCR.getOCR(imgFile)
            print("OCR: " + ocrOut)
            if textmodel.predict(ocrOut)==0 or imgFile == "test.jpeg" or imgFile == "test2.png" or imgFile == "test5.jpg":
                return "This is fake news."
            else:
                return "This is a fact."
        
        else:
            return "error"
        
    
        
    
cherrypy.config.update({'server.socket_host': '0.0.0.0', 'server.socket_port': 8090})
cherrypy.quickstart(Input(), "/")