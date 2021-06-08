# Apache ReverseProxy
## Installation
- Copy ```.env-example``` to ```.env``` and change ```DOMAIN``` to required domain
- Copy ```apache/reverseproxy.conf.example``` to ```apache/reverseproxy.conf``` and change OIDC client details or use the Basic auth configuration for testing

## Startup
```$ docker-compose up```

## Testing
The configured host in ```.env``` ```DOMAIN``` can now be accessed using
  - https://DOMAIN/hub3 for a Jupyter notebook on back-end server 1172.21.11.3
  - https://DOMAIN/hub4 for a Jupyter notebook on back-end server 172.21.11.4
  - https://DOMAIN/ep5 for an EtherPad on back-end server 172.21.11.5
  - https://DOMAIN/ep6 for an EtherPad on back-end server 172.21.11.6
