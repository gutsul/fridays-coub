# Friday's coub v1.0

`coub` is tool that publish coubs to slack channel from a own coubs library.


## Installation  

`coub` tool need installed **python 3** and run with **root** permissions.

### Install Python
```bash
sudo apt-get install python3-pip
```


### Install coub tool

```bash
# Clone tool to `/usr/src/gcloud-resize` folder
sudo git clone https://github.com/gutsul/fridays-coub.git /usr/src/fridays-coub

# Go to gcloud-resize folder 
cd /usr/src/fridays-coub

# Install dependencies
sudo pip3 install -r requirements.txt

# Create symbol link
sudo ln -s /usr/src/fridays-coub/coub /usr/local/bin/

```

### Configure environment

Create `.env` file from sample `.env.sample` and set [settings](#settings).

```
# Go to gcloud-resize folder 
cd /usr/src/fridays-coub

# Copy sample
sudo cp .env.sample .env
```

### Crontab
Configure how often need to check disks.
```bash
# Edit root crontab:
sudo crontab -e

# Add lines below to end of file:

# Publish coub at 17:55 of Friday
55 17 * * 5 /usr/src/fridays-coub/coub publish 
```

## Settings

Location `/usr/src/gcloud-resize/.env`

| Key                  | Type    | Value Example                          | Description |
| :------------------- | :-----: | -------------------------------------- | ----------- |
| `SLACK_WEBHOOK`      | String  | 'https://hooks.slack.com/'             | **Required**. Slack incoming webhook url.  |
| `DATA_FOLDER`        | String  | '/usr/src/fridays-coub/data/'          | **Required**. Full path to data folder.    |
