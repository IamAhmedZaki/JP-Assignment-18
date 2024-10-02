import bcrypt


def check_missing_fields(fields,body):
    missed_fields=[]
    for field in fields:
        if field not in body:
            missed_fields.append(field)
        
    return missed_fields

def hash_password(password):
    salt=bcrypt.gensalt()
    byte=password.encode('utf-8')
    hash=bcrypt.hashpw(byte,salt)
    return hash
