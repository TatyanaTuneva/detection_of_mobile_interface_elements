image_upload_wrap = $('.image-upload-wrap')
file_upload_input = $('.file-upload-input')
file_upload_image = $('.file-upload-image')
predict_image = $('.predict-image')
time = $('.time')
let image_file = 123;
let start

function readURL(input) {
  if (input.files && input.files[0]) {
    start = new Date().getTime();
    var reader = new FileReader();

    reader.onload = function(e) {
      image_upload_wrap.hide();

      image_file = input.files[0];

      file_upload_image.attr('src', e.target.result);

      file_upload_image.show();
      let url = 'http://127.0.0.1:8000/get_prediction/'
      var form_data = new FormData();
      form_data.append('image', image_file)

      fetch(url, {
        method: 'POST',
        body: form_data,
      }).then((response) => {
        return response;
      }).then((data) => {handleResult(data);})

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

  let prediction_time = new Date().getTime() - start;
  time.text(prediction_time + ' ms')
}
