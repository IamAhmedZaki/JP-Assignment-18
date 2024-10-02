from flask import Flask,request,make_response
import pymysql
import db
from blueprints.all_bps import auth_bp
from blueprints.all_bps import notes_bp


app = Flask(__name__)
app.register_blueprint(auth_bp, url_prefix='/api')
app.register_blueprint(notes_bp, url_prefix='/api')
#app.register_blueprint(category_bp, url_prefix='/api')
    
  



# print(myapp.url_map)
# for rule in myapp.url_map.iter_rules():
#     print(rule)


if __name__ == "__main__":
   app.run(
    debug=True,
    port=5000
)