# -*- coding: utf-8 -*-
CELERY_RESULT_BACKEND = os.environ.get(
    'CELERY_RESULT_BACKEND', 'redis://localhost'
)
