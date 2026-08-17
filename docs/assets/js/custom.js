/* ============================================================
   XOOTAY GOX YI — custom.js
   Animation géométrique contrôlable par l'utilisateur
   Version adaptée à ton fichier actuel
   ============================================================ */

document$.subscribe(function () {
  const STORAGE_KEY = 'xgy-background-animation';
  const savedPreference = localStorage.getItem(STORAGE_KEY);
  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Première visite : respecter la préférence système.
  // Ensuite : conserver le choix manuel de l'utilisateur.
  let isEnabled = savedPreference === null
    ? !prefersReducedMotion
    : savedPreference === 'on';

  let animationFrame = null;
  let particlesArray = [];
  let canvas = null;
  let ctx = null;
  const mouse = { x: null, y: null, radius: 100 };

  function updateToggleButton() {
    const button = document.getElementById('xgy-background-toggle');
    if (!button) return;

    button.setAttribute('aria-pressed', String(isEnabled));
    button.setAttribute(
      'aria-label',
      isEnabled
        ? 'Désactiver l’arrière-plan animé'
        : 'Activer l’arrière-plan animé'
    );
    button.setAttribute(
      'title',
      isEnabled
        ? 'Désactiver l’arrière-plan animé'
        : 'Activer l’arrière-plan animé'
    );
    button.textContent = isEnabled ? '◌' : '○';
  }

  function createToggleButton() {
    // Évite de créer plusieurs boutons pendant la navigation instantanée.
    let button = document.getElementById('xgy-background-toggle');
    if (button) {
      updateToggleButton();
      return button;
    }

    // .md-header__option correspond à la zone droite de la barre Material.
    const headerOption = document.querySelector('.md-header__option');
    if (!headerOption) return null;

    button = document.createElement('button');
    button.id = 'xgy-background-toggle';
    button.type = 'button';
    button.className = 'xgy-background-toggle md-icon';

    button.addEventListener('click', function () {
      isEnabled = !isEnabled;
      localStorage.setItem(STORAGE_KEY, isEnabled ? 'on' : 'off');
      updateToggleButton();

      if (isEnabled) {
        startAnimation();
      } else {
        stopAnimation();
      }
    });

    // Le bouton est placé dans la barre supérieure, à droite.
    headerOption.insertBefore(button, headerOption.firstChild);
    updateToggleButton();
    return button;
  }

  function setCanvasSize() {
    if (!canvas) return;
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
  }

  function createCanvas() {
    const existingCanvas = document.getElementById('xgy-particles');
    if (existingCanvas) existingCanvas.remove();

    canvas = document.createElement('canvas');
    canvas.id = 'xgy-particles';
    canvas.setAttribute('aria-hidden', 'true');
    document.body.insertBefore(canvas, document.body.firstChild);

    ctx = canvas.getContext('2d');
    setCanvasSize();
  }

  window.addEventListener('resize', function () {
    setCanvasSize();
    if (isEnabled) init();
  });

  window.addEventListener('mousemove', function (event) {
    mouse.x = event.clientX;
    mouse.y = event.clientY;
  });

  window.addEventListener('mouseout', function () {
    mouse.x = null;
    mouse.y = null;
  });

  class Particle {
    constructor(x, y, directionX, directionY, size) {
      this.x = x;
      this.y = y;
      this.directionX = directionX;
      this.directionY = directionY;
      this.size = size;
    }

    draw(color) {
      ctx.beginPath();
      ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2, false);
      ctx.fillStyle = color;
      ctx.fill();
    }

    update(color) {
      if (this.x > canvas.width || this.x < 0) {
        this.directionX = -this.directionX;
      }
      if (this.y > canvas.height || this.y < 0) {
        this.directionY = -this.directionY;
      }

      if (mouse.x !== null && mouse.y !== null) {
        const dx = mouse.x - this.x;
        const dy = mouse.y - this.y;
        const distance = Math.sqrt(dx * dx + dy * dy);

        if (distance < mouse.radius) {
          this.x -= dx / 20;
          this.y -= dy / 20;
        }
      }

      this.x += this.directionX;
      this.y += this.directionY;
      this.draw(color);
    }
  }

  function init() {
    if (!canvas) return;

    particlesArray = [];
    let numberOfParticles = (canvas.height * canvas.width) / 14000;

    // Moins de particules sur mobile.
    if (window.innerWidth < 600) {
      numberOfParticles *= 0.65;
    }
    if (numberOfParticles > 90) {
      numberOfParticles = 90;
    }

    for (let i = 0; i < numberOfParticles; i += 1) {
      const size = Math.random() * 1.5 + 0.8;
      const x = Math.random() * (canvas.width - size * 2) + size;
      const y = Math.random() * (canvas.height - size * 2) + size;
      const directionX = Math.random() * 0.6 - 0.3;
      const directionY = Math.random() * 0.6 - 0.3;

      particlesArray.push(
        new Particle(x, y, directionX, directionY, size)
      );
    }
  }

  function connect(lineColor) {
    for (let a = 0; a < particlesArray.length; a += 1) {
      for (let b = a + 1; b < particlesArray.length; b += 1) {
        const dx = particlesArray[a].x - particlesArray[b].x;
        const dy = particlesArray[a].y - particlesArray[b].y;
        const distance = dx * dx + dy * dy;

        if (distance < (canvas.width / 10) * (canvas.height / 10)) {
          ctx.strokeStyle = lineColor;
          ctx.lineWidth = 1;
          ctx.beginPath();
          ctx.moveTo(particlesArray[a].x, particlesArray[a].y);
          ctx.lineTo(particlesArray[b].x, particlesArray[b].y);
          ctx.stroke();
        }
      }
    }
  }

  function animate() {
    if (!isEnabled || !ctx || !canvas) return;

    ctx.clearRect(0, 0, canvas.width, canvas.height);

    const isDarkMode = document.body.getAttribute('data-md-color-scheme') === 'slate';
    const pointColor = isDarkMode
      ? 'rgba(255, 255, 255, 0.10)'
      : 'rgba(0, 0, 0, 0.14)';
    const lineColor = isDarkMode
      ? 'rgba(255, 255, 255, 0.035)'
      : 'rgba(0, 0, 0, 0.07)';

    for (let i = 0; i < particlesArray.length; i += 1) {
      particlesArray[i].update(pointColor);
    }

    connect(lineColor);
    animationFrame = requestAnimationFrame(animate);
  }

  function startAnimation() {
    if (!canvas) createCanvas();
    init();
    cancelAnimationFrame(animationFrame);
    animate();
  }

  function stopAnimation() {
    cancelAnimationFrame(animationFrame);
    animationFrame = null;
    particlesArray = [];

    if (ctx && canvas) {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
    }
  }

  createToggleButton();
  createCanvas();

  if (isEnabled) {
    startAnimation();
  } else {
    stopAnimation();
  }
});
