from blog.DB.model import User, db
import re


def insert(**kwargs):
    out_invalid_field = {}
    out_improper_field = {}
    for key in kwargs.keys():
        if key in ["name", "age", "email"]:
            pass
        else:
            out_invalid_field[key] = "Not a valid field"
    if len(out_invalid_field) > 0:
        out_invalid_field['mandatory'] = "only name age and email are valid and mandatory field"
        return out_invalid_field
    if isinstance(kwargs.get('name'), str) and isinstance(kwargs.get('age'), int) and isinstance(kwargs.get('email'),
                                                                                                 str):
        field_error = {}
        email_regex = r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        name_regex = r'^[a-z\sA-Z]{2,20}$'
        age_regex = r'^[0-9]{3}$'
        email = kwargs.get('email')
        name = kwargs.get('name')
        age = str(kwargs.get('age'))
        field_error = {**check_valid(email_regex, email, "email"), **check_valid(age_regex, age, "age"),
                       **check_valid(name_regex, name, "name")}
        if len(field_error) > 0:
            return field_error
        u1 = User(**kwargs)
        db.session.add(u1)
        db.session.commit()
        return u1
    else:
        if not isinstance(kwargs.get('name'), str):
            out_improper_field['name'] = "should be string"
        if not isinstance(kwargs.get('age'), int):
            out_improper_field['age'] = "should be in integer"
        if not isinstance(kwargs.get('email'), str):
            out_improper_field['email'] = "should be in string"
    if len(out_improper_field) > 0:
        return out_improper_field


def get(user_id):
    u1 = User.query.filter_by(id=user_id).first()
    if not u1:
        u1 = "No user Exist with passed user id"
    else:
        db.session.add(u1)
    return u1


def update(user_id, **kwargs):
    out_invalid_field = {}
    out_improper_field = {}
    for key in kwargs.keys():
        if key in ["name", "age", "email"]:
            pass
        else:
            out_invalid_field[key] = "Not a valid field"
    if len(out_invalid_field) > 0:
        return out_invalid_field

    u1 = User.query.filter_by(id=user_id).first()
    if not u1:
        return "User with id does not exist"

    if isinstance(kwargs.get('name', u1.name), str) and isinstance(kwargs.get('age', u1.age), int) and isinstance(
            kwargs.get('email', u1.email), str):

        email_regex = r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        name_regex = r'^[a-z\sA-Z]{2,20}$'
        age_regex = r'^[0-9]{3}$'
        email = kwargs.get('email', u1.email)
        name = kwargs.get('name', u1.name)
        age = str(kwargs.get('age', u1.age))

        out_improper_field = {**check_valid(email_regex, email, "email"), **check_valid(age_regex, age, "age"),
                              **check_valid(name_regex, name, "name")}
        if len(out_improper_field) > 0:
            return out_improper_field
        u1.name = kwargs.get('name', u1.name)
        u1.age = kwargs.get('age', u1.age)
        u1.email = kwargs.get('email', u1.email)
        db.session.commit()
        return u1
    else:
        if not isinstance(kwargs.get('name', u1.name), str):
            out_improper_field['name'] = "should be string"
        if not isinstance(kwargs.get('age', u1.age), int):
            out_improper_field['age'] = "should be in integer"
        if not isinstance(kwargs.get('email', u1.email), str):
            out_improper_field['email'] = "should be in string"

    if len(out_improper_field) > 0:
        return out_improper_field


def delete(user_id):
    u1 = User.query.filter_by(id=user_id).first()
    if u1:
        db.session.delete(u1)
        db.session.commit()
        return True
    return False


def get_all():
    u1 = User.query.all()
    if u1:
        return u1
    return False


def check_valid(regex, field_value, field_type):
    error = {}
    if field_type == "email":
        if re.search(regex, field_value):
            pass
        else:
            error['email'] = "Enter Valid Email Address"

    if field_type == "name":
        if re.search(regex, field_value):
            pass
        else:
            error['name'] = "name should be in letter and max length is 20"

    if field_type == "age":
        if re.search(regex, field_value):
            x = re.search(regex, field_value)
            if int(x.group()) <= 150:
                pass
            else:
                error['age'] = "age should be in integer and less than 150 "
    return error
