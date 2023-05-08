from flask import request

class Validate:

    def validarCampo(self, tipo, nom_campo, valor, obligatorio = False):

       mensaje = "OK"
       error = 200

       if (valor is "" or valor is None) and obligatorio:
        mensaje = f"El campo {nom_campo} es obligatorio"
        error = 400
       else:
         if type(valor) != tipo:
            mensaje = f"El campo {nom_campo} debe ser {tipo}"
            error = 400

       return {"status": error, "mensaje": mensaje, "data": {}}
    
    def validarMultiplesCampos(self, campos):
       for c in campos:
           resp = self.validarCampo(c['tipo'], c['nom_campo'], c['valor'], c['obligatorio'])

           return resp
   
    def validarCampoExiste(self, key):

       if key in request.json:
          return request.json[key]
       else:
          return ""


            
        

            