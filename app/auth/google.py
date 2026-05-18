import httpx

from app.constants import environment

GOOGLE_AUTH_URL  = "https://accounts.google.com/o/oauth2/v2/auth"
GOOGLE_TOKEN_URL = "https://oauth2.googleapis.com/token"
GOOGLE_USERINFO_URL = "https://www.googleapis.com/oauth2/v3/userinfo"
def get_google_auth_url(state: str) -> str:
    params = {
        "client_id":     environment.GOOGLE_CLIENT_ID,
        "redirect_uri":  environment.GOOGLE_REDIRECT_URI,
        "response_type": "code",
        "scope":         "openid email profile",
        "state":         state,
    }
    query = "&".join(f"{k}={v}" for k, v in params.items())
    return f"{GOOGLE_AUTH_URL}?{query}"
async def exchange_code_for_token(code: str) -> dict:
    async with httpx.AsyncClient() as client:
        resp = await client.post(GOOGLE_TOKEN_URL, data={
            "code":          code,
            "client_id":     environment.GOOGLE_CLIENT_ID,
            "client_secret": environment.GOOGLE_CLIENT_SECRET,
            "redirect_uri":  environment.GOOGLE_REDIRECT_URI,
            "grant_type":    "authorization_code",
        })
        resp.raise_for_status()
        return resp.json()
async def get_google_user(access_token: str) -> dict:
    async with httpx.AsyncClient() as client:
        resp = await client.get(
            GOOGLE_USERINFO_URL,
            headers={"Authorization": f"Bearer {access_token}"}
        )
        resp.raise_for_status()
        return resp.json()
