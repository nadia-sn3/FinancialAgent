IN TERMINAL RUN:

(using pythons virtual environemtn -> venv)
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

or


(using conda)
    conda create -n demo python=3.12 -y
    conda activate demo
    pip install -r requirements.txt


run:

python financial_agent.py