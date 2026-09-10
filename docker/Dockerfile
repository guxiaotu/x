FROM ghcr.m.daocloud.io/astral-sh/uv:python3.14-bookworm-slim

WORKDIR /app

COPY ./ ./

RUN <<EOT
uv sync --no-dev
EOT

ENTRYPOINT ["uv", "run", "manage.py", "runserver"]