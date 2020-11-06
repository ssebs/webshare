# webshare

Share files via HTTP or via the website

## API endpoints:
- `POST`
  - `/upload/:filename`
    - Body: file body
    - Returns: Path for uploaded file
- `GET`
  - `/download/:path`
    - Returns: File
  - `/`
    - Returns: React web app

## Usage
- `curl --data-binary @sample.png  http://127.0.0.1:5000/api/upload/sample.png`
  - `http://localhost:5000/f179df-test.png`
- `wget http://localhost:5000/f179df-test.png`
  - `‘f179df-test.png’ saved [2217/2217]`

## Installation
- Clone this repo
- `$ cd webshare`
- `$ python3 -m venv venv`
- `$ source ./venv/bin/activate`
- `(venv) $ pip install -r requirements.txt`
- `(venv) $ cd frontend/`
- `(venv) $ npm i`
- `(venv) $ npm run build`
- `(venv) $ cd ..`
- `(venv) $ python wsgi.py`

## License
[MIT](./LICENSE)
