class S3Error(Exception):
    pass

class ConfigParseError(Exception):
    pass

class ConfigValidationError(Exception):
    pass

class AwsCredentialNotFound(Exception):
    pass

class SecretAccessKeyNotFound(AwsCredentialNotFound):
    pass

class AccessKeyIdNotFound(AwsCredentialNotFound):
    pass