# Simple REST API in Python with Flask

Create virtual environment:

```bash
python3 -m venv venv 
source venv/bin/activate      
```

Install packages:

```bash
pip3 install -r requirements.txt      
pip3 list
```

Start app:

```bash
python3 main.py  
```

Test app:

```bash
python -m pytest test.py
```

Test app and generate report:

```bash
pytest test.py --html=report.html 
pytest test.py --junit-xml=report.xml 
```

Containerizing app:

```bash
docker build -t sebastian-czech/simple-rest-api-python-flask .
```

Run app in container:

```bash
docker run -p 48080:48080 sebastian-czech/simple-rest-api-python-flask
```