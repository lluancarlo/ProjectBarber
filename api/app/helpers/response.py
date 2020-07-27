from flask import jsonify

def response_wrapper(success, status,  message=None, data=None):
    return jsonify(
        success=success,
        status=status,
        message=message,
        data=data
    )


def response_wrapper_success(data, message=None):
    """Função para mensagens de 200 ou success.
    """
    return response_wrapper(True, 200, message, data)


def response_wrapper_error(code, message, data):
    return response_wrapper(False, code, message, data)