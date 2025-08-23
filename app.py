# Recordá que debes correr la aplicación en la terminal con el siguiente comando:
# flask --app app run

from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)

DATA_FILE = "vuelos.json"

# Crea una función cargar_datos() que:
def cargar_datos():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

# Función auxiliar: guardar datos  
def guardar_datos(datos):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)

    
# Consigna 1:
# Crea un endpoint de inicio GET / que retorne:
# {"mensaje": "API de Vuelos"} en formato JSON
@app.route("/", methods=["GET"])
def inicio():
    pass

# Consigna 2:
# Crea un endpoint GET /api/vuelos que:
# 1. Cargue todos los datos usando cargar_datos()
# 2. Retorne los datos en formato JSON usando jsonify()
# 3. Aplique el método str.title() al campo "destino" de cada vuelo, de modo que se devuelva con la primera letra en mayúscula.
@app.route("/api/vuelos", methods=["GET"])
def listar_vuelos():
    pass

# Consigna 3:
# Crea un endpoint GET /api/vuelos/<int:vuelo_id> que:
# 1. Cargue todos los datos
# 2. Busque el vuelo con el ID especificado
# 3. Si lo encuentra, retorne el vuelo en JSON
# 4. Si no lo encuentra, retorne {"error": "Vuelo no encontrado"} con código 404
# 5. Aplique el método str.title() al campo "destino" del vuelo, de modo que se devuelva con la primera letra en mayúscula.
@app.route("/api/vuelos/<int:vuelo_id>", methods=["GET"])
def obtener_vuelo(vuelo_id):
    pass

# Consigna 4:
# Crea un endpoint POST /api/vuelos que:
# 1. Obtenga los datos JSON de la petición con request.get_json()
# 2. Valide que el campo "destino" esté presente y no esté vacío
# 3. Si no está, retorne {"error": "El campo 'destino' es obligatorio"} con código 400
# 4. Cargue los datos existentes
# 5. Asigne un ID automático: último ID + 1, o 1 si no hay datos
# 6.  Asigne valores por defecto: capacidad=100, vendidos=0 si no se especifican.
#     Convierta siempre el campo "destino" a minúsculas antes de guardar usando el método str.lower().
# 7. Agregue el nuevo vuelo a la lista
# 8. Guarde los datos actualizados
# 9. Retorne el nuevo vuelo con código 201
# 10. Minuscula
@app.route("/api/vuelos", methods=["POST"])
def agregar_vuelo():
    pass

# Consigna 5:
# Crea un endpoint PUT /api/vuelos/<int:vuelo_id> que:
# 1. Obtenga los datos JSON de la petición
# 2. Cargue todos los datos existentes
# 3. Busque el vuelo por ID
# 4. Si lo encuentra, actualice sus campos con vuelo.update().
#    Convierta siempre el campo "destino" a minúsculas antes de actualizar usando el método str.lower()
# 5. Guarde los datos actualizados y retorne el vuelo actualizado
# 6. Si no lo encuentra, retorne {"error": "Vuelo no encontrado"} con código 404
# 7. Minuscula
@app.route("/api/vuelos/<int:vuelo_id>", methods=["PUT"])
def actualizar_vuelo(vuelo_id):
    pass

# Consigna 6:
# Crea un endpoint DELETE /api/vuelos/<int:vuelo_id> que:
# 1. Cargue todos los datos
# 2. Filtre los datos excluyendo el vuelo con el ID especificado (opcionalmente podés usar listas por comprensión).
# 3. Compare si las listas tienen el mismo tamaño (no se eliminó nada)
# 4. Si son iguales, retorne {"error": "Vuelo no encontrado"} con código 404
# 5. Si son diferentes, guarde los datos filtrados
# 6. Retorne {"mensaje": f"Vuelo {vuelo_id} eliminado correctamente"}
@app.route("/api/vuelos/<int:vuelo_id>", methods=["DELETE"])
def eliminar_vuelo(vuelo_id):
    pass

# Consigna 7:
# Crear un endpoint POST /vender que:
# 1. Obtenga los datos JSON de la petición.
# El campo id del vuelo se envía en el body del request, por ejemplo:
# {
#   "id": 1
# }
# Tips: en Flask se obtiene así:
# datos = request.get_json()
# vuelo_id = datos.get("id")
# 2. Cargue todos los vuelos existentes.
# 3. Busque el vuelo por su id.
# 4. Si no lo encuentra, devuelva {"error": "Vuelo no encontrado"} con código 404.
# 5. Verifique que vendidos < capacidad:
#   - Si hay lugar disponible, incremente "vendidos" en 1.
#   - Si el vuelo está completo (vendidos >= capacidad), devuelva {"error": "Vuelo completo"} con código 400.
# 6. Guarde los datos actualizados.
# 7. Devuelva el vuelo actualizado en formato JSON.
@app.route("/api/vender", methods=["POST"])
def vender_vuelo():
    pass

if __name__ == "__main__":
    if not os.path.exists(DATA_FILE):
        guardar_datos([])
    app.run(debug=True)


# EJEMPLOS DE CÓMO PROBAR LA API:

# Crear vuelo:
# curl -X POST http://localhost:5000/api/vuelos \
#   -H "Content-Type: application/json" \
#   -d '{"destino": "Buenos Aires", "capacidad": 150}'

# Listar vuelos:
# curl http://localhost:5000/api/vuelos

# Ver vuelo específico:
# curl http://localhost:5000/api/vuelos/1

# Actualizar vuelo:
# curl -X PUT http://localhost:5000/api/vuelos/1 \
#   -H "Content-Type: application/json" \
#   -d '{"destino": "Córdoba", "vendidos": 25}'

# Eliminar vuelo:
# curl -X DELETE http://localhost:5000/api/vuelos/1

#Vender vuelo:
#curl -X POST http://localhost:5000/vender \
#  -H "Content-Type: application/json" \
#  -d '{"id": 1}'