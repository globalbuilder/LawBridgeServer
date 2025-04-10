from rest_framework.views import APIView
from rest_framework.response import Response

class APIDocumentationView(APIView):
    """
    Returns a JSON dictionary containing details of all available API endpoints.
    """
    def get(self, request):
        docs = {
            "accounts": [
                {
                    "name": "Register",
                    "url": "/api/accounts/register/",
                    "method": "POST",
                    "body": {
                        "username": "string (required)",
                        "password1": "string (required)",
                        "password2": "string (required)",
                        "first_name": "string (optional)",
                        "last_name": "string (optional)",
                        "image": "file (optional)"
                    },
                    "headers": {
                        "Content-Type": "application/json"
                    }
                },
                {
                    "name": "Login",
                    "url": "/api/accounts/login/",
                    "method": "POST",
                    "body": {
                        "username": "string (required)",
                        "password": "string (required)"
                    },
                    "headers": {
                        "Content-Type": "application/json"
                    }
                },
                {
                    "name": "Logout",
                    "url": "/api/accounts/logout/",
                    "method": "POST",
                    "headers": {
                        "Authorization": "Token <your_token>"
                    }
                },
                {
                    "name": "Change Password",
                    "url": "/api/accounts/change-password/",
                    "method": "POST",
                    "body": {
                        "old_password": "string (required)",
                        "new_password1": "string (required)",
                        "new_password2": "string (required)"
                    },
                    "headers": {
                        "Content-Type": "application/json",
                        "Authorization": "Token <your_token>"
                    }
                },
                {
                    "name": "User Info (Retrieve/Update)",
                    "url": "/api/accounts/me/",
                    "method": "GET/PUT/PATCH",
                    "headers": {
                        "Authorization": "Token <your_token>"
                    }
                }
            ],
            "educational_opportunities": [
                {
                    "name": "List Educational Opportunities",
                    "url": "/api/educationalopportunities/",
                    "method": "GET",
                    "query_params": {
                        "search": "optional search keyword (by title)"
                    },
                    "headers": {
                        "Authorization": "Token <your_token>"
                    }
                },
                {
                    "name": "Educational Opportunity Detail",
                    "url": "/api/educationalopportunities/<id>/",
                    "method": "GET",
                    "headers": {
                        "Authorization": "Token <your_token>"
                    }
                },
                {
                    "name": "List Favorite Educational Opportunities",
                    "url": "/api/educationalopportunities/favorites/",
                    "method": "GET",
                    "headers": {
                        "Authorization": "Token <your_token>"
                    }
                },
                {
                    "name": "Add Favorite Educational Opportunity",
                    "url": "/api/educationalopportunities/favorites/add/",
                    "method": "POST",
                    "body": {
                        "opportunity_id": "number (required)"
                    },
                    "headers": {
                        "Content-Type": "application/json",
                        "Authorization": "Token <your_token>"
                    }
                },
                {
                    "name": "Remove Favorite Educational Opportunity",
                    "url": "/api/educationalopportunities/favorites/remove/<id>/",
                    "method": "DELETE",
                    "headers": {
                        "Authorization": "Token <your_token>"
                    }
                }
            ],
            "legal_resources": [
                {
                    "name": "List Legal Resources",
                    "url": "/api/legalresources/",
                    "method": "GET",
                    "query_params": {
                        "search": "optional search keyword (by title)"
                    },
                    "headers": {
                        "Authorization": "Token <your_token>"
                    }
                },
                {
                    "name": "Legal Resource Detail",
                    "url": "/api/legalresources/<id>/",
                    "method": "GET",
                    "headers": {
                        "Authorization": "Token <your_token>"
                    }
                },
                {
                    "name": "List Favorite Legal Resources",
                    "url": "/api/legalresources/favorites/",
                    "method": "GET",
                    "headers": {
                        "Authorization": "Token <your_token>"
                    }
                },
                {
                    "name": "Add Favorite Legal Resource",
                    "url": "/api/legalresources/favorites/add/",
                    "method": "POST",
                    "body": {
                        "resource_id": "number (required)"
                    },
                    "headers": {
                        "Content-Type": "application/json",
                        "Authorization": "Token <your_token>"
                    }
                },
                {
                    "name": "Remove Favorite Legal Resource",
                    "url": "/api/legalresources/favorites/remove/<id>/",
                    "method": "DELETE",
                    "headers": {
                        "Authorization": "Token <your_token>"
                    }
                }
            ],
            "notifications": [
                {
                    "name": "List Notifications",
                    "url": "/api/notifications/",
                    "method": "GET",
                    "headers": {
                        "Authorization": "Token <your_token>"
                    }
                },
                {
                    "name": "Notification Detail / Update",
                    "url": "/api/notifications/<id>/",
                    "method": "GET/PATCH",
                    "body": {
                        "is_read": "boolean (optional, for marking as read)"
                    },
                    "headers": {
                        "Content-Type": "application/json",
                        "Authorization": "Token <your_token>"
                    }
                }
            ]
        }
        return Response(docs)
