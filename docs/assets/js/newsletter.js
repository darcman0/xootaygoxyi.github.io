(function () {
    if (window.__xgyNewsletterInitialized) {
      return;
    }
  
    window.__xgyNewsletterInitialized = true;
  
    document.addEventListener("submit", function (event) {
      var form = event.target;
  
      if (
        !form.classList ||
        !form.classList.contains("nl-form")
      ) {
        return;
      }
  
      event.preventDefault();
  
      var message = form.parentNode.querySelector(".nl-msg");
      var button = form.querySelector("button");
  
      function showMessage(success, text) {
        message.className = "nl-msg " + (success ? "ok" : "ko");
        message.textContent = text;
      }
  
      button.disabled = true;
  
      var emailInput = form.querySelector('input[name="EMAIL"]');
      var email = emailInput.value.trim();
  
      var checkUrl =
        "https://newsletter-check-xgy.darcman8.workers.dev";
  
      fetch(checkUrl, {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          email: email
        })
      })
        .then(function (response) {
          return response.json();
        })
        .then(function (data) {
          if (data.status === "already") {
            showMessage(
              true,
              "Cette adresse est déjà inscrite à la newsletter. Vous n'avez rien à faire."
            );
  
            form.reset();
            return;
          }
  
          return sendToBrevo();
        })
        .catch(function () {
          return sendToBrevo();
        })
        .then(function () {
          window.setTimeout(function () {
            button.disabled = false;
          }, 5000);
        });
  
      function sendToBrevo() {
        return fetch(form.action, {
          method: "POST",
          body: new FormData(form),
          redirect: "manual",
          headers: {
            Accept: "application/json"
          }
        })
          .then(function (response) {
            if (response.type === "opaqueredirect") {
              return true;
            }
  
            return response.json().then(
              function (data) {
                return response.ok && data.success !== false;
              },
              function () {
                return response.ok;
              }
            );
          })
          .then(function (success) {
            if (success) {
              showMessage(
                true,
                "Merci ! Un email de validation vient de vous être envoyé. Ouvrez-le, vérifiez aussi vos spams, puis cliquez sur le lien pour confirmer votre inscription. Si vous êtes déjà abonné, vous n'avez rien à faire."
              );
  
              form.reset();
            } else {
              showMessage(
                false,
                "Nous n'avons pas pu enregistrer votre inscription. Vérifiez l'adresse email et réessayez."
              );
            }
          })
          .catch(function () {
            showMessage(
              true,
              "Demande envoyée. Si vous ne recevez aucun email dans quelques minutes, vérifiez vos spams ou réessayez."
            );
          });
      }
    });
  })();
  