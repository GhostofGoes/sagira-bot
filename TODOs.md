# TODOs

## Features
- Add ability for posts to be edited by others than the original author
    - Restrict editing by roles (this would be a field in the post creation Modal)
    - If a edit is made by someone other than the original author, then add a new field, "Edited by", with the user who edited the post. If multiple people make edits, append them to this field.
- Note if a post has been edited, and maybe a timestamp of when the edit occurred?

## Development
- Implement Elasticsearch security
    - SSL certificates for Elasticsearch, Kibana, and Beats
    - Enable security for Elasticsearch, Kibana, and Beats
- Filebeat
    - Collect bot logs using Filebeat
    - Collect Elasticsearch and Kibana logs using Filebeat
- Metricbeat
- Configurable memory limits for Elastic+Kibana in production
- Add HEALTHCHECK for bot Docker container
