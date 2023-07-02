

var fileUpload2 = document.querySelector('input[name="imagen_2"]')
var reader2 = new FileReader();
fileUpload2.addEventListener('change', () => {
  var extensionPermitida = /(\.jpg|\.jpeg|\.png)$/i;
  var file2 = fileUpload2.files[0];

  if (!extensionPermitida.exec(file2.name)) {
    alert('Tipo de archivo no válido. Solo se permiten archivos JPG, JPEG o PNG.');
    fileUpload2.value = '';
    return false;
  }

  reader2.readAsDataURL(file2);
  reader2.onload = (e) => {
    var image2 = new Image();
    image2.src = e.target.result;
    image2.onload = () => {

      var height2 = image2.height;
      var width2 = image2.width;
      console.log(height2 + " " + width2);
      
      if (width2 >= 0 && height2 >= 0) {
        if (height2 < 1080 || width2 < 720) {
          fileUpload2.value = '';
          alert("La resolución mínima de la imagen debe ser 1080x720.");
          return false;
        }
        alert("Imagen aceptada!");
        return true;
      } else {
        alert('El archivo seleccionado no es una imagen.');
        fileUpload2.value = '';
        return false;
      }
    };
  };
});



var fileUpload4 = document.querySelector('input[name="imagen_4"]')
var reader4 = new FileReader();
fileUpload4.addEventListener('change', () => {
  var extensionPermitida = /(\.jpg|\.jpeg|\.png)$/i;
  var file4 = fileUpload4.files[0];

  if (!extensionPermitida.exec(file4.name)) {
    alert('Tipo de archivo no válido. Solo se permiten archivos JPG, JPEG o PNG.');
    fileUpload4.value = '';
    return false;
  }

  reader4.readAsDataURL(file4);
  reader4.onload = (e) => {
    var image4 = new Image();
    image4.src = e.target.result;
    image4.onload = () => {

      var height4 = image4.height;
      var width4 = image4.width;
      console.log(height4 + " " + width4);
      
      if (width4 >= 0 && height4 >= 0) {
        if (height4 < 1080 || width4 < 720) {
          fileUpload4.value = '';
          alert("La resolución mínima de la imagen debe ser 1080x720.");
          return false;
        }
        alert("Imagen aceptada!");
        return true;
      } else {
        alert('El archivo seleccionado no es una imagen.');
        fileUpload4.value = '';
        return false;
      }
    };
  };
});

  

var fileUpload3 = document.querySelector('input[name="imagen_3"]')
var reader3 = new FileReader();
fileUpload3.addEventListener('change', () => {
  var extensionPermitida = /(\.jpg|\.jpeg|\.png)$/i;
  var file3 = fileUpload3.files[0];

  if (!extensionPermitida.exec(file3.name)) {
    alert('Tipo de archivo no válido. Solo se permiten archivos JPG, JPEG o PNG.');
    fileUpload3.value = '';
    return false;
  }

  reader3.readAsDataURL(file3);
  reader3.onload = (e) => {
    var image3 = new Image();
    image3.src = e.target.result;
    image3.onload = () => {

      var height3 = image3.height;
      var width3 = image3.width;
      console.log(height3 + " " + width3);

      if (width3 >= 0 && height3 >= 0) {
        if (height3 < 1080 || width3 < 720) {
          fileUpload3.value = '';
          alert("La resolución mínima de la imagen debe ser 1080x720.");
          return false;
        }
        alert("Imagen aceptada!");
        return true;
      } else {
        alert('El archivo seleccionado no es una imagen.');
        fileUpload3.value = '';
        return false;
      }
    };
  };
});


  var fileUpload1 = document.querySelector('input[name="imagen_1"]')
  var reader1 = new FileReader();
  fileUpload1.addEventListener('change', () => {
    var extensionPermitida = /(\.jpg|\.jpeg|\.png)$/i;
    var file = fileUpload1.files[0];

    if (!extensionPermitida.exec(file.name)) {
      alert('Tipo de archivo no válido. Solo se permiten archivos JPG, JPEG o PNG.');
      fileUpload1.value = '';
      return false;
    }

    reader1.readAsDataURL(file);
    reader1.onload = (e) => {
      var image1 = new Image();
      image1.src = e.target.result;
      image1.onload = () => {

        var height1 = image1.height;
        var width1 = image1.width;
        console.log(height1 + " " + width1);

        if (width1 >= 0 && height1 >= 0) {
          if (height1 < 1080 || width1 < 720) {
            fileUpload1.value = '';
            alert("La resolución mínima de la imagen debe ser 1080x720.");
            return false;
          }
          alert("Imagen aceptada!");
          return true;
        } else {
          alert('El archivo seleccionado no es una imagen.');
          fileUpload1.value = '';
          return false;
        }
      };
    };
  });
  