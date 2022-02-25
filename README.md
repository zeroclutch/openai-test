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