# rescale-doe-api
Example of submitting Rescale Design of Experiments (DOE) job with REST API

## Usage
Clone this repository, and build the image
```bash
$ git clone git@github.com:TakahisaShiratori/rescale-doe-api.git
$ cd rescale-doe-api/
$ docker build -t rescale-doe-api .
```

RESCALE_API_KEY is required environmental variable to run the built image.
```bash
$ docker run \
> -e RESCALE_API_KEY=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX \
> rescale-doe-api
```

Use RESCALE_PLATFORM to specify platform. For example, Japan platform can be used by
```bash
$ docker run \
> -e RESCALE_PLATFORM=platform.rescale.jp \
> -e RESCALE_API_KEY=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX \
> rescale-doe-api
```

By default, RESCALE_PLATFORM is platform.rescale.com
