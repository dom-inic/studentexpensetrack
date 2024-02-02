from . base import *

# settings for postgresql. enable this to postgres instead of sqlite on production
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASS'],
        'HOST': os.environ['DB_HOST'],
        'PORT': os.environ['DB_PORT'],
        
    }
}

AWS_ACCESS_KEY_ID=os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY=os.environ['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME=os.environ['AWS_STORAGE_BUCKET_NAME']
AWS_QUERYSTRING_AUTH = False

# s3 storages
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None

# enable this is using aws storage
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_HEADERS = {  
    # see http://developer.yahoo.com/performance/rules.html#expires
    'Expires': 'Sun, 27 Feb 2099 20:00:00 GMT',
    'Cache-Control': 'max-age=94608000',
}