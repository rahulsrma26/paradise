# Paradise

A file sharing and media streaming solution for local networks. Using this utility you can start a local server on your machine that is visible to other devices like mobile, laptop etc. Which can be used to download/upload files from other machines.

## Why it's needed?

### Can't I just transfer files from/to External drive or internet.

This utility is useful for people that are using office/work laptop/device that usually disables USB ports and/or external disks. And you want to transfer locally, so that it will be faster as well as don't your internet data.

## Getting Started

These instructions will get you a server up and running on your local machine.

### Prerequisites

Requires: python 3.6+

### Installing

Paradise is available on [PyPi](https://pypi.org/project/paradise/) and can be easily installed using pip.

```
pip install paradise
```

If you already have paradise and want to update to a newer version

```
pip install -U paradise
```

You can get the cutting edge version directly from dev branch (this can be unstable)

```
python -m pip install git+https://github.com/rahulsrma26/paradise
```

## Running

```
paradise
```

This will show the output and ip of your machine on local network

```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [14192] using statreload
INFO:     Started server process [1580]
INFO:     Waiting for application startup.
[Visit url] http://192.168.0.123:8000
INFO:     Application startup complete.
```

Web server can be reached using http://127.0.0.1:8000 on your browser on the same machine. But if you want to access the web server from other devices then you need to open `Visit url` in the browser. In this example it is `http://192.168.0.123:8000`.

## Built With

* [FastAPI](http://https://fastapi.tiangolo.com/) - Backend
* [Vue.js](https://vuejs.org/) - Client framework

## Authors

* **Rahul Sharma** - *Initial work* - [Rahul Sharma](https://github.com/rahulsrma26)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration - [Testing & Packaging by Hynek Schlawack](https://hynek.me/articles/testing-packaging/)
