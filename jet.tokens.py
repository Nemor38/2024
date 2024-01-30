import datetime
import jwt
import settings

def decode_jwt(encoded_token):
    try:
        decoded_payload = jwt.decode(
            encoded_token,
            settings.JWT_SECRET,
            algorithms=["HS256"],
        )
        return decoded_payload
    except jwt.ExpiredSignatureError:
        print("Token has expired.")
        return None
    except jwt.InvalidTokenError:
        print("Invalid token.")
        return None

encoded_jwt = jwt.encode(
    payload={
        "my_name": "Vasyl",
        "age": 10,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=60),
    },
    key=settings.JWT_SECRET,
    algorithm="HS256",
)

decoded_result = decode_jwt(encoded_jwt)

if decoded_result is not None:
    print(decoded_result)

