FROM python:3.8-slim
COPY Pipfile* ./
RUN pip install pipenv && \
    pipenv install --system --deploy
COPY run.py .
CMD ["python","-u","run.py"]
