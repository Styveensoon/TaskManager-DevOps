const API = "/api/tareas";
let filtroActual = "todos";

const form = document.getElementById("form-tarea");
const inputNombre = document.getElementById("nombre");
const inputDescripcion = document.getElementById("descripcion");
const selectPrioridad = document.getElementById("prioridad");
const selectEstado = document.getElementById("estado");
const btnGuardar = document.getElementById("btn-guardar");
const mensaje = document.getElementById("mensaje");
const cuerpoTabla = document.getElementById("cuerpo-tabla");
const vacio = document.getElementById("vacio");
const btnFiltros = document.querySelectorAll(".btn-filtro");

let modoEdicion = false;
let tareaEditandoId = null;

function mostrarMensaje(texto, tipo) {
  mensaje.textContent = texto;
  mensaje.className = "mensaje " + tipo;
  mensaje.style.display = "block";
  setTimeout(() => {
    mensaje.style.display = "none";
  }, 4000);
}

function limpiarMensaje() {
  mensaje.style.display = "none";
}

async function cargarTareas() {
  try {
    const respuesta = await fetch(API);
    if (!respuesta.ok) throw new Error("Error al cargar tareas");
    const tareas = await respuesta.json();
    renderizarTareas(tareas);
  } catch (error) {
    console.error(error);
    mostrarMensaje("No se pudieron cargar las tareas", "error");
  }
}

function renderizarTareas(tareas) {
  cuerpoTabla.innerHTML = "";

  const filtradas =
    filtroActual === "todos"
      ? tareas
      : tareas.filter((t) => t.estado === filtroActual);

  if (filtradas.length === 0) {
    vacio.style.display = "block";
  } else {
    vacio.style.display = "none";
    filtradas.forEach((t) => {
      const tr = document.createElement("tr");
      const prioridadClase = "prioridad-" + (t.prioridad || "media").toLowerCase();
      const estadoClase = "estado-" + (t.estado || "pendiente").toLowerCase().replace(" ", "-");

      tr.innerHTML = `
        <td>${t.id}</td>
        <td><strong>${escapeHtml(t.nombre)}</strong></td>
        <td>${escapeHtml(t.descripcion || "")}</td>
        <td><span class="${prioridadClase}">${t.prioridad}</span></td>
        <td><span class="estado-badge ${estadoClase}">${t.estado}</span></td>
        <td>${t.fecha_creacion ? t.fecha_creacion.slice(0, 16) : ""}</td>
        <td class="acciones">
          <button class="btn btn-warning btn-editar" data-id="${t.id}">Editar</button>
          <button class="btn btn-success btn-estado" data-id="${t.id}" data-estado="${t.estado}">${estadoBoton(t.estado)}</button>
          <button class="btn btn-danger btn-eliminar" data-id="${t.id}">Eliminar</button>
        </td>
      `;
      cuerpoTabla.appendChild(tr);
    });
  }

  document.querySelectorAll(".btn-editar").forEach((btn) =>
    btn.addEventListener("click", (e) => prepararEdicion(parseInt(e.target.dataset.id)))
  );
  document.querySelectorAll(".btn-eliminar").forEach((btn) =>
    btn.addEventListener("click", (e) => eliminarTarea(parseInt(e.target.dataset.id)))
  );
  document.querySelectorAll(".btn-estado").forEach((btn) =>
    btn.addEventListener("click", (e) =>
      cambiarEstado(parseInt(e.target.dataset.id), e.target.dataset.estado)
    )
  );
}

function estadoBoton(estado) {
  if (estado === "Terminada") return "Reabrir";
  if (estado === "En Proceso") return "Terminar";
  return "En Proceso";
}

function escapeHtml(texto) {
  if (!texto) return "";
  const div = document.createElement("div");
  div.textContent = texto;
  return div.innerHTML;
}

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  limpiarMensaje();
  btnGuardar.disabled = true;

  const payload = {
    nombre: inputNombre.value.trim(),
    descripcion: inputDescripcion.value.trim(),
    prioridad: selectPrioridad.value,
    estado: selectEstado.value,
  };

  try {
    let respuesta;
    if (modoEdicion) {
      respuesta = await fetch(`${API}/${tareaEditandoId}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      });
    } else {
      respuesta = await fetch(API, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      });
    }

    if (!respuesta.ok) {
      const err = await respuesta.json();
      throw new Error(err.error || "Error al guardar la tarea");
    }

    mostrarMensaje(
      modoEdicion ? "Tarea actualizada correctamente" : "Tarea registrada correctamente",
      "exito"
    );
    form.reset();
    selectPrioridad.value = "Media";
    selectEstado.value = "Pendiente";
    modoEdicion = false;
    tareaEditandoId = null;
    btnGuardar.textContent = "Guardar tarea";
    cargarTareas();
  } catch (error) {
    mostrarMensaje(error.message, "error");
  } finally {
    btnGuardar.disabled = false;
  }
});

function prepararEdicion(id) {
  limpiarMensaje();
  fetch(`${API}/${id}`)
    .then((r) => r.json())
    .then((t) => {
      inputNombre.value = t.nombre || "";
      inputDescripcion.value = t.descripcion || "";
      selectPrioridad.value = t.prioridad || "Media";
      selectEstado.value = t.estado || "Pendiente";
      modoEdicion = true;
      tareaEditandoId = id;
      btnGuardar.textContent = "Actualizar tarea";
      inputNombre.focus();
    })
    .catch(() => mostrarMensaje("No se pudo cargar la tarea", "error"));
}

async function eliminarTarea(id) {
  if (!confirm("¿Estas seguro de que quieres eliminar esta tarea?")) return;
  try {
    const respuesta = await fetch(`${API}/${id}`, { method: "DELETE" });
    if (!respuesta.ok) throw new Error("Error al eliminar la tarea");
    mostrarMensaje("Tarea eliminada correctamente", "exito");
    cargarTareas();
  } catch (error) {
    mostrarMensaje(error.message, "error");
  }
}

async function cambiarEstado(id, estadoActual) {
  let siguiente;
  if (estadoActual === "Pendiente") siguiente = "En Proceso";
  else if (estadoActual === "En Proceso") siguiente = "Terminada";
  else siguiente = "Pendiente";

  try {
    const respuesta = await fetch(`${API}/${id}/estado`, {
      method: "PATCH",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ estado: siguiente }),
    });
    if (!respuesta.ok) throw new Error("Error al cambiar el estado");
    mostrarMensaje("Estado actualizado a " + siguiente, "exito");
    cargarTareas();
  } catch (error) {
    mostrarMensaje(error.message, "error");
  }
}

btnFiltros.forEach((btn) => {
  btn.addEventListener("click", () => {
    btnFiltros.forEach((b) => b.classList.remove("activo"));
    btn.classList.add("activo");
    filtroActual = btn.dataset.estado;
    cargarTareas();
  });
});

// Inicializar
cargarTareas();
