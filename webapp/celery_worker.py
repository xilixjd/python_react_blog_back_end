# -*- coding: utf-8 -*-

from webapp import create_app
from webapp.extensions import celery

app = create_app('webapp.config.DevConfig')
app.app_context().push()
# app.run(host='0.0.0.0')
# app.run()
