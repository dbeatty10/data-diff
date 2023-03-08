from dbtc import dbtCloudClient

# first party

def get_client(service_token):
    client = dbtCloudClient(service_token=service_token)
    return client

def dynamic_request(_prop, method, *args, **kwargs):
    return getattr(_prop, method)(*args, **kwargs)

if __name__ == '__main__':
    pass
