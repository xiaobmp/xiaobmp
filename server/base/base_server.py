import tornado.web


class BaseHandler(tornado.web.RequestHandler):

    def data_received(self, chunk):
        pass
