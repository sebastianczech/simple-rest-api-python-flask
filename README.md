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

Unit test:

```bash
python -m pytest test.py
```

Unit test and generate report:

```bash
pytest test.py --html=report.html 
pytest test.py --junit-xml=report.xml 
```

Acceptance test:

```bash
robot --outputdir results atest/ 
```

Containerizing app:

```bash
docker build -t sebastian-czech/simple-rest-api-python-flask .
```

Run app in container:

```bash
docker run -p 48080:48080 sebastian-czech/simple-rest-api-python-flask
```