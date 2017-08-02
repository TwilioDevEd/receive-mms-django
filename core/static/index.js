var POLL_INTERVAL = 3000;

function ReceiveMMSController(){
  function showEnvVarUnsetWarning() {
    alert('Please be sure to set your environment variables. Similar to those found in the .env file in the root of this repository.');
  }

  function init() {
    return $.get('/config')
      .then(function(res){
        if (!res.twilioPhoneNumber) {
            return showEnvVarUnsetWarning();
        }

        var phoneNumber = res.twilioPhoneNumber.replace(/(\+\d{1})(\d{3})(\d{3})(\d{4})/, '$1($2)-$3-$4')
        $('.twilio-number').html(phoneNumber);

        pollForIncomingImages();
      })
  }

  function showImages() {
    $.get('/images').then(function(images) {
      $('.image-container').append(images.data.map(function(filename) {
        return '<img width="100%" class="col-md-4" src="/images/' + filename + '"/>';
      }).join(''));
    });
  }

  function pollForIncomingImages() {
    setInterval(showImages, POLL_INTERVAL);
  }

  return {
    init: init,
  }
}

$(document).ready(function(){
  var receiveMMSController = ReceiveMMSController();
  receiveMMSController.init();
});
