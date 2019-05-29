1. Install virtualenv && flask

   **pip install virtualenv**

   **mkdir backend-api**

   **cd backend-api**

   **virtualenv flask**

   **flask/bin/pip install flask**

2. Running command

   **./5000.py**

It will start a flask python process and listening tcp 5000 port.

Start 5 processes by run once command (tcp 5001 to tcp 5005)

   **for i in {1..5}; do cp -f ./5000.py ./500$i.py; done**

   **for i in {1..5}; do nohup ./500$i.py &/; done**

   **for i in {1..5}; do rm -f ./500$i.py; done**
