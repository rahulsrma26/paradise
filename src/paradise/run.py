#TODO: Create cmd args for host and port

import uvicorn

def main():
    uvicorn.run("paradise.server:app", host="0.0.0.0", port=8000, log_level="info")

if __name__ == "__main__":
    main()
