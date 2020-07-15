from app.helpers.json import sanetize


def response_wrapper(success, status, data, message=None):
    d = dict(
        success=success,
        message=message,
        status=status,
        data=sanetize(data)
    )
    return d


def response_wrapper_success(data, message=None):
    return response_wrapper(True, 200, data, message)


def response_wrapper_error(code, message, data=None):
    return response_wrapper(False, code, data, message)