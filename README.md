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
