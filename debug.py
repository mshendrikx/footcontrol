import project
import os

os.environ['MYSQL_ROOT_PASSWORD'] = 'M4r14d8P455'
os.environ['MYSQL_HOST'] = 'hendrikx.com.br:3306'
os.environ['FOOTDRAW_EMAIL'] = 'footdraw@hendrikx.com.br'
os.environ['SMTP_SERVER'] = 'localhost'
os.environ['SMTP_PORT'] = '25'
      
app = project.create_app()

app.run(host="0.0.0.0", port=7904)