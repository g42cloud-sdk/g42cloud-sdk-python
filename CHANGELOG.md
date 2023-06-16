# 0.0.7-beta 2023-06-16

### G42Cloud SDK CCE

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ShowNode**
    - changes of response param
      - `+ status.lastProbeTime`
  - **UpdateNode**
    - changes of response param
      - `+ status.lastProbeTime`
  - **DeleteNode**
    - changes of response param
      - `+ status.lastProbeTime`
  - **CreateNode**
    - changes of response param
      - `+ status.lastProbeTime`
  - **ListNodes**
    - changes of response param
      - `+ items.status.lastProbeTime`

### G42Cloud SDK CSE

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **DownloadKie**
    - changes of response param
      - `+ data.id`
  - **CreateEngine**
    - changes of response param
      - `+ jobId`
      - `- job_id`
  - **DeleteEngine**
    - changes of response param
      - `+ jobId`
      - `- job_id`

### G42Cloud SDK ECS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **CreateServers**
    - changes of request param
      - `+ server.data_volumes.delete_on_termination`
  - **CreatePostPaidServers**
    - changes of request param
      - `+ server.data_volumes.delete_on_termination`

### G42Cloud SDK SMN

- _Features_
  - Support the following interfaces：
    - `UpdateSubscription`
    - `ListLogtank`
    - `CreateLogtank`
    - `UpdateLogtank`
    - `DeleteLogtank`
- _Bug Fix_
  - None
- _Change_
  - **ListTopicDetails**
    - changes of response param
      - `+ topic_id`
  - **ListTopics**
    - changes of request param
      - `+ topic_id`
    - changes of response param
      - `+ topics.topic_id`
  - **ListTopicAttributes**
    - changes of response param
      - `+ attributes.access_policy`
      - `+ attributes.introduction`
      - `- attributes.Version`
      - `- attributes.Id`
      - `- attributes.Statement`
  - **AddSubscription**
    - changes of request param
      - `+ extension`

# 0.0.6-beta 2023-05-12

### G42Cloud SDK CBR

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Remove the following interfaces：
    - `CopyCheckpoint`
    - `MigrateVaultResource`
    - `ImportBackup`
    - `CopyBackup`
    - `ShowReplicationCapabilities`
  - **ShowVaultResourceInstances**
    - changes of response param
      - `* resources.resource_detail: list<Vault> -> object<InstancesResourceDetail>`
  - **ShowBackup**
    - changes of response param
      - `- backup.image_type: enum value [backup,replication]`
      - `- backup.resource_type: enum value [OS::Nova::Server,OS::Cinder::Volume]`
  - **ListBackups**
    - changes of request param
      - `+ incremental`
      - `+ image_type: enum value [backup,replication]`
      - `+ resource_type: enum value [OS::Cinder::Volume,OS::Nova::Server]`
    - changes of response param
      - `- backups.image_type: enum value [backup,replication]`
      - `- backups.resource_type: enum value [OS::Nova::Server,OS::Cinder::Volume]`
  - **ListPolicies**
    - changes of response param
      - `- policies.operation_type: enum value [replication]`
  - **CreatePolicy**
    - changes of request param
      - `- policy.operation_type: enum value [backup,replication]`
    - changes of response param
      - `- policy.operation_type: enum value [replication]`
  - **ShowPolicy**
    - changes of response param
      - `- policy.operation_type: enum value [replication]`
  - **UpdatePolicy**
    - changes of response param
      - `- policy.operation_type: enum value [replication]`
  - **ListVault**
    - changes of request param
      - `+ cloud_type: enum value [public,hybrid]`
      - `+ protect_type: enum value [backup,replication]`
    - changes of response param
      - `- vaults.billing.charging_mode: enum value [pre_paid,post_paid]`
      - `- vaults.billing.cloud_type: enum value [public,hybrid]`
      - `- vaults.billing.consistent_level: enum value [app_consistent,crash_consistent]`
      - `- vaults.billing.object_type: enum value [server,disk]`
      - `- vaults.billing.protect_type: enum value [backup,replication,hybrid]`
      - `- vaults.billing.spec_code: enum value [vault.backup.server.normal,vault.backup.volume.normal]`
      - `* vaults.bind_rules.tags: list<Tag> -> list<BindRulesTags>`
  - **CreateVault**
    - changes of request param
      - `* vault.bind_rules.tags: list<Tag> -> list<BindRulesTags>`
      - `+ vault.billing.promotion_info`
      - `+ vault.billing.purchase_mode`
      - `+ vault.billing.order_id`
      - `- vault.billing.cloud_type: enum value [public,hybrid]`
      - `- vault.billing.consistent_level: enum value [app_consistent,crash_consistent]`
      - `- vault.billing.object_type: enum value [server,disk,turbo]`
      - `- vault.billing.protect_type: enum value [backup,replication]`
      - `- vault.billing.charging_mode: enum value [post_paid,pre_paid]`
    - changes of response param
      - `- vault.billing.charging_mode: enum value [pre_paid,post_paid]`
      - `- vault.billing.cloud_type: enum value [public,hybrid]`
      - `- vault.billing.consistent_level: enum value [app_consistent,crash_consistent]`
      - `- vault.billing.object_type: enum value [server,disk]`
      - `- vault.billing.protect_type: enum value [backup,replication,hybrid]`
      - `- vault.billing.spec_code: enum value [vault.backup.server.normal,vault.backup.volume.normal]`
      - `* vault.bind_rules.tags: list<Tag> -> list<BindRulesTags>`
  - **ShowVault**
    - changes of response param
      - `- vault.billing.charging_mode: enum value [pre_paid,post_paid]`
      - `- vault.billing.cloud_type: enum value [public,hybrid]`
      - `- vault.billing.consistent_level: enum value [app_consistent,crash_consistent]`
      - `- vault.billing.object_type: enum value [server,disk]`
      - `- vault.billing.protect_type: enum value [backup,replication,hybrid]`
      - `- vault.billing.spec_code: enum value [vault.backup.server.normal,vault.backup.volume.normal]`
      - `* vault.bind_rules.tags: list<Tag> -> list<BindRulesTags>`
  - **UpdateVault**
    - changes of request param
      - `* vault.bind_rules.tags: list<Tag> -> list<BindRulesTags>`
    - changes of response param
      - `- vault.billing.charging_mode: enum value [pre_paid,post_paid]`
      - `- vault.billing.cloud_type: enum value [public,hybrid]`
      - `- vault.billing.consistent_level: enum value [app_consistent,crash_consistent]`
      - `- vault.billing.object_type: enum value [server,disk]`
      - `- vault.billing.protect_type: enum value [backup,replication,hybrid]`
      - `- vault.billing.spec_code: enum value [vault.backup.server.normal,vault.backup.volume.normal]`
      - `* vault.bind_rules.tags: list<Tag> -> list<BindRulesTags>`
  - **ListProtectable**
    - changes of response param
      - `- instances.protectable.vault.billing.charging_mode: enum value [pre_paid,post_paid]`
      - `- instances.protectable.vault.billing.cloud_type: enum value [public,hybrid]`
      - `- instances.protectable.vault.billing.consistent_level: enum value [app_consistent,crash_consistent]`
      - `- instances.protectable.vault.billing.object_type: enum value [server,disk]`
      - `- instances.protectable.vault.billing.protect_type: enum value [backup,replication,hybrid]`
      - `- instances.protectable.vault.billing.spec_code: enum value [vault.backup.server.normal,vault.backup.volume.normal]`
      - `+ instances.protectable.vault.tags.value`
      - `- instances.protectable.vault.tags.values`
      - `* instances.protectable.vault.tags: list<TagsResp> -> list<Tag>`
      - `* instances.protectable.vault.bind_rules.tags: list<Tag> -> list<BindRulesTags>`
  - **ShowProtectable**
    - changes of response param
      - `- instance.protectable.vault.billing.charging_mode: enum value [pre_paid,post_paid]`
      - `- instance.protectable.vault.billing.cloud_type: enum value [public,hybrid]`
      - `- instance.protectable.vault.billing.consistent_level: enum value [app_consistent,crash_consistent]`
      - `- instance.protectable.vault.billing.object_type: enum value [server,disk]`
      - `- instance.protectable.vault.billing.protect_type: enum value [backup,replication,hybrid]`
      - `- instance.protectable.vault.billing.spec_code: enum value [vault.backup.server.normal,vault.backup.volume.normal]`
      - `+ instance.protectable.vault.tags.value`
      - `- instance.protectable.vault.tags.values`
      - `* instance.protectable.vault.tags: list<TagsResp> -> list<Tag>`
      - `* instance.protectable.vault.bind_rules.tags: list<Tag> -> list<BindRulesTags>`

### G42Cloud SDK ECS

- _Features_
  - Support the interface `NovaAttachInterface`
- _Bug Fix_
  - None
- _Change_
  - None

### G42Cloud SDK IMS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ListImages**
    - changes of request param
      - `+ __imagetype: enum value [market]`

### G42Cloud SDK RDS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - **ListRestoreTimes**
    - changes of response param
      - `* restore_time.start_time: int32 -> int64`
      - `* restore_time.end_time: int32 -> int64`
  - **ListOffSiteRestoreTimes**
    - changes of response param
      - `* restore_time.start_time: int32 -> int64`
      - `* restore_time.end_time: int32 -> int64`
  - **RestoreToExistingInstance**
    - changes of request param
      - `* source.restore_time: int32 -> int64`
  - **RestoreExistInstance**
    - changes of request param
      - `* source.restore_time: int32 -> int64`
  - **CreateInstance**
    - changes of request param
      - `* restore_point.restore_time: int32 -> int64`
    - changes of response param
      - `* instance.restore_point.restore_time: int32 -> int64`
  - **CreateRestoreInstance**
    - changes of request param
      - `* restore_point.restore_time: int32 -> int64`
    - changes of response param
      - `* instance.restore_point.restore_time: int32 -> int64`

# 0.0.5-beta 2023-04-14

### G42Cloud SDK Core

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Optimize the code structure.

# 0.0.4-beta 2023-02-20

### G42Cloud SDK CBR

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - The request parameter `policy_id` changed to required of the interface `AssociateVaultPolicy`

### G42Cloud SDK IMS

- _Features_
  - None
- _Bug Fix_
  - None
- _Change_
  - Add the enum values `IsoImage` to the request parameter `type` to the interface `CreateImage`

# 0.0.3-beta 2023-01-06

### G42Cloud SDK IMS

- _Features_
  - New Support IMS
- _Bug Fix_
  - None
- _Change_
  - None

### G42Cloud SDK SMN

- _Features_
  - New Support SMN
- _Bug Fix_
  - None
- _Change_
  - None

# 0.0.2-beta 2022-11-29

### G42Cloud SDK CBR

- _Features_
  - New Support CBR
- _Bug Fix_
  - None
- _Change_
  - None

### G42Cloud SDK CES

- _Features_
  - New Support CES
- _Bug Fix_
  - None
- _Change_
  - None

### G42Cloud SDK CSE

- _Features_
  - New Support CSE
- _Bug Fix_
  - None
- _Change_
  - None

### G42Cloud SDK CTS

- _Features_
  - New Support CTS
- _Bug Fix_
  - None
- _Change_
  - None

### G42Cloud SDK ELB

- _Features_
  - New Support ELB
- _Bug Fix_
  - None
- _Change_
  - None

# 0.0.1-beta 2022-11-23

### G42Cloud SDK CCE

- _Features_
  - New Support CCE
- _Bug Fix_
  - None
- _Change_
  - None

### G42Cloud SDK CDN

- _Features_
  - New Support CDN
- _Bug Fix_
  - None
- _Change_
  - None

### G42Cloud SDK ECS

- _Features_
  - New Support ECS
- _Bug Fix_
  - None
- _Change_
  - None

### G42Cloud SDK EVS

- _Features_
  - New Support EVS
- _Bug Fix_
  - None
- _Change_
  - None

### G42Cloud SDK RDS

- _Features_
  - New Support RDS
- _Bug Fix_
  - None
- _Change_
  - None

### G42Cloud SDK VPC

- _Features_
  - New Support VPC
- _Bug Fix_
  - None
- _Change_
  - None
