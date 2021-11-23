from app import app,db
import logging
from logging.handlers import RotatingFileHandler


if __name__ == '__main__':
    handler = RotatingFileHandler('INFO4.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    db.create_all()
    app.run(debug=True,use_reloader=True,threaded=True)
