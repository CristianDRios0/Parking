 /*codigo para visualizar los detalles de la celda ocupada*/
  document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll(".cell.ocupado").forEach(cell => {
      cell.addEventListener("click", () => {
        const celdaId = cell.dataset.id;
  
        fetch(`/celdas/detalle/${celdaId}/`)
          .then(response => response.text())
          .then(html => {
            document.getElementById("detalleCeldaContent").innerHTML = html;
            const modal = new bootstrap.Modal(document.getElementById("infoCeldaModal"));
            modal.show();
          })
          .catch(error => console.error("Error cargando la info de la celda:", error));
      });
    });
  });

  /*codigo para crear parqueo*/
  document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll(".cell.libre").forEach(cell => {
      cell.addEventListener("click", () => {
        const celdaId = cell.dataset.id;
  
        fetch(`/parqueos/formulario/${celdaId}/`)
          .then(res => res.text())
          .then(html => {
            document.getElementById("formularioParqueoBody").innerHTML = html;
            const modal = new bootstrap.Modal(document.getElementById("crearParqueoModal"));
            modal.show();
  
            document.getElementById("crearParqueoForm").addEventListener("submit", function (e) {
              e.preventDefault();
              const formData = new FormData(this);
  
              fetch(`/parqueos/crear/${celdaId}/`, {
                method: "POST",
                body: formData,
                headers: {
                  'X-CSRFToken': formData.get('csrfmiddlewaretoken')
                }
              })
                .then(res => res.json())
                .then(data => {
                  if (data.success) {
                    modal.hide();
                    location.reload();
                  } else {
                    alert("Errores en el formulario");
                    console.log(data.errors);
                  }
                });
            });
          });
      });
    });
  });

  /* JS para el comportamiento al crear el pago */

  document.addEventListener("DOMContentLoaded", () => {
    document.body.addEventListener("click", function (e) {
      if (e.target.classList.contains("generar-pago-btn")) {
        const parqueoId = e.target.dataset.parqueoId;
  
        fetch(`/parqueos/formulario-pago/${parqueoId}/`)
          .then(res => res.text())
          .then(html => {
            document.getElementById("registrarPagoModalBody").innerHTML = html;
  
            const pagoModal = new bootstrap.Modal(document.getElementById("registrarPagoModal"));
            pagoModal.show();
  
            const pagoForm = document.getElementById("formularioPago");
  
            if (pagoForm) {
              pagoForm.addEventListener("submit", function (e) {
                e.preventDefault();
                const formData = new FormData(this);
  
                fetch(`/pagos/crear/${parqueoId}/`, {
                  method: "POST",
                  body: formData,
                  headers: {
                    'X-CSRFToken': formData.get('csrfmiddlewaretoken')
                  }
                })
                  .then(res => res.json())
                  .then(data => {
                    if (data.success) {
                      pagoModal.hide();
                      location.reload();  // Recarga para actualizar el estado de la celda
                    } else {
                      alert("Errores en el formulario");
                      console.log(data.errors);
                    }
                  });
              });
            }
          });
      }
    });
  });

  /* JS para manejar el comportamiento de la modal al crear vehiculo*/
  
  document.addEventListener("DOMContentLoaded", () => {
    const btnAbrirModal = document.getElementById("btnAbrirModalVehiculo");
  
    if (btnAbrirModal) {
      btnAbrirModal.addEventListener("click", (e) => {
        e.preventDefault();
  
        fetch("/vehiculos/formulario-vehiculo/")
          .then(res => res.text())
          .then(html => {
            document.getElementById("modalVehiculoBody").innerHTML = html;
  
            const modal = new bootstrap.Modal(document.getElementById("modalVehiculo"));
            modal.show();
  
            const form = document.getElementById("formularioVehiculo");
  
            if (form) {
              form.addEventListener("submit", function (e) {
                e.preventDefault();
                const formData = new FormData(this);
  
                fetch("/vehiculos/crear/", {
                  method: "POST",
                  body: formData,
                  headers: {
                    "X-CSRFToken": formData.get("csrfmiddlewaretoken")
                  }
                })
                .then(res => res.json())
                .then(data => {
                  if (data.success) {
                    modal.hide();
                    alert("Vehículo registrado correctamente");
                  } else {
                    alert("Errores en el formulario");
                    console.log(data.errors);
                  }
                });
              });
            }
          });
      });
    }
  });

  document.getElementById('logoutBtn').addEventListener('click', function() {
    const form = document.createElement('form');
    form.method = 'POST';
    form.action = '/logout/';

    // CSRF token
    const csrfToken = getCookie('csrftoken');
    const csrfInput = document.createElement('input');
    csrfInput.type = 'hidden';
    csrfInput.name = 'csrfmiddlewaretoken';
    csrfInput.value = csrfToken;
    form.appendChild(csrfInput);

    document.body.appendChild(form);
    form.submit();
});

// Utilidad para obtener el CSRF token desde cookies
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // cookie formato: name=value
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}