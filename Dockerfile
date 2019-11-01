FROM python:3.7.3

RUN pip install requests; \
    groupadd -r rescale && useradd -r -g rescale rescale; \
    mkdir /home/rescale; \
    chown rescale /home/rescale; \
    chgrp rescale /home/rescale

ENV RESCALE_PLATFORM="platform.rescale.com"

USER rescale
WORKDIR /home/rescale

ADD airfoil2D_DOE.zip /home/rescale/
ADD doe_job_config.json /home/rescale/
ADD freestreamvalue.csv /home/rescale/
ADD submit_doe_job.py /home/rescale/
ADD utemplate /home/rescale/

CMD ["python","submit_doe_job.py"]
