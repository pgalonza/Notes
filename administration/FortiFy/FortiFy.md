# FortiFy

Scanning the project
```
sourceanaluzer -b <build id> -clean
sourceanaluzer -b <build id> <build_command>
sourceanaluzer -b -scan -f <file_name>.fpr
```

Converting FPR to PDF
```
ReportGenerator -format pdf -source <file_name>.fpr -f <file_name>.pdf -template <template_name>
```

Upload FPR to SSC
```
fortifyclient -url <scc url> -authtoken <upload_derctypted_token> -file <file_name>.fpr -application <application_name> -applicationVersion <application_version>
```

Limiting resource consumption

* nice -n <priority_number> - set priority of proccess
* -Xmx<size_number>G - set maximum RAM size
* com.fortify.sca.ThreadCount - set number of threads
