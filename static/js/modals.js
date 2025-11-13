
// Scripts para os modais com data-attributes

// Abrir o modal
function openModal(sel){
  var el = document.querySelector(sel);
  el.classList.remove('hidden');
  document.body.classList.add('overflow-y-hidden');
}

// Fechar o modal
function closeModal(sel){
  var el = document.querySelector(sel);
  el.classList.add('hidden');
  document.body.classList.remove('overflow-y-hidden');
}

// Abrir modal usando elementos com data-open-modal (Ex: ícone de informação)
document.querySelectorAll('[data-open-modal]').forEach(function(btn){
  btn.addEventListener('click', function(e){

    // Lógica que evita que botões/forms internos abram o modal acidentalmente (botão de excluir)
    var interactiveEl = e.target.closest('button,form');
    var interactiveNearestOpener = interactiveEl.closest('[data-open-modal]');
    var interactiveIsOpener = interactiveEl.hasAttribute('data-open-modal') || (interactiveNearestOpener && interactiveNearestOpener !== btn);
    if(interactiveNearestOpener === btn && !interactiveIsOpener){
      return;
    }

    var sel = btn.getAttribute('data-open-modal');
    openModal(sel);
  });
});

// Fechar modal usando elementos com data-close-modal (Ex: botão X)
document.querySelectorAll('[data-close-modal]').forEach(function(btn){
  btn.addEventListener('click', function(){
    var sel = btn.getAttribute('data-close-modal');
    closeModal(sel);
  });
});

// Enviar form usando elementos com data-submit-form e fechar modal
document.querySelectorAll('[data-submit-form]').forEach(function(btn){
  btn.addEventListener('click', function(){
    var formSel = btn.getAttribute('data-submit-form');
    document.querySelector(formSel).requestSubmit();
    var closeSel = btn.getAttribute('data-close-modal');
    closeModal(closeSel);
  });
});

// Clicando para fora fecha os modais com .modal-backdrop
document.querySelectorAll('.modal-backdrop').forEach(function(backdrop){
  backdrop.addEventListener('click', function(e){
      var sel = backdrop.id ? ('#' + backdrop.id) : null;
      closeModal(sel);
  });
});