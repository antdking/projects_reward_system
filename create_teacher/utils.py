from django.contrib.auth.models import User


def create_teacher_object(first_name, last_name, admin=False):
    """
    function for creating a teacher object, that will be returned
    input:
      first_name: The first name of the teacher
      last_name: The last name of the teacher
    output:
      user: A user object containing:
        username: of the teacher
        first_name: of the teacher
        last_name: of the teacher
        password: defaults to "goodluck"
    """
    # the username is made up of the first letter of the first name
    # and the last name
    username = "".join([first_name[0], last_name])
    x_username = username  # temporary hold for username
    break_point = False  # break point variable for the while loop
    number = 1  # number to concatonate onto the username

    # while loop to make sure all usernames are unique
    while not break_point:
        # query the database to see if the username exists
        try:
            u = User.objects.get(username__exact=x_username)
        except User.DoesNotExist:
            username = x_username
            break_point = True
        else:
            x_username = "".join([username, str(number)])
    password = "goodluck"

    # now we must create the user object, and add on the information we need
    user = User.objects.create_user(username, password=password)
    user.first_name = first_name
    user.last_name = last_name
    if admin:
        user.is_staff = True
    # finally we save the user object to the database
    return user
