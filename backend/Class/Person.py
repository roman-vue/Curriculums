import config
import json

class Person:

    def createPerson(self, data):

        config.mongo.db.personData.insert_one(data)

        response = {'error': 200, 'mensaje': 'OK', 'data': '2'}
        return response
