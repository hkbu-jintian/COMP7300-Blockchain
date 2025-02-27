import hashlib

proof = 0
index = 21
previous_hash = "abc1234"
timestamp = 123456
transaction_data = [
	{ "index": 0, "sender": "mining", "recipient": "dea1af", "amount": 10.00, "signature": "" },
	{ "index": 1, "sender": "fea123", "recipient": "087efa", "amount": 5.00, "signature": "abcdef"}
]

str = f"{index}{previous_hash}{timestamp}{str(transaction_data)}{proof}"

def calculate_hash(str):
		# Encode the string to bytes and calculate the hash
    # hexdigest() returns a hexadecimal string of the hash
    return hashlib.sha256(str.encode()).hexdigest()

while not calculate_hash(str).startswith("0000"):
    proof += 1
    str = f"{index}{previous_hash}{timestamp}{transaction_data}{proof}"

print(f"Proof of work found: {proof}")
print(calculate_hash(str))