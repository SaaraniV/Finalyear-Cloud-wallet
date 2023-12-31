import boto3

CLOUD_WALLET = "cloud-wallet"
STATIC_CLOUD_WALLET = "static-cloud-wallet"

s3 = boto3.client("s3")

#upload to cloud-wallet
with open("./Alfredtas.webp", "rb") as f:
    s3.upload_fileobj(f, CLOUD_WALLET, "Alfredtas.webp")

#upload to static-cloud-wallet
with open("./Alfredtas.webp", "rb") as f:
    s3.upload_fileobj(f, STATIC_CLOUD_WALLET, "Alfredtas.webp")

