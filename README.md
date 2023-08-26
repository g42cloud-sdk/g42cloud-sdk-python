<p align="center">
<a href="https://www.g42cloud.com/"><img src="https://upload.wikimedia.org/wikipedia/en/4/43/Group_42_Logo.jpg"></a>
</p>

<h1 align="center">G42 Cloud Python Software Development Kit (Python SDK)</h1>

The G42 Cloud Python SDK allows you to easily work with G42 Cloud services such as Elastic Compute Service (ECS)
and Virtual Private Cloud (VPC) without the need to handle API related tasks.

This document introduces how to obtain and use G42 Cloud Python SDK.

## Requirements

- To use G42 Cloud Python SDK, you must have G42 Cloud account as well as the Access Key (AK) and Secret key (SK) of the
  G42 Cloud account. You can create an Access Key in the G42 Cloud console. 

- To use G42 Cloud Python SDK to access the APIs of specific service, please make sure you do have activated the
  service in [G42 Cloud console](https://console.g42cloud.com/console/) if needed.

- G42 Cloud Python SDK requires **Python 3.3** or later, run command `python --version` to check the version of Python.

## Install Python SDK

You could use **pip** or **source code** to install dependencies.

### Individual Cloud Service

Take using VPC SDK for example, you need to install `g42cloudsdkvpc` library:

- Use python pip

```bash
# Install the VPC management library
pip install g42cloudsdkvpc
```

## Code example

- The following example shows how to query a list of VPC in a specific region, you need to substitute your
  real `{Service}Client` for `VpcClient` in actual use.
- Substitute the values for `{your ak string}`, `{your sk string}`, `{your endpoint string}` and `{your project id}`.

```python
# coding: utf-8


from g42cloudsdkcore.auth.credentials import BasicCredentials
from g42cloudsdkcore.exceptions import exceptions
from g42cloudsdkcore.http.http_config import HttpConfig

# import specified service library g42cloudsdk{service}, take vpc for example
from g42cloudsdkvpc.v2 import *


def list_vpc(client):
    try:
        request = ListVpcsRequest(limit=1)
        response = client.list_vpcs(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)


if __name__ == "__main__":
    ak = "{your ak string}"
    sk = "{your sk string}"
    endpoint = "{your endpoint}"
    project_id = "{your project id}"

    config = HttpConfig.get_default_config()
    config.ignore_ssl_verification = True
    credentials = BasicCredentials(ak, sk, project_id)

    vpc_client = VpcClient.new_builder() \
        .with_http_config(config) \
        .with_credentials(credentials) \
        .with_endpoint(endpoint) \
        .build()

    list_vpc(vpc_client)
```

## Changelog

Detailed changes for each released version are documented in
the [CHANGELOG.md](https://github.com/g42cloud-sdk/g42cloud-sdk-python/blob/master/CHANGELOG.md).

## User Manual [:top:](#g42-cloud-python-software-development-kit-python-sdk)

* [1. Client Configuration](#1-client-configuration-top)
    * [1.1 Default Configuration](#11-default-configuration-top)
    * [1.2 Network Proxy](#12-network-proxy-top)
    * [1.3 Timeout Configuration](#13-timeout-configuration-top)
    * [1.4 SSL Certification](#14-ssl-certification-top)
* [2. Credentials Configuration](#2-credentials-configuration-top)
    * [2.1 Use Permanent AK&SK](#21-use-permanent-aksk-top)
    * [2.2 Use Temporary AK&SK](#22-use-temporary-aksk-top)
* [3. Client Initialization](#3-client-initialization-top)
    * [3.1 Initialize the client with specified Endpoint](#31-initialize-the-serviceclient-with-specified-endpoint-top)
* [4. Send Requests and Handle Responses](#4-send-requests-and-handle-responses-top)
    * [4.1 Exceptions](#41-exceptions-top)
    * [4.2 Get Response Object](#42-get-response-object-top)
* [5. Use Asynchronous Client](#5-use-asynchronous-client-top)
* [6. Troubleshooting](#6-troubleshooting-top)
    * [6.1 Access Log](#61-access-log-top)
    * [6.2 Original HTTP Listener](#62-original-http-listener-top)
* [7. Upload and download files](#7-upload-and-download-files-top)

### 1. Client Configuration [:top:](#user-manual-top)

#### 1.1 Default Configuration [:top:](#user-manual-top)

```python
from g42cloudsdkcore.http.http_config import HttpConfig

#  Use default configuration
config = HttpConfig.get_default_config()
```

#### 1.2 Network Proxy [:top:](#user-manual-top)

```python
# Use Proxy if needed
config.proxy_protocol = 'http'
config.proxy_host = 'proxy.g42cloud.com'
config.proxy_port = 80
config.proxy_user = 'username'
config.proxy_password = 'password'
```

#### 1.3 Timeout Configuration [:top:](#user-manual-top)

```python
# The default connection timeout is 60 seconds, the default read timeout is 120 seconds
# Set the connection timeout and read timeout to 120 seconds
config.timeout = 120
# Set the connection timeout to 60 seconds and the read timeout to 120 seconds
config.timeout = (60, 120)
```

#### 1.4 SSL Certification [:top:](#user-manual-top)

```python
# Skip SSL certifaction checking while using https protocol if needed
config.ignore_ssl_verification = True
# Configure the server's CA certificate for the SDK to verify the legitimacy of the server
config.ssl_ca_cert = ssl_ca_cert
```

### 2. Credentials Configuration [:top:](#user-manual-top)

There are two types of G42 Cloud services, `regional` services and `global` services.

Global services contain IAM.

For `regional` services' authentication, projectId is required to initialize BasicCredentials.

For `global` services' authentication, domainId is required to initialize GlobalCredentials.

The following authentications are supported:

- permanent AK&SK
- temporary AK&SK + SecurityToken

#### 2.1 Use Permanent AK&SK [:top:](#user-manual-top)

**Parameter description**:

- `ak` is the access key ID for your account.
- `sk` is the secret access key for your account.
- `project_id` is the ID of your project depending on your region which you want to operate.
- `domain_id` is the account ID of G42 Cloud.

```python
# Regional services
basic_credentials = BasicCredentials(ak, sk, project_id)

# Global services
global_credentials = GlobalCredentials(ak, sk, domain_id)
```

#### 2.2 Use Temporary AK&SK [:top:](#user-manual-top)

It's required to obtain temporary AK&SK and security token first, which could be obtained through
permanent AK&SK or through an agency.

**Parameter description**:

- `ak` is the access key ID for your account.
- `sk` is the secret access key for your account.
- `security_token` is the security token when using temporary AK/SK.
- `project_id` is the ID of your project depending on your region which you want to operate.
- `domain_id` is the account ID of G42 Cloud.

After the temporary AK&SK&SecurityToken is successfully obtained, you can use the following example to initialize the authentication:

```python
# Regional services
basic_credentials = BasicCredentials(ak, sk, project_id).with_security_token(security_token)

# Global services
global_credentials = GlobalCredentials(ak, sk, domain_id).with_security_token(security_token)
```

### 3. Client Initialization [:top:](#user-manual-top)

#### 3.1 Initialize the {Service}Client with specified Endpoint [:top:](#user-manual-top)

```python
# Specify the endpoint, take the endpoint of VPC service in region of cn-north-4 for example
endpoint = "https://vpc.cn-north-4.g42cloud.com"

# Initialize the credentials, you should provide project_id or domain_id in this way, take initializing BasicCredentials for example
basic_credentials = BasicCredentials(ak, sk, project_id)

# Initialize specified service client instance, take initializing the regional service VPC's VpcClient for example
client = VpcClient.new_builder() \
    .with_http_config(config) \
    .with_credentials(basic_credentials) \
    .with_endpoint(endpoint) \
    .build()
```

### 4. Send Requests and Handle Responses [:top:](#user-manual-top)

```python
# Initialize a request and print response, take interface of ListVpcs for example
request = ListVpcsRequest(limit=1)

response = client.list_vpcs(request)
print(response)
```

#### 4.1 Exceptions [:top:](#user-manual-top)

| Level 1 | Notice | Level 2 | Notice |
| :---- | :---- | :---- | :---- |
| ConnectionException | Connection error | HostUnreachableException | Host is not reachable |
| | | SslHandShakeException | SSL certification error |
| RequestTimeoutException | Request timeout | CallTimeoutException | timeout for single request |
| | | RetryOutageException | no response after retrying |
| ServiceResponseException | service response error | ServerResponseException | server inner error, http status code: [500,] |
| | | ClientRequestException | invalid request, http status code: [400? 500) |

```python
# handle exceptions
try:
    request = ListVpcsRequest(limit=1)
    response = client.list_vpcs(request)
    print(response)
except exception.ServiceResponseException as e:
    print(e.status_code)
    print(e.request_id)
    print(e.error_code)
    print(e.error_msg)
```

#### 4.2 Get Response Object [:top:](#user-manual-top)

The default response format of each request is `json string`, if you want to obtain the response object, the Python SDK
supports using method `to_json_object()` to get it.

```python
request = ListVpcsRequest(limit=1)
# original response json string
response = client.list_vpcs(request)
print(response)
# response object
response_obj = response.to_json_object()
print(response_obj["vpcs"])
```

**Notice:** This method is only supported in version `3.0.34-rc` or later.

### 5. Use Asynchronous Client [:top:](#user-manual-top)

```python
# Initialize asynchronous client, take VpcAsyncClient for example
client = VpcAsyncClient.new_builder() \
    .with_http_config(config) \
    .with_credentials(basic_credentials) \
    .with_endpoint(endpoint) \
    .build()

# send asynchronous request
request = ListVpcsRequest(limit=1)
response = client.list_vpcs_async(request)

# get asynchronous response
print(response.result())
```

### 6. Troubleshooting [:top:](#user-manual-top)

SDK supports `Access` log and `Debug` log which could be configured manually.

#### 6.1 Access Log [:top:](#user-manual-top)

SDK supports print access log which could be enabled by manual configuration, the log could be output to the console or
specified files.

Initialize specified service client instance, take VpcClient for example:

```python
client = VpcClient.new_builder() \
    .with_http_config(config) \
    .with_credentials(basic_credentials) \
    .with_endpoint(endpoint) \
    .with_file_log(path="test.log", log_level=logging.INFO) \  # Write log files
    .with_stream_log(log_level=logging.INFO) \                 # Write log to console
    .build()
```

**where:**

- `with_file_log`:
    - `path` means log file path.
    - `log_level` means log level, default is INFO.
    - `max_bytes` means size of single log file, the default value is 10485760 bytes.
    - `backup_count` means count of log file, the default value is 5.
- `with_stream_log`:
    - `stream` means stream object, the default value is sys.stdout.
    - `log_level` means log level, the default value is INFO.

After enabled log, the SDK will print the access log by default, every request will be recorded to the console like:

```text
2020-06-16 10:44:02,019 4568 G42Cloud-SDK http_handler.py 28 INFO "GET https://vpc.cn-north-1.myg42cloud.com/v1/0904f9e1f100d2932f94c01f9aa1cfd7/vpcs" 200 11 0:00:00.543430 b5c927ffdab8401e772e70aa49972037
```

The format of access log is:

```python
%(asctime)s %(thread)d %(name)s %(filename)s %(lineno)d %(levelname)s %(message)s
```

#### 6.2 Original HTTP Listener [:top:](#user-manual-top)

In some situation, you may need to debug your http requests, original http request and response information will be
needed. The SDK provides a listener function to obtain the original encrypted http request and response information.

> :warning:  Warning: The original http log information is used in debugging stage only, please do not print the original http header or body in the production environment. These log information is not encrypted and contains sensitive data such as the password of your ECS virtual machine, or the password of your IAM user account, etc. When the response body is binary content, the body will be printed as "***" without detailed information.

```python
import logging
from g42cloudsdkcore.http.http_handler import HttpHandler


def response_handler(**kwargs):
    logger = kwargs.get("logger")
    response = kwargs.get("response")
    request = response.request

    base = "> Request %s %s HTTP/1.1" % (request.method, request.path_url) + "\n"
    if len(request.headers) != 0:
        base = base + "> Headers:" + "\n"
        for each in request.headers:
            base = base + "    %s : %s" % (each, request.headers[each]) + "\n"
    base = base + "> Body: %s" % request.body + "\n\n"

    base = base + "< Response HTTP/1.1 %s " % response.status_code + "\n"
    if len(response.headers) != 0:
        base = base + "< Headers:" + "\n"
        for each in response.headers:
            base = base + "    %s : %s" % (each, response.headers[each],) + "\n"
    base = base + "< Body: %s" % response.content
    logger.debug(base)


if __name__ == "__main__":
    client = VpcClient.new_builder() \
        .with_http_config(config) \
        .with_credentials(basic_credentials) \
        .with_stream_log(log_level=logging.DEBUG) \
        .with_http_handler(HttpHandler().add_response_handler(response_handler)) \
        .with_endpoint(endpoint) \
        .build()
```

**Notice:**

HttpHandler supports method `add_request_handler` and `add_response_handler`.

### 7. Upload and download files [:top:](#user-manual-top)

Take the interface `CreateImageWatermark` of the service `Data Security Center` as an example, this interface needs to upload an image file and return the watermarked image file stream:

```python
# coding: utf-8
from g42cloudsdkcore.auth.credentials import BasicCredentials
from g42cloudsdkcore.exceptions import exceptions
from g42cloudsdkcore.http.http_config import HttpConfig
from g42cloudsdkcore.http.formdata import FormFile
from g42cloudsdkservice.v1 import *


def upload_and_download_file(client):

    try:
        request = UploadFileRequest()
        # Open the file in mode "rb", create a Formfile object.
        image_file = FormFile(open("demo.jpg", "rb"))
        body = UploadFileRequestBody(file=image_file, file_name="rename.jpg")
        request.body = body
        response = client.upload_file(request)
        image_file.close()
        
        # Define the method of downloading files.
        def save(stream):
            with open("result.jpg", "wb") as f:
                f.write(stream.content)
        # Download the file.
        response.consume_download_stream(save)
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)


if __name__ == "__main__":
    ak = "{your ak string}"
    sk = "{your sk string}"
    endpoint = "{your endpoint}"
    project_id = "{your project id}"
    config = HttpConfig.get_default_config()
    config.ignore_ssl_verification = True
    credentials = BasicCredentials(ak, sk, project_id)
    service_client = ServiceClient.new_builder() \
        .with_http_config(config) \
        .with_credentials(credentials) \
        .with_endpoint(endpoint) \
        .build()

    upload_and_download_file(service_client)
```
