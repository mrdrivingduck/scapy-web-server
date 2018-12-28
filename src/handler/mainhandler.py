import tornado.web

class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.write("GET - testing pages")

    def post(self):
        self.write("POST - testing pages")