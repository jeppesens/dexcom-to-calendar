# BG Calendar

---

## Structure
- Get values from Dexcom
- Publishes it to the calendar
- Calendar client pulls the info

---

## Setup in Heroku
1. Create an app
2. Add this github repo (or a fork)
3. Add the buildpacks
```
https://github.com/moneymeets/python-poetry-buildpack.git
heroku/python
```
4. Add your credentials in the env to the keys
```
DEXCOM_USERNAME
DEXCOM_PASSWORD
```
5. If you are in the US set the env DEXCOM_OUTSIDE_US=false
6. Choose username and password in the envs, this will be used for the calendar
```
CALDAV_USER
CALDAV_PASSWORD
```
7. Login to the caldav account on your device

---
