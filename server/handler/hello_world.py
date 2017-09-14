from server.base.base_server import BaseHandler


class MainHandler(BaseHandler):
    def get(self):
        self.write("Hello, World")
