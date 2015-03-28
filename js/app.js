var webhookUrl = "https://hooks.slack.com/services/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"


var main = function() {

  $( "#notify-button" ).click(function() {
    var location = $("input[name='radioLocation']:checked").val();
    var channel = $( "#input-channel" ).val();
    var username = $( "#input-username" ).val();


    notifySlack(channel, username, location);
  });

};


var notifySlack = function(channel, username, location) {
  console.log("channel = " + channel);
  console.log("username = " + username);
  console.log("location = " + location)

}

$(document).ready(main);
