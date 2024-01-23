from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja_model import Ninja

DATABASE = "dojos_and_ninjas_schema"


class Dojo:
    def __init__ (self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []


    @classmethod
    def get_dojos(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(DATABASE).query_db(query)

        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos
    
    @classmethod
    def save(cls, form_data):
        query = """
            INSERT INTO dojos (name) 
            VALUES (%(dojo_name)s);
    """
        return connectToMySQL (DATABASE).query_db(query, form_data)

    # @classmethod
    # def dojos_ninjas(cls, data):
    #     query = "SELECT * FROM ninjas JOIN dojos ON dojos.id = ninjas.dojo_id WHERE dojo_id = %(id)s;"
    #     result = connectToMySQL('dojos_and_ninjas_schema').query_db(query)

    #     dojo = cls(result[0])
    #     for row in result:
    #         ninja_data = {
    #             "id" : row ["ninja.id"], 
    #             "first_name" : row ["first_name"],
    #             "last_name" : row ["last_name"],
    #             "age" : row ["age"],
    #             "created_at" : row ["ninjas.created_at"],
    #             "updated_at" : row ["ninjas.updated_at"],
    #             "dojo_id" : row ["ninjas.dojo_id"]
    #         }

    #         dojo.ninjas.append(Ninja(ninja_data))
    #     return dojo

    # We need to import the burger class from our models
    @classmethod
    def dojo_ninjas( cls , data ):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db( query , data )

        # this is for if you were to see bool is not subscriptable
        if not results:
            return []

        # results will be a list of topping objects with the burger attached to each row. 
        dojo = cls( results[0] )
        for row in results:
            # Now we parse the burger data to make instances of burgers and add them into our list.
            ninja_data = {
                "id" : row ["ninjas.id"], 
                "first_name" : row ["first_name"],
                "last_name" : row ["last_name"],
                "age" : row ["age"],
                "created_at" : row ["ninjas.created_at"],
                "updated_at" : row ["ninjas.updated_at"],
                "dojo_id" : row ["dojo_id"]
            }
            dojo.ninjas.append( Ninja( ninja_data ) )
        return dojo

