from flask import Blueprint

mod=Blueprint('api',__name__)
@mod.route('/getstuff')
def get_stuff():
    return '{"result":"hello"}'