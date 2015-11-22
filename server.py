import tornado.ioloop
import tornado.web
import tornado.httpserver
from tornado.options import define, options

class FingerPrintHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

    def post(self):
        res = self

        res.write('0')


if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", FingerPrintHandler, dict())
    ])
    server = tornado.httpserver.HTTPServer(app)
    server.listen(5000)
    tornado.ioloop.IOLoop.instance().start()
