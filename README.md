# The Hive analysis ~420 second analysis failure
This is a known issue [Issue #1156](https://github.com/TheHive-Project/TheHive/issues/1156)

When an Analyzer takes longer than ~420 seconds to complete The Hive fails to fetch the results producing the following error in the ```application.log```

```
[ERROR] from connectors.cortex.services.CortexAnalyzerSrv in application-akka.actor.default-dispatcher-18 - Request of status of job AW9sr4VYP6SxSXN1erTd in cortex LOCAL CORTEX fails and the number of errors reaches the limit, aborting
```

## The Hive UI Error
The UI shows an error:
![The Hive UI error](/Images/the_hive_failure.png)

## Cortex
The raw report etc... is availble in Cortex with a job Status of ```Success```

## Cortex Job Success
![The Hive UI error](/Images/cortex_success.png)
