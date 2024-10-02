from flask import Flask,request,make_response,Blueprint
import pymysql
import db
from blueprints.auth import signup
from blueprints.auth import login
from blueprints.auth import logout
from blueprints.notes import create_note
from blueprints.notes import update_notes
from blueprints.notes import delete_notes,get_all_notes

auth_bp=Blueprint('auth',__name__)

auth_bp.add_url_rule("/signup",view_func=signup,methods=['POST'])
auth_bp.add_url_rule("/login",view_func=login,methods=['POST'])
auth_bp.add_url_rule("/logout",view_func=logout,methods=['POST'])

notes_bp=Blueprint('notes',__name__)

notes_bp.add_url_rule("/notes/create",view_func=create_note,methods=['POST'])
notes_bp.add_url_rule("/notes/update/<id>",view_func=update_notes,methods=['PUT'])
notes_bp.add_url_rule("/notes/delete/<id>",view_func=delete_notes,methods=['DELETE'])
notes_bp.add_url_rule("/notes",view_func=get_all_notes,methods=['GET'])

