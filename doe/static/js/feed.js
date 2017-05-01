$(document).ready(function() {
  $('.score').each(function() {
    value = $(this).html();
    value = value/10000000000000;
    if(value>99) {
      value = value/10;
    }
    value = parseInt(value);
    style = "width: "+value+"%";
    console.log(value);
    $(this).attr("style",style);
    $(this).html("");
  });
});

$('.smackDat').click(function(e) {
  console.log("hit a button");
  console.log(alert("You smacked dat!"));
  username = e.target.id;
  console.log(username);
  $.ajax({
    url: '/ajax/ajax_like',
    data: {
      'username': username
    },
    dataType: 'json',
    success: function (data) {
      console.log("success")
    }
  })
});

$('.noThanks').click(function(e) {
  console.log("hit a button");
  console.log(alert("They're not for you."));
  username = e.target.id;
  console.log(username);
  $.ajax({
    url: '/ajax/ajax_dislike',
    data: {
      'username': username
    },
    dataType: 'json',
    success: function (data) {
      console.log("success")
    }
  })
});
