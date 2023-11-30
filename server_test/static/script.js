// console.log('Hello From JS');
$(document).ready(function(){
    $('#uploadBttn').on('click', function(e){
        e.preventDefault();
        var file = $('fileInput').val();

        if(file){
            var formData = new formData();
            formData.append('file',file);

            fetch('/', {
                method: 'POST',
                body: file
            })
            .then(response => response.text())
            .then(message => {
                console.log(message);
            })
            .catch(error => {
                console.error('Error', error);
            });
        } else {
            console.log('No File Selected.');
        }
    });
});
