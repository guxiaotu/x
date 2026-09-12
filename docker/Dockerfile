# ---- builder ----
FROM docker.m.daocloud.io/python:3.14-alpine AS builder

WORKDIR /app

ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy
ENV UV_PYTHON_DOWNLOADS=never

# install uv tool
COPY --from=ghcr.m.daocloud.io/astral-sh/uv:0.12.13 /uv /usr/local/bin/uv

# download dependencies by use cache layer(exclude dev dependencies)
COPY pyproject.toml uv.lock ./

# ---- uv / pip cache ----
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    uv sync --locked --no-install-project --no-dev

# copy source code(exclude dev dependencies)
COPY . .
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=cache,target=/root/.cache/pip \
    uv sync --locked --no-dev

# ---- build app ----
FROM docker.m.daocloud.io/python:3.14-alpine

WORKDIR /app

ENV PATH="/app/.venv/bin:$PATH"
ENV PYTHONUNBUFFERED=1
# no need to download python packages in production
ENV UV_PYTHON_DOWNLOADS=never
ENV DJANGO_SETTINGS_MODULE=config.settings

COPY --from=builder /app /app

EXPOSE 8000

# use uvicorn run asgi server
ENTRYPOINT ["uvicorn", "config.asgi:application", "--host", "0.0.0.0", "--port", "8000"]