import hashlib
import base64

# 原始密碼
password = "123456"

# 將密碼轉換成SHA-256哈希值
hashed_password = hashlib.sha256(password.encode()).digest()

# 將哈希值轉換成Base64 URL編碼
encoded_password = base64.urlsafe_b64encode(hashed_password).decode()

print(encoded_password)
