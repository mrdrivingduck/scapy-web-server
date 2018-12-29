'''
    @author - mrdrivingduck
    @version - 2018.12.29
    @function - 
        Handler for root URL.
        Used only for testing.
'''

import tornado.web

class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.write("GET - testing pages")

    def post(self):
        self.write("POST - testing pages")