var main = function() {

  $( "#notify-button" ).click(function() {
    var location =  $("input[name='radioLocation']:checked").val();
    var channel =   $( "#input-channel" ).val();
    var username =  $( "#input-username" ).val();

    notifySlack(channel, username, location);
  });
};


var notifySlack = function(channel, username, location) {
  console.log("channel = " + channel);
  console.log("username = " + username);
  console.log("location = " + location);
  data = {"channel": channel,
          "location": location,
          "username": username
  };
  $.ajax({
    url:        "/_post_slack",
    data:       $('form').serialize(),
    type:       'POST',
    success:    slack_success,
    error:      slack_error
  });
}

var slack_success = function(response) {
    console.log("success!");
    console.log(response);

}

var slack_error = function(error) {
    console.log("error!");
    console.log(error);

}

$(document).ready(main);
