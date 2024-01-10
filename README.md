# FastAPI Serverless POC

### Instructions

Install dependencies

```bash
virtualenv env
source ./env/bin/activate
pip install -r ./src/requirements.txt
```

Set up pre-commit

```bash
pre-commit install
```

Run the app locally(not serverless)

```bash
python ./src/main.py
```

### Test in AWS Lambda

To test the application in Lambda, you will need to simulate a fake API Gateway Proxy request. To do this, navigate to the Lambdas test page and select the "apigateway-aws-proxy" template. From there, you can adjust the path and other relevant parameters as needed.

### Further steps

- Dockerize
- Infrastructure with Terraform -> API Gateway with Custom Domain

### License

MIT
