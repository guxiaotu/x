# ---- builder ----
FROM docker.m.daocloud.io/python:3.10-slim AS builder

# 安装uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy

WORKDIR /app

# 依赖层（先只拷 lock，利用缓存）
COPY pyproject.toml uv.lock ./
RUN uv sync --locked --no-install-project --no-dev

# 源码层
COPY . .
RUN uv sync --locked --no-dev

# ---- runtime ----
FROM docker.m.daocloud.io/python:3.10-slim AS runtime

ENV PATH="/app/.venv/bin:$PATH" \
    PYTHONUNBUFFERED=1 \
    DJANGO_SETTINGS_MODULE=config.settings

WORKDIR /app
COPY --from=builder /app /app

# 非 root 用户
#RUN useradd -m appuser
#USER appuser

EXPOSE 8000

# 生产环境需要使用uvicorn运行asgi服务，未来支持异步功能
CMD ["uvicorn", "config.asgi:application", "--host", "0.0.0.0", "--port", "8000"]