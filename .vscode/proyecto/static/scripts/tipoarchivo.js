function validar1() {
    // Obtener nombre de archivo
    let archivo = document.querySelector('input[name="imagen_1"]').value,
    // Obtener extensión del archivo
        extension = archivo.substring(archivo.lastIndexOf('.'),archivo.length);
    // Si la extensión obtenida no está incluida en la lista de valores
    // del atributo "accept", mostrar un error.
    if(document.querySelector('input[name="imagen_1"]').getAttribute('accept').split(',').indexOf(extension) < 0) {

      alert('Archivo inválido. No se permite la extensión ' + extension);
      archivo.value = '';
    }
  }

  function validar2() {
    // Obtener nombre de archivo
    let archivo = document.querySelector('input[name="imagen_2"]').value,
    // Obtener extensión del archivo
        extension = archivo.substring(archivo.lastIndexOf('.'),archivo.length);
    // Si la extensión obtenida no está incluida en la lista de valores
    // del atributo "accept", mostrar un error.
    if(document.querySelector('input[name="imagen_2"]').getAttribute('accept').split(',').indexOf(extension) < 0) {
      alert('Archivo inválido. No se permite la extensión ' + extension);
      archivo.value = '';

    }
  }

  function validar3() {
    // Obtener nombre de archivo
    let archivo = document.querySelector('input[name="imagen_3"]').value,
    // Obtener extensión del archivo
        extension = archivo.substring(archivo.lastIndexOf('.'),archivo.length);
    // Si la extensión obtenida no está incluida en la lista de valores
    // del atributo "accept", mostrar un error.
    if(document.querySelector('input[name="imagen_3"]').getAttribute('accept').split(',').indexOf(extension) < 0) {
      alert('Archivo inválido. No se permite la extensión ' + extension);
      archivo.value = '';

    }
  }

  function validar4() {
    // Obtener nombre de archivo
    let archivo = document.querySelector('input[name="imagen_4"]').value,
    // Obtener extensión del archivo
        extension = archivo.substring(archivo.lastIndexOf('.'),archivo.length);
    // Si la extensión obtenida no está incluida en la lista de valores
    // del atributo "accept", mostrar un error.
    if(document.querySelector('input[name="imagen_4"]').getAttribute('accept').split(',').indexOf(extension) < 0) {
      alert('Archivo inválido. No se permite la extensión ' + extension);
      archivo.value = '';

    }
  }