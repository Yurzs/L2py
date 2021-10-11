from aiojsonapi import JsonTemplate, routes

from data.models.account import Account


@routes.post("/api/data/account.authenticate")
@JsonTemplate(
    {
        "username": str,
        "password": str,
        "__required__": ["__all__"],
    }
)
async def account_authenticate(request, validated_data):
    """Authenticates account login."""

    response = {"account": None, "authenticated": False}
    account = await Account.one(username=validated_data["username"])
    if account is not None:
        authenticated = account.authenticate(validated_data["password"])
        if authenticated:
            response.update(
                {
                    "account": account,
                    "authenticated": authenticated,
                }
            )
    return response
