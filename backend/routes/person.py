from flask import Blueprint, request
from Class.Person import Person
from Class.Validate import Validate


person = Blueprint('person', __name__)
PersonC = Person()
ValidateC = Validate()

@person.route("/createPerson", methods = ['POST'])
def createPerson():

    name = ValidateC.validarCampoExiste("name")
    lastname = ValidateC.validarCampoExiste("lastname")
    profession = ValidateC.validarCampoExiste("profession")
    phone = ValidateC.validarCampoExiste("phone")
    
    validarName = ValidateC.validarCampo(dict, 'name', name, True)
    if validarName['status'] != 200:
        return validarName
    else:
        data = {'name': name, 'lastname': lastname, 'profession': profession, 'phone': phone}
        resp = PersonC.createPerson(data)
        return resp  
 
