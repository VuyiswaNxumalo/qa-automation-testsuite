import os

BASE_URL = "https://reqres.in/api"
API_KEY = os.environ.get("REQRES_API_KEY")

if not API_KEY:
    raise RuntimeError("  "REQRES_API_KEY environment variable not set. "
        "Get a free key at https://app.reqres.in/api-keys and export it:\n"
        "  export REQRES_API_KEY='your_key_here'"
    
)

HEADERS ={"x-api-key": API_KEY}


