
def check_temporary_password(user):

    """Returns False if temporary password is the same as the actual password,
    redirecting to account/password """

    return not user.check_password(user.temporary_password)
