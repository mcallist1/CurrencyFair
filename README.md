For demonstration purposes a loader script is used to load a bunch of historical data from kaggle for the graph, which has only been parameterised against GBP.

In practice, we'd need to set up a cron job, that examines all the data that was added to the system from the app endpoint. Then then summarises that into a daily price.

Since actual lifetime of the project is very short, the cron job was not implemented (the cron job wouldn't have the time to run. If required how this is done can be demonstrated on request)

The display of the content that we get from ajax has been sanitised because the data comes from external sources. So we escaping the html tags. And you will see some of that in the sample data.

Deployed on digital ocean using apache and flask. 

end point for getting the raw message data 
http://138.197.178.59/message

end point for retrieving processed data for graphing
http://138.197.178.59/graph-data

front end for processed display
http://138.197.178.59/graph

end point for posting.
http://138.197.178.59/message

(two separate functions for handing GET and POST in the app.)