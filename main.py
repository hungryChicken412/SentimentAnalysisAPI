# Misc
from flask import Flask
from flask_restful import Api, Resource
from flask import request


app = Flask(__name__)
api = Api(app)


class AppAPI(Resource):
    def __init__(self):
        pass

    def get(self):
        returnMessage = """
            500-server-crashed-the-disk-seems-to-be-currupt-initiating-self-destruct-sequence
            """  # I'm bored, I'm going to delete this
        return returnMessage

    def post(self):
        data = request.json
        text = data['text']
        print(data)
        try:
            calculateSentiment(text)

            returnMessage = {
                "sentiment": sentiment
            }
            return returnMessage

        except Exception as e:
            print(e)
            returnMessage = {
                "sentiment": 'none'
            }

            return returnMessage


api.add_resource(AppAPI, "/")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
