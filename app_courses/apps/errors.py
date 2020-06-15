### CLASSIC ERRORS START 204*-207* ###
class DosntFoundQueryset:
    ERROR = 10040
    DESCRIPTION = 'Dosnt found queryset'

class DosntValidId:
    ERROR = 10041
    DESCRIPTION = 'Dosnt valid id'

class DosntValidParameters:
    ERROR = 10042
    DESCRIPTION = 'Dosnt valid parameters'

### USER ERRORS START 204*-207* ###

class GoodResponseUser:
    ERROR = 2039
    DESCRIPTION = 'OK'

class UserNotValidSession:
    ERROR = 2040
    DESCRIPTION = 'Some problem with session or uuid'

class UserActivate:
    ERROR = 2041
    DESCRIPTION = 'User already activate. Please, login or registration on another email'

class UserNotActive:
    ERROR = 2042
    DESCRIPTION = 'User not activeted. Please, check your email.'

class UserNotValidPassOrEmail:
    ERROR = 2043
    DESCRIPTION = 'Not valid password or email'
