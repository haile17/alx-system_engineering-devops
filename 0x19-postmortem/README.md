# service outage

## Issue summary:

-  The duration of the outage started September 5, 2022 at 7:00pm Localtime and ended at September 8, 2022 at 4:00pm Localtime.
## The impact:
- on the server was that the servers stop responding new request after some user attempted to upload new images. 100% of users that were using the web-app during this time experienced this problem.
![ALt text](internet.png)
## The root cause:
- was the server was very busy uploading images to google storage and could not server the request to made by users.
## Timeline:

-    2022 September 6 at 9:00am Localtime: The issue detected.
-    2022 September 6 at 9:00pm Localtime: The issue was detected when monitoring response times.
-    2022 September 5 at 9:15pm Localtime: The actions taken were blocked the option that allow users to uploaded images until service was fixed.
-    2022 September 5 at 9:30pm Localtime: There were some manually run to check if this was the real problem.
-    2022 September 5 at 11:00pm Localtime: The incident escalated to the CTO.
-    2022 September 8 at 4:00pm Localtime: The incident was resolved moving the image uploading service to the front-end.

### Root cause and resolution:

-   The issue was caused when user uploaded an image. There weren't any background job to to this task. So server had to upload the image to Google storage and expect a successful outcome in order to respond to client and serve next page causing to exceed server time response.
-  The issue was fixed moving the uploading image logic to front-end using JavaScript. So now the front end crop image and upload the image to google storage but return URL to server for db storage.

### Corrective and preventative measures:

-    When working with image processing and uploading is always better to run this process in front/client side and if it is not possible create a background job that can handle this process.
-   A list of tasks to address the issue: Always monitor response times, move the most amount of logic to front-end, use background jobs to control logic on back-end when long processes need to be run.
![alt text](back.png)