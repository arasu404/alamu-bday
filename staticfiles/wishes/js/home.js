document.addEventListener('DOMContentLoaded', () => {
    const audio = document.getElementById('bg-audio');
    const btn = document.getElementById('music-toggle');
  
    let playing = false;
    btn.addEventListener('click', () => {
      if (!playing) {
        audio.play().catch(()=>{});
        btn.textContent = 'Pause Music';
      } else {
        audio.pause();
        btn.textContent = 'Play Music';
      }
      playing = !playing;
    });
  
    const form = document.getElementById('wish-form');
    const list = document.getElementById('wishes-list');
  
    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      const name = document.getElementById('w-name').value || 'Anonymous';
      const message = document.getElementById('w-message').value;
      if (!message.trim()) return alert('Please write a message.');
  
      const resp = await fetch('/api/wishes/add/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name, message })
      });
      if (!resp.ok) return alert('Failed to send. Try again.');
  
      const data = await resp.json();
      const node = document.createElement('div');
      node.className = 'wish';
      node.innerHTML = `<strong>${data.name}</strong><p>${data.message}</p><small>Just now</small>`;
      list.insertAdjacentElement('afterbegin', node);
      form.reset();
    });
  });
  