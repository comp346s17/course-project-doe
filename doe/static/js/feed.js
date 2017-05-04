$(document).ready(function() {
  $('.profile_score').each(function() {
    value = $(this).html();
    console.log(value);
  });

  $('.score').each(function() {
    value = $(this).html();
    console.log(value);
    value = parseInt(value);
    if(value > 10) {
      value = Math.abs(10 - value);
    }
    value = value * 10;
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
