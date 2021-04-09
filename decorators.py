def user_id_validator(source_function):
    """Function which can be used as a decorator to validate the user id"""

    def function_wrapper(*args, **kwargs):
        exe_res = source_function(*args, **kwargs)

        return exe_res

    return function_wrapper


@user_id_validator
def sample_function(arg1, arg2):
    """Basic doc string format of reStructuredText

    :param int arg1:
    :param str arg2:
    :return int: Addition of two number
    """
    pass

