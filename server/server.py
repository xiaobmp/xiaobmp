import tornado.ioloop
import tornado.web

from handler import hello_world


application = tornado.web.Application(
    [
        (r"/blog/", hello_world.MainHandler)
    ]
)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
