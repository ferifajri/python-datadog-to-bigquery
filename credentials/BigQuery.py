def BQ_json():
    # Put Your Google JSON credential file path here ex:  "/home/work/myjsonfile.json"  "
    json_path = "C:\Code\Datadog\\venv\\billing-production-infra-29ba-02abdd9608dc.json"
    # put your service_account here : myserviceaccountt@domain.iam.gserviceaccount.com
    service_account = "csv-import@billing-production-infra-29ba.iam.gserviceaccount.com"
    # put your Project_ID here
    project_id = "billing-production-infra-29ba"
    return json_path, service_account, project_id
