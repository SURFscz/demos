"""
jupyterhub_config.py-docker
---------------------------

Configuration for JupyterHub tutorial - used for docker deployment
"""

# User whitelist - set of users allowed to use the Hub
c.Authenticator.allowed_users = {'admin', 'user1', 'user2', 'user3'}

# Administrators - set of users who can administer the Hub itself
c.Authenticator.admin_users = {'admin'}

# Authenticator
c.JupyterHub.authenticator_class = 'jhub_remote_user_authenticator.remote_user_auth.RemoteUserLocalAuthenticator'
c.RemoteUserLocalAuthenticator.header_name = "X-Authenticated-User"

c.LocalAuthenticator.create_system_users = True

c.JupyterHub.base_url = '/hub3/'
