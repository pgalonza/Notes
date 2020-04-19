# New installation
## BigBlueButton
Requirements
* Ubuntu 16.04 64-bit OS running Linux kernel 4.x
* TCP ports 80 and 443 are accessible
* UDP ports 16384 - 32768 are accessible
* Dedicated (bare metal) hardware

Install entr daemon for VM
```
apt-get install haveged
```

Add repository for ffmpeg and yq
```
add-apt-repository ppa:jonathonf/ffmpeg-4 -y
add-apt-repository ppa:rmescandon/yq -y
```

Install MongoDB
```
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 0C49F3730359A14518585931BC711F9BA15703C6
echo "deb [ arch=amd64,arm64 ] http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.4.list
sudo apt-get update
$ sudo apt-get install -y mongodb-org curl
```

Install NodeJS
```
curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -
sudo apt-get install -y nodejs
```

Repository key
```
wget https://ubuntu.bigbluebutton.org/repo/bigbluebutton.asc -O- | sudo apt-key add -
```

Bigbluebutton repository
```
echo "deb https://ubuntu.bigbluebutton.org/xenial-220/ bigbluebutton-xenial main" | sudo tee /etc/apt/sources.list.d/bigbluebutton.list
```

Install bigbluebutton
```
apt-get install bigbluebutton
apt-get install bbb-html5
```

Enable HTML5 client and disable SWF
_/usr/share/bbb-web/WEB-INF/classes/bigbluebutton.properties_
```
attendeesJoinViaHTML5Client=true
moderatorsJoinViaHTML5Client=true
swfSlidesRequired=false
```

Set the hostname
```
bbb-conf --setip server_hostname
```

Check installation
```
bbb-conf --check
bbb-conf --status
```

## Greenlight
### Install docker
Packages to use a repository over HTTPS
```
apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common
```

Add GPG key
```
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```

Add repository
```
add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
```

Install
```
apt-get update
apt-get install docker-ce docker-ce-cli containerd.io
```

### Install docker-compose
Get stable release
```
sudo curl -L "https://github.com/docker/compose/releases/download/1.24.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```

Make executable
```
chmod +x /usr/local/bin/docker-compose
```

Symlink
```
ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
```


### Install web-application
Create directory
```
mkdir ~/greenlight && cd ~/greenlight
```

Generate the environment file
```
docker run --rm bigbluebutton/greenlight:v2 cat ./sample.env > .env
```

Get compose file
```
docker run --rm bigbluebutton/greenlight:v2 cat ./docker-compose.yml > docker-compose.yml
```

### Install web-application for customization
Clone repository
```
git clone https://github.com/bigbluebutton/greenlight.git
```

Add remote repository
```
git remote add upstream https://github.com/bigbluebutton/greenlight.git
```

Fetch to upstream
```
git fetch upstream
```

Create new branch base off release 2.4-b2
```
git checkout -b release-2.4-b2
```

Copy docker compose file
```
cp docker-compose.yml docker-compose.yml.default
```

Edit the compose file and set new name
_docker-compose.yml_
```
image: image_name/greenlight:release-v2
```

Add certificate in container
_Dockerfile_
```
# Adding certificate
COPY ./name-CA.crt /usr/local/share/ca-certificates/
RUN update-ca-certificates
```

Build the image
```
./scripts/image_build.sh image_name/greenlight release-v2
```

### Settings
Get the secret key
```
docker run --rm bigbluebutton/greenlight:v2 bundle exec rake secret
```

Set the secret key
_greenlight/.env_
```
SECRET_KEY_BASE=secret
```

Get the secret
```
bbb-conf --secret
```

Set the secret
_greenlight/.env_
```
BIGBLUEBUTTON_ENDPOINT=url
BIGBLUEBUTTON_SECRET=secret
```

Verifying configuration
```
docker run --rm --env-file .env bigbluebutton/greenlight:v2 bundle exec rake conf:check
```

Nginx configuration file
```
docker run --rm bigbluebutton/greenlight:v2 cat ./greenlight.nginx | sudo tee /etc/bigbluebutton/nginx/greenlight.nginx
systemctl restart nginx
```

Run
```
docker-compose up -d
```

Stop
```
docker-compose down
```

### SSL
#### Nginx
Make dir
```
mkdir /etc/nginx/ssl
```

Create file for key and certificate
```
touch /etc/nginx/ssl/server_hostname.key
touch /etc/nginx/ssl/server_hostname.crt
```

Diffie Hellman certificate
```
openssl dhparam -out /etc/nginx/ssl/dhp-2048/4096.pem 2048/4096
```

Nginx configuration file
_/etc/nginx/sites-available/bigbluebutton_
```
listen 443 ssl;
  listen [::]:443 ssl;

  ssl_certificate /etc/nginx/ssl/server_hostname.crt;
  ssl_certificate_key /etc/nginx/ssl/server_hostname.key;
  ssl_session_cache shared:SSL:10m;
  ssl_session_timeout 10m;
  ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
  ssl_ciphers "ECDH+AESGCM:DH+AESGCM:ECDH+AES256:DH+AES256:ECDH+AES128:DH+AES:ECDH+3DES:DH+3DES:RSA+AESGCM:RSA+AES:RSA+3DES:!aNULL:!MD5:!DSS:!AES256";
  ssl_prefer_server_ciphers on;
  ssl_dhparam /etc/nginx/ssl/dhp-2048.pem;
```

#### FreeSWITCH
_/etc/bigbluebutton/nginx/sip.nginx_
```
proxy_pass https://203.0.113.1:7443;  
```

#### BigBlueButton session
HTTPS for initiating an audio connection
_/usr/share/bbb-web/WEB-INF/classes/bigbluebutton.properties_
```
bigbluebutton.web.serverURL=https://server_hostname
```

_/usr/share/red5/webapps/screenshare/WEB-INF/screenshare.properties_
```
jnlpUrl=https://server_hostname/screenshare
jnlpFile=https://server_hostname/screenshare/screenshare.jnlp
```

Load components via HTTPS
```
sed -e 's|http://|https://|g' -i /var/www/bigbluebutton/client/conf/config.xml
```

_/usr/share/meteor/bundle/programs/server/assets/app/config/settings.yml_
```
wsUrl: wss://server_hostname/bbb-webrtc-sfu
url: https://server_hostname/pad
```

_/usr/local/bigbluebutton/core/scripts/bigbluebutton.yml_
```
playback_protocol: https
```

## Coturn
Install coturn
```
apt-get install coturn
```

Generate random key
```
openssl rand -hex 16
```

Configue coturn
_/etc/turnserver.conf_
```
listening-port=3478
tls-listening-port=443
fingerprint
lt-cred-mech
use-auth-secret
static-auth-secret=<random value>
realm=example.com
cert=fullchain.key
pkey=privkey.pem
cipher-list="ECDH+AESGCM:ECDH+CHACHA20:DH+AESGCM:ECDH+AES256:DH+AES256:ECDH+AES128:DH+AES:RSA+AESGCM:RSA+AES:!aNULL:!MD5:!DSS"
dh2066
no-tlsv1
no-tlsv1_1
log-file=/var/log/coturn.log
```

Log rotation
```
/var/log/coturn.log
{
    rotate 30
    daily
    missingok
    notifempty
    delaycompress
    compress
    postrotate
    systemctl kill -sHUP coturn.service
    endscript
}
```

Make enable
_/etc/default/coturn_
```
TURNSERVER_ENABLED=1
```

Configue BigBlueButton
_/usr/share/bbb-web/WEB-INF/classes/spring/turn-stun-servers.xml_
```
<beans xmlns="http://www.springframework.org/schema/beans"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://www.springframework.org/schema/beans
            http://www.springframework.org/schema/beans/spring-beans-2.5.xsd
            ">

    <bean id="stun1" class="org.bigbluebutton.web.services.turn.StunServer">
        <constructor-arg index="0" value="stun:coturn1.example.com"/>
    </bean>

    <bean id="turn1" class="org.bigbluebutton.web.services.turn.TurnServer">
        <constructor-arg index="0" value="<random value>"/>
        <constructor-arg index="1" value="turns:coturn1.example.com:443?transport=tcp"/>
        <constructor-arg index="2" value="86400"/>
    </bean>

    <bean id="stunTurnService" class="org.bigbluebutton.web.services.turn.StunTurnService">
    <property name="stunServers">
        <set>
            <ref bean="stun1" />
            <!--ref bean="stun2" /-->
        </set>
    </property>
    <property name="turnServers">
        <set>
            <ref bean="turn1" />
            <!--ref bean="turn2" /-->
        </set>
    </property>
    <property name="remoteIceCandidates">
        <set>
            <!--ref bean="iceCandidate1" /-->
            <!--ref bean="iceCandidate2" /-->
        </set>
    </property>
</bean>
</beans>
```

## FreeSWITCH and FreePBX, add a phone number to the conference bridge
FreeSWITCH trunk
_/opt/freeswitch/conf/sip_profiles/freepbx.xml_
```
<include>
    <gateway name="asterisk">
      <param name="username" value="freepbx"/>
      <param name="password" value="register:false"/>
      <param name="proxy" value="ip_address"/>
      <param name="register" value="false"/>
      <param name="context" value="default"/>
      <param name="caller-id-in-from" value="true"/>
    </gateway>
</include>
```

FreePBX trunk
```
[FreeSwitch]
type=peer
host=ip_address
port=5060
disallow=all
allow=alaw,ulaw
qualify=yes
insecure=invite,port
context=from-trunk
```

FreeSWITCH dialplan
_/opt/freeswitch/conf/dialplan/public/freepbx.xml_
```
<extension name="freepbx">
 <condition field="destination_number" expression="^EXTERNALDID">
   <action application="answer"/>
   <action application="sleep" data="500"/>
   <action application="play_and_get_digits" data="5 5 3 7000 # conference/conf-pin.wav ivr/ivr-that_was_an_invalid_entry.wav pin \d+"/>
   <action application="transfer" data="SEND_TO_CONFERENCE XML public"/>
 </condition>
</extension>
<extension name="check_if_conference_active">
 <condition field="${conference ${pin} list}" expression="/sofia/g" />
 <condition field="destination_number" expression="^SEND_TO_CONFERENCE$">
   <action application="set" data="bbb_authorized=true"/>
   <action application="transfer" data="${pin} XML default"/>
 </condition>
</extension>
```

Set permission
```
chown freeswitch:daemon /opt/freeswitch/conf/dialplan/public/freepbx.xml
chown freeswitch:daemon /opt/freeswitch/conf/sip_profiles/freepbx.xml
```

Show number and pin in welcome message
_/usr/share/bbb-web/WEB-INF/classes/bigbluebutton.properties_
```
defaultDialAccessNumber=77998
defaultWelcomeMessage=%%DIALNUM%% %%CONFNUM%%
defaultWelcomeMessageFooter=%%DIALNUM%% %%CONFNUM%%
```

## Meteor NodeJS
### Problems
 Error parsing image size. Error: self signed certificate in certificate chain.
 _/usr/share/meteor/bundle/main.js_
 ```
 process.env['NODE_TLS_REJECT_UNAUTHORIZED'] = 0;
 ```
