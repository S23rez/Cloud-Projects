==============
CREATE TABLE
==============
aws dynamodb create-table \
    --table-name SecurityAlerts \
    --attribute-definitions AttributeName=AlertID,AttributeType=S \
    --key-schema AttributeName=AlertID,KeyType=HASH \
    --billing-mode PAY_PER_REQUEST

===============
ADD ITEMS
===============
aws dynamodb put-item \
    --table-name SecurityAlerts \
    --item '{
        "AlertID": {"S": "ALT-SEC-84920"},
        "Severity": {"S": "Critical"},
        "ThreatType": {"S": "Brute Force Attack"},
        "SourceIP": {"S": "198.51.100.42"},
        "TargetEndpoint": {"S": "core-auth-prod-01"},
        "FailedAttempts": {"N": "45"},
        "IsMitigated": {"BOOL": false}
    }'

================
VERIFY ITEMS
================
aws dynamodb get-item \
    --table-name SecurityAlerts \
    --key '{"AlertID": {"S": "ALT-SEC-84920"}}'