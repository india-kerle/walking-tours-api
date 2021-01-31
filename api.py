from flask import Flask, request
from flask_restful import Resource, Api
import scraper

app = Flask(__name__)
api = Api(app)

#class Home(Resource):
#    def get(self):
#        return make_response(render_template('index.html'))

class tours(Resource):
    def get(self):
    	start = request.args.get('start-date', type = str, default = None)
    	end = request.args.get('end-date', type = str, default = None)
    	tour = scraper.get_tours(start, end)

    	return tour


class guides(Resource):
    def get(self):
    	guide = scraper.get_guide_info()

    	return guide

#app.add_resource(home, '/')
api.add_resource(tours, '/tours')
api.add_resource(guides, '/guides')

if __name__ == '__main__':
    app.run()