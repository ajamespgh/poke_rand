venv\Scripts\Activate.ps1
$env:FLASK_APP = "poke_rand"
$env:FLASK_ENV = "development"
flask run
