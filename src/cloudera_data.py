import requests
from requests_kerberos import HTTPKerberosAuth, OPTIONAL

# Cloudera Manager API endpoint
CM_API = 'http://cloudera-manager.example.com:7180/api/v19'

# Setup Kerberos authentication
kerberos_auth = HTTPKerberosAuth(mutual_authentication=OPTIONAL)

def fetch_cluster_info():
    url = f'{CM_API}/clusters'
    response = requests.get(url, auth=kerberos_auth)
    response.raise_for_status()
    return response.json()

def fetch_service_info(cluster_name):
    url = f'{CM_API}/clusters/{cluster_name}/services'
    response = requests.get(url, auth=kerberos_auth)
    response.raise_for_status()
    return response.json()

def fetch_host_info():
    url = f'{CM_API}/hosts'
    response = requests.get(url, auth=kerberos_auth)
    response.raise_for_status()
    return response.json()

if __name__ == '__main__':
    cluster_info = fetch_cluster_info()
    print('Cluster Info:', cluster_info)

    # Assuming you have one cluster, get its name
    cluster_name = cluster_info['items'][0]['name']

    service_info = fetch_service_info(cluster_name)
    print('Service Info:', service_info)

    host_info = fetch_host_info()
    print('Host Info:', host_info)
