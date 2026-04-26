const chatForm = document.getElementById('chatForm');
const chatBox = document.getElementById('chatBox');
const mensajeInput = document.getElementById('mensajeInput');

function addMessage(texto, tipo) {
  const el = document.createElement('div');
  el.className = `msg ${tipo}`;
  el.textContent = texto;
  chatBox.appendChild(el);
  chatBox.scrollTop = chatBox.scrollHeight;
}

chatForm.addEventListener('submit', async (event) => {
  event.preventDefault();
  const mensaje = mensajeInput.value.trim();

  if (!mensaje) {
    return;
  }

  addMessage(mensaje, 'user');
  mensajeInput.value = '';

  try {
    const response = await fetch('/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ mensaje }),
    });

    const data = await response.json();

    if (!response.ok) {
      addMessage(data.error || 'Error al procesar la solicitud.', 'bot');
      return;
    }

    addMessage(data.respuesta || 'Sin respuesta.', 'bot');
  } catch (error) {
    addMessage('No se pudo conectar con el servidor.', 'bot');
  }
});
