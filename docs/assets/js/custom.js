/* ============================================================
   XOOTAY GOX YI — custom.js
   Animation géométrique globale et persistante
   ============================================================ */

   (function () {
    const STORAGE_KEY = 'xgy-background-animation';
    const STATE_KEY = '__xgyParticlesController';
  
    function createController() {
      const savedPreference = localStorage.getItem(STORAGE_KEY);
      const prefersReducedMotion = window.matchMedia(
        '(prefers-reduced-motion: reduce)'
      ).matches;
  
      const controller = {
        isEnabled: savedPreference === null
          ? !prefersReducedMotion
          : savedPreference === 'on',
        animationFrame: null,
        particles: [],
        canvas: null,
        ctx: null,
        resizeHandler: null,
      };
  
      class Particle {
        constructor(x, y, directionX, directionY, size) {
          this.x = x;
          this.y = y;
          this.directionX = directionX;
          this.directionY = directionY;
          this.size = size;
        }
  
        draw(color) {
          controller.ctx.beginPath();
          controller.ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2, false);
          controller.ctx.fillStyle = color;
          controller.ctx.fill();
        }
  
        update(color) {
          if (this.x > controller.canvas.width || this.x < 0) {
            this.directionX = -this.directionX;
          }
          if (this.y > controller.canvas.height || this.y < 0) {
            this.directionY = -this.directionY;
          }
  
          this.x += this.directionX;
          this.y += this.directionY;
          this.draw(color);
        }
      }
  
      controller.setCanvasSize = function () {
        if (!controller.canvas) return;
        controller.canvas.width = window.innerWidth;
        controller.canvas.height = window.innerHeight;
      };
  
      controller.createCanvas = function () {
        const existingCanvas = document.getElementById('xgy-particles');
        if (existingCanvas) existingCanvas.remove();
  
        controller.canvas = document.createElement('canvas');
        controller.canvas.id = 'xgy-particles';
        controller.canvas.setAttribute('aria-hidden', 'true');
        document.body.insertBefore(controller.canvas, document.body.firstChild);
        controller.ctx = controller.canvas.getContext('2d');
        controller.setCanvasSize();
      };
  
      controller.init = function () {
        if (!controller.canvas) return;
  
        controller.particles = [];
        let numberOfParticles = (
          controller.canvas.height * controller.canvas.width
        ) / 18000;
  
        if (window.innerWidth < 600) {
          numberOfParticles *= 0.65;
        }
        if (numberOfParticles > 65) {
          numberOfParticles = 65;
        }
  
        for (let i = 0; i < numberOfParticles; i += 1) {
          const size = Math.random() * 1.1 + 0.6;
          const x = Math.random() * (
            controller.canvas.width - size * 2
          ) + size;
          const y = Math.random() * (
            controller.canvas.height - size * 2
          ) + size;
          const directionX = Math.random() * 0.3 - 0.15;
          const directionY = Math.random() * 0.3 - 0.15;
  
          controller.particles.push(
            new Particle(x, y, directionX, directionY, size)
          );
        }
      };
  
      controller.connect = function (lineColor) {
        for (let a = 0; a < controller.particles.length; a += 1) {
          for (let b = a + 1; b < controller.particles.length; b += 1) {
            const dx = controller.particles[a].x - controller.particles[b].x;
            const dy = controller.particles[a].y - controller.particles[b].y;
            const distance = dx * dx + dy * dy;
  
            if (distance < (
              controller.canvas.width / 10
            ) * (
              controller.canvas.height / 10
            )) {
              controller.ctx.strokeStyle = lineColor;
              controller.ctx.lineWidth = 1;
              controller.ctx.beginPath();
              controller.ctx.moveTo(
                controller.particles[a].x,
                controller.particles[a].y
              );
              controller.ctx.lineTo(
                controller.particles[b].x,
                controller.particles[b].y
              );
              controller.ctx.stroke();
            }
          }
        }
      };
  
      controller.animate = function () {
        if (!controller.isEnabled || !controller.ctx || !controller.canvas) {
          return;
        }
  
        controller.ctx.clearRect(
          0,
          0,
          controller.canvas.width,
          controller.canvas.height
        );
  
        const isDarkMode = document.body.getAttribute(
          'data-md-color-scheme'
        ) === 'slate';
        const pointColor = isDarkMode
          ? 'rgba(255, 255, 255, 0.16)'
          : 'rgba(0, 0, 0, 0.10)';
        const lineColor = isDarkMode
          ? 'rgba(255, 255, 255, 0.055)'
          : 'rgba(0, 0, 0, 0.045)';
  
        for (let i = 0; i < controller.particles.length; i += 1) {
          controller.particles[i].update(pointColor);
        }
  
        controller.connect(lineColor);
        controller.animationFrame = requestAnimationFrame(
          controller.animate
        );
      };
  
      controller.start = function () {
        if (!controller.canvas) controller.createCanvas();
        controller.init();
        cancelAnimationFrame(controller.animationFrame);
        controller.animate();
      };
  
      controller.stop = function () {
        cancelAnimationFrame(controller.animationFrame);
        controller.animationFrame = null;
        controller.particles = [];
  
        if (controller.ctx && controller.canvas) {
          controller.ctx.clearRect(
            0,
            0,
            controller.canvas.width,
            controller.canvas.height
          );
        }
      };
  
      controller.updateButton = function () {
        const button = document.getElementById('xgy-background-toggle');
        if (!button) return;
  
        button.setAttribute('aria-pressed', String(controller.isEnabled));
        button.setAttribute(
          'aria-label',
          controller.isEnabled
            ? 'Désactiver l’arrière-plan animé'
            : 'Activer l’arrière-plan animé'
        );
        button.setAttribute(
          'title',
          controller.isEnabled
            ? 'Désactiver l’arrière-plan animé'
            : 'Activer l’arrière-plan animé'
        );
        button.textContent = controller.isEnabled ? '◌' : '○';
      };
  
      controller.attachButton = function () {
        let button = document.getElementById('xgy-background-toggle');
        if (!button) {
          const headerOption = document.querySelector('.md-header__option');
          if (!headerOption) return;
  
          button = document.createElement('button');
          button.id = 'xgy-background-toggle';
          button.type = 'button';
          button.className = 'xgy-background-toggle md-icon';
          headerOption.insertBefore(button, headerOption.firstChild);
        }
  
        // onclick est remplacé à chaque navigation : aucun ancien handler ne reste actif.
        button.onclick = function () {
          controller.isEnabled = !controller.isEnabled;
          localStorage.setItem(
            STORAGE_KEY,
            controller.isEnabled ? 'on' : 'off'
          );
          controller.updateButton();
  
          if (controller.isEnabled) {
            controller.start();
          } else {
            controller.stop();
          }
        };
  
        controller.updateButton();
      };
  
      controller.resizeHandler = function () {
        controller.setCanvasSize();
        if (controller.isEnabled) controller.init();
      };
  
      window.addEventListener('resize', controller.resizeHandler);
      controller.createCanvas();
  
      if (controller.isEnabled) {
        controller.start();
      } else {
        controller.stop();
      }
  
      return controller;
    }
  
    
    function getController() {
      if (!window[STATE_KEY]) {
        window[STATE_KEY] = createController();
      }
      return window[STATE_KEY];
    }
  
    // Compatible avec la navigation instantanée de Material for MkDocs.
    document$.subscribe(function () {
      const controller = getController();
      controller.attachButton();
    });
  })();
  