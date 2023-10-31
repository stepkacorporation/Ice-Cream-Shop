from django.core.signing import Signer

_signer = Signer()


def get_token_by_username(username: str) -> str:
    token = _signer.sign(username)
    return token


def unsign_token(token: str) -> str:
    return _signer.unsign(token)
