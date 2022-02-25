1. Clone this repo

```bash
git clone https://github.com/zeroclutch/openai-test
```

2. Install the gcloud package

https://cloud.google.com/sdk/docs/install

3. Create a Cloud Functions Project

4. Do this in on your personal machine's directory

```bash
pip install -r requirements.txt
gcloud auth login
```

5. To deploy, use

```bash
gcloud functions deploy functionNameGoesHere \
--runtime python39 --trigger-http --allow-unauthenticated --entry-point handler
```

To test, use
```bash
functions_framework --target=handler
```

When testing, you need to make a POST request with the content you want to http://localhost:8080.

[Here's how you make a POST request in Postman](https://stackoverflow.com/a/29365126). Instead of putting in JSON, put in the string you want to use.
