// console.log('Hello From JS');
$(document).ready(function(){
    $('.input_output_container').css('display', 'none');
    $('#uploadBttn').on('click', function(e){
        e.preventDefault();
        var fileInput = document.getElementById('fileInput');
        var file = fileInput.files[0];

        // Check if a file is selected
        if (!file) {
            $('.error_msg').removeClass('d-none');
            setTimeout(function () {
                $('.error_msg').addClass('d-none');
            }, 5000);
            return;
        }

        // Display the selected image temporarily
        displayTempImage(file);
    
        var formData = new FormData();
        formData.append('file', file);

        $.ajax({
            type: 'POST',
            url: '/',
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                // console.log(response.prediction);
                displayResult(response.prediction);
                // If you want to permanently display the uploaded image after saving it,
                // you can call the displayImage function here with the file path.
                // displayImage(response.file_path);
            },
            error: function(error) {
                console.log(error);
                // Handle error scenarios
            }
        });
    });
});

function displayTempImage(file) {
    // Read the file and convert it to a data URL
    var reader = new FileReader();
    reader.onload = function (e) {
        // Update the src attribute of an image element to display the uploaded image temporarily
        $('#uploadedImage').attr('src', e.target.result);
        $('.input_output_container').css('display', 'block');
    };
    reader.readAsDataURL(file);
}

function displayResult(prediction) {
    var resultContainer = $('.result');
    resultContainer.html('<h1 class=outputText>' + prediction + '</h1>');
}