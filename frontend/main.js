image_upload_wrap = $('.image-upload-wrap')
file_upload_input = $('.file-upload-input')
file_upload_image = $('.file-upload-image')
file_prediction_time = $('.file-prediction-time')
predict_image = $('.predict-image')
time = $('.time')
let image_file = 123;
let server_url = 'http://127.0.0.1:8000'

function readURL(input) {
  if (input.files && input.files[0]) {
    var reader = new FileReader();

    reader.onload = function(e) {
      image_upload_wrap.hide();

      image_file = input.files[0];

      file_upload_image.attr('src', e.target.result);

      file_upload_image.show();
      let url = server_url + '/get_prediction/'
      var form_data = new FormData();
      form_data.append('image', image_file)

      fetch(url, {
        method: 'POST',
        body: form_data,
      }).then((response) => {
        return response;
      }).then((data) => {handleResult(data);}).then(() => {get_time();})

    };

    reader.readAsDataURL(input.files[0]);

  }
}

async function handleResult(data) {

  var imageBlob = await data.blob();

  let reader = new FileReader();
  reader.onload = function (e) {
    predict_image.attr('src', e.target.result);
    predict_image.show();
  }
  reader.readAsDataURL(imageBlob);
}


async function get_time() {
  let url = server_url + '/get_time/'
  fetch(url, {
        method: 'GET'
      }).then((response) => {
        return response.json();
      }).then((data) => {handleTime(data);})
}

async function handleTime(data) {
  let prediction_time = data['time'];
  time.text(prediction_time + ' ms')
}