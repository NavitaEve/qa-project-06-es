import sender_stand_request
import data

# Función para cambiar el valor del parametro name en el cuerpo de la solicitud
def get_kit_body(name):
    # Copia el diccionario con el cuerpo de la solicitud desde el archivo data
    current_kit_body = data.kit_body.copy()
    # Se cambia el valor del parámetro name
    current_kit_body["name"] = name
    # Se devuelve un nuevo diccionario con el valor name requerido
    return current_kit_body

# Función de prueba positiva
def positive_assert(name):
    # El cuerpo de la solicitud actualizada guarda en la variable kit_body
    kit_body = get_kit_body(name)
    # El resultado de la solicitud para crear un nuevo kit se guarda en la variable response
    kit_body_response = sender_stand_request.post_new_client_kit(kit_body)
    kit_body_response_data = kit_body_response.json()

    # Comprueba si el codigo de estado es 201
    assert kit_body_response.status_code == 201
    # Comprueba que el campo authToken este en la respuesta y contiene un valor
    assert kit_body_response.data["name"] == kit_body
# Función de prueba negativa para los casos en los que la solicitud devuelve un error relacionado con caracteres
def negative_assert_symbol(name):
    # El cuerpo de la solicitud actualizada se guarda en la variable kit_body
    kit_body = get_kit_body(name)

    # El resultado se guarda en la variable response
    response = sender_stand_request.post_new_client_kit(kit_body)

    # Comprueba si el codigo de estado es 400
    assert response.status_code == 400

    # Comprueba que los atributos code en el cuerpo de respuesta es 400
    assert response.json()["code"] == 400
    # Comprueba el atributo message en el cuerpo de respuesta
    assert response.json()["message"] == "El nombre que ingresaste es incorrecto. " \
                                         "Los nombres solo pueden contener caracteres latinos,  "\
                                         "los nombres deben tener al menos 2 caracteres y no más de 511 caracteres"

# Función de prueba negativa cuando el error es "No se enviaron todos los parametros requeridos

def negative_assert_no_name(kit_body):
    # El resultado se guarda en la variable response
    response = sender_stand_request.post_new_client_kit(kit_body)

    # Comprueba si el código de estado es 400
    assert response.status_code == 400

    # Comprreba que el atributo code en el cuerpo de respuesta es 400
    assert  response.json()["code"] == 400
    # Comprueba el atributo message en el cuerpo de respuesta
    assert response.json()["message"] == "No se enviaron todos los parámetros requeridos"

# Prueba 1. Kit creado con éxito. El parámetro name contiene 1 carácter
def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert_kit_body = { "name": "a"}

# Prueba 2. Kit creado con éxito. El parámetro name contiene 511 carácteres
def test_create_kit_511_letter_in_name_get_success_response():
    positive_assert_kit_body ={"AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"}

# Prueba 3. Error. El parámetro name contiene un string vacío
def test_create_kit_empty_name_get_error_response():
    kit_body = get_kit_body = { }
    negative_assert_no_name_kit_body = { "name": "" }

# Prueba 4. Error. El parámetro name contiene 512 carácteres
def test_create_kit_512_letter_in_name_get_error_response():
    kit_body = get_kit_body= {""}
    negative_assert_no_name_kit_body = {  "name":"AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"}

# Prueba 5. Kit creado con éxito. El parámetro name contiene carácteres especiales
def test_create_kit_has_special_symbol_in_name_get_success_response():
    positive_assert_kit_body = { "name": "\"№%@\"," }

# Prueba 6. Kit creado con éxito. El parámetro name contiene carácteres con espacios
def test_craete_kit_has_spaces_in_name_get_success_response():
    positive_assert_kit_body = { "name": " A Aaa " }

#Prueba 7. Kit creado con éxito. El parametro name contiene un string de numeros
def test_create_kit_has_number_in_name_get_success_response():
    positive_assert_kit_body = { "name": "123" }

# Prueba 8. Error. El parámetro name no se pasa a la solicitud
def test_create_kit_no_name_get_error_response():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    negative_assert_no_name_kit_body = { }

# Prueba 9. Error. El parámetro name contiene números
def test_create_kit_has_number_type_in_name_get_error_response():
    kit_body = get_kit_body(123)
    negative_assert_no_name_kit_body =  { "name": 123 }
    response = sender_stand_request.post_new_client_kit(kit_body)

    # Comprueba el código de estado de l respuesta
    assert response.status_code == 400















