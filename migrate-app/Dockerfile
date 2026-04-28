FROM python:3.12-alpine
WORKDIR /usr/local/migrate-app

RUN addgroup -S pymigrate && adduser -S pymigrate -G pymigrate \
    && chown pymigrate:pymigrate /usr/local/migrate-app

COPY --chown=pymigrate:pymigrate requirements.txt ./

RUN apk add --no-cache gcc musl-dev libffi-dev \
    && pip install --no-cache-dir -r requirements.txt \
    && apk del gcc musl-dev libffi-dev

COPY --chown=pymigrate:pymigrate app ./app

USER pymigrate
EXPOSE 3000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "3000"]

# FROM python:3.12-slim-trixie
# WORKDIR /usr/local/migrate-app

# RUN useradd pymigrate && chown pymigrate:pymigrate /usr/local/migrate-app

# COPY --chown=pymigrate:pymigrate requirements.txt ./

# RUN pip install --no-cache-dir -r requirements.txt && \
#     chmod +x /usr/local/lib/python3.12/site-packages/fastapi_tailwind/

# COPY --chown=pymigrate:pymigrate app ./app

# USER pymigrate

# EXPOSE 3000

# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "3000"]