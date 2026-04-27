const chatForm = document.getElementById('chatForm');
const chatBox = document.getElementById('chatBox');
const mensajeInput = document.getElementById('mensajeInput');
const micBtn = document.getElementById('micBtn');
const voiceToggleBtn = document.getElementById('voiceToggleBtn');

let vozActiva = true;

const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
const recognition = SpeechRecognition ? new SpeechRecognition() : null;

if (recognition) {
  recognition.lang = 'es-ES';
  recognition.interimResults = false;
  recognition.maxAlternatives = 1;

  recognition.addEventListener('start', () => {
    micBtn.classList.add('is-recording');
  });

  recognition.addEventListener('end', () => {
    micBtn.classList.remove('is-recording');
  });

  recognition.addEventListener('result', (event) => {
    const texto = event.results[0][0].transcript || '';
    mensajeInput.value = texto.trim();
    mensajeInput.focus();
  });

  recognition.addEventListener('error', () => {
    addMessage('No se pudo reconocer la voz en este momento.', 'bot');
  });
} else {
  micBtn.disabled = true;
  micBtn.title = 'Web Speech API no disponible en este navegador';
}

function addMessage(texto, tipo) {
  const el = document.createElement('div');
  el.className = `msg ${tipo}`;
  el.textContent = texto;
  chatBox.appendChild(el);
  chatBox.scrollTop = chatBox.scrollHeight;
}

function hablar(texto) {
  if (!vozActiva || !('speechSynthesis' in window)) {
    return;
  }

  window.speechSynthesis.cancel();
  const utterance = new SpeechSynthesisUtterance(texto);
  utterance.lang = 'es-ES';
  utterance.rate = 1;
  utterance.pitch = 1;
  window.speechSynthesis.speak(utterance);
}

voiceToggleBtn.addEventListener('click', () => {
  vozActiva = !vozActiva;

  if (!vozActiva) {
    window.speechSynthesis.cancel();
  }

  voiceToggleBtn.classList.toggle('is-active', vozActiva);
  voiceToggleBtn.textContent = vozActiva ? '🔊 Voz ON' : '🔇 Voz OFF';
  voiceToggleBtn.title = vozActiva ? 'Voz activada' : 'Voz desactivada';
});

micBtn.addEventListener('click', () => {
  if (!recognition) {
    addMessage('Tu navegador no soporta reconocimiento de voz.', 'bot');
    return;
  }

  recognition.start();
});

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

    const respuesta = data.respuesta || 'Sin respuesta.';
    addMessage(respuesta, 'bot');
    hablar(respuesta);
  } catch (error) {
    addMessage('No se pudo conectar con el servidor.', 'bot');
  }
});
