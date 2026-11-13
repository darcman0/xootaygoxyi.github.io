/* Commentaires Waline (serveur sur Vercel, base Neon) */
import { init } from "https://unpkg.com/@waline/client@3.16.2/dist/waline.js";

let instance = null;

function initialiserWaline() {
  if (instance) {
    instance.destroy();
    instance = null;
  }

  const element = document.querySelector("#waline");
  if (!element) return;

  instance = init({
    el: element,
    serverURL: "https://commentaires.xootaygoxyi.com",
    path: window.location.pathname,
    lang: "fr",
    login: "disable",
    requiredMeta: ["nick"],
    dark: 'body[data-md-color-scheme="slate"]',
    wordLimit: 1000,
    imageUploader: false,
    search: false,
    reaction: false,
    noRss:true,
    locale: {
      placeholder: "Votre commentaire sera publié après validation."
    }
  });
}

document$.subscribe(initialiserWaline);
