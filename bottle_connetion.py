import bottle
import pymongo


@bottle.route('/')
def index():

    connection = pymongo.MongoClient('localhost', 27017)
    db = connection.students
    name = db.grades
    item = name.find_one()

    return '<b>Hello {} !</b>'.format(item)


bottle.run(host='localhost', port=8082)
