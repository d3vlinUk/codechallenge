
def authenticate_on_subscribe_noncompliant(self, event) -> None:
    import boto3
    subscriptions_failed = 0
    for record in event["Records"]:
        message = record["body"]
        if message["Type"] == "SubscriptionConfirmation":
            try:
                topic_arn = message["TopicArn"]
                token = message["Token"]
                sns_client = boto3.client("sns",
                                          region_name=topic_arn.split(":")[3])
                sns_client.confirm_subscription(TopicArn=topic_arn,
                                                Token=token)
            except Exception:
                subscriptions_failed += 1