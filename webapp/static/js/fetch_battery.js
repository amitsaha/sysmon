/*Web worker responsible for fetching the
  battery stats*/

self.addEventListener('message', function(e) {

    /*Once we have the response, send it to the calling
     Javascript*/
    function send_data(request){
	var response = request.responseText;
	self.postMessage(response);
    }

    /* In a web worker, I cannot use jQuery, hence using
       XMLHttpRequest.
       Also, I am calling the API synchronously
       */
    function fetch_battery(){
	request = new XMLHttpRequest();
	/* TODO: Better way to do this? */
	request.open("GET", "http://" + location.host + "/battery", false);
	request.send(null);
	send_data(request);
    }

    /* This allows us to "push" the data every 2 minutes*/
    setInterval(function() {
	fetch_battery();
    },120000);}, false);
