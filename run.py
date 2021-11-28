from app import app,db
import logging
from logging.handlers import RotatingFileHandler


if __name__ == '__main__':
    handler = RotatingFileHandler('./logs/info.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    db.create_all()
    app.run(host=app.config["startup_conf"]["host"],port=app.config["startup_conf"]["port"],debug=app.config["startup_conf"]["debug"],use_reloader=app.config["startup_conf"]["use_reloader"],threaded=True)
