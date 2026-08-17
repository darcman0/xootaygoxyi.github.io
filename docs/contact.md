---
hide:
  - toc
  - navigation
title: "Xootay Gox Yi | Contact & Collaborations - Abdou Aziz Darc"
description: "Une mission, un levé drone ou un projet SIG au Sénégal ou ailleurs ? Retrouvez mes canaux de contact professionnels, GitHub, LinkedIn."
---

# Contact

Une mission, une collaboration, une question sur ce que vous avez trouvé ici. Je suis disponible et joignable via les canaux ci-dessous.

---

<div class="contact-container" markdown="1">

[Me laisser un mail :material-email:](mailto:darcman8@gmail.com){ .md-button .md-button }

[Visiter mon Github :fontawesome-brands-github:](https://github.com/darcman0){ .md-button .md-button }

[Visiter mon Gitlab :fontawesome-brands-gitlab:](https://gitlab.com/darcman0){ .md-button .md-button }

[Me retrouver sur Linkedin :fontawesome-brands-linkedin:](https://linkedin.com/in/abdou-aziz-darc){ .md-button .md-button }

</div>

---

## Ou envoyer un message direct

Si tu préfères passer par le formulaire ci-dessous, je reçois la notification et je te réponds dès que possible.

<form action="https://formspree.io/f/xrpzypgg" method="POST" class="contact-form" id="contactForm">
  
  <!-- Piège à spam (Honeypot invisible) -->
  <input type="text" name="_gotcha" style="display:none !important" tabindex="-1" autocomplete="off">

  <div class="form-row">
    <div class="form-group">
      <label for="prenom">Prénom</label>
      <input type="text" name="prenom" id="prenom" required placeholder="Ton prenom">
    </div>
    <div class="form-group">
      <label for="nom">Nom</label>
      <input type="text" name="nom" id="nom" required placeholder="Ton nom">
    </div>
  </div>
  <div class="form-group">
    <label for="email">Email</label>
    <input type="email" name="email" id="email" required placeholder="ton@email.com">
    <small id="email-error" style="color: #e53935; display: none; margin-top: 0.3rem; font-size: 0.85rem;">Veuillez entrer une adresse email valide (ex: nom@domaine.com).</small>
  </div>
  <div class="form-group">
    <label for="message">Message</label>
    <textarea name="message" id="message" rows="8" required placeholder="Ton message ici..."></textarea>
  </div>
  <button type="submit" class="md-button md-button">Envoyer</button>
</form>

<script>
document.getElementById('contactForm').addEventListener('submit', function(e) {
  const emailInput = document.getElementById('email');
  const emailError = document.getElementById('email-error');
  
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

  if (!emailRegex.test(emailInput.value.trim())) {
    e.preventDefault();
    emailError.style.display = 'block';
    emailInput.style.borderColor = '#e53935';
    emailInput.focus();
  } else {
    emailError.style.display = 'none';
    emailInput.style.borderColor = '';
  }
});
</script>