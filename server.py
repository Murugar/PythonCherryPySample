import cherrypy

class Root:
    @cherrypy.expose
    def index(self):
        return "Hello World From CherryPy!"

if __name__ == '__main__':
    cherrypy.config.update({'server.socket_host': '0.0.0.0'})
    cherrypy.quickstart(Root())
