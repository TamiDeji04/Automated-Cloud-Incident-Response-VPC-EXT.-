# Screenshots

All screenshots are cropped to the AWS console (browser and OS chrome removed) and named by phase in build order.

## Prefix Guide

| Prefix | Meaning |
|---|---|
| 01- | Phase 1: Isolation security group |
| 02- | Phase 2: Enable GuardDuty |
| 03- | Phase 3: Lambda IAM execution role |
| 04- | Phase 4: Python Lambda function |
| 05- | Phase 5: EventBridge rule |
| 06- | Phase 6: Testing and validation |

## Catalog

| File | What It Shows |
|---|---|
| 01a-sg-create-form.png | Create security group form (name, description, VPC `tami-cloud`) |
| 01b-sg-create-rules.png | Inbound empty, outbound rule shown during creation |
| 01c-sg-inbound-empty.png | Confirming zero inbound rules |
| 01d-sg-outbound-rule.png | Outbound rules tab |
| 01e-sg-details.png | Final SG details (`sg-013b730ecffce4ef5`) |
| 02-guardduty-enabled.png | GuardDuty successfully enabled, zero findings |
| 03-lambda-create-role.png | Create-function screen using `Lambda-EC2-Quarantine-Role` |
| 04a-lambda-code.png | Deployed Lambda function code |
| 04b-lambda-code-source.png | Code source view after successful deploy |
| 05a-eventbridge-rule-detail.png | Rule `Trigger-GuardDuty-Incident-Response` detail |
| 05b-eventbridge-event-pattern.png | Event pattern (`aws.guardduty` / GuardDuty Finding) |
| 05c-eventbridge-target.png | Lambda target `Isolate-Compromised-EC2` |
| 06a-guardduty-sample-findings.png | Generate sample findings in GuardDuty settings |
| 06b-guardduty-summary.png | GuardDuty summary populated with findings |
| 06c-cloudwatch-log-groups.png | `/aws/lambda/Isolate-Compromised-EC2` log group |
| 06d-cloudwatch-log-streams.png | Log streams, one per invocation |
| 06e-lambda-test-success.png | Lambda test result: `statusCode 200`, instance isolated |
| 06f-ec2-isolated.png | EC2 instance now carrying the isolation SG |
