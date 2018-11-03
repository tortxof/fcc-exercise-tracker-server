# fcc-exercise-tracker-server

## A REST API server for logging exercise sessions.

### Deploying to AWS Lambda using zappa

First, you need an S3 bucket to host the static files. Create an S3 bucket and
add this CORS configuration.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<CORSConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
<CORSRule>
    <AllowedOrigin>*</AllowedOrigin>
    <AllowedMethod>GET</AllowedMethod>
    <MaxAgeSeconds>3000</MaxAgeSeconds>
    <AllowedHeader>Authorization</AllowedHeader>
</CORSRule>
</CORSConfiguration>
```

Use Django's `collectstatic` command to process and upload the static files to
the S3 bucket.

```
AWS_STORAGE_BUCKET_NAME=bucket_name ./manage.py collectstatic --noinput
```

This will replace the `staticfiles.json` file in the repo. Commit the changes if
the file is different.

The `exercise_tracker.storage.StaticStorage` class is configured to allow
multiple versions of the app to share the same bucket. This allows us to deploy
static files before updating the app for zero-downtime deploys.

To configure zappa, create `zappa_settings.json` in the root of this repo, and
start with the following to configure the deployment.

```json
{
  "dev": {
    "aws_region": "us-east-1",
    "django_settings": "exercise_tracker.settings",
    "profile_name": "default",
    "project_name": "fcc-exercise-tracker",
    "runtime": "python3.6",
    "s3_bucket": "CHANGE_ME",
    "domain": "CHANGE_ME",
    "certificate_arn": "CHANGE_ME",
    "aws_environment_variables": {
      "AWS_STORAGE_BUCKET_NAME": "CHANGE_ME",
      "DJANGO_ALLOWED_HOSTS": "CHANGE_ME",
      "DJANGO_DB_ENGINE": "postgresql",
      "PG_HOST": "CHANGE_ME",
      "PG_NAME": "CHANGE_ME",
      "PG_USER": "CHANGE_ME",
      "PG_PASSWORD": "CHANGE_ME"
    }
  },
  "production": {
    "extends": "dev",
    "domain": "CHANGE_ME",
    "aws_environment_variables": {
      "DJANGO_DEBUG": "false",
      "AWS_STORAGE_BUCKET_NAME": "CHANGE_ME",
      "DJANGO_ALLOWED_HOSTS": "CHANGE_ME",
      "DJANGO_DB_ENGINE": "postgresql",
      "PG_HOST": "CHANGE_ME",
      "PG_NAME": "CHANGE_ME",
      "PG_USER": "CHANGE_ME",
      "PG_PASSWORD": "CHANGE_ME"
    }
  }
}
```


Most of the environment variables should be self explanatory.
`AWS_STORAGE_BUCKET_NAME` should be the same one used for the `collectstatic`
command.

See the [Zappa](https://github.com/Miserlou/Zappa) docs to finish the
deployment.
