# python-blockchain
Use python to build a blockchain system.
## Install packages
Run the command
```
pip install -r requirements.txt
```
## Run single node
```
python node.py
```
After installing packages, open the browser with the URL `localhost:5000` (default)
## Run multiple nodes
For example, if we want to run 2 nodes in the network. Open two terminals and input the following commands for the corresponding terminal.
Node 1 (This node runs in port 5000)
```
python node.py
```
Node 2 (This node runs in port 5001, you can change the port by yourself)
```
python node.py -p 5001
```
## Install Pycrypto
Install `pycryptodome`, instead of `pycrypto`.
```
pip install pycryptodome
```
## Reference
1. https://www.bilibili.com/video/BV1Hb411c7oH/
2. https://www.udemy.com/course/learn-python-by-building-a-blockchain-cryptocurrency/?couponCode=D_0323
