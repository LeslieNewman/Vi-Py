#!/bin/tcsh

#
# setup the environment to kick off node.js vision-dbms connector and webserver
#

setenv VisionNodeServeRoot $VisionRoot/vision-xa-nodejs-serve
setenv vision_xa_nodejs_serve_http_port 10000
setenv VxaICE 1

#----  Possible settings for logging
#setenv TracingDevices true
#setenv VcaDeviceLog $HOME/node.log
#setenv vision_xa_nodejs_serve_vision_api_logging DOIT

# run node.js vision-dbsm/connect and express.js server
setenv VcaSessionsFile $YOUR_AREA/sessions.cfg
setenv VisionStartExpr ' "$YOUR_AREA/order.vis" asFileContents evaluate'
cd $VisionNodeServeRoot
node index &

#--- let's try priming the pump
echo "... Pausing"
sleep 5
echo "... Accessing"
curl '$YOUR_IP_ADDRESS:10000/vision/api?expression=AdminTools+totalNetworkAllocation+printWithCommasNL:18.0;'
